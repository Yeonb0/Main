#!/usr/bin/env python3
"""
decompose.py

통합 정리 md 한 개를 받아 원자적 개념 노트 + MOC 로 분해한다
LLM 호출부는 백엔드 두 가지를 지원한다

  --backend cc    Claude Code 헤드리스 (claude -p)   : API 키 불필요, 구독 사용
  --backend api   Anthropic API 직접 호출            : 결정적, ANTHROPIC_API_KEY 필요
  --backend mock  고정 응답으로 배선만 테스트

의존성 없음 (표준 라이브러리만 사용)

사용 예:
  python decompose.py _inbox\\JVM정리.md --vault . --backend api
  python decompose.py _inbox\\JVM정리.md --vault . --backend cc --show-prompt
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

MODEL = "claude-sonnet-4-6"
API_URL = "https://api.anthropic.com/v1/messages"
WIN_FORBIDDEN = r'[\\/:*?"<>|]'

RULES = """\
너는 옵시디언 제텔카스텐 볼트를 관리한다.
아래 '통합 문서'를 원자적 개념 노트로 분해하라.

## 분해 규칙
1. 1노트 = 1개념. 다른 글에서 [[ ]] 로 부를 만한 단위가 아니면 쪼개지 마라.
2. 노트 제목이 곧 링크 이름이다. "2. 메모리 관리" 같은 목차형 제목은 금지.
3. 본문에서 다른 개념을 언급하면 [[ ]] 로 감싸라. 개념당 노트 내 1회만.
4. 사전(index)에 이미 있는 개념은 반드시 그 이름 그대로 써라. 새로 짓지 마라.
   - kind=note : 이미 파일이 있는 개념
   - kind=stub : 파일은 없지만 이미 다른 노트가 예약해 둔 이름. 이것도 그대로 재사용하라.
5. 사전에 없는 개념이라도 앞으로 노트가 될 만하면 [[ ]] 를 걸고 new_concepts 에 넣어라.
   단, 한 문서에서 새로 만드는 이름은 8개를 넘기지 마라.
6. 원본의 서사(개념 간 순서와 인과)는 버리지 말고 MOC 본문에 남겨라.
   MOC 는 설명을 반복하지 말고 '연결하는 문장 + [[ ]]' 로만 구성한다.
7. 본문은 한국어 존댓말이 아닌 평서체로 쓴다. 코드블록은 원문 그대로 보존한다.

## 출력 형식
JSON 객체 하나만 출력한다. 설명, 인사말, 마크다운 코드펜스 모두 금지.

{
  "notes": [
    {
      "title": "가비지 컬렉션",
      "folder": "백엔드/Java",
      "aliases": ["GC"],
      "tags": ["java", "jvm"],
      "body": "마크다운 본문. 제목(#) 줄은 넣지 마라."
    }
  ],
  "moc": {
    "title": "JVM 메모리 관리",
    "folder": "_MOC",
    "body": "개념들을 잇는 서사. [[ ]] 링크 위주."
  },
  "new_concepts": ["G1 GC"]
}
"""


# ---------------------------------------------------------------------------
# 프롬프트 조립
# ---------------------------------------------------------------------------

def load_index(path, limit=1200):
  """obsidian_autolink.py --write-index 로 만든 TSV 를 읽는다"""
  if not path or not Path(path).exists():
    return "(사전 없음 - 볼트가 비어 있거나 인덱스를 아직 만들지 않음)"
  Lines = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if l and not l.startswith("#")]
  if len(Lines) > limit:
    Lines = Lines[:limit]
    Lines.append("... (이하 생략)")
  return "\n".join(Lines)


def load_folders(vault, limit=80):
  """기존 폴더 구조를 보여줘 새 노트가 엉뚱한 곳에 생기지 않게 한다"""
  Folders = set()
  for root, dirs, _ in os.walk(vault):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("_inbox", "_pending", "scripts", "node_modules")]
    rel = os.path.relpath(root, vault).replace(os.sep, "/")
    if rel != ".":
      Folders.add(rel)
  return "\n".join(sorted(Folders)[:limit]) or "(폴더 없음)"


def build_prompt(doc_text, doc_name, index_text, folders_text):
  return (
    RULES
    + "\n## 기존 폴더 구조\n" + folders_text
    + "\n\n## 사전 (kind\tterm\ttarget)\n" + index_text
    + "\n\n## 통합 문서 : " + doc_name + "\n" + doc_text
  )


# ---------------------------------------------------------------------------
# 백엔드
# ---------------------------------------------------------------------------

def call_api(prompt, model, max_tokens):
  key = os.environ.get("ANTHROPIC_API_KEY")
  if not key:
    raise SystemExit("ANTHROPIC_API_KEY 환경변수가 없습니다")
  payload = json.dumps({
    "model": model,
    "max_tokens": max_tokens,
    "messages": [{"role": "user", "content": prompt}],
  }).encode("utf-8")
  req = urllib.request.Request(API_URL, data=payload, method="POST", headers={
    "content-type": "application/json",
    "x-api-key": key,
    "anthropic-version": "2023-06-01",
  })
  with urllib.request.urlopen(req, timeout=600) as resp:
    data = json.loads(resp.read().decode("utf-8"))
  return "".join(b.get("text", "") for b in data.get("content", []) if b.get("type") == "text")


def call_claude_code(prompt):
  exe = shutil.which("claude") or shutil.which("claude.cmd")
  if not exe:
    raise SystemExit("claude 실행 파일을 찾을 수 없습니다. Claude Code 를 설치하고 PATH 를 확인하세요")
  proc = subprocess.run(
    [exe, "-p", "--output-format", "text"],
    input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=1800,
  )
  if proc.returncode != 0:
    raise SystemExit("claude 호출 실패 : %s" % (proc.stderr or "")[:500])
  return proc.stdout


MOCK = json.dumps({
  "notes": [
    {"title": "가비지 컬렉션", "folder": "백엔드/Java", "aliases": ["GC"],
     "tags": ["java"], "body": "[[JVM 메모리 구조]]의 힙 영역을 대상으로 동작한다. [[G1 GC]]는 그 구현 중 하나다."},
    {"title": "JVM 메모리 구조", "folder": "백엔드/Java", "aliases": ["런타임 데이터 영역"],
     "tags": ["java"], "body": "메서드 영역, 힙, 스택으로 나뉜다."},
  ],
  "moc": {"title": "JVM 메모리 관리", "folder": "_MOC",
          "body": "[[JVM 메모리 구조]]를 먼저 이해해야 [[가비지 컬렉션]]의 동작을 설명할 수 있다."},
  "new_concepts": ["G1 GC"],
}, ensure_ascii=False)


# ---------------------------------------------------------------------------
# 응답 파싱 및 파일 쓰기
# ---------------------------------------------------------------------------

def extract_json(raw):
  """코드펜스나 잡담이 섞여 있어도 JSON 객체만 뽑아낸다"""
  text = raw.strip()
  text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE).strip()
  start, end = text.find("{"), text.rfind("}")
  if start == -1 or end <= start:
    raise SystemExit("LLM 응답에서 JSON 을 찾지 못했습니다:\n" + raw[:800])
  return json.loads(text[start:end + 1])


def safe_name(title):
  name = re.sub(WIN_FORBIDDEN, " ", title).strip().rstrip(".")
  return re.sub(r"\s+", " ", name) or "untitled"


def existing_titles(vault):
  Titles = {}
  for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("_pending", "node_modules")]
    for f in files:
      if f.endswith(".md"):
        rel = os.path.relpath(os.path.join(root, f), vault).replace(os.sep, "/")
        Titles.setdefault(f[:-3], rel)
  return Titles


def render(note, source_name, is_moc=False):
  Front = ["---"]
  aliases = [a for a in note.get("aliases", []) if a]
  if aliases:
    Front.append("aliases: [%s]" % ", ".join(aliases))
  tags = note.get("tags", []) + (["moc"] if is_moc else [])
  if tags:
    Front.append("tags: [%s]" % ", ".join(dict.fromkeys(tags)))
  Front.append("source: %s" % source_name)
  Front.append("created: %s" % date.today().isoformat())
  Front.append("status: pending")
  Front.append("---")
  return "\n".join(Front) + "\n\n# " + note["title"] + "\n\n" + note.get("body", "").strip() + "\n"


def write_notes(result, vault, pending, source_name, overwrite):
  Known = existing_titles(vault)
  Written, Skipped = [], []

  Items = [(n, False) for n in result.get("notes", [])]
  if result.get("moc"):
    Items.append((result["moc"], True))

  for note, is_moc in Items:
    title = safe_name(note.get("title", ""))
    if not title:
      continue
    folder = re.sub(r"^[./\\]+", "", note.get("folder", "")).replace("\\", "/")
    out = pending / folder / (title + ".md")

    if title in Known and not overwrite:
      Skipped.append((title, Known[title]))
      continue

    out.parent.mkdir(parents=True, exist_ok=True)
    note["title"] = title
    out.write_text(render(note, source_name, is_moc), encoding="utf-8")
    Written.append(str(out.relative_to(pending)).replace(os.sep, "/"))

  return Written, Skipped


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
  ap = argparse.ArgumentParser(description="통합 md 를 원자 노트 + MOC 로 분해")
  ap.add_argument("document", help="분해할 통합 md 파일")
  ap.add_argument("--vault", default=".", help="볼트 루트 (기본 현재 폴더)")
  ap.add_argument("--pending", default="_pending", help="결과를 쌓을 폴더 (기본 _pending)")
  ap.add_argument("--index", default="_index.tsv", help="obsidian_autolink.py --write-index 산출물")
  ap.add_argument("--backend", choices=["cc", "api", "mock"], default="api")
  ap.add_argument("--model", default=MODEL)
  ap.add_argument("--max-tokens", type=int, default=16000)
  ap.add_argument("--show-prompt", action="store_true", help="프롬프트만 출력하고 종료")
  ap.add_argument("--overwrite", action="store_true", help="볼트에 같은 제목이 있어도 결과를 생성")
  args = ap.parse_args()

  vault = Path(args.vault).resolve()
  doc = Path(args.document).resolve()
  pending = vault / args.pending
  if not doc.is_file():
    raise SystemExit("문서를 찾을 수 없습니다 : %s" % doc)

  prompt = build_prompt(
    doc.read_text(encoding="utf-8"),
    doc.name,
    load_index(vault / args.index),
    load_folders(vault),
  )

  if args.show_prompt:
    print(prompt)
    return 0

  print("[1/3] LLM 호출 (%s) ..." % args.backend)
  if args.backend == "api":
    raw = call_api(prompt, args.model, args.max_tokens)
  elif args.backend == "cc":
    raw = call_claude_code(prompt)
  else:
    raw = MOCK

  print("[2/3] 응답 파싱 ...")
  result = extract_json(raw)

  print("[3/3] %s 에 쓰기 ..." % pending)
  Written, Skipped = write_notes(result, vault, pending, doc.name, args.overwrite)

  print("\n생성 %d개 :" % len(Written))
  for w in Written:
    print("  + %s" % w)
  if Skipped:
    print("\n볼트에 이미 있어 건너뜀 %d개 (합칠지 직접 판단하세요) :" % len(Skipped))
    for t, rel in Skipped:
      print("  = %s  ->  %s" % (t, rel))
  New = result.get("new_concepts", [])
  if New:
    print("\n새로 예약된 개념(아직 파일 없음) %d개 : %s" % (len(New), ", ".join(New)))
  return 0


if __name__ == "__main__":
  try:
    sys.exit(main())
  except KeyboardInterrupt:
    sys.exit(130)
