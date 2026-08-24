---
aliases:
  - CBOW
  - Continuous Bag-of-Words
  - CBOW 모델(Continuous Bag-of-Words)
---

- 맥락으로부터 타깃 (target) 추측용 [[머신러닝/신경망|신경망]]
- [[머신러닝/word2vec]] 의 대표 모델
- 타깃 : 중앙 단어 / 맥락 (context) : 중앙 단어 주변 단어

### 구조
![[word2vec-10.png]]
- 입력 : 맥락 (단어들의 목록) -> 원핫 표현 변환
- 맥락으로 고려할 단어 N 개 -> 입력층 N 개
- 은닉층 = 각 입력층 × [[가중치]] 의 평균
	- 입력층 $\mathbf{h}_1, \mathbf{h}_2$ -> 은닉층 $\mathbf{h} = \frac{1}{2}(\mathbf{h}_1 + \mathbf{h}_2)$
	- [[가중치]] = [[단어의 분산 표현]]

![[word2vec-11.png]]
- [[출력층]] : 어휘 수만큼 각 단어의 점수 -> [[소프트맥스 함수 1|소프트맥스 함수]] 적용 -> 확률 변환
- [[활성화 함수]] 사용 X

### 추론
![[word2vec-12.png]]

```python
import sys
sys.path.append('../')
import numpy as np
from common.layers import MatMul

# 샘플 맥락 데이터
c0 = np.array([[1, 0, 0, 0, 0, 0, 0]])  
c1 = np.array([[0, 0, 1, 0, 0, 0, 0]])

# 가중치 초기화
W_in = np.random.rand(7, 3) 
W_out = np.random.rand(3, 7)

# 계층 생성
in_layer0 = MatMul(W_in)
in_layer1 = MatMul(W_in)
out_layer = MatMul(W_out)

# 순전파
h0 = in_layer0.forward(c0)
h1 = in_layer1.forward(c1)
h = 0.5 * (h0 + h1)  # 평균
s = out_layer.forward(h)

print(s)
```

> [!note]- 실행 결과
> ![[word2vec-13.png]]

### 학습
![[word2vec-14.png]]
- 올바른 예측 하도록 [[가중치]] 조정
- 다중 [[클래스]] 분류 -> [[소프트맥스 함수 1|소프트맥스]] & [[교차 엔트로피 오차]] 이용
	- [[소프트맥스 함수 1|소프트맥스]] : 점수 -> 확률 변환
	- [[교차 엔트로피 오차]] : 정답 - 확률 -> [[손실 함수|손실]] 로 사용

![[word2vec-15.png]]
![[word2vec-16.png]]
- 두 계층 묶어 [[Softmax-with-Loss 계층]] 으로 구현
- 구현체 : [[SimpleCBOW]]

### 확률 표기
| 표기 | 의미 |
| --- | --- |
| $P(A)$ | $A$ 가 일어날 확률 |
| $P(A, B)$ | 동시 확률 -> $A, B$ 가 동시에 일어날 확률 |
| $P(A \mid B)$ | 사후 확률 (조건부 확률) -> $B$ 주어졌을 때 $A$ 가 일어날 확률 |

![[word2vec-27.png]]
- 맥락 $w_{t-1}, w_{t+1}$ 주어졌을 때 타깃이 $w_t$ 가 될 확률 -> $P(w_t |  w_{t-1} w_{t+1})$

### 손실 함수
- $w_t$ 만 1, 나머지 0 인 원핫 벡터 -> $L = -\sum_kt_k\log y_k$ 의 시그마 소거
- 확률에 $\log$ 취하고 부호 반전 -> Negative log likelihood
- [[말뭉치]] 전체로 확장

$$
L = \frac{1}{T}\sum^T_{t=1}\log P(w_t|w_{t-1}w_{t+1})
$$

- 목표 : $L$ 값 최대한 작게

### 언어 모델로서의 CBOW
![[순환-신경망-(RNN)-02.png]]
- 맥락을 왼쪽 ==2개== 단어로 한정 -> $P(w_t \mid w_{t-2}, w_{t-1})$
- 이때 [[손실 함수|손실]] -> $L = -\log P(w_t \mid w_{t-2}, w_{t-1})$
- 2층 [[마르코프 연쇄]] 근사 -> [[언어 모델]] 로 사용 O
- 한계 : 맥락 길이 고정 · 맥락 내 단어 순서 무시
- 대안 -> [[순환 신경망]]
