---
aliases:
  - Modulation and Coding Scheme
  - MCS(Modulation and Coding Scheme)
---

- [[Modulation|변조]] 차수 + coding rate + spatial stream 조합 index
- sender 가 ==32 개(0 ~ 31)== 중 하나 선택해 전송

![[Case-Study-Wi-Fi-05.png]]

### 구성
| 항목 | 내용 |
| --- | --- |
| Type | 몇 bit 수신 -> [[Quadrature Amplitude Modulation\|QAM]] 차수 |
| Coding rate | 일반 코드 / 전체 코드 비율 -> ECC 비중 |
| Spatial Streams | TX · RX 안테나 사용 갯수 -> [[MIMO]] |

### Coding
- [[Error]] Correcting Code (ECC) : 오류 수정 가능한 코드 -> [[Error Correction]]
- coding rate ↓ -> ECC 비중 ↑ -> 오류 견딤 ↑, 실제 [[데이터]] ↓

### Rate Adaptation
- [[SNR]] ↑ (송신 good) -> 높은 index 선택
- [[SNR]] ↓ (송신 bad) -> 낮은 index 선택
- 요구 SNR -> [[Receiver Sensitivity]] 결정
