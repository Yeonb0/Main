---
aliases:
  - Mermaid Syntax
  - 머메이드 작성 규칙
  - Mermaid 문법
---

- 텍스트로 [[다이어그램]] 그리는 [[마크다운]] 친화 도구
- 이미지 파일 X, ==코드== -> [[Git]] diff · [[버전 관리]] O
- GitHub · GitLab · Obsidian · Notion · VS Code 기본 지원

### 절차
1. 코드블록 언어 식별자 `mermaid` 지정
2. 첫 줄에 다이어그램 종류 키워드 선언
3. 이후 줄에 [[뉴런|노드]]와 관계 기술
	- 들여쓰기는 [[Readability|가독성]] 목적, 일부 유형은 문법상 필수

### 종류
| 키워드 | [[이름]] | 핵심 질문 |
| --- | --- | --- |
| `flowchart` | [[Flowchart]] | 어떤 순서로 처리되는가 |
| `sequenceDiagram` | [[순차 다이어그램]] | 누가 누구에게 언제 |
| `classDiagram` | [[Class Diagram]] | 구조와 관계는 어떤가 |
| `stateDiagram-v2` | [[State Diagram]] | 어떤 [[state\|상태]]에 머무는가 |
| `erDiagram` | [[ER Diagram]] | [[데이터]]는 어떻게 연결되는가 |
| `gantt` | [[Gantt Chart]] | 언제까지 무엇을 |
| `pie` | [[Pie Chart]] | 비율이 어떻게 되는가 |
| `gitGraph` | [[Git Graph]] | 브랜치가 어떻게 흘렀는가 |
| `mindmap` | [[Mindmap]] | 개념이 어떻게 갈라지는가 |
| `timeline` | [[Timeline]] | 시간 순으로 무슨 일이 |
| `journey` | [[User Journey]] | 사용자가 어떻게 느꼈는가 |
| `quadrantChart` | [[Quadrant Chart]] | 두 축에서 어디에 위치하는가 |
| `xychart-beta` | [[XY Chart]] | 수치가 어떻게 변했는가 |
| `sankey-beta` | [[Sankey Diagram]] | 흐름의 양이 얼마인가 |

### 참고
- https://mermaid.js.org/intro/ : 공식 문서
- https://mermaid.live/ : 실시간 에디터, 문법 검증용
- https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams : GitHub 지원 범위
