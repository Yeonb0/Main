---
aliases:
  - MNIST 데이터셋
  - 손글씨 숫자 데이터셋
source: 신경망.md
created: 2026-07-30
---

- 손글씨 숫자 이미지 집합. 0 ~ 9 숫자 이미지로 구성
- 훈련 이미지 60,000 장 / 시험 이미지 10,000 장
- 훈련 이미지로 모델 학습 -> 학습한 모델로 시험 이미지 분류 정확성 평가

### 형태
- 28 × 28 크기의 회색조 이미지
- 각 픽셀은 0 ~ 255 값
- 이미지가 실제 의미하는 숫자가 레이블로 부착

### `load_mnist()`
- MNIST 데이터셋 내려받아 이미지를 [[넘파이]] [[배열]] 로 변환
- 원본 : https://github.com/WegraLee/deep-learning-from-scratch/blob/master/dataset/mnist.py
- [[데이터]] 안 받아지면 -> `url_base` 를 `https://ossci-datasets.s3.amazonaws.com/mnist/` 로 교체 & `_download()` 에 `User-Agent` 헤더 추가

> [!note]- mnist.py (URL & 다운로드 방식 수정본)
> ```python
> # coding: utf-8
> try:
>     import urllib.request
> except ImportError:
>     raise ImportError('You should use Python 3.x')
> import os.path
> import gzip
> import pickle
> import os
> import numpy as np
> 
> url_base = 'https://ossci-datasets.s3.amazonaws.com/mnist/'
> key_file = {
>     'train_img':'train-images-idx3-ubyte.gz',
>     'train_label':'train-labels-idx1-ubyte.gz',
>     'test_img':'t10k-images-idx3-ubyte.gz',
>     'test_label':'t10k-labels-idx1-ubyte.gz'
> }
> 
> dataset_dir = os.path.dirname(os.path.abspath(__file__))
> save_file = dataset_dir + "/mnist.pkl"
> 
> train_num = 60000
> test_num = 10000
> img_dim = (1, 28, 28)
> img_size = 784
> 
> def _download(file_name):
>     file_path = dataset_dir + "/" + file_name
>     
>     if os.path.exists(file_path):
>         return
> 
>     print("Downloading " + file_name + " ... ")
>     request = urllib.request.Request(url_base + file_name,
>                                      headers={'User-Agent': 'Mozilla/5.0'})
>     with urllib.request.urlopen(request) as response, open(file_path, 'wb') as f:
>         f.write(response.read())
>     print("Done")
>     
> def download_mnist():
>     for v in key_file.values():
>         _download(v)
>         
> def _load_label(file_name):
>     file_path = dataset_dir + "/" + file_name
>     
>     print("Converting " + file_name + " to NumPy Array ...")
>     with gzip.open(file_path, 'rb') as f:
>             labels = np.frombuffer(f.read(), np.uint8, offset=8)
>     print("Done")
>     
>     return labels
> 
> def _load_img(file_name):
>     file_path = dataset_dir + "/" + file_name
>     
>     print("Converting " + file_name + " to NumPy Array ...")    
>     with gzip.open(file_path, 'rb') as f:
>             data = np.frombuffer(f.read(), np.uint8, offset=16)
>     data = data.reshape(-1, img_size)
>     print("Done")
>     
>     return data
>     
> def _convert_numpy():
>     dataset = {}
>     dataset['train_img'] =  _load_img(key_file['train_img'])
>     dataset['train_label'] = _load_label(key_file['train_label'])    
>     dataset['test_img'] = _load_img(key_file['test_img'])
>     dataset['test_label'] = _load_label(key_file['test_label'])
>     
>     return dataset
> 
> def init_mnist():
>     download_mnist()
>     dataset = _convert_numpy()
>     print("Creating pickle file ...")
>     with open(save_file, 'wb') as f:
>         pickle.dump(dataset, f, -1)
>     print("Done!")
> 
> def _change_one_hot_label(X):
>     T = np.zeros((X.size, 10))
>     for idx, row in enumerate(T):
>         row[X[idx]] = 1
>         
>     return T
>     
> 
> def load_mnist(normalize=True, flatten=True, one_hot_label=False):
>     """MNIST 데이터셋 읽기
>     
>     Parameters
>     ----------
>     normalize : 이미지의 픽셀 값을 0.0~1.0 사이의 값으로 정규화할지 정한다.
>     one_hot_label : 
>         one_hot_label이 True면、레이블을 원-핫(one-hot) 배열로 돌려준다.
>         one-hot 배열은 예를 들어 [0,0,1,0,0,0,0,0,0,0]처럼 한 원소만 1인 배열이다.
>     flatten : 입력 이미지를 1차원 배열로 만들지를 정한다. 
>     
>     Returns
>     -------
>     (훈련 이미지, 훈련 레이블), (시험 이미지, 시험 레이블)
>     """
>     if not os.path.exists(save_file):
>         init_mnist()
>         
>     with open(save_file, 'rb') as f:
>         dataset = pickle.load(f)
>     
>     if normalize:
>         for key in ('train_img', 'test_img'):
>             dataset[key] = dataset[key].astype(np.float32)
>             dataset[key] /= 255.0
>             
>     if one_hot_label:
>         dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
>         dataset['test_label'] = _change_one_hot_label(dataset['test_label'])    
>     
>     if not flatten:
>         for key in ('train_img', 'test_img'):
>             dataset[key] = dataset[key].reshape(-1, 1, 28, 28)
> 
>     return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label']) 
> 
> if __name__ == '__main__':
>     init_mnist()
> ```

#### Parameters
- `bool` normalize : 이미지의 픽셀 값을 0.0 ~ 1.0 사이 값으로 [[정규화]] 할지 결정
	- 정규화 (Normalization) : 데이터를 특정 범위로 변환하는 처리
- `bool` one_hot_label
	- `True` -> 레이블을 원-핫 (one-hot) 배열로 return
	- 원-핫 배열 : 딱 한 값만 1 이고 나머지는 0 인 배열
- `bool` flatten : 입력 이미지를 1차원 배열로 만들지 결정

#### Returns
- (훈련 이미지, 훈련 레이블), (시험 이미지, 시험 레이블)

### 이미지 확인
```python
import numpy as np
import matplotlib.pyplot as plt
import sys, os
sys.path.append(os.pardir)  # 부모 디렉터리의 파일을 가져올 수 있도록 설정

from mnist import load_mnist
from PIL import Image

def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

img = x_train[0]
label = t_train[0]
print(label)  # 이미지 레이블 확인 (5)

print(img.shape)  # 이미지 데이터 확인 (784,)
img = img.reshape(28, 28)  # 원래 이미지 형태로 변형 (28*28)
print(img.shape)  # 이미지 데이터 확인 (28, 28)

img_show(img)  # 이미지 표시
```

> [!note]- 실행 결과
> ![[신경망-32.png]]
> ![[신경망-33.png]]

- flatten = `true` -> 1차원 넘파이 배열로 저장 -> `reshape(28, 28)` 로 28 × 28 복원
- 넘파이 이미지 -> PIL 용 데이터 [[객체]] 변환 필요 -> `Image.fromarray()`

### 인식 정확도
![[딥러닝-02.png]]
- 기법별 순위 정리 : https://rodrigob.github.io/are_we_there_yet/build/classification_datasets_results.html
- 상위권 대부분 [[합성곱 신경망|CNN]] 기반
- [[깊은 CNN]] -> ==99.38%==
