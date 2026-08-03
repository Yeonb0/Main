---
aliases:
  - 오류 제어
  - Error Control(오류 제어)
---

- [[ACK]] 이용 재전송으로 [[Error|오류]] 복구

![[Transport-Layer-10.png]]

### layer 별 한계
- layer 2 에도 error control 존재 -> [[Router|router]] 내부 발생 [[Error Detection|오류 검출]] X
- layer 4 는 end point 에만 존재 -> 중간 router 오류 control X
- -> layer 2 & 4 둘 다 error control 사용
