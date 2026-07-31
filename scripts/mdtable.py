#!/usr/bin/env python3
"""
mdtable.py

표 안의 위키링크 파이프(`[[대상|표시]]`)를 `\\|` 로 이스케이프한다

마크다운 표에서 `|` 는 셀 구분자다. 표 셀 안에 별칭 링크를 그냥 쓰면
`| [[다층 퍼셉트론|MLP]] 의 flatten |` 이 두 셀로 쪼개지면서 표 전체가 밀린다.
옵시디언 공식 해법은 `[[다층 퍼셉트론\\|MLP]]` 처럼 백슬래시로 막는 것이다.

두 군데서 쓴다.
  - obsidian_autolink.py : 표 줄에 링크를 넣을 때 처음부터 이스케이프해서 넣는다
  - decompose.py         : LLM 이 뱉은 body 를 _pending 에 쓰기 전에 교정한다

단독 실행하면 이미 깨진 표를 찾아 고친다 (기본은 dry-run).

  python scripts/mdtable.py .            # 어디가 깨졌는지만 출력
  python scripts/mdtable.py . --apply    # 실제로 수정
  python scripts/mdtable.py "머신러닝/im2col.md" --apply

의존성 없음 (Python 3.8+ 표준 라이브러리만 사용)
"""

import argparse
import os
import re
import sys
from pathlib import Path

# 펜스 코드블록 시작/끝 - 이 안의 `|` 는 표가 아니다
FENCE_RE = re.compile(r"^\s*(```|~~~)")

# 표 줄 - 콜아웃 안(`> | a | b |`)도 표다
ROW_RE = re.compile(r"^\s*>?\s*\|")

# 위키링크 한 덩어리 (임베드 `![[ ]]` 포함, 안에 `|` 가 있어도 잡는다)
LINK_RE = re.compile(r"\[\[(.*?)\]\]")

EXCLUDE_DIRS = {".obsidian", ".git", ".trash", "node_modules", "_inbox"}


def escape_link(inner):
  """위키링크 내부(`[[` 와 `]]` 사이)의 파이프를 `\\|` 로 통일한다

  - 이미 이스케이프된 것은 그대로 둔다 (재실행해도 `\\\\|` 로 늘어나지 않는다)
  - 표 정렬 때문에 낀 `대상  |  표시` 의 여분 공백도 턴다
    (`[[다층 퍼셉트론  ` 로는 노트를 못 찾기 때문)"""
  if "|" not in inner:
    return inner
  Parts = [p.strip() for p in inner.replace("\\|", "|").split("|")]
  return "\\|".join(Parts)


def fix_line(line):
  """표 줄 하나를 교정한다 - 표 줄이 아니면 그대로 돌려준다"""
  if not ROW_RE.match(line):
    return line
  return LINK_RE.sub(lambda m: "[[%s]]" % escape_link(m.group(1)), line)


def fix_text(text):
  """(교정본, 고친 줄 수) - 펜스 코드블록 안은 건드리지 않는다"""
  Out, fixed, fence = [], 0, None
  for line in text.split("\n"):
    m = FENCE_RE.match(line)
    if m:
      fence = None if fence == m.group(1) else (fence or m.group(1))
      Out.append(line)
      continue
    if fence:
      Out.append(line)
      continue
    new = fix_line(line)
    if new != line:
      fixed += 1
    Out.append(new)
  return "\n".join(Out), fixed


def in_table_row(text, pos):
  """text 의 pos 위치가 표 줄 안인가 - 링크를 넣기 전에 물어보는 용도

  펜스 코드블록 판정은 호출부(autolink)의 마스크가 이미 걸러 주므로 여기선 줄만 본다"""
  start = text.rfind("\n", 0, pos) + 1
  end = text.find("\n", pos)
  return bool(ROW_RE.match(text[start:len(text) if end == -1 else end]))


# ---------------------------------------------------------------------------
# 단독 실행 - 이미 깨진 표 찾아 고치기
# ---------------------------------------------------------------------------

def iter_md(target):
  if target.is_file():
    yield target
    return
  for root, Dirs, Files in os.walk(target):
    Dirs[:] = [d for d in Dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
    for name in sorted(Files):
      if name.endswith(".md"):
        yield Path(root) / name


def main():
  ap = argparse.ArgumentParser(description="표 안 위키링크 파이프 이스케이프 교정")
  ap.add_argument("target", nargs="?", default=".", help="볼트 루트 또는 md 파일 (기본 .)")
  ap.add_argument("--apply", action="store_true", help="실제로 파일을 수정한다 (기본은 dry-run)")
  args = ap.parse_args()

  target = Path(args.target).resolve()
  if not target.exists():
    print("경로가 없습니다 : %s" % target, file=sys.stderr)
    return 1

  base = target if target.is_dir() else target.parent
  total_files, total_lines = 0, 0

  for path in iter_md(target):
    try:
      text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
      print("[warn] 읽기 실패 : %s (%s)" % (path, e), file=sys.stderr)
      continue
    new, fixed = fix_text(text)
    if not fixed:
      continue

    total_files += 1
    total_lines += fixed
    try:
      rel = path.relative_to(base)
    except ValueError:
      rel = path
    print("%s  (%d줄)" % (str(rel).replace(os.sep, "/"), fixed))
    Old, New = text.split("\n"), new.split("\n")
    for i, (o, n) in enumerate(zip(Old, New), 1):
      if o != n:
        print("    L%-5d %s" % (i, n.strip()))

    if args.apply:
      path.write_text(new, encoding="utf-8")

  mode = "적용 완료" if args.apply else "dry-run (실제 수정 없음)"
  print("\n%s : 파일 %d개, 줄 %d개" % (mode, total_files, total_lines))
  return 0


if __name__ == "__main__":
  try:
    sys.exit(main())
  except KeyboardInterrupt:
    sys.exit(130)
