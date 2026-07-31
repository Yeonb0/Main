---
aliases:
  - 디지털 신호
  - Digital Signal(디지털 신호)
---

- amplitude, frequency, phase 사용해 bit (0, 1) 정보로 만든 signal
- 이산적인 전압 레벨의 연속

![[Data-and-Signals-10.png]]

### bit rate
- 1초에 전송하는 bit 수
- 단위 : bps (bit per second)
- 1 Kbps = 1000 bps
- 1 Mbps = 1000 Kbps
- 1 Gbps = 1000 Mbps

### signal level
- signal level 증가 가능
- bit 갯수 n -> 한 번에 $2^n$ 만큼의 pattern 전송
	- ==ex)== two bits

![[Data-and-Signals-11.png]]

- level ↑ -> [[신호]] 간 차이 ↓ -> [[Noise]] 취약

### 전송 방법
- 유선 -> [[Baseband Transmission]]
- 무선 -> [[Bandpass Channel]] + [[Modulation]]
