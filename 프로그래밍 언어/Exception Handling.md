---
aliases:
  - 예외 처리
  - 예외 처리(Exception Handling)
---

- 실행 중 오류 상황 처리 -> [[Reliability|신뢰성]] 확보
- ==ex)== 0으로 나누기, 메모리 부족

### 시점
- dynamic : run-time error 잡기
- static : [[컴파일]] 단계에서 잡기

### 데이터 바인딩
- [[바인딩 시점]] -> 용도에 따라 선택
- static : 컴파일 시 저장 공간 결정 ==ex)== [[C]]
	- 융통성↓, 속도↑
- dynamic : [[변수]] 먼저 설정, run-time 입력 시 저장 공간 설정 ==ex)== [[Java]], [[Python]]
	- 융통성↑, 속도↓
