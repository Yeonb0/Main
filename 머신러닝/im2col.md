---
aliases:
  - image to column
  - im2col(image to column)
---

- 입력 [[데이터]] 를 필터링 하기 좋게 펼치는 [[함수]] (image to column)
- 4차원 [[배열]] -> 2차원 배열 변환
- [[합성곱 계층]] · [[풀링 계층]] 구현 트릭 -> 4중 [[for|for 문]] 회피

### 4차원 배열
- [[합성곱 신경망]] 의 계층 사이 데이터 -> 4차원
	- ==ex)== (10, 1, 28, 28) -> 28 × 28, 채널 1개 데이터 10개
```python
x = np.random.rand(10, 1, 28, 28) # 무작위로 데이터 생성 (0 ~ 1)
print(x.shape)
```
![[합성곱-신경망-(CNN)-23.png]]
- 첫 번째 데이터 접근 -> `x[0]`
- 첫 번째 데이터의 첫 채널 -> `x[0, 0]` or `x[0][0]`

### 형태
![[합성곱-신경망-(CNN)-24.png]]
- 3차원 [[Block|블록]]을 한 줄로 전개
![[합성곱-신경망-(CNN)-25.png]]
- 입력 [[데이터]] -> 행렬 / [[가중치]] -> 행렬 -> [[행렬의 곱]] 후 `reshape` 로 4차원 복원
![[합성곱-신경망-(CNN)-26.png]]
- 행렬 계산 문제화 -> 선형 대수 라이브러리로 효율 ↑

### MLP flatten 과의 차이

|         | [[다층 퍼셉트론\|MLP]] 의 flatten | im2col                            |
| ------- | -------------------------- | --------------------------------- |
| 무엇을 펴는가 | 이미지 전체                     | 커널이 보는 국소 patch 하나하나 -> 겹치는 부분 발생 |
| 위치 관계   | 소실                         | 행 안에 보존                           |
| 가중치 공유  | X                          | O ([[필터]] [[재사용(Reuse)\|재사용]])    |
| 목적      | (원래 목적 아님, 그냥 구조)          | 컨볼루션을 GEMM 으로 빠르게 계산              |

- ==ex)== 원본 데이터
	- a b c d / e f g h / i j k l / m n o p
	- patch 1 : a b c e f g i j k
	- patch 2 : b c d f g h j k l
	- patch 3 : e f g i j k m n o
	- patch 4 : f g h j k l n o p
- 겹치는 부분 다수 -> 메모리 소비 ↑ 단점

### 구현
```python
def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
    """다수의 이미지를 입력받아 2차원 배열로 변환한다(평탄화).
    
    Parameters
    ----------
    input_data : 4차원 배열 형태의 입력 데이터(이미지 수, 채널 수, 높이, 너비)
    filter_h : 필터의 높이
    filter_w : 필터의 너비
    stride : 스트라이드
    pad : 패딩
    
    Returns
    -------
    col : 2차원 배열
    """
    N, C, H, W = input_data.shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1

    img = np.pad(input_data, [(0,0), (0,0), (pad, pad), (pad, pad)], 'constant')
    col = np.zeros((N, C, filter_h, filter_w, out_h, out_w))

    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            col[:, :, y, x, :, :] = img[:, :, y:y_max:stride, x:x_max:stride]

    col = col.transpose(0, 4, 5, 1, 2, 3).reshape(N*out_h*out_w, -1)
    return col

def col2im(col, input_shape, filter_h, filter_w, stride=1, pad=0):
    """(im2col과 반대) 2차원 배열을 입력받아 다수의 이미지 묶음으로 변환한다.
    
    Parameters
    ----------
    col : 2차원 배열(입력 데이터)
    input_shape : 원래 이미지 데이터의 형상（예：(10, 1, 28, 28)）
    filter_h : 필터의 높이
    filter_w : 필터의 너비
    stride : 스트라이드
    pad : 패딩
    
    Returns
    -------
    img : 변환된 이미지들
    """
    N, C, H, W = input_shape
    out_h = (H + 2*pad - filter_h)//stride + 1
    out_w = (W + 2*pad - filter_w)//stride + 1
    col = col.reshape(N, out_h, out_w, C, filter_h, filter_w).transpose(0, 3, 4, 5, 1, 2)

    img = np.zeros((N, C, H + 2*pad + stride - 1, W + 2*pad + stride - 1))
    for y in range(filter_h):
        y_max = y + stride*out_h
        for x in range(filter_w):
            x_max = x + stride*out_w
            img[:, :, y:y_max:stride, x:x_max:stride] += col[:, :, y, x, :, :]

    return img[:, :, pad:H + pad, pad:W + pad]
```

### Parameters
```python
im2col(input_data, filter_h, filter_w, stride=1, pad=0)
```

| 인수           | 내용                                  |
| ------------ | ----------------------------------- |
| `input_data` | (데이터 수, 채널 수, 높이, 너비) 4차원 배열 입력 데이터 |
| `filter_h`   | 필터 높이                               |
| `filter_w`   | 필터 너비                               |
| `stride`     | [[스트라이드]] (간격)                      |
| `pad`        | [[패딩]] (0)                          |

- ==ex)==
```python
x1 = np.random.rand(1, 3, 7, 7) # (데이터 수, 채널 수, 높이, 너비)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape) # (9, 75)

x2 = np.random.rand(10, 3, 7, 7) # 데이터 10개
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape) # (90, 75)
```

> [!note]- 실행 결과
> ![[합성곱-신경망-(CNN)-27.png]]
