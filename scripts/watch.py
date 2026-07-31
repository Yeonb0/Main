#!/usr/bin/env python3
"""
watch.py

_inbox 폴더를 감시하다가 새 문서가 들어오면 파이프라인을 돌린다

  0) ingest.py                             (노션 export zip/폴더 -> 이미지는 images/ 로, md 는 정규화)
  1) obsidian_autolink.py --write-index   (기존 노트 + 미해결 링크 사전 갱신)
  2) decompose.py                          (LLM 분해 -> _pending 에 신규 노트 + 기존 노트 수정판)
  3) obsidian_autolink.py --only _pending --apply  (LLM 이 놓친 기존 개념 보강)
  4) decompose.py --rediff                 (링크 보강 반영해 수정판 .diff 재계산, LLM 호출 없음)
  5) _inbox 의 원본을 _inbox/_done 으로 이동

의존성 없음 - 폴링 방식이라 watchdog 설치가 필요 없고 Windows 에서 그대로 돈다

사용 예:
  python watch.py --vault . --backend api
  python watch.py --vault . --once            # 감시 없이 지금 쌓인 것만 처리
"""

import argparse
import subprocess
import sys
import time
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent


def run(argv, cwd):
  """자식 출력을 줄 단위로 흘려보낸다

  모아서 한 번에 찍으면 LLM 호출처럼 몇 분 걸리는 단계에서 멈춘 것처럼 보인다.
  자식은 -u 로 띄워야 파이프에서도 버퍼링 없이 나온다"""
  print("  $ " + " ".join(str(a) for a in argv), flush=True)
  proc = subprocess.Popen(
    [sys.executable, "-u"] + [str(a) for a in argv], cwd=str(cwd),
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    text=True, encoding="utf-8", errors="replace", bufsize=1)
  for line in proc.stdout:
    print("    " + line.rstrip("\r\n"), flush=True)
  code = proc.wait()
  if code != 0:
    print("    [error] 종료 코드 %d" % code, flush=True)
  return code == 0


def stable(path, wait=1.5):
  """파일 복사가 끝났는지 확인 - 크기가 두 번 연속 같으면 완료로 본다"""
  try:
    a = path.stat().st_size
    time.sleep(wait)
    return a == path.stat().st_size
  except OSError:
    return False


def process(doc, vault, index, pending, backend, model, no_update, max_context, on_conflict):
  print("\n=== %s ===" % doc.name)
  if not stable(doc):
    print("  아직 쓰는 중 - 다음 주기에 재시도")
    return

  ok = run([SCRIPTS / "obsidian_autolink.py", vault, "--write-index", index], vault)
  if not ok:
    return

  Argv = [SCRIPTS / "decompose.py", doc, "--vault", vault,
          "--pending", pending, "--index", index,
          "--backend", backend, "--model", model,
          "--max-context-notes", max_context, "--on-conflict", on_conflict]
  if no_update:
    Argv.append("--no-update")
  ok = run(Argv, vault)
  if not ok:
    print("  분해 실패 - 원본을 _inbox 에 남겨 둡니다")
    return

  run([SCRIPTS / "obsidian_autolink.py", vault, "--only", pending, "--apply"], vault)

  # 링크 보강이 수정판을 또 고치므로 diff 를 마지막에 다시 계산한다 (LLM 호출 없음)
  run([SCRIPTS / "decompose.py", "--rediff", "--vault", vault, "--pending", pending], vault)

  done = doc.parent / "_done"
  done.mkdir(exist_ok=True)
  target = done / doc.name
  if target.exists():
    target = done / ("%s_%s%s" % (doc.stem, int(time.time()), doc.suffix))
  doc.rename(target)
  print("  완료 - 원본 이동 : %s" % target.relative_to(vault))
  print("  검수 후 %s 에서 볼트로 옮기세요 (status: updated 는 덮어쓰기, .diff 로 차이 확인)" % pending)


def main():
  ap = argparse.ArgumentParser(description="_inbox 감시 -> 분해 파이프라인")
  ap.add_argument("--vault", default=".", help="볼트 루트")
  ap.add_argument("--inbox", default="_inbox")
  ap.add_argument("--pending", default="_pending")
  ap.add_argument("--images", default="images", help="노션 첨부를 모을 폴더")
  ap.add_argument("--index", default="_index.tsv")
  ap.add_argument("--backend", choices=["cc", "api", "mock"], default="cc")
  ap.add_argument("--model", default="claude-sonnet-4-6")
  ap.add_argument("--interval", type=float, default=3.0, help="폴링 주기(초)")
  ap.add_argument("--once", action="store_true", help="한 번만 처리하고 종료")
  ap.add_argument("--no-update", action="store_true",
                  help="기존 노트 보강을 끄고 신규 노트만 만든다 (LLM 호출 1번)")
  ap.add_argument("--max-context-notes", type=int, default=12,
                  help="보강 대상으로 본문을 첨부할 기존 노트 최대 개수")
  ap.add_argument("--on-conflict", choices=["auto", "number", "skip"], default="auto",
                  help="볼트에 같은 제목이 있을 때 : auto=폴더가 다르면 'AMI (1)' 로 번호, 같으면 건너뜀 "
                       "/ number=항상 번호 / skip=항상 건너뜀 (기본 auto)")
  args = ap.parse_args()

  vault = Path(args.vault).resolve()
  inbox = vault / args.inbox
  inbox.mkdir(parents=True, exist_ok=True)
  (vault / args.pending).mkdir(parents=True, exist_ok=True)

  print("감시 시작 : %s (%.1fs 주기, Ctrl+C 로 종료)" % (inbox, args.interval))
  Seen = set()
  Last = frozenset()

  while True:
    # 인박스 구성이 바뀐 주기에만 ingest 를 돌린다 - 매 폴링마다 부르면 로그가 시끄럽다
    sig = frozenset(p.name for p in inbox.iterdir()
                    if p.name != "_done" and not p.name.startswith("."))
    if sig and sig != Last:
      run([SCRIPTS / "ingest.py", "--vault", vault, "--inbox", args.inbox,
           "--images", args.images], vault)
      sig = frozenset(p.name for p in inbox.iterdir()
                      if p.name != "_done" and not p.name.startswith("."))
    Last = sig

    Docs = sorted(p for p in inbox.glob("*.md") if p.is_file())
    for doc in Docs:
      key = (doc.name, doc.stat().st_mtime)
      if key in Seen:
        continue
      Seen.add(key)
      process(doc, vault, args.index, args.pending, args.backend, args.model,
              args.no_update, args.max_context_notes, args.on_conflict)

    if args.once:
      return 0
    time.sleep(args.interval)


if __name__ == "__main__":
  try:
    sys.exit(main())
  except KeyboardInterrupt:
    print("\n종료")
    sys.exit(0)
