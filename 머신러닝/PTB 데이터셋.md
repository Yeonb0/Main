---
aliases:
  - PTB
  - Penn Treebank
  - PTB 데이터셋(Penn Treebank)
---

- Penn Treebank (펜 트리뱅크) [[말뭉치]]
- 한 문장짜리 예제를 넘어선 본격적 규모의 텍스트 [[데이터]]
- [[통계 기반 기법]] · [[_inbox/_done/word2vec]] 평가에 사용

### 형태
- 텍스트 파일, 원래 PTB 문장에 몇 가지 전처리 적용
	- 희소 단어 -> `<unk>` 특수 문자 치환
	- 구체적 숫자 -> `N` 대체
- 한 문장이 한 줄로 저장
- 각 문장 = 하나의 큰 시계열 [[데이터]] -> 문장 끝에 `<eos>` 삽입

### 사용
```python
import sys
sys.path.append('../')
from dataset import ptb

corpus, word_to_id, id_to_word = ptb.load_data('train')

print('말뭉치 크기 :', len(corpus))
print('corpus[:30] :', corpus[:30])
```

| `ptb.load_data()` 인수 | 용도 |
| --- | --- |
| `'train'` | [[훈련 데이터]] |
| `'test'` | [[시험 데이터]] |
| `'valid'` | [[검증 데이터]] |

- `corpus` : 단어 ID 목록
- `id_to_word` : 단어 ID -> 단어 변환 딕셔너리
- `word_to_id` : 단어 -> 단어 ID 변환 딕셔너리

> [!note]- 실행 결과
> ![[자연어와-단어의-분산-표현-14.png]]

### 통계 기반 기법 적용
```python
import sys
sys.path.append('../')
import numpy as np
from common.util import most_similar, create_co_matrix, ppmi
from dataset import ptb

window_size = 2
wordvec_size = 100

corpus, word_to_id, id_to_word = ptb.load_data('train')
vocab_size = len(word_to_id)
print('동시발생 수 계산 ...')
C = create_co_matrix(corpus, vocab_size, window_size)
print('PPMI 계산 ...')
W = ppmi(C, verbose=True)

print('SVD 계산 ...')
try:
    # truncate SVD (빠름!)
    from sklearn.utils.extmath import randomized_svd
    U, S, V = randomized_svd(W, n_components=wordvec_size, n_iter=5,
                            random_state=None)

except ImportError:
    # full SVD (느림!)
    U, S, V = np.linalg.svd(W)

word_vecs = U[:, :wordvec_size]  # 단어 벡터

querys = ['you', 'year', 'car', 'toyota']
for query in querys:
    most_similar(query, word_to_id, id_to_word, word_vecs, top=5)
```
- 큰 행렬 -> `randomized_svd()` 로 고속 [[특잇값분해]]

> [!note]- 실행 결과
> ![[자연어와-단어의-분산-표현-15.png]]

- 의미 · 문법적 관점에서 유사한 단어가 상위 랭킹

### RNNLM 학습 데이터 구성
```python
corpus, word_to_id, id_to_word = ptb.load_data('train')
corpus_size = 1000
corpus = corpus[:corpus_size]
vocab_size = int(max(corpus) + 1)

xs = corpus[:-1]  # 입력
ts = corpus[1:]   # 출력 (정답 레이블)
```
- 입력 `corpus[:-1]` / [[정답 레이블]] `corpus[1:]` -> 한 칸 시프트
- 작은 [[RNNLM]] 학습 시 앞 ==1000개== 단어만 절단 사용
