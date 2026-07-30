#!/usr/bin/env python3
"""
decompose.py

통합 정리 md 한 개를 받아 원자적 개념 노트 + MOC 로 분해한다
동시에 **기존 볼트 노트에 덧붙일 내용**도 수정판으로 뽑는다 (2패스)

  1패스 : 문서를 읽고 '보강할 기존 노트' 목록만 고른다 (사전만 첨부, 값싸다)
  2패스 : 그 노트들의 본문 전문을 첨부해 분해 + 수정판을 함께 받는다

수정판은 볼트를 직접 건드리지 않는다. `_pending/<원본과 같은 경로>.md` 와
그 옆의 `.md.diff` 로 나오고, 사람이 검수한 뒤 덮어쓴다.

LLM 호출부는 백엔드 두 가지를 지원한다

  --backend cc    Claude Code 헤드리스 (claude -p)   : 기본값. 구독으로 청구, API 키 불필요
  --backend api   Anthropic API 직접 호출            : 결정적. 별도 ANTHROPIC_API_KEY 와 충전 필요
  --backend mock  고정 응답으로 배선만 테스트

의존성 없음 (표준 라이브러리만 사용)

사용 예:
  python decompose.py _inbox\\JVM정리.md --vault .
  python decompose.py _inbox\\JVM정리.md --vault . --show-prompt
  python decompose.py _inbox\\JVM정리.md --vault . --backend api
"""

import argparse
import difflib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

MODEL = "claude-sonnet-4-6"
API_URL = "https://api.anthropic.com/v1/messages"
WIN_FORBIDDEN = r'[\\/:*?"<>|]'

RULES = """\
너는 옵시디언 제텔카스텐 볼트를 관리한다.
아래 '통합 문서'를 이 볼트의 기존 노트와 똑같은 형식으로 원자적 개념 노트로 분해하라.

## 분해 규칙
1. 1노트 = 1개념. 다른 글에서 [[ ]] 로 부를 만한 단위가 아니면 쪼개지 마라.
2. 노트 제목이 곧 링크 이름이다. "2. 메모리 관리" 같은 목차형 제목은 금지.
3. 사전(index)에 이미 있는 개념은 반드시 그 term 을 글자 그대로 써라. 새로 짓지 마라.
   - kind=note : 이미 파일이 있는 개념
   - kind=stub : 파일은 없지만 이미 다른 노트가 예약해 둔 이름. 이것도 그대로 재사용하라.
4. 사전에 없는 개념이라도 앞으로 노트가 될 만하면 [[ ]] 를 걸어라.
   단, 한 문서에서 새로 만드는 이름은 8개를 넘기지 마라.
5. new_concepts = **링크만 걸어두고 이번에 노트로 만들지 않은** 이름들이다.
   notes 로 생성한 제목은 절대 new_concepts 에 넣지 마라.
6. 원본의 순서는 MOC 의 섹션 구성과 불릿 순서로 남긴다.
   개념 간 인과는 **개별 노트 본문**에 `->` 로 쓴다. MOC 에 문장으로 쓰지 마라.
7. 코드블록 · 수식($, $$)은 원문 그대로 보존한다.
8. 이미지는 항상 `![[파일명]]` 위키링크 임베드로 쓴다.
   원문이 `![alt](image%201.png)` 처럼 마크다운 링크면 `![[image 1.png]]` 로 바꿔라.
   경로는 버리고 파일명만 남기고, `%20` 같은 URL 인코딩은 디코드한다.

## 글쓰기 형식 — 이 볼트의 기존 노트 규칙이다. 반드시 지켜라
### 본문
- **`# 제목` 줄을 넣지 마라.** 파일명이 제목이다. 첫 불릿부터 바로 시작한다.
- **산문 단락을 쓰지 마라. 본문은 거의 전부 불릿 리스트다.**
- 노트 맨 위 = 그 개념을 정의하는 불릿 1~3개. "~에 대해 알아보자" 같은 도입부 금지.
- 하위 내용은 탭으로 중첩한다.
- **명사형으로 압축해서 끝낸다. `~이다` / `~한다` / `~된다` / `~있다` 로 끝내지 마라.**
  - O : `분산 컴퓨팅 환경에서 원만한 통신 이뤄지도록 서비스 제공`
  - O : `표준화 [[인터페이스]] -> 일관성 보장`
  - X : `분산 컴퓨팅 환경에서 통신이 원만하게 이뤄지도록 서비스를 제공한다.`
- 조사와 서술어를 아낀다. 인과 · 귀결 · 대응은 `->` 또는 `→` 로 대체한다.
- 증감은 `↑` `↓`, 가능/불가는 `O` `X` 로 쓴다.
- 소제목은 `###` (더 필요하면 `####`). 자주 쓰는 이름 :
  정의 / 종류 / 형태 / 구조 / 기능 / 상태 / 특징 / 장점 / 단점 / 절차 / 조건
- 순서가 있는 절차는 `1. 2. 3.` 번호 목록.
- 속성-설명 짝이 3개 이상이면 표를 쓴다. (`| 항목 | 내용 |`)
- 예시는 `==ex)==` 로 시작한다.
- `==하이라이트==` 는 개념이 아닌 것을 강조할 때만 쓴다. (수치, 조건, 대비되는 단어 등)
  **개념 이름은 하이라이트가 아니라 링크다.** `==임곗값==` X -> `[[임곗값]]` O
- 실행 결과처럼 접어둘 내용은 `> [!note]- 실행 결과` 콜아웃.

### 링크
- 사전의 term 을 글자 그대로 링크한다. 별칭도 term 이므로 `[[다형성(Polymorphism)]]` 처럼 직접 링크 가능.
- 문장에서 다르게 읽혀야 하면 파이프 별칭을 쓴다.
  ex) `[[RPC|RPC(Remote Procedure Call)]]`, `[[데이터베이스|DB(Database)]]`
- 같은 개념을 한 노트 안에서 여러 번 링크해도 된다. 자연스러운 자리마다 걸어라.

### aliases
- 한글 제목이면 영문 표기를, 영문 제목이면 한글 표기를 넣는다.
- `한글(English)` 결합형도 함께 넣는다.
  ex) 제목 `다형성` -> ["Polymorphism", "다형성(Polymorphism)"]

## MOC 형식
- MOC 는 **순수 링크 목록**이다. `###` 섹션 제목 + `- [[링크]]` 불릿, 그것뿐이다.
- **링크 뒤에 어떤 설명도 붙이지 마라.** `:` 로 잇는 설명, `->` 로 잇는 문구, 산문 문장 전부 금지.
  - O : `- [[가중치]]`
  - O : `- [[스크럼|스크럼(Scrum)]]`  (파이프 별칭은 허용)
  - O : `- [[Linked Stack]] / [[Linked Queue]]`  (짧게 묶는 것은 허용)
  - X : `- [[가중치]] : 각 입력 신호의 중요도`
  - X : `- [[임곗값]] -> $-b$ 치환 -> [[편향]]`
  - X : `- 세 게이트 -> [[퍼셉트론]] 구조 동일, 매개변수만 상이`
- 개념 자체가 한 섹션 단위면 `### [[개념]]` 처럼 제목에 링크를 걸어도 된다.
- 원본의 순서와 묶음은 **섹션 구성과 불릿 순서로만** 남긴다. 인과 설명은 개별 노트가 할 일이다.
- folder 는 해당 주제 폴더 아래의 `_MOC` 로 지정한다. ex) `백엔드/Java/_MOC`

## 기존 노트 보강 (updates)
'수정 대상 후보' 섹션으로 기존 노트 본문이 첨부돼 있으면, 통합 문서에 그 노트를
**보강할 내용이 있을 때만** updates 항목을 만든다. 없으면 updates 는 빈 배열이다.

허용되는 것은 세 가지뿐이다.
1. 새 불릿 · 새 `###` 섹션 추가
2. 기존 문장 안의 개념 이름에 `[[ ]]` 걸기
3. aliases 추가

**절대 금지 :**
- 기존 불릿을 지우기
- 기존 문장을 다시 쓰기 · 줄이기 · 말투 고치기 (오탈자도 건드리지 마라)
- 섹션 순서 바꾸기, 섹션 합치기
- 이미 있는 내용을 표현만 바꿔 다시 넣기 (중복 추가 금지)

`body` 에는 **원본 본문 전체를 그대로 담고 거기에 추가분을 넣은 최종 결과**를 쓴다.
원본에 있던 줄은 링크를 거는 것 말고는 글자 하나도 바꾸지 마라.
검수 스크립트가 원본 줄이 사라졌는지 자동으로 검사하므로, 지우면 경고로 잡힌다.
추가한 줄이 어디로 갔는지 `summary` 에 한 줄로 적는다.
frontmatter 는 쓰지 마라. 스크립트가 원본 frontmatter 를 보존해서 합친다.

이미 노트가 있는 개념은 notes 로 새로 만들지 말고 updates 로 보강하라.
같은 노트를 notes 와 updates 에 동시에 넣지 마라.

## 출력 형식
JSON 객체 하나만 출력한다. 설명, 인사말, 마크다운 코드펜스 모두 금지.

{
  "notes": [
    {
      "title": "가비지 컬렉션",
      "folder": "백엔드/Java",
      "aliases": ["GC", "Garbage Collection", "가비지 컬렉션(Garbage Collection)"],
      "body": "- [[JVM 메모리 구조]]의 힙 영역 대상으로 동작\\n- 참조 끊긴 [[객체]] 자동 회수 -> 메모리 누수 방지\\n\\n### 종류\\n- [[G1 GC]] : 힙을 region 단위로 분할\\n\\t- 짧은 정지 시간 목표\\n- ==ex)== `-XX:+UseG1GC`"
    }
  ],
  "updates": [
    {
      "target": "백엔드/Java/JVM.md",
      "summary": "### 종류 아래에 HotSpot 항목 추가, '클래스 로더' 에 링크",
      "add_aliases": ["Java Virtual Machine"],
      "body": "- 자바 바이트코드 실행 [[가상 머신]]\\n\\n### 구조\\n- [[클래스 로더]] : .class 적재\\n- 실행 엔진\\n\\t- HotSpot : 자주 쓰는 코드 JIT 컴파일"
    }
  ],
  "moc": {
    "title": "JVM 메모리 관리",
    "folder": "백엔드/Java/_MOC",
    "body": "### 메모리 구조\\n- [[JVM 메모리 구조]]\\n- [[객체]]\\n\\n### 회수\\n- [[가비지 컬렉션]]\\n- [[G1 GC]]"
  },
  "new_concepts": ["G1 GC"]
}
"""

SELECT_RULES = """\
너는 옵시디언 제텔카스텐 볼트를 관리한다.
아래 '통합 문서' 를 원자 노트로 분해하기 전 단계다. 지금은 노트를 쓰지 마라.

## 할 일
통합 문서의 내용으로 **보강할 만한 기존 노트**를 사전에서 골라라.
다음 단계에서 그 노트들의 본문 전문을 첨부해 줄 것이다.

## 고르는 기준
1. 통합 문서가 그 개념을 실제로 다루고, 기존 노트에 없을 만한 내용을 담고 있을 때만 고른다.
2. 사전의 **target 컬럼(경로)을 글자 그대로** 쓴다. 새로 짓거나 고치지 마라.
   ex) 사전 줄이 `가비지 컬렉션\t백엔드/Java/가비지 컬렉션` 이면 `"백엔드/Java/가비지 컬렉션"`
3. 사전에 있는 경로만 고른다. 사전에 없는 개념은 다음 단계가 새 노트로 만든다.
4. 이름만 스쳐 지나가는 개념은 고르지 마라. 링크만 걸면 되는 것은 다음 단계가 알아서 한다.
5. 날짜 노트(2026-07-30 같은 것)와 MOC(`_MOC/`) 는 고르지 마라.
6. 최대 %d개. 확신이 없으면 적게 골라라. 하나도 없으면 빈 배열.

## 출력 형식
JSON 객체 하나만 출력한다. 설명, 인사말, 코드펜스 모두 금지.

{"targets": ["백엔드/Java/JVM", "백엔드/Java/가비지 컬렉션"]}
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
    dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("_inbox", "_pending", "scripts", "images", "node_modules")]
    rel = os.path.relpath(root, vault).replace(os.sep, "/")
    if rel != ".":
      Folders.add(rel)
  return "\n".join(sorted(Folders)[:limit]) or "(폴더 없음)"


PIPELINE_DIRS = ("_pending", "_inbox", "scripts", "images", "node_modules")


def is_vault_path(rel):
  """볼트 본체 경로인지 - 파이프라인 폴더와 상위 탈출은 보강 대상이 될 수 없다"""
  Parts = [p for p in rel.replace("\\", "/").split("/") if p]
  return bool(Parts) and ".." not in Parts and Parts[0] not in PIPELINE_DIRS


def index_rows(path):
  """사전 TSV 를 (kind, term, target) 튜플로 읽는다"""
  if not path or not Path(path).exists():
    return []
  Rows = []
  for line in Path(path).read_text(encoding="utf-8").splitlines():
    if not line or line.startswith("#"):
      continue
    Cols = line.split("\t")
    if len(Cols) >= 3:
      Rows.append((Cols[0], Cols[1], Cols[2]))
  return Rows


def note_index_text(Rows, limit=1500):
  """1패스용 - 파일이 실제로 있는 개념만 (stub 은 고를 수 없으므로 제외)"""
  Lines = ["%s\t%s" % (term, target) for kind, term, target in Rows if kind == "note"]
  if not Lines:
    return "(사전 없음 - 볼트가 비어 있거나 인덱스를 아직 만들지 않음)"
  if len(Lines) > limit:
    Lines = Lines[:limit] + ["... (이하 생략)"]
  return "\n".join(Lines)


def resolve_targets(Terms, Rows, vault, cap):
  """LLM 이 고른 이름을 실제 md 경로로 바꾼다 - 별칭도 사전에 있으므로 그대로 해석된다

  term 대신 target 경로(`자료구조/스택`)를 돌려주는 경우가 흔해서 둘 다 받는다.
  같은 파일을 가리키는 이름이 여러 개면 하나로 합치고, 파일이 없으면 버린다"""
  ByTerm = {term: target for kind, term, target in Rows if kind == "note"}
  ByPath = {t[:-3] if t.endswith(".md") else t: t for t in ByTerm.values()}
  Paths, Dropped = [], []
  for term in Terms:
    key = str(term).strip().replace("\\", "/").lstrip("/")
    bare = key[:-3] if key.endswith(".md") else key
    target = ByTerm.get(term) or ByTerm.get(key) or ByPath.get(bare)
    if not target:
      Dropped.append(term)
      continue
    rel = target if target.endswith(".md") else target + ".md"
    if not is_vault_path(rel) or not (vault / rel).is_file():
      Dropped.append(term)
      continue
    if rel not in Paths:
      Paths.append(rel)
  return Paths[:cap], Dropped


def load_candidates(Rels, vault, char_cap=40000):
  """2패스 프롬프트에 붙일 기존 노트 전문 - 총 글자 수 상한을 넘으면 뒤를 자른다"""
  Blocks, Used, Kept = [], 0, []
  for rel in Rels:
    body = strip_front((vault / rel).read_text(encoding="utf-8"))[1].strip()
    block = "### %s\n```md\n%s\n```" % (rel, body)
    if Used + len(block) > char_cap and Kept:
      break
    Blocks.append(block)
    Used += len(block)
    Kept.append(rel)
  return "\n\n".join(Blocks), Kept


def build_select_prompt(doc_text, doc_name, note_text, max_targets):
  return (
    SELECT_RULES % max_targets
    + "\n## 사전 (term\ttarget)\n" + note_text
    + "\n\n## 통합 문서 : " + doc_name + "\n" + doc_text
  )


def build_prompt(doc_text, doc_name, index_text, folders_text, candidates_text=""):
  Parts = [
    RULES,
    "\n## 기존 폴더 구조\n" + folders_text,
    "\n\n## 사전 (kind\tterm\ttarget)\n" + index_text,
  ]
  if candidates_text:
    Parts.append(
      "\n\n## 수정 대상 후보 (기존 노트 전문 - updates 로 보강할 것)\n"
      "아래는 볼트에 이미 있는 노트다. 경로가 곧 target 이다.\n"
      "frontmatter 는 떼어 냈으니 본문만 보고 판단하라.\n\n" + candidates_text
    )
  Parts.append("\n\n## 통합 문서 : " + doc_name + "\n" + doc_text)
  return "".join(Parts)


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

  # ANTHROPIC_API_KEY 가 설정되어 있으면 Claude Code 가 구독 대신 API 키로 인증해 별도 과금된다
  # 이 호출에서만 키를 제거해 구독으로 청구되도록 보장한다
  Env = os.environ.copy()
  if Env.pop("ANTHROPIC_API_KEY", None):
    print("  [알림] 이번 호출에서는 ANTHROPIC_API_KEY 를 제외했습니다 (구독으로 청구)")

  proc = subprocess.run(
    [exe, "-p", "--output-format", "text"],
    input=prompt, capture_output=True, text=True, encoding="utf-8", timeout=1800, env=Env,
  )
  if proc.returncode != 0:
    raise SystemExit("claude 호출 실패 : %s" % (proc.stderr or "")[:500])
  return proc.stdout


MOCK = json.dumps({
  "notes": [
    {"title": "가비지 컬렉션", "folder": "백엔드/Java",
     "aliases": ["GC", "Garbage Collection", "가비지 컬렉션(Garbage Collection)"],
     "body": "- [[JVM 메모리 구조]]의 힙 영역 대상으로 동작\n"
             "- 참조 끊긴 [[객체]] 자동 회수 -> 메모리 누수 방지\n\n"
             "### 종류\n- [[G1 GC]] : 힙을 region 단위로 분할\n\t- 짧은 정지 시간 목표"},
    {"title": "JVM 메모리 구조", "folder": "백엔드/Java",
     "aliases": ["런타임 데이터 영역", "Runtime Data Area"],
     "body": "- [[JVM]] 이 관리하는 메모리 영역\n\n### 종류\n"
             "- 메서드 영역 : [[클래스]] 정보 · static 변수\n- 힙 : [[객체]] 저장 -> [[가비지 컬렉션]] 대상\n"
             "- 스택 : 메서드 호출 프레임"},
  ],
  "moc": {"title": "JVM 메모리 관리", "folder": "백엔드/Java/_MOC",
          "body": "### 메모리 구조\n- [[JVM 메모리 구조]]\n- [[객체]]\n\n"
                  "### 회수\n- [[가비지 컬렉션]]\n- [[G1 GC]]"},
  "updates": [],
  "new_concepts": ["G1 GC"],
}, ensure_ascii=False)

MOCK_SELECT = json.dumps({"targets": []}, ensure_ascii=False)


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
  """볼트에 이미 있는 노트 제목 - _inbox 는 아직 볼트가 아니므로 제외한다
  (제외하지 않으면 지금 분해하는 원본이 '이미 있는 노트'로 잡혀 같은 제목 노트가 안 생긴다)"""
  Titles = {}
  for root, dirs, files in os.walk(vault):
    dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("_inbox", "_pending", "node_modules")]
    for f in files:
      if f.endswith(".md"):
        rel = os.path.relpath(os.path.join(root, f), vault).replace(os.sep, "/")
        Titles.setdefault(f[:-3], rel)
  return Titles


FRONT_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)
LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def strip_front(text):
  """(frontmatter 본문, 나머지 본문) - frontmatter 가 없으면 앞이 빈 문자열"""
  m = FRONT_RE.match(text)
  if not m:
    return "", text
  return m.group(1), text[m.end():]


def parse_front(front):
  """(aliases 목록, aliases 를 뺀 나머지 frontmatter 줄) - 최소 파서, YAML 의존성 없음"""
  Aliases, Rest = [], []
  in_aliases = False
  for line in front.splitlines():
    if re.match(r"^aliases\s*:", line):
      in_aliases = True
      inline = line.split(":", 1)[1].strip()
      if inline.startswith("["):
        Aliases.extend(a.strip().strip("'\"") for a in inline.strip("[]").split(",") if a.strip())
        in_aliases = False
      continue
    if in_aliases:
      if re.match(r"^\s*-\s+", line):
        Aliases.append(re.sub(r"^\s*-\s+", "", line).strip().strip("'\""))
        continue
      in_aliases = False
    Rest.append(line)
  return [a for a in Aliases if a], Rest


def norm_line(line):
  """줄 대조용 정규화 - 위키링크와 강조 표시를 벗겨 '링크만 새로 걸린 줄' 을 같은 줄로 본다"""
  s = LINK_RE.sub(lambda m: m.group(2) or m.group(1), line)
  s = s.replace("==", "").replace("**", "")
  return re.sub(r"\s+", "", s)


def lost_lines(old_body, new_body):
  """원본에 있었는데 수정판에서 사라진 줄 - '기존 내용 삭제 금지' 규칙 검사용"""
  Budget = Counter(norm_line(l) for l in new_body.splitlines() if norm_line(l))
  Lost = []
  for line in old_body.splitlines():
    key = norm_line(line)
    if not key:
      continue
    if Budget[key] > 0:
      Budget[key] -= 1
    else:
      Lost.append(line)
  return Lost


def render_update(old_text, new_body, add_aliases):
  """원본 frontmatter 를 보존하고 aliases 만 합친 수정판 전문

  검수용 정보는 노트에 넣지 않는다 - 볼트에 그대로 덮어쓸 수 있어야 하기 때문이다
  (뭐가 바뀌었는지는 옆의 .diff 파일이 알려준다)"""
  front, _ = strip_front(old_text)
  Aliases, Rest = parse_front(front)
  Merged = list(dict.fromkeys(Aliases + [a for a in add_aliases if a]))

  Out = ["---"]
  if Merged:
    Out.append("aliases:")
    Out.extend("  - %s" % a for a in Merged)
  Out.extend(l for l in Rest if l.strip())
  Out.append("---")
  if len(Out) == 2:  # 원본에 frontmatter 가 없었다
    return new_body.strip() + "\n"
  return "\n".join(Out) + "\n\n" + new_body.strip() + "\n"


def write_diff(vault, pending, rel, Header):
  """볼트 원본과 _pending 수정판을 대조해 .diff 를 쓴다 - 소실된 줄 목록을 돌려준다"""
  old_body = strip_front((vault / rel).read_text(encoding="utf-8"))[1].strip()
  out = pending / rel
  new_body = strip_front(out.read_text(encoding="utf-8"))[1].strip()
  Lost = lost_lines(old_body, new_body)

  Lines = list(Header)
  if Lost:
    Lines.append("# guard : 기존 줄 %d개가 사라졌습니다 - 통째로 덮어쓰지 말고 필요한 + 줄만 옮기세요" % len(Lost))
  Lines.extend(difflib.unified_diff(
    old_body.splitlines(), new_body.splitlines(),
    fromfile=rel + " (볼트 원본)", tofile=rel + " (수정판)", lineterm="", n=2))
  (out.parent / (out.name + ".diff")).write_text("\n".join(Lines) + "\n", encoding="utf-8")
  return Lost


def rediff(vault, pending):
  """_pending 의 모든 수정판 .diff 를 다시 계산한다

  링크 보강 단계가 수정판을 또 고치므로 파이프라인 끝에서 한 번 더 돌려야 diff 가 맞는다.
  '수정판' 판별 기준은 _pending 의 상대 경로가 볼트에도 있는 것이다"""
  Redone = []
  for path in sorted(pending.rglob("*.md")):
    rel = path.relative_to(pending).as_posix()
    if not is_vault_path(rel) or not (vault / rel).is_file():
      continue
    # 이전 diff 의 머리말(# 로 시작하는 줄)은 살린다 - source · change 기록이 들어 있다
    old_diff = path.parent / (path.name + ".diff")
    Header = []
    if old_diff.is_file():
      for line in old_diff.read_text(encoding="utf-8").splitlines():
        if not line.startswith("#"):
          break
        if not line.startswith("# guard"):
          Header.append(line)
    Redone.append((rel, write_diff(vault, pending, rel, Header)))
  return Redone


def write_updates(result, vault, pending, source_name):
  """기존 노트 수정판을 _pending 의 같은 경로에 쓰고 옆에 .diff 를 남긴다

  볼트 원본은 절대 건드리지 않는다 - 검수한 사람이 직접 덮어쓴다"""
  Updated, Rejected = [], []

  for upd in result.get("updates", []) or []:
    rel = str(upd.get("target", "")).replace("\\", "/").strip().lstrip("/")
    if rel and not rel.endswith(".md"):
      rel += ".md"
    src = vault / rel
    new_body = (upd.get("body") or "").strip()
    if not rel or not is_vault_path(rel) or not src.is_file():
      Rejected.append((rel or "(경로 없음)", "볼트 본체에 그 경로가 없음"))
      continue
    if not new_body:
      Rejected.append((rel, "body 가 비어 있음"))
      continue

    old_text = src.read_text(encoding="utf-8")
    old_body = strip_front(old_text)[1].strip()
    if norm_line(old_body) == norm_line(new_body):
      Rejected.append((rel, "바뀐 내용 없음"))
      continue

    added = len([l for l in new_body.splitlines() if l.strip()]) - len([l for l in old_body.splitlines() if l.strip()])

    out = pending / rel
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_update(old_text, new_body, upd.get("add_aliases", [])), encoding="utf-8")

    Header = ["# 볼트 원본 : %s" % rel, "# 출처 문서 : %s" % source_name]
    summary = (upd.get("summary") or "").replace("\n", " ").strip()
    if summary:
      Header.append("# 바뀐 것 : %s" % summary)
    Lost = write_diff(vault, pending, rel, Header)

    Updated.append((rel, added, Lost))

  return Updated, Rejected


def render(note, is_moc=False):
  """기존 볼트 관례에 맞춘 frontmatter - aliases 는 블록 리스트, 제목(#) 줄 없음

  검수용 필드(source · created · status)는 넣지 않는다 - 볼트로 그대로 옮길 수 있어야 한다"""
  Front = ["---"]
  Aliases = [a for a in note.get("aliases", []) if a and a != note["title"]]
  if Aliases:
    Front.append("aliases:")
    Front.extend("  - %s" % a for a in dict.fromkeys(Aliases))
  if is_moc:
    Front.extend(["tags:", "  - MOC"])
  Front.append("---")
  if len(Front) == 2:
    return note.get("body", "").strip() + "\n"
  return "\n".join(Front) + "\n\n" + note.get("body", "").strip() + "\n"


def write_notes(result, vault, pending, overwrite):
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
    # LLM 이 파이프라인 폴더를 골랐으면 떼어낸다 - _pending 안에 또 _inbox 가 생기는 것 방지
    Parts = [p for p in folder.split("/") if p and p not in ("_inbox", "_pending")]
    folder = "/".join(Parts)
    out = pending / folder / (title + ".md")

    if title in Known and not overwrite:
      Skipped.append((title, Known[title]))
      continue

    out.parent.mkdir(parents=True, exist_ok=True)
    note["title"] = title
    out.write_text(render(note, is_moc), encoding="utf-8")
    Written.append(str(out.relative_to(pending)).replace(os.sep, "/"))

  return Written, Skipped


# ---------------------------------------------------------------------------
# 메인
# ---------------------------------------------------------------------------

def main():
  ap = argparse.ArgumentParser(description="통합 md 를 원자 노트 + MOC 로 분해")
  ap.add_argument("document", nargs="?", help="분해할 통합 md 파일 (--rediff 면 생략)")
  ap.add_argument("--vault", default=".", help="볼트 루트 (기본 현재 폴더)")
  ap.add_argument("--pending", default="_pending", help="결과를 쌓을 폴더 (기본 _pending)")
  ap.add_argument("--index", default="_index.tsv", help="obsidian_autolink.py --write-index 산출물")
  ap.add_argument("--backend", choices=["cc", "api", "mock"], default="cc")
  ap.add_argument("--model", default=MODEL)
  ap.add_argument("--max-tokens", type=int, default=16000)
  ap.add_argument("--show-prompt", action="store_true", help="프롬프트만 출력하고 종료 (1패스는 실제로 돈다)")
  ap.add_argument("--overwrite", action="store_true", help="볼트에 같은 제목이 있어도 결과를 생성")
  ap.add_argument("--no-update", action="store_true",
                  help="기존 노트 보강을 끄고 신규 노트만 만든다 (LLM 호출 1번)")
  ap.add_argument("--max-context-notes", type=int, default=12,
                  help="본문을 첨부할 기존 노트 최대 개수 (기본 12)")
  ap.add_argument("--context-chars", type=int, default=40000,
                  help="첨부하는 기존 노트 본문 총 글자 상한 (기본 40000)")
  ap.add_argument("--rediff", action="store_true",
                  help="LLM 호출 없이 _pending 의 수정판 .diff 만 다시 계산 (링크 보강 뒤에 돌린다)")
  args = ap.parse_args()

  vault = Path(args.vault).resolve()
  pending = vault / args.pending

  if args.rediff:
    Redone = rediff(vault, pending)
    if not Redone:
      print("수정판 없음 - 갱신할 diff 가 없습니다")
      return 0
    print("diff 갱신 %d개 :" % len(Redone))
    for rel, Lost in Redone:
      print("  ~ %s%s" % (rel, "  [경고] 기존 줄 %d개 소실" % len(Lost) if Lost else ""))
    return 0

  if not args.document:
    raise SystemExit("분해할 문서를 지정하세요 (또는 --rediff)")
  doc = Path(args.document).resolve()
  if not doc.is_file():
    raise SystemExit("문서를 찾을 수 없습니다 : %s" % doc)

  doc_text = doc.read_text(encoding="utf-8")
  Rows = index_rows(vault / args.index)
  steps = 3 if args.no_update else 4
  step = 0

  # ---- 1패스 : 보강할 기존 노트 고르기 -------------------------------------
  candidates_text, Kept = "", []
  if not args.no_update and Rows:
    step += 1
    select_prompt = build_select_prompt(doc_text, doc.name, note_index_text(Rows), args.max_context_notes)
    print("[%d/%d] 보강 대상 선별 (%s, 문서 %.0fKB) ... 몇 분 걸립니다"
          % (step, steps, args.backend, len(doc_text) / 1024))
    t0 = time.time()
    if args.backend == "api":
      raw = call_api(select_prompt, args.model, 2000)
    elif args.backend == "cc":
      raw = call_claude_code(select_prompt)
    else:
      raw = MOCK_SELECT
    print("  응답 %.0f초" % (time.time() - t0))
    Terms = extract_json(raw).get("targets", []) or []
    Rels, Dropped = resolve_targets(Terms, Rows, vault, args.max_context_notes)
    candidates_text, Kept = load_candidates(Rels, vault, args.context_chars) if Rels else ("", [])
    print("  대상 %d개 : %s" % (len(Kept), ", ".join(Kept) or "없음"))
    if Dropped:
      print("  사전에 없어 무시 : %s" % ", ".join(str(d) for d in Dropped))
    if len(Kept) < len(Rels):
      print("  글자 상한(%d)에 걸려 %d개 제외" % (args.context_chars, len(Rels) - len(Kept)))

  # ---- 2패스 : 분해 + 보강 --------------------------------------------------
  prompt = build_prompt(doc_text, doc.name, load_index(vault / args.index), load_folders(vault), candidates_text)

  if args.show_prompt:
    print(prompt)
    return 0

  step += 1
  print("[%d/%d] 분해 호출 (%s, 프롬프트 %.0fKB) ... 몇 분 걸립니다"
        % (step, steps, args.backend, len(prompt) / 1024))
  t0 = time.time()
  if args.backend == "api":
    raw = call_api(prompt, args.model, args.max_tokens)
  elif args.backend == "cc":
    raw = call_claude_code(prompt)
  else:
    raw = MOCK
  print("  응답 %.0f초 / %.0fKB" % (time.time() - t0, len(raw) / 1024))

  step += 1
  print("[%d/%d] 응답 파싱 ..." % (step, steps))
  result = extract_json(raw)

  step += 1
  print("[%d/%d] %s 에 쓰기 ..." % (step, steps, pending))
  Written, Skipped = write_notes(result, vault, pending, args.overwrite)
  Updated, Rejected = ([], []) if args.no_update else write_updates(result, vault, pending, doc.name)

  print("\n생성 %d개 :" % len(Written))
  for w in Written:
    print("  + %s" % w)

  if Updated:
    print("\n기존 노트 보강 %d개 (볼트 원본은 그대로, 검수 후 덮어쓰세요) :" % len(Updated))
    for rel, added, Lost in Updated:
      print("  ~ %s  (+%d줄)%s" % (rel, added, "  [경고] 기존 줄 %d개 소실" % len(Lost) if Lost else ""))
      for line in Lost[:5]:
        print("      - %s" % line.strip()[:100])
      if len(Lost) > 5:
        print("      ... 외 %d줄, diff 확인" % (len(Lost) - 5))
  if Rejected:
    print("\n보강 무시 %d개 :" % len(Rejected))
    for rel, why in Rejected:
      print("  x %s  (%s)" % (rel, why))

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