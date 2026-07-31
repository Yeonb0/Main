#!/usr/bin/env python3
"""
relink.py

`[[_pending/...]]` 로 굳어버린 링크를 볼트 본체 링크로 되돌린다

왜 생기나 :
  `_pending` 의 수정판은 볼트 원본과 **이름이 같다** (`_pending/머신러닝/학습률.md` ↔ `머신러닝/학습률.md`).
  그래서 `_pending` 안의 노트에 있는 `[[학습률]]` 은 옆에 있는 `_pending` 쪽으로 붙는다.
  이 상태에서 노트를 볼트로 옮기면, 옵시디언이 "링크가 가리키던 파일을 그대로 유지"하려고
  `[[_pending/머신러닝/학습률]]` 처럼 경로를 박아 넣는다 (`alwaysUpdateLinks: true`).
  결국 볼트 노트가 검수 대기소를 가리키게 되고, `_pending` 을 비우면 전부 깨진다.

이 스크립트가 하는 일 :
  `_pending/` 접두사를 떼고, 같은 이름의 볼트 노트로 다시 건다.
    [[_pending/머신러닝/학습률]]              -> [[학습률]]
    [[_pending/머신러닝/확률적 경사 하강법|SGD]] -> [[확률적 경사 하강법|SGD]]
  이름이 볼트에 둘 이상이면 짧게 줄이지 않고 볼트 경로로 남긴다.
    [[_pending/백엔드/AMI]]                  -> [[백엔드/AMI]]
  표 안이면 파이프 이스케이프(`\\|`)를 그대로 지킨다.

  python scripts/relink.py .            # 어디가 걸렸는지만 출력 (기본 dry-run)
  python scripts/relink.py . --apply    # 실제로 수정
  python scripts/relink.py "머신러닝/AdaGrad.md" --apply

의존성 없음 (Python 3.8+ 표준 라이브러리만 사용)
"""

import argparse
import os
import re
import sys
from pathlib import Path

# 검수 대기소 - 링크가 여기를 가리키면 안 된다
PENDING = "_pending"

EXCLUDE_DIRS = {".obsidian", ".git", ".trash", "node_modules", "_inbox"}

# 인라인 코드 또는 위키링크 - 코드 안의 `[[_pending/...]]` 은 설명문이므로 건드리면 안 된다
TOKEN_RE = re.compile(r"`[^`\n]*`|(!?)\[\[([^\]\n]+?)\]\]")

# 펜스 코드블록 - 이 안도 마찬가지다
FENCE_RE = re.compile(r"^\s*(```|~~~)")


def split_target(raw):
  """`대상#헤딩^블록|표시` 를 (대상, 꼬리) 로 나눈다 - 꼬리는 그대로 되돌려 붙인다

  표 안에서는 별칭 구분자가 `\\|` 라서 백슬래시까지 꼬리에 포함시킨다"""
  m = re.search(r"(\\?\||#|\^)", raw)
  if not m:
    return raw, ""
  return raw[:m.start()], raw[m.start():]


def vault_notes(vault):
  """(제목 -> [볼트 상대경로, ...]) - `_pending` 은 볼트가 아니므로 뺀다"""
  Titles = {}
  for root, Dirs, Files in os.walk(vault):
    Dirs[:] = [d for d in Dirs if d not in EXCLUDE_DIRS and d != PENDING and not d.startswith(".")]
    for name in Files:
      if name.endswith(".md"):
        rel = str((Path(root) / name).relative_to(vault)).replace(os.sep, "/")[:-3]
        Titles.setdefault(name[:-3], []).append(rel)
  return Titles


def resolve(target, Titles):
  """`_pending/머신러닝/학습률` -> 볼트에서 쓸 링크 대상 (바꿀 필요 없으면 None)"""
  stripped = target.strip().lstrip("/")
  if not (stripped == PENDING or stripped.startswith(PENDING + "/")):
    return None

  rel = stripped[len(PENDING) + 1:]
  title = rel.split("/")[-1]
  Same = Titles.get(title, [])

  if len(Same) == 1:
    return title            # 볼트에 하나뿐 - 볼트 관례대로 제목만
  if len(Same) > 1:
    return rel if rel in Same else Same[0]   # 동명이인 - 경로로 못박는다
  return title              # 아직 볼트에 없음 - 제목 링크로 두면 옮기는 순간 붙는다


def fix_text(text, Titles):
  """(교정본, [(원래대상, 바뀐대상), ...]) - 코드블록·인라인 코드 안은 건드리지 않는다

  이 README 처럼 `[[_pending/...]]` 을 예시로 적어 둔 문서를 망가뜨리지 않기 위해서다"""
  Changed = []

  def repl(m):
    if m.group(2) is None:          # 인라인 코드
      return m.group(0)
    target, tail = split_target(m.group(2))
    dest = resolve(target, Titles)
    if dest is None:
      return m.group(0)
    Changed.append((target.strip(), dest))
    return "%s[[%s%s]]" % (m.group(1), dest, tail)

  Out, fence = [], None
  for line in text.split("\n"):
    m = FENCE_RE.match(line)
    if m:
      fence = None if fence == m.group(1) else (fence or m.group(1))
      Out.append(line)
      continue
    Out.append(line if fence else TOKEN_RE.sub(repl, line))
  return "\n".join(Out), Changed


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
  ap = argparse.ArgumentParser(description="_pending 을 가리키는 링크를 볼트 링크로 되돌린다")
  ap.add_argument("target", nargs="?", default=".", help="볼트 루트 또는 md 파일 (기본 .)")
  ap.add_argument("--vault", default=None, help="볼트 루트 (target 이 파일일 때 필요, 기본은 자동 추정)")
  ap.add_argument("--apply", action="store_true", help="실제로 파일을 수정한다 (기본은 dry-run)")
  args = ap.parse_args()

  target = Path(args.target).resolve()
  if not target.exists():
    print("경로가 없습니다 : %s" % target, file=sys.stderr)
    return 1

  vault = Path(args.vault).resolve() if args.vault else (target if target.is_dir() else target.parent)
  # 파일 하나만 고칠 때도 볼트 전체를 알아야 동명이인을 판단할 수 있다
  if not args.vault and target.is_file():
    up = target.parent
    while up.parent != up and not (up / ".obsidian").is_dir():
      up = up.parent
    if (up / ".obsidian").is_dir():
      vault = up

  Titles = vault_notes(vault)
  total_files, total_links = 0, 0

  for path in iter_md(target):
    try:
      text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
      print("[warn] 읽기 실패 : %s (%s)" % (path, e), file=sys.stderr)
      continue
    if PENDING not in text:
      continue
    new, Changed = fix_text(text, Titles)
    if not Changed:
      continue

    total_files += 1
    total_links += len(Changed)
    rel = str(path.relative_to(vault)).replace(os.sep, "/") if vault in path.parents else str(path)
    print("%s  (%d개)" % (rel, len(Changed)))
    for src, dest in Changed:
      print("    %s  ->  %s" % (src, dest))

    if args.apply:
      path.write_text(new, encoding="utf-8")

  if not total_files:
    print("_pending 을 가리키는 링크 없음")
    return 0

  mode = "적용 완료" if args.apply else "dry-run (실제 수정 없음)"
  print("\n%s : 파일 %d개, 링크 %d개" % (mode, total_files, total_links))
  return 0


if __name__ == "__main__":
  try:
    sys.exit(main())
  except KeyboardInterrupt:
    sys.exit(130)
