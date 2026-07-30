#!/usr/bin/env python3
"""
ingest.py

노션 export 를 볼트가 먹을 수 있는 형태로 정규화한다
_inbox 에 zip 을 던지든 압축을 푼 폴더를 던지든 md 하나만 던지든 똑같이 처리한다

  1) zip 이면 임시 폴더에 풀고(안에 Part-1.zip 이 또 있으면 그것도 푼다),
     폴더면 그대로, md 하나면 같은 이름의 형제 폴더를 자원 폴더로 본다
  2) md 안의 이미지 참조를 전부 찾아 실제 파일을 해석한다
     - `![alt](image%201.png)`  마크다운 링크
     - `![[image 1.png]]`       이미 위키링크인 것
     - 한글 파일명 이중 인코딩(`%25ED%2595...`)도 풀어서 찾는다
  3) 이미지를 볼트 images/ 로 옮기고 `노트슬러그-01.png` 식으로 재명명한다
     - 내용(sha256)이 같은 파일이 이미 images/ 에 있으면 복사하지 않고 그걸 재사용
     - 이름이 겹치면 번호를 올린다 (기존 `image 1 1.png` 같은 충돌 방지)
  4) 모든 참조를 `![[새이름.png]]` 위키링크로 바꾸고 파일명에서 노션 해시를 떼어
     _inbox 루트에 정리된 md 를 쓴다  ->  watch.py 가 이걸 집어 분해 파이프라인을 돈다
  5) 원본(zip / 폴더 / 해시 붙은 md)은 _inbox/_done 으로 치운다

의존성 없음 (표준 라이브러리만 사용)

사용 예:
  python ingest.py --vault .                       # _inbox 에 쌓인 것 전부 처리
  python ingest.py _inbox\\퍼셉트론.zip --vault .
  python ingest.py --vault . --dry-run             # 뭘 할지만 출력
"""

import argparse
import hashlib
import os
import re
import shutil
import sys
import tempfile
import time
import urllib.parse
import zipfile
from pathlib import Path

WIN_FORBIDDEN = r'[\\/:*?"<>|]'
NOTION_HASH = re.compile(r"[ _-]+[0-9a-f]{32}$")

# 임베드로 쓸 확장자 - 나머지 첨부는 `[[ ]]` 링크로 건다
MEDIA_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".avif",
             ".mp4", ".webm", ".mov", ".mp3", ".wav", ".m4a", ".ogg", ".pdf"}
EXTERNAL = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//|#)", re.I)

MD_LINK = re.compile(r"(!?)\[([^\]\n]*)\]\(\s*<?([^)>\n]+?)>?\s*\)")
WIKI_LINK = re.compile(r"(!?)\[\[([^\]|#\n]+?)((?:\||#)[^\]\n]*)?\]\]")


# ---------------------------------------------------------------------------
# 이름 다루기
# ---------------------------------------------------------------------------

def strip_hash(name):
  """'퍼셉트론 3993a7483f97808cb9a4f750e8e0bdf0' -> '퍼셉트론'"""
  return NOTION_HASH.sub("", name).strip()


def safe_name(title):
  name = re.sub(WIN_FORBIDDEN, " ", title).strip().rstrip(".")
  return re.sub(r"\s+", " ", name) or "untitled"


def slugify(name):
  """이미지 접두어로 쓸 짧은 이름 - 공백은 하이픈, 길면 자른다"""
  s = safe_name(strip_hash(name))
  s = re.sub(r"[\s_]+", "-", s).strip("-")
  return s[:40] or "attach"


def sha256(path):
  h = hashlib.sha256()
  with open(path, "rb") as f:
    for chunk in iter(lambda: f.read(1 << 20), b""):
      h.update(chunk)
  return h.hexdigest()


# ---------------------------------------------------------------------------
# 참조 해석
# ---------------------------------------------------------------------------

def decodings(target):
  """노션은 한글 파일명을 이중 인코딩해서 링크에 박는다 - 후보를 순서대로 만든다"""
  Cand, cur = [], target
  for _ in range(3):
    if cur not in Cand:
      Cand.append(cur)
    nxt = urllib.parse.unquote(cur)
    if nxt == cur:
      break
    cur = nxt
  return Cand


class Resolver:
  """md 기준 상대경로 -> 실제 파일. 못 찾으면 자원 폴더에서 파일명으로 뒤진다"""

  def __init__(self, md_path, Roots):
    self.base = md_path.parent
    self.Roots = Roots
    self.ByName = {}
    for root in Roots:
      for p in sorted(root.rglob("*")):
        if p.is_file() and p.suffix.lower() != ".md":
          self.ByName.setdefault(p.name, p)

  def resolve(self, target):
    if not target or EXTERNAL.match(target):
      return None
    for cand in decodings(target.replace("\\", "/")):
      hit = (self.base / cand)
      if hit.is_file():
        return hit.resolve()
      hit = self.ByName.get(Path(cand).name)
      if hit:
        return hit.resolve()
    return None


# ---------------------------------------------------------------------------
# images/ 로 옮기기
# ---------------------------------------------------------------------------

class Store:
  """볼트 images/ 를 관리한다 - 내용 중복 회피 + 이름 충돌 회피"""

  def __init__(self, images_dir, dedupe=True, dry_run=False):
    self.dir = images_dir
    self.dedupe = dedupe
    self.dry_run = dry_run
    self.dir.mkdir(parents=True, exist_ok=True)
    self.Taken = {p.name for p in self.dir.iterdir() if p.is_file()}
    self.ByHash = {}
    if dedupe:
      for p in sorted(self.dir.iterdir()):
        if p.is_file():
          self.ByHash.setdefault(sha256(p), p.name)

  def put(self, src, slug):
    """반환 : (볼트 내 파일명, 재사용 여부)"""
    if self.dedupe:
      digest = sha256(src)
      if digest in self.ByHash:
        return self.ByHash[digest], True

    ext = src.suffix.lower() or ".bin"
    n = 1
    while True:
      name = "%s-%02d%s" % (slug, n, ext)
      if name not in self.Taken:
        break
      n += 1

    self.Taken.add(name)
    if self.dedupe:
      self.ByHash[digest] = name
    if not self.dry_run:
      shutil.copy2(src, self.dir / name)
    return name, False


# ---------------------------------------------------------------------------
# md 재작성
# ---------------------------------------------------------------------------

def rewrite(text, resolver, store, slug, Log):
  """이미지·첨부 참조를 전부 볼트 위키링크로 바꾼다"""
  Mapped = {}

  def adopt(src):
    key = str(src)
    if key not in Mapped:
      name, reused = store.put(src, slug)
      Mapped[key] = name
      Log.append((src.name, name, reused))
    return Mapped[key]

  def embed(name):
    return "![[%s]]" % name if Path(name).suffix.lower() in MEDIA_EXT else "[[%s]]" % name

  def on_md(m):
    bang, alt, target = m.group(1), m.group(2), m.group(3)
    src = resolver.resolve(target)
    if not src:
      return m.group(0)
    name = adopt(src)
    if bang:
      return embed(name)                    # 임베드는 임베드로, 링크는 링크로 유지한다
    return "[[%s|%s]]" % (name, alt) if alt else "[[%s]]" % name

  def on_wiki(m):
    bang, target, tail = m.group(1), m.group(2), m.group(3) or ""
    src = resolver.resolve(target)
    if not src:
      return m.group(0)          # 이미 볼트에 있는 노트/이미지 - 건드리지 않는다
    name = adopt(src)
    return "%s[[%s%s]]" % (bang or "!", name, tail)

  text = MD_LINK.sub(on_md, text)
  text = WIKI_LINK.sub(on_wiki, text)
  return text


# ---------------------------------------------------------------------------
# 처리 단위 찾기
# ---------------------------------------------------------------------------

def needs_ingest(md):
  """이미 정리된 md 를 다시 집어 무한루프 도는 걸 막는다"""
  if NOTION_HASH.search(md.stem):
    return True
  if (md.parent / md.stem).is_dir():
    return True
  try:
    text = md.read_text(encoding="utf-8")
  except (OSError, UnicodeDecodeError):
    return False
  return any(not EXTERNAL.match(m.group(3)) for m in MD_LINK.finditer(text))


def find_units(inbox):
  """(종류, 경로) 목록 - zip / 폴더 / 해시 붙은 md"""
  Units = []
  for p in sorted(inbox.iterdir()):
    if p.name.startswith(".") or p.name == "_done":
      continue
    if p.is_file() and p.suffix.lower() == ".zip":
      Units.append(("zip", p))
    elif p.is_dir():
      Units.append(("dir", p))
    elif p.is_file() and p.suffix.lower() == ".md" and needs_ingest(p):
      Units.append(("md", p))
  # 형제 폴더를 가진 md 가 있으면 그 폴더는 단독 단위에서 제외한다
  Owned = {(p.parent / p.stem).resolve() for kind, p in Units if kind == "md"}
  return [(k, p) for k, p in Units if not (k == "dir" and p.resolve() in Owned)]


def stash(path, done):
  done.mkdir(parents=True, exist_ok=True)
  target = done / path.name
  if target.exists():
    target = done / ("%s_%d%s" % (path.stem, int(time.time()), path.suffix))
  shutil.move(str(path), str(target))
  return target


def unique_md(inbox, stem):
  out = inbox / (stem + ".md")
  n = 2
  while out.exists():
    out = inbox / ("%s-%d.md" % (stem, n))
    n += 1
  return out


def unzip(src, dest, depth=0):
  """노션은 export 가 크면 zip 안에 Part-1.zip 을 또 넣는다 - 끝까지 푼다"""
  with zipfile.ZipFile(src) as z:
    z.extractall(dest)
  if depth >= 4:                                    # zip 폭탄 방어
    return
  for inner in sorted(dest.rglob("*.zip")):
    if not inner.is_file():
      continue
    sub = inner.with_suffix("")
    n = 2
    while sub.exists():
      sub = inner.with_name("%s-%d" % (inner.stem, n))
      n += 1
    sub.mkdir(parents=True)
    unzip(inner, sub, depth + 1)
    inner.unlink()                                  # 껍데기는 지운다


# ---------------------------------------------------------------------------
# 단위 하나 처리
# ---------------------------------------------------------------------------

def process(kind, path, inbox, store, dry_run):
  print("\n=== %s (%s) ===" % (path.name, kind))
  tmp = None
  try:
    if kind == "zip":
      tmp = Path(tempfile.mkdtemp(prefix="notion_"))
      unzip(path, tmp)
      Roots, Docs = [tmp], sorted(tmp.rglob("*.md"))
    elif kind == "dir":
      Roots, Docs = [path], sorted(path.rglob("*.md"))
    else:
      sibling = path.parent / path.stem
      Roots = [sibling] if sibling.is_dir() else []
      Docs = [path]

    if not Docs:
      Found = sorted({p.suffix.lower() or "(확장자 없음)"
                      for r in (Roots or [path.parent]) if r.is_dir()
                      for p in r.rglob("*") if p.is_file()})
      print("  md 가 없습니다 - 건너뜀 (안에 있는 것 : %s)" % (", ".join(Found) or "비어 있음"))
      print("  노션에서 Export format 을 'Markdown & CSV' 로 받았는지 확인하세요")
      return 0

    made, Plan = 0, []
    for md in Docs:
      stem = safe_name(strip_hash(md.stem))
      slug = slugify(md.stem)
      Base = Roots or [md.parent]
      resolver = Resolver(md, [r for r in Base if r.is_dir()])

      Log = []
      text = rewrite(md.read_text(encoding="utf-8"), resolver, store, slug, Log)
      Plan.append((md, stem, text, Log))

    # 인박스에 그냥 놓인 md 인데 바꿀 게 하나도 없으면 손대지 않고 watch 에 넘긴다
    if kind == "md" and not any(L or s != d.stem for d, s, _, L in Plan):
      print("  바뀔 내용 없음 - 그대로 둠")
      return 0

    for md, stem, text, Log in Plan:
      out = unique_md(inbox, stem)
      print("  %s  ->  %s" % (md.name, out.name))
      for orig, name, reused in Log:
        print("    %s %s  ->  %s" % ("=" if reused else "+", orig, name))
      if not Log:
        print("    (옮길 첨부 없음)")
      if not dry_run:
        out.write_text(text, encoding="utf-8")
      made += 1

    if not dry_run:
      done = inbox / "_done"
      stash(path, done)
      if kind == "md":
        sib = path.parent / path.stem
        if sib.is_dir():
          stash(sib, done)
    return made
  finally:
    if tmp and tmp.exists():
      shutil.rmtree(tmp, ignore_errors=True)


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
  ap = argparse.ArgumentParser(description="노션 export -> 볼트 형식으로 정규화")
  ap.add_argument("source", nargs="?", help="zip / 폴더 / md (생략하면 _inbox 전체)")
  ap.add_argument("--vault", default=".", help="볼트 루트")
  ap.add_argument("--inbox", default="_inbox")
  ap.add_argument("--images", default="images", help="첨부를 모을 폴더")
  ap.add_argument("--no-dedupe", action="store_true", help="내용이 같아도 새 파일로 복사")
  ap.add_argument("--dry-run", action="store_true", help="쓰지 않고 계획만 출력")
  args = ap.parse_args()

  vault = Path(args.vault).resolve()
  inbox = vault / args.inbox
  inbox.mkdir(parents=True, exist_ok=True)

  if args.source:
    src = Path(args.source).resolve()
    if not src.exists():
      raise SystemExit("찾을 수 없습니다 : %s" % src)
    kind = "zip" if src.suffix.lower() == ".zip" else ("dir" if src.is_dir() else "md")
    Units = [(kind, src)]
  else:
    Units = find_units(inbox)

  if not Units:
    return 0

  store = Store(vault / args.images, dedupe=not args.no_dedupe, dry_run=args.dry_run)
  total = 0
  for kind, path in Units:
    try:
      total += process(kind, path, inbox, store, args.dry_run)
    except Exception as e:                                    # 하나 실패해도 나머지는 계속
      print("  [error] %s : %s" % (path.name, e))

  print("\n정규화 %d개%s" % (total, " (dry-run)" if args.dry_run else ""))
  return 0


if __name__ == "__main__":
  try:
    sys.exit(main())
  except KeyboardInterrupt:
    sys.exit(130)
