---
aliases:
  - 모델-뷰-컨트롤러 패턴
  - Model-View-Controller Pattern
  - 모델-뷰-컨트롤러 패턴(Model-View-Controller Pattern)
---

![[Pasted image 20260707105830.png]]

### M (Model)
- 애플리케이션의 핵심 로직 & 데이터 담당
- [[데이터베이스|DB]]와 연동되어 정보 저장 & 불러오기 역할
- ex) 사용자 정보, 게시글 목록, 주문 내역 처리

### V (View)
- [[UI|사용자 인터페이스(UI, User Interface)]]
- [[HTML]], [[Thymeleaf]], [[JSON]] 등의 형태로 데이터 출력 역할
- 여러 개의 뷰 사용 가능
- ex) 웹페이지, JSON 응답, [[UI]]

### C (Controller)
- 사용자의 요청을 받아 ==Model== 호출, 처리된 데이터를 ==View== 에 전달
- [[클라이언트]] <-> [[서버]] 간의 비즈니스 로직 조율 핵심 부분

### 장점
- 각 역할이 분리되어 있어 유지보수 용이
- 개발자가 특정 부분만 집중 가능
- 팀 개발 시 역할 나눠 협업 용이