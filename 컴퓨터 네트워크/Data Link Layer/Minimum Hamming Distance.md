---
aliases:
  - MHD
  - 최소 해밍 거리
  - Minimum Hamming Distance(최소 해밍 거리)
---

- 어떤 codeword set 의 최소 [[Hamming Distance]]
- (MHD - 1) 까지 [[Error Detection]] 가능
- correction bit = n -> MHD > 2n (최소 2n + 1)

![[Error-Detection-and-Correction-05.png]]

### 특징
- [[Linear Block Code]] -> 1의 갯수가 가장 적은 codeword (00..00 제외) 가 MHD
- ==ex)== MHD = 3 -> 2-bit error detection & 1-bit error correction
- ==ex)== [[Simple Parity Check Code]] MHD = 2 / [[Hamming Code]] MHD = 3
