# 기술 위키

컴퓨터공학 개념을 **원자 단위 노트**로 쌓고, `[[ ]]` 링크로 연결한 개인 기술 위키입니다.

Obsidian 볼트를 그대로 저장소에 올려 두고, [Quartz](https://quartz.jzhao.xyz/)로 정적 사이트를 빌드해 Cloudflare Pages로 배포합니다.

- **작성** : Notion에서 통합 글로 쓰고 → 스크립트로 개념 단위 분해
- **연결** : 모든 노트는 `[[ ]]`로 서로 물려 있고, 진입점은 `_MOC`
- **공개** : `main` 브랜치에 push하면 자동 빌드 & 배포

<!-- 배포 주소 : https://your-domain.example -->

---

## 목차

- [기술 위키](#기술-위키)
  - [목차](#목차)
  - [설계 원칙](#설계-원칙)
  - [폴더 구조](#폴더-구조)
  - [노트 작성 규칙](#노트-작성-규칙)
    - [frontmatter](#frontmatter)
    - [링크 규칙](#링크-규칙)
    - [제목 중복 금지](#제목-중복-금지)
  - [MOC 규칙](#moc-규칙)
  - [자동화 스크립트](#자동화-스크립트)
    - [흐름](#흐름)
    - [자주 쓰는 명령](#자주-쓰는-명령)
  - [로컬에서 열기](#로컬에서-열기)
    - [사용 중인 플러그인](#사용-중인-플러그인)
    - [.gitignore](#gitignore)
  - [배포 파이프라인](#배포-파이프라인)
  - [공개 범위 관리](#공개-범위-관리)
  - [커밋 관례](#커밋-관례)
  - [유지보수 체크리스트](#유지보수-체크리스트)

---

## 설계 원칙

이 볼트는 **문서 저장소가 아니라 개념 그래프**입니다. 아래 네 가지가 전부입니다.

**1노트 = 1개념**
"다른 글에서 `[[ ]]`로 부를 만한 단위인가?"가 유일한 분해 기준입니다. 아니라면 쪼개지 않습니다.

**제목이 곧 링크 이름**
파일명은 본문에서 자연스럽게 부를 이름과 같아야 합니다. `2. 메모리 관리 방식` 같은 목차형 제목은 링크가 될 수 없으므로 금지합니다.

**서사는 MOC에, 설명은 개별 노트에**
원자 노트로만 쪼개면 "왜 이 개념 다음에 저 개념이 오는가"라는 맥락이 사라집니다. 그 맥락은 `_MOC`가 담당합니다.

**없는 노트에도 링크를 건다**
아직 쓰지 않은 개념이라도 `[[G1 GC]]`처럼 미리 링크합니다. 옵시디언에서 **미해결 링크**로 남아 그래프 뷰에 빈 노드로 표시되고, 이것이 곧 **앞으로 쓸 노트 백로그**가 됩니다.

---

## 폴더 구조

```
.
├─ _MOC/                  진입점. 주제별 목차 노트
├─ _inbox/                Notion 정리본 투입구 (자동화 입력)
│   └─ _done/             처리 완료된 원본
├─ _pending/              분해 결과 대기소. 검수 후 아래 폴더로 이동 
├─ images/                모든 첨부. ingest.py 가 `노트슬러그-01.png` 로 재명명해 모음
│
├─ 자료구조/
├─ 알고리즘 설계와 분석/
├─ 컴퓨터 네트워크/
├─ 데이터베이스시스템/
├─ 프로그래밍 언어/
├─ AWS/
├─ 멋쟁이사자처럼/
│   ├─ 백엔드/            Java, Spring
│   └─ 프론트엔드/         웹, CSS, JS, React, Tailwind CSS, Vercel
├─ 정보처리기사/
├─ 빅데이터분석기사/
├─ 머신러닝/
│
└─ scripts/               자동화 스크립트 + 사용 설명서
```

**언더스코어(`_`)로 시작하는 폴더는 노트가 아니라 파이프라인 인프라입니다.** 검색과 그래프에서 구분하기 쉬우라고 붙인 관례입니다.

---

## 노트 작성 규칙

### frontmatter

```yaml
---
aliases: [GC, Garbage Collection]
tags: [java, jvm]
source: JVM정리.md          # 자동 분해된 노트만
created: 2026-07-29
---
```

| 필드 | 필수 | 설명 |
| --- | --- | --- |
| `aliases` | 권장 | 약어, 영문명, 다른 표기. **자동 링크가 이걸 보고 연결합니다** |
| `tags` | 권장 | 소문자 영문. Dataview 쿼리와 MOC 자동 생성의 기준 |
| `source` | 자동 | 분해 원본 문서명 |
| `created` | 자동 | 생성일 |
| `status: pending` | 임시 | 검수 전 상태. 볼트로 옮긴 뒤 삭제 |
| `autolink: false` | 선택 | 이 노트 본문에 자동 링크를 넣지 않음 |
| `autolink-in: false` | 선택 | 이 노트를 링크 대상에서 제외 (제목이 흔할 때) |

### 링크 규칙

- 같은 대상 노트로는 **노트당 1회만** 링크합니다. 첫 등장에만 걸면 충분하고, 매번 걸면 본문이 링크로 도배됩니다
- 표시 텍스트를 바꿔야 하면 `[[가비지 컬렉션|GC]]` 형태를 씁니다
- 한글 조사는 링크 밖에 둡니다 → `[[가비지 컬렉션]]은` (O) / `[[가비지 컬렉션은]]` (X)

### 제목 중복 금지

옵시디언의 `[[Java]]`는 경로가 아니라 **파일명**으로 해석됩니다. 같은 이름의 노트가 둘 이상이면 어디로 연결될지 보장되지 않고, 자동 링크에서도 제외됩니다.

```
Java  →  Java (언어) / Java (백엔드 스택)
CSS   →  CSS (문법)  / CSS (프론트엔드 개요)
```

주기적으로 확인하세요.

```bash
python scripts/obsidian_autolink.py . --report
```

---

## MOC 규칙

`_MOC` 노트는 **설명하지 않습니다.** `###` 섹션 제목과 `- [[링크]]` 불릿으로만 구성합니다.

```markdown
---
tags:
  - MOC
---

### 메모리 구조
- [[JVM 메모리 구조]]
- [[객체]]

### 회수
- [[가비지 컬렉션]]
- [[G1 GC]]
```

지켜야 할 것:

- **링크 뒤에 설명을 붙이지 않습니다.** `- [[가중치]] : 각 입력 신호의 중요도` 같은 형태는 금지.
- 파이프 별칭(`- [[스크럼|스크럼(Scrum)]]`)과 짧은 묶음(`- [[Linked Stack]] / [[Linked Queue]]`)은 허용.
- 개념 자체가 한 섹션 단위면 `### [[개념]]` 처럼 제목에 링크를 걸어도 됩니다.
- 원본의 순서와 묶음은 **섹션 구성과 불릿 순서로만** 남깁니다. 인과(`->`)는 개별 노트 본문이 담당합니다.
- 파일명이 제목이므로 `# 제목` 줄은 넣지 않습니다.

설명이 MOC에 들어가기 시작하면 개별 노트와 내용이 중복되고, 둘 중 어느 쪽을 고쳐야 할지 알 수 없게 됩니다.

태그가 잘 붙어 있으면 목록 부분은 Dataview로 대체할 수 있습니다.

````markdown
```dataview
LIST FROM #java AND -#moc
SORT file.name ASC
```
````

---

## 자동화 스크립트

`scripts/` 아래에 있으며 **외부 패키지 없이 Python 표준 라이브러리만** 사용합니다.

| 파일 | 역할 |
| --- | --- |
| `watch.py` | `_inbox/` 감시 → 전체 파이프라인 실행 |
| `ingest.py` | Notion export(zip / 폴더 / md) 정규화 → 첨부는 `images/` 로 이동·재명명 |
| `decompose.py` | 통합 md → 원자 노트 + MOC 로 분해 (LLM 호출) |
| `obsidian_autolink.py` | 자동 위키링크 삽입, 인덱스 / 중복 / 미해결 링크 보고 |

### 흐름

```
_inbox/ 에 Notion export 투입 (zip 그대로 / 압축 푼 폴더 / md 하나)
  → ⓪ 정규화        ingest.py
       · 첨부 → images/노트슬러그-01.png 로 이동·재명명 (내용 같으면 재사용)
       · 참조 → ![[ ]] 위키링크로 치환 (한글 이중 인코딩 포함)
       · 파일명에서 노션 해시 32자 제거
  → ① 사전 갱신     obsidian_autolink.py --write-index
  → ② LLM 분해      decompose.py
  → ③ 링크 보강     obsidian_autolink.py --only _pending --apply
  → ④ 원본 이동     _inbox/_done/
  → _pending/ 에서 검수 후 볼트로 이동
```

`images/`는 예외적으로 ⓪단계에서 볼트 본체에 바로 씁니다. 첨부는 검수 대상이 아니고,
`_pending/`에 있는 동안에도 미리보기가 보여야 하기 때문입니다.

**볼트 본체에 직접 쓰는 단계는 없습니다.** 결과는 항상 `_pending/`을 거칩니다.

### 자주 쓰는 명령

```bash
# 감시 시작 (평소 사용법) - _inbox 에 zip 을 떨구면 알아서 돈다
python scripts/watch.py --vault . --backend api

# 분해 없이 첨부 정리만 (뭘 할지 먼저 확인)
python scripts/ingest.py --vault . --dry-run
python scripts/ingest.py --vault .

# 제목이 중복된 개념 확인
python scripts/obsidian_autolink.py . --report

# 앞으로 쓸 노트 백로그 (참조 많은 순)
python scripts/obsidian_autolink.py . --unresolved

# 링크 삽입 미리보기 (파일 수정 없음)
python scripts/obsidian_autolink.py . --only "백엔드/Java"
```

전체 옵션과 단계별 상세 설명은 [`scripts/README.md`](scripts/README.md)를 보세요.

---

## 로컬에서 열기

```bash
git clone <this-repo> vault
```

Obsidian → **Open folder as vault** → 위 폴더 선택.

### 사용 중인 플러그인

| 플러그인 | 용도 |
| --- | --- |
| Dataview | MOC 자동 생성, 태그 기반 쿼리 |
| Templater | 노트 템플릿, 데일리 노트 자동 생성 |
| LaTeX Suite | 수식 입력 스니펫 |
| Omnisearch | 전문 검색 |

`.obsidian/` 중 워크스페이스 파일은 기기마다 달라지므로 추적하지 않습니다.

### .gitignore

```gitignore
# 옵시디언 로컬 상태
.obsidian/workspace*.json
.obsidian/cache
.trash/

# 파이프라인 산출물
_index.tsv
_inbox/_done/
__pycache__/

# Quartz 빌드
public/
.quartz-cache/

# OS
.DS_Store
Thumbs.db
```

---

## 배포 파이프라인

```
Obsidian (로컬 편집)
  → git push (main)
  → Cloudflare Pages 가 감지
  → Quartz 빌드
  → Custom Domain 으로 공개
```

Quartz는 `[[ ]]` 위키링크를 하이퍼링크와 백링크로 변환하고, 그래프 뷰도 그대로 제공합니다. **즉 볼트에서 보던 화면이 웹에서 거의 그대로 재현됩니다.**

빌드 설정 :

| 항목 | 값 |
| --- | --- |
| Build command | `npx quartz build` |
| Build output | `public` |
| Node version | 20 이상 |

로컬 미리보기 :

```bash
npx quartz build --serve
```

---

## 공개 범위 관리

공개 사이트로 나가는 저장소이므로, **모든 노트가 공개된다는 점을 전제로 작성합니다.**

공개하지 않을 노트는 frontmatter로 제외합니다.

```yaml
---
publish: false
---
```

다음은 아예 커밋하지 마세요.

- API 키, 토큰, 비밀번호 (`.env`는 `.gitignore`에 있어도 실수로 붙여넣기 쉽습니다)
- 과제 / 시험 문제 원문, 강의 자료 PDF 등 저작권이 있는 자료
- 타인의 개인정보가 담긴 회의록, 스터디 기록

`_inbox/`와 `_pending/`은 검수 전 상태라 공개 대상이 아닙니다. Quartz 설정에서 제외하거나 `publish: false`를 기본값으로 두세요.

---

## 커밋 관례

| 접두어 | 용도 |
| --- | --- |
| `note:` | 노트 추가 / 수정 |
| `moc:` | MOC 구조 변경 |
| `link:` | 자동 링크 적용 결과 |
| `fix:` | 오타, 링크 깨짐 수정 |
| `chore:` | 스크립트, 설정, 플러그인 |

```
note: JVM 메모리 구조 · 가비지 컬렉션 추가
link: 백엔드/Java 자동 링크 적용 (+37)
```

**`--apply` 계열 명령은 반드시 워킹트리가 깨끗한 상태에서 실행하세요.** 결과가 마음에 안 들면 `git checkout .`으로 되돌리는 것이 유일하고 확실한 안전장치입니다.

---

## 유지보수 체크리스트

**매주**

- [ ] `--unresolved`로 백로그 확인 → 참조 많은 개념부터 노트 작성
- [ ] `_pending/`에 검수 안 된 노트가 쌓여 있지 않은지 확인

**매월**

- [ ] `--report`로 제목 중복 정리
- [ ] `status: pending`이 남아 있는 노트 검색해서 정리
- [ ] 고아 노트(들어오는 링크가 0인 노트) 확인 후 MOC에 연결

```dataview
LIST
WHERE length(file.inlinks) = 0 AND !contains(file.folder, "_")
```

**분기**

- [ ] 폴더 구조가 실제 사고 구조와 어긋나지 않는지 점검
- [ ] `decompose.py`의 `RULES` 프롬프트를 최근 결과에 맞춰 조정