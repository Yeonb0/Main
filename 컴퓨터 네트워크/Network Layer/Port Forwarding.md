---
aliases:
  - 포트 포워딩
  - Port Forwarding(포트 포워딩)
---

- [[NAT]] router 에 static mapping 수동 추가하는 설정
- 내부 [[서버]]를 외부에 공개할 때 사용

![[Other-Network-Layer-Related-Protocols-15.png]]

### 배경
- NAT : 내부 -> 외부 나가는 packet 있을 때 NAT table 생성
- 내부에 서버 존재 -> 외부發 최초 요청의 mapping 부재 -> Port forwarding 필요

### 동작
| 설정 | 내용 |
| --- | --- |
| 포트 포워딩 규칙 | TCP :80 -> `192.168.0.10:80` |
| 외부 [[클라이언트]] 요청 | `Dst: 203.0.113.5 : 80` |
| NAT 라우터 변환 후 | `Dst: 192.168.0.10 : 80` |

- 외부 client 가 공인 [[IP]] 로 요청 -> [[Router|router]] 가 내부 서버 주소로 rewrite 후 전달
