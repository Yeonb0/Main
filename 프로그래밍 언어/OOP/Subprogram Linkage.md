---
aliases:
  - 서브프로그램 연결
  - 서브프로그램 연결(Subprogram Linkage)
---

- subprogram call + return 을 합친 것
- linkage 의 semantics -> 구현 방법 결정

### Subprogram Call
- [[매개 변수|parameter]] passing mechanism
- local [[변수]] storage 할당 & [[바인딩]]
- 실행 status 저장
- control 을 subprogram 으로 이동, 실행 완료 시 올바른 위치로 재이동
- nonlocal 변수 접근 메커니즘 제공 -> [[Nested Subprograms]]

### Subprogram Return
- out mode parameter (a ← f)
	- copy 방식 : formal parameter 의 지역 값 -> actual parameter 로 이동
	- 참조(by-reference) : 이동 필요 X, 애초에 같은 것 가리킴
- local 변수 storage deallocate
- nonlocal 변수 참조 메커니즘 return
- control 을 caller 에게 return

### Simple Subprogram
- ==ex)== FORTRAN
	- 재귀 X
	- nonlocal 변수 -> `COMMON` 으로 공유
	- local 변수 -> static, 프로그램 실행 전 미리 메모리 고정
- [[stack]]-dynamic local 변수 사용 언어 -> [[Activation Record]] 필요
