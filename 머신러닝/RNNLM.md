---
aliases:
  - RNN Language Model
  - RNNLM(RNN Language Model)
---

- [[순환 신경망]] 을 사용한 [[언어 모델]]
- 각 시각 [[데이터]] 마다 Embedding -> RNN -> Affine -> Softmax 순 처리

### 구조
![[순환-신경망-(RNN)-20.png]]

| 계층 | 역할 |
| --- | --- |
| [[Embedding 계층]] | 단어 ID -> [[단어의 분산 표현]] (단어 벡터) 변환 |
| [[RNN 계층]] | 입력 -> [[은닉 상태]] 변환 -> 위 계층 & 옆 RNN 계층으로 출력 |
| [[Affine 계층]] | [[은닉 상태]] -> 어휘 수만큼 점수 |
| [[Softmax-with-Loss 계층]] | 점수 -> 확률 & [[손실 함수\|손실]] |

- [[시계열 데이터]] 일괄 처리 -> [[Time 계층]] 으로 구현

### 동작
![[순환-신경망-(RNN)-21.png]]
- ==ex)== `You say goodbye and I say hello.`
- 다음에 나올 단어 예측
- [[RNN 계층]] 이 맥락 기억 -> [[Affine 계층]] & 다음 시각 [[RNN 계층]] 에 전달
- (이론상) 등장한 모든 단어 정보 기억 O

### 구현체
- [[SimpleRnnlm]]

### 평가
- [[퍼플렉서티]]
