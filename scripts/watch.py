#!/usr/bin/env python3
"""
watch.py

_inbox 폴더를 감시하다가 새 md 가 들어오면 파이프라인을 돌린다

  1) obsidian_autolink.py --write-index   (기존 노트 + 미해결 링크 사전 갱신)
  2) decompose.py                          (LLM 분해 -> _pending 에 쓰기)
  3) obsidian_autolink.py --only _pending --apply  (LLM 이 놓친 기존 개념 보강)
  4) _inbox 의 원본을 _inbox/_done 으로 이동

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
  print("  $ " + " ".join(str(a) for a in argv))
  proc = subprocess.run([sys.executable] + [str(a) for a in argv], cwd=str(cwd),
                        capture_output=True, text=True, encoding="utf-8")
  out = (proc.stdout or "").strip()
  if out:
    print("\n".join("    " + l for l in out.splitlines()))
  if proc.returncode != 0:
    print("    [error] " + (proc.stderr or "").strip()[:800])
  return proc.returncode == 0


def stable(path, wait=1.5):
  """파일 복사가 끝났는지 확인 - 크기가 두 번 연속 같으면 완료로 본다"""
  try:
    a = path.stat().st_size
    time.sleep(wait)
    return a == path.stat().st_size
  except OSError:
    return False


def process(doc, vault, index, pending, backend, model):
  print("\n=== %s ===" % doc.name)
  if not stable(doc):
    print("  아직 쓰는 중 - 다음 주기에 재시도")
    return

  ok = run([SCRIPTS / "obsidian_autolink.py", vault, "--write-index", index], vault)
  if not ok:
    return

  ok = run([SCRIPTS / "decompose.py", doc, "--vault", vault,
            "--pending", pending, "--index", index,
            "--backend", backend, "--model", model], vault)
  if not ok:
    print("  분해 실패 - 원본을 _inbox 에 남겨 둡니다")
    return

  run([SCRIPTS / "obsidian_autolink.py", vault, "--only", pending, "--apply"], vault)

  done = doc.parent / "_done"
  done.mkdir(exist_ok=True)
  target = done / doc.name
  if target.exists():
    target = done / ("%s_%s%s" % (doc.stem, int(time.time()), doc.suffix))
  doc.rename(target)
  print("  완료 - 원본 이동 : %s" % target.relative_to(vault))
  print("  검수 후 %s 에서 볼트로 옮기세요" % pending)


def main():
  ap = argparse.ArgumentParser(description="_inbox 감시 -> 분해 파이프라인")
  ap.add_argument("--vault", default=".", help="볼트 루트")
  ap.add_argument("--inbox", default="_inbox")
  ap.add_argument("--pending", default="_pending")
  ap.add_argument("--index", default="_index.tsv")
  ap.add_argument("--backend", choices=["cc", "api", "mock"], default="api")
  ap.add_argument("--model", default="claude-sonnet-4-6")
  ap.add_argument("--interval", type=float, default=3.0, help="폴링 주기(초)")
  ap.add_argument("--once", action="store_true", help="한 번만 처리하고 종료")
  args = ap.parse_args()

  vault = Path(args.vault).resolve()
  inbox = vault / args.inbox
  inbox.mkdir(parents=True, exist_ok=True)
  (vault / args.pending).mkdir(parents=True, exist_ok=True)

  print("감시 시작 : %s (%.1fs 주기, Ctrl+C 로 종료)" % (inbox, args.interval))
  Seen = set()

  while True:
    Docs = sorted(p for p in inbox.glob("*.md") if p.is_file())
    for doc in Docs:
      key = (doc.name, doc.stat().st_mtime)
      if key in Seen:
        continue
      Seen.add(key)
      process(doc, vault, args.index, args.pending, args.backend, args.model)

    if args.once:
      return 0
    time.sleep(args.interval)


if __name__ == "__main__":
  try:
    sys.exit(main())
  except KeyboardInterrupt:
    print("\n종료")
    sys.exit(0)
