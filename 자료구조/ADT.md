---
aliases:
  - 추상 데이터 타입
  - ADT (Abstract Data Type)
  - Abstract Data Type
  - 추상 데이터 타입 (Abstract Data Type)
---
- [[객체|객체(Object)]]의 명세와 그 [[함수|연산(Operation)]]의 명세가 그 객체의 표현과 연산의 구현으로부터 분리된 [[데이터 타입]]

### 연산 종류
1. [[생성자|생성자(Creator)]] / 구성자 (Constructor) : 지정된 타입에 맞는 새로운 [[인스턴스]] 생성
	- 전달 X 생성 O
2. 변환자 (Transformer) : 1개 이상의 다른 [[인스턴스]] 이용해 지정된 타입의 한 인스턴스 만듬
	- 전달 O 생성 O
3. 관찰자 (Observers) / 보고자 (Reporter) : 데이터 타입의 인스턴스에 대한 정보 제공. 변경은 X
	- 전달 O 생성 O -> 반환값 [[boolean]]
