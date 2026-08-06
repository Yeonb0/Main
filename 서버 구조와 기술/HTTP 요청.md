---
aliases:
  - HTTP Request
  - HTTP 요청(HTTP Request)
---

- [[클라이언트]] -> [[웹 서버]] 방향 [[HTTP]] 메시지

### 구성
| 정보 | 내용 |
| --- | --- |
| 요청 라인 | [[메소드]] [[이름]] · 대상 리소스 URI · [[HTTP]] 버전 |
| 헤더 부분 | 클라이언트 수용 가능 유형 등 정보 |
| 바디 부분 | [[서버]]에 보내는 정보 |

- 메소드 종류 : `GET`, `POST`

### 예시
- ==ex)==

```yaml
GET/HTTP/1.1
Host: example.com
```
