#!/usr/bin/env python3
"""
obsidian_autolink.py

옵시디언 볼트를 스캔해 노트 제목 / alias 를 인덱스로 만들고,
본문에 등장하는 개념어를 [[ ]] 위키링크로 자동 변환한다

의존성 없음 (Python 3.8+ 표준 라이브러리만 사용)

사용 예:
  python3 obsidian_autolink.py .                  # dry-run, 무엇이 바뀔지만 출력
  python3 obsidian_autolink.py . --apply          # 실제로 파일 수정
  python3 obsidian_autolink.py . --index          # 인덱스만 출력
  python3 obsidian_autolink.py . --report         # 중복 제목 / 충돌 보고서
  python3 obsidian_autolink.py . --only "백엔드/Java" --apply
"""

import argparse
import os
import re
import sys
from pathlib import Path

from mdtable import in_table_row

# ---------------------------------------------------------------------------
# 설정 기본값
# ---------------------------------------------------------------------------

# _inbox 는 아직 볼트가 아니다 - 인덱스에 넣으면 LLM 이 _inbox 를 폴더로 착각한다
# _pending 은 검수 대기 노트끼리 링크가 걸려야 하므로 제외하지 않는다
DEFAULT_EXCLUDE_DIRS = {".obsidian", ".git", ".trash", "node_modules", "templates", "_templates", "_inbox"}

# 파이프라인 대기소 - 링크 삽입 대상은 되지만 링크 대상 사전에는 올리지 않는다
PIPELINE_PREFIXES = ("_pending/", "_inbox/")

# decompose.py 가 수정판에 붙이는 마커 (`학습률.updated.md`)
UPDATED_SUFFIX = ".updated"

# 너무 흔해서 링크로 만들면 소음이 되는 단어
DEFAULT_STOPWORDS = {
  "개요", "정리", "요약", "메모", "index", "readme", "home", "untitled",
  "TODO", "노트", "기타", "참고", "목차",
}

# 한글 조사 - 긴 것부터 매칭해야 하므로 길이 내림차순으로 정렬해 사용한다
JOSA = [
  "이라는", "라는", "이라고", "라고", "이란", "이나", "으로써", "으로서", "로써", "로서",
  "에서는", "에서의", "에서", "에게서", "에게는", "에게", "으로는", "으로도", "으로",
  "까지", "부터", "보다", "처럼", "만큼", "마다", "조차", "이든", "든지", "이며",
  "이고", "이다", "입니다", "한다", "하는", "하면", "해서", "와의", "과의",
  "은", "는", "이", "가", "을", "를", "의", "에", "와", "과", "도", "만",
  "로", "라", "다", "요", "고", "며", "면", "임", "인", "일", "할", "함",
]
JOSA.sort(key=len, reverse=True)

HANGUL_RE = re.compile(r"[\uac00-\ud7a3\u1100-\u11ff\u3130-\u318f]")

# 링크를 넣으면 안 되는 구간 - 순서 중요 (앞쪽이 우선 보호된다)
PROTECT_PATTERNS = [
  (r"^---\n.*?\n---\n", re.DOTALL),          # YAML frontmatter (파일 맨 앞)
  (r"```.*?```", re.DOTALL),                  # 펜스 코드블록
  (r"~~~.*?~~~", re.DOTALL),                  # 펜스 코드블록 (물결)
  (r"\$\$.*?\$\$", re.DOTALL),                # 수식 블록
  (r"<!--.*?-->", re.DOTALL),                 # HTML 주석
  (r"!\[\[[^\]]*\]\]", 0),                    # 임베드
  (r"\[\[[^\]]*\]\]", 0),                     # 이미 걸린 위키링크
  (r"!?\[[^\]]*\]\([^)]*\)", 0),              # 마크다운 링크 / 이미지
  (r"`[^`\n]+`", 0),                          # 인라인 코드
  (r"\$[^$\n]+\$", 0),                        # 인라인 수식
  (r"https?://\S+", 0),                       # 맨 URL
  (r"^#{1,6}[ \t].*$", re.MULTILINE),         # 헤딩 라인
  (r"^\s*>\s*\[!\w+\].*$", re.MULTILINE),     # 콜아웃 헤더
  (r"(?<![\w가-힣])#[\w가-힣/_-]+", 0),        # 태그
  (r"<[^>\n]{1,80}>", 0),                     # 인라인 HTML 태그
]


# ---------------------------------------------------------------------------
# frontmatter 파싱
# ---------------------------------------------------------------------------

def split_frontmatter(text):
  """(frontmatter 문자열, 본문 시작 오프셋) 반환 - 없으면 ('', 0)"""
  if not text.startswith("---\n"):
    return "", 0
  end = text.find("\n---", 3)
  if end == -1:
    return "", 0
  stop = text.find("\n", end + 1)
  stop = len(text) if stop == -1 else stop + 1
  return text[4:end], stop


def parse_aliases(front):
  """frontmatter 에서 aliases / alias 값을 리스트로 뽑는다 (YAML 라이브러리 없이)"""
  Aliases = []
  lines = front.split("\n")
  i = 0
  while i < len(lines):
    line = lines[i]
    m = re.match(r"^(aliases|alias)\s*:\s*(.*)$", line, re.IGNORECASE)
    if not m:
      i += 1
      continue
    rest = m.group(2).strip()
    if rest.startswith("[") and rest.endswith("]"):
      # 인라인 형태: aliases: [GC, Garbage Collection]
      body = rest[1:-1]
      Aliases += [s.strip().strip("\"'") for s in body.split(",")]
    elif rest:
      # 단일 값 형태: aliases: GC
      Aliases.append(rest.strip("\"'"))
    else:
      # 블록 형태:
      #   aliases:
      #     - GC
      j = i + 1
      while j < len(lines):
        item = re.match(r"^\s*-\s*(.+?)\s*$", lines[j])
        if not item:
          break
        Aliases.append(item.group(1).strip("\"'"))
        j += 1
      i = j - 1
    i += 1
  return [a for a in Aliases if a]


def parse_flag(front, key):
  """frontmatter 의 bool 플래그를 읽는다 - 없으면 None"""
  m = re.search(r"^%s\s*:\s*(\S+)\s*$" % re.escape(key), front, re.MULTILINE | re.IGNORECASE)
  if not m:
    return None
  return m.group(1).strip().lower() in ("true", "yes", "1", "on")


# ---------------------------------------------------------------------------
# 인덱스 구축
# ---------------------------------------------------------------------------

class Note:
  def __init__(self, path, rel, title, aliases, autolink_in, autolink_out):
    self.path = path
    self.rel = rel
    self.title = title
    self.aliases = aliases
    self.autolink_in = autolink_in    # 이 노트를 링크 대상으로 삼을지
    self.autolink_out = autolink_out  # 이 노트 본문에 링크를 넣을지


def collect_notes(vault, exclude_dirs):
  Notes = []
  for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith(".")]
    for name in files:
      if not name.endswith(".md"):
        continue
      path = Path(root) / name
      rel = str(path.relative_to(vault)).replace(os.sep, "/")
      try:
        text = path.read_text(encoding="utf-8")
      except (UnicodeDecodeError, OSError) as e:
        print("[warn] 읽기 실패 : %s (%s)" % (rel, e), file=sys.stderr)
        continue
      front, _ = split_frontmatter(text)
      Notes.append(Note(
        path=path,
        rel=rel,
        title=path.stem,
        aliases=parse_aliases(front),
        autolink_in=parse_flag(front, "autolink-in") is not False,
        autolink_out=parse_flag(front, "autolink") is not False,
      ))
  return Notes


def build_index(Notes, min_len, stopwords):
  """
  term -> [Note, ...] 매핑을 만든다
  같은 term 이 여러 노트를 가리키면 모호(ambiguous)로 분류한다
  """
  Terms = {}
  for note in Notes:
    if not note.autolink_in:
      continue
    for term in [note.title] + note.aliases:
      key = term.strip()
      if len(key) < min_len:
        continue
      if key.lower() in {s.lower() for s in stopwords}:
        continue
      Terms.setdefault(key, [])
      if note not in Terms[key]:
        Terms[key].append(note)

  Resolved, Ambiguous = {}, {}
  for term, notes in Terms.items():
    if len(notes) == 1:
      Resolved[term] = notes[0]
    else:
      Ambiguous[term] = notes
  return Resolved, Ambiguous


# ---------------------------------------------------------------------------
# 보호 구간 마스킹
# ---------------------------------------------------------------------------

def build_mask(text):
  """링크를 넣으면 안 되는 위치를 True 로 표시한 바이트 마스크"""
  Mask = bytearray(len(text))
  for pattern, flags in PROTECT_PATTERNS:
    for m in re.finditer(pattern, text, flags):
      for i in range(m.start(), m.end()):
        Mask[i] = 1
  return Mask


def is_free(Mask, start, end):
  return not any(Mask[start:end])


# ---------------------------------------------------------------------------
# 경계 검사 (한글 조사 처리 포함)
# ---------------------------------------------------------------------------

def is_hangul(ch):
  return bool(HANGUL_RE.match(ch))


def is_ascii_word(ch):
  return ch.isascii() and (ch.isalnum() or ch == "_")


def left_ok(text, start):
  if start == 0:
    return True
  prev = text[start - 1]
  if is_hangul(prev) or is_ascii_word(prev):
    return False
  return True


def consume_josa(text, pos, depth=0):
  """pos 부터 조사가 연달아 붙은 경우까지 소비하고 끝나면 True ('이라고도', '에서만' 등)"""
  if pos >= len(text) or not is_hangul(text[pos]):
    return True
  if depth >= 3:
    return False
  for j in JOSA:
    if text.startswith(j, pos) and consume_josa(text, pos + len(j), depth + 1):
      return True
  return False


def right_ok(text, end):
  """뒤에 조사가 붙는 경우만 허용하고, 다른 한글이 이어지면 거부한다"""
  if end >= len(text):
    return True
  nxt = text[end]
  if is_ascii_word(nxt):
    return False
  if is_hangul(nxt):
    return consume_josa(text, end)
  return True


# ---------------------------------------------------------------------------
# 링크 삽입
# ---------------------------------------------------------------------------

def scan_wikilinks(Notes):
  """볼트 전체의 [[ ]] 링크를 모아 (대상, 참조한 노트) 목록으로 반환한다 (임베드 제외)"""
  Refs = []
  for note in Notes:
    try:
      text = note.path.read_text(encoding="utf-8")
    except OSError:
      continue
    for m in re.finditer(r"(?<!!)\[\[([^\]]+)\]\]", text):
      raw = m.group(1)
      target = raw.split("|")[0].split("#")[0].split("^")[0].strip().rstrip("/")
      if target:
        Refs.append((target, note.rel))
  return Refs


def unresolved_links(Notes):
  """
  아직 파일이 없는 링크 대상을 참조 횟수 순으로 반환한다
  이게 '앞으로 써야 할 노트' 백로그이자, LLM 에 넘길 예약어 목록이 된다
  """
  Known = set()
  for note in Notes:
    Known.add(note.title)
    Known.add(note.rel[:-3])
    for a in note.aliases:
      Known.add(a)

  Missing = {}
  for target, src in scan_wikilinks(Notes):
    if target in Known or target.split("/")[-1] in Known:
      continue
    if re.search(r"\.(png|jpg|jpeg|gif|svg|webp|pdf|excalidraw)$", target, re.IGNORECASE):
      continue
    Missing.setdefault(target, []).append(src)
  return Missing





_SCANNER_CACHE = {}


def compile_scanner(Resolved):
  """모든 term 을 하나의 정규식으로 합쳐 파일당 1회만 스캔한다 (긴 term 이 앞에 와야 우선 매칭됨)"""
  key = id(Resolved)
  if key not in _SCANNER_CACHE:
    Terms = sorted(Resolved.keys(), key=len, reverse=True)
    _SCANNER_CACHE[key] = re.compile("|".join(re.escape(t) for t in Terms))
  return _SCANNER_CACHE[key]


def existing_link_counts(text):
  """이미 본문에 걸려 있는 위키링크의 대상별 개수 - 재실행 시 중복 링크를 막는다"""
  Counts = {}
  for m in re.finditer(r"(?<!!)\[\[([^\]\|#\^]+)", text):
    target = m.group(1).strip().rstrip("/")
    for key in {target, target.split("/")[-1]}:
      Counts[key] = Counts.get(key, 0) + 1
  return Counts


def vault_counterpart(rel):
  """_pending 파일이 볼트의 어느 노트에 해당하는지 - 대응이 없으면 그대로 돌려준다

  수정판(`_pending/머신러닝/학습률.updated.md`)은 검수 후 볼트 원본(`머신러닝/학습률.md`)에
  덮어쓸 내용이다. 이걸 모르면 자동 링크가 수정판 본문에 `[[학습률]]` 을 넣고,
  그 자기 자신 링크가 볼트 원본까지 따라 들어간다"""
  for p in PIPELINE_PREFIXES:
    if rel.startswith(p):
      rel = rel[len(p):]
      break
  tail = UPDATED_SUFFIX + ".md"
  return rel[:-len(tail)] + ".md" if rel.endswith(tail) else rel


def find_matches(text, Mask, Resolved, self_note, max_per_target, use_path):
  """
  (start, end, 치환문자열, term, 대상경로) 리스트를 반환한다
  1) 긴 term 부터 구간을 선점해 'JVM 메모리 구조' 가 'JVM' 보다 우선하도록 한다
  2) 대상 노트별로 앞쪽 등장분만 예산만큼 남긴다
  """
  Candidates = []
  scanner = compile_scanner(Resolved)
  # 자기 자신 링크 금지 - _pending 수정판은 볼트 원본을 자기 자신으로 본다
  Self = {self_note.rel, vault_counterpart(self_note.rel)} if self_note is not None else set()

  for m in scanner.finditer(text):
    s, e = m.start(), m.end()
    term = m.group(0)
    target = Resolved[term]
    if target.rel in Self:
      continue
    if not is_free(Mask, s, e):
      continue
    if not left_ok(text, s) or not right_ok(text, e):
      continue
    Candidates.append((s, e, term, target))

  Existing = existing_link_counts(text)
  Budget = {}
  Matches = []

  for s, e, term, target in sorted(Candidates, key=lambda x: x[0]):
    stem = target.rel[:-3]
    if stem not in Budget:
      used = max(Existing.get(target.title, 0), Existing.get(stem, 0))
      Budget[stem] = max_per_target - used
    if Budget[stem] <= 0:
      continue

    dest = stem if use_path else target.title
    if term == target.title and not use_path:
      repl = "[[%s]]" % term
    else:
      # 표 셀 안에서는 `|` 가 셀 구분자다 - 그냥 넣으면 표가 밀린다
      bar = "\\|" if in_table_row(text, s) else "|"
      repl = "[[%s%s%s]]" % (dest, bar, term)

    Matches.append((s, e, repl, term, target.rel))
    Budget[stem] -= 1

  return Matches


def apply_matches(text, Matches):
  out, cursor = [], 0
  for s, e, repl, _term, _rel in Matches:
    out.append(text[cursor:s])
    out.append(repl)
    cursor = e
  out.append(text[cursor:])
  return "".join(out)


def line_of(text, pos):
  return text.count("\n", 0, pos) + 1


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
  ap = argparse.ArgumentParser(description="옵시디언 볼트 자동 위키링크 삽입")
  ap.add_argument("vault", help="볼트 루트 경로")
  ap.add_argument("--apply", action="store_true", help="실제로 파일을 수정한다 (기본은 dry-run)")
  ap.add_argument("--index", action="store_true", help="인덱스만 출력하고 종료")
  ap.add_argument("--report", action="store_true", help="모호한 제목 보고서만 출력하고 종료")
  ap.add_argument("--unresolved", action="store_true",
                  help="아직 파일이 없는 [[ ]] 링크를 참조 횟수 순으로 출력 (앞으로 쓸 노트 백로그)")
  ap.add_argument("--write-index", default=None,
                  help="기존 노트 + 미해결 링크를 TSV 로 저장 (LLM 프롬프트에 넣을 사전)")
  ap.add_argument("--only", default=None, help="이 경로 접두사에 해당하는 노트만 처리")
  ap.add_argument("--min-len", type=int, default=2, help="링크 대상 최소 글자 수 (기본 2)")
  ap.add_argument("--max-per-target", type=int, default=1,
                  help="한 노트에서 같은 대상 노트로 몇 번까지 링크할지 (기본 1)")
  ap.add_argument("--path-links", action="store_true",
                  help="[[폴더/제목|표시]] 형태의 경로 포함 링크를 생성")
  ap.add_argument("--stopwords", default=None, help="제외할 단어 목록 파일 (한 줄에 하나)")
  args = ap.parse_args()

  vault = Path(args.vault).resolve()
  if not vault.is_dir():
    print("볼트 경로가 아닙니다 : %s" % vault, file=sys.stderr)
    return 1

  Stopwords = set(DEFAULT_STOPWORDS)
  if args.stopwords:
    Stopwords |= {l.strip() for l in Path(args.stopwords).read_text(encoding="utf-8").splitlines() if l.strip()}

  Notes = collect_notes(vault, DEFAULT_EXCLUDE_DIRS)
  # _pending 은 아직 볼트가 아니다 - 링크 대상 사전과 미해결 목록에서 빼야 한다
  # (빼지 않으면 검수 대기 중인 노트가 사전에 올라가 decompose 가 그걸 기존 노트로 착각한다)
  # --only _pending 으로 수정하는 대상에서는 빠지지 않는다
  Vault = [n for n in Notes if not any(n.rel.startswith(p) for p in PIPELINE_PREFIXES)]
  Resolved, Ambiguous = build_index(Vault, args.min_len, Stopwords)

  print("노트 %d개 / 링크 가능 개념 %d개 / 모호한 개념 %d개\n" % (len(Vault), len(Resolved), len(Ambiguous)))

  if args.write_index:
    Lines = ["# kind\tterm\ttarget"]
    for term in sorted(Resolved):
      Lines.append("note\t%s\t%s" % (term, Resolved[term].rel[:-3]))
    for term, srcs in sorted(unresolved_links(Vault).items(), key=lambda x: -len(x[1])):
      Lines.append("stub\t%s\t(%d회 참조, 아직 없음)" % (term, len(srcs)))
    Path(args.write_index).write_text("\n".join(Lines) + "\n", encoding="utf-8")
    print("인덱스 저장 : %s (%d줄)" % (args.write_index, len(Lines) - 1))
    return 0

  if args.unresolved:
    Missing = unresolved_links(Vault)
    if not Missing:
      print("미해결 링크 없음")
      return 0
    print("아직 파일이 없는 링크 %d개 (참조 많은 순) :\n" % len(Missing))
    for term, srcs in sorted(Missing.items(), key=lambda x: (-len(x[1]), x[0])):
      print("  %3d회  %s" % (len(srcs), term))
      for s in sorted(set(srcs))[:3]:
        print("           <- %s" % s)
    return 0

  if args.index:
    for term in sorted(Resolved):
      print("%s\t%s" % (term, Resolved[term].rel))
    return 0

  if args.report:
    if not Ambiguous:
      print("모호한 제목 없음")
      return 0
    print("아래 개념은 같은 이름의 노트가 둘 이상이라 자동 링크에서 제외했습니다.")
    print("제목을 유니크하게 바꾸거나 --path-links 를 쓰세요.\n")
    for term in sorted(Ambiguous):
      print("  %s" % term)
      for n in Ambiguous[term]:
        print("      - %s" % n.rel)
    return 0

  if Ambiguous:
    print("[warn] 모호한 개념 %d개는 건너뜁니다. --report 로 목록을 확인하세요.\n" % len(Ambiguous))

  total_files, total_links = 0, 0
  for note in Notes:
    if not note.autolink_out:
      continue
    if args.only and not note.rel.startswith(args.only):
      continue

    text = note.path.read_text(encoding="utf-8")
    Mask = build_mask(text)
    Matches = find_matches(text, Mask, Resolved, note, args.max_per_target, args.path_links)
    if not Matches:
      continue

    total_files += 1
    total_links += len(Matches)
    print("%s  (+%d)" % (note.rel, len(Matches)))
    for s, e, repl, term, rel in Matches:
      print("    L%-5d %s  ->  %s" % (line_of(text, s), term, repl))

    if args.apply:
      note.path.write_text(apply_matches(text, Matches), encoding="utf-8")

  mode = "적용 완료" if args.apply else "dry-run (실제 수정 없음)"
  print("\n%s : 파일 %d개, 링크 %d개" % (mode, total_files, total_links))
  return 0


if __name__ == "__main__":
  try:
    sys.exit(main())
  except BrokenPipeError:
    # head 등으로 파이프를 끊었을 때 조용히 종료
    os.dup2(os.open(os.devnull, os.O_WRONLY), sys.stdout.fileno())
    sys.exit(0)
  except KeyboardInterrupt:
    sys.exit(130)
