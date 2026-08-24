---
aliases:
  - MatMul Node
  - MatMul 노드(MatMul Node)
  - 행렬 곱 노드
---

- [[행렬의 곱]] 을 담당하는 [[node]]
- [[완전연결계층]] · [[Affine 계층]] 의 핵심 [[연산]]

### 형태
- [[순전파]] : $y = xW$
- [[역전파]]
	- $\frac{\partial L}{\partial x} = \frac{\partial L}{\partial y} W^{\mathrm{T}}$
	- $\frac{\partial L}{\partial W} = x^{\mathrm{T}} \frac{\partial L}{\partial y}$
- 형상 검사로 확인 O -> $\frac{\partial L}{\partial W}$ 형상 = $W$ 형상
- 계산 결과 [[기울기]] 는 `grads` 에 보관 -> [[계층 구현 규칙]]

### 원핫 벡터 입력
- 입력이 원핫 벡터 -> 결과 = $W$ 에서 한 줄 뽑는 것과 동일

![[word2vec-09.png]]
- 한 줄 추출에 [[행렬의 곱]] 사용 -> 비효율 -> 개선 여지
- ==ex)== [[CBOW 모델]] 입력층
