---
aliases:
  - 양자화
  - Quantization
  - 양자화(Quantizing)
---

- amplitude 값을 discrete level 로 변환 -> [[PCM]] 2단계
	- 듬성듬성 -> 용량 ↓, 오차 심함
	- 빽빽하게 -> 용량 ↑, 정확도 ↑

![[Digital-Transmission-18.png]]

### ==ex)== 8개의 level 로 나누기
| 항목 | 내용 |
| --- | --- |
| normalized PAM values | 원래 값을 5로 나눈 값 |
| normalized quantized value | X.5 중간 값으로 바꾼 값 |
| normalized error | quantized values - PAM values 차이값 |
| quantization code | 각 level 번호 |
| encoded word | 보내지는 [[신호]] |

### 한계
- [[Quantization Error]] 발생
