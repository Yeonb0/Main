---
aliases:
  - 쿠파이
  - CuPy(쿠파이)
---

- GPU 로 병렬 계산 수행하는 [[NumPy]] 호환 라이브러리
- 대량 [[행렬의 곱]] 반복하는 [[딥러닝]] 학습 고속화 목적

### 조건
- 엔비디아 GPU 에서만 동작
- CUDA 설치 필요 -> https://developer.nvidia.com/cuda-downloads

### 특징
- [[NumPy]] 와 호환되는 [[API]] 제공
- 보통 `numpy` -> `cupy` 치환만으로 GPU 전환 O

### 계산 고속화
- [[NumPy]] 실수 기본 ==64 bit==
- 계산 속도 · 버스 [[Bandwidth|대역폭]] -> ==32 bit== 실수 사용 유리
- 학습된 [[가중치]] 저장 -> ==16 bit== 실수로 충분
