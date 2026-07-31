---
aliases:
  - call-by-reference
  - 참조에 의한 전달
  - Pass-by-Reference(참조에 의한 전달)
---

- inout-mode (actual <-> formal)
- 접근 경로, 주로 주소(address) 전달
- actual [[매개 변수|parameter]] 를 호출된 [[Subprogram]] 과 공유 -> 원본 변경 O

### 장점
- 복사 overhead X
- 중복 공간 X

### 단점
- indirect addressing -> formal parameter 접근 느림
- actual parameter 의 의도치 않은 변경
- alias 생성 -> debugging 어려움

### 구현
- actual parameter 의 주소만 [[stack]] 저장
- 표현식 -> subprogram 넘어가기 직전 평가 -> 결과 저장 주소가 stack 에 저장

### 사용 언어
- [[C]] : parameter 로 pointer 사용 시
- C++ : reference type (특별한 pointer 타입) 제공
- [[Java]] : [[객체|객체(Object)]] 전달 시
