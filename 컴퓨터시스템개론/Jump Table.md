---
aliases:
  - 점프 테이블
  - Jump Table(점프 테이블)
---

- [[switch]] 문에서 어디로 jump 할지 나타내는 table
- case 값 -> target address 매핑 -> 비교 없이 1회 간접 분기
- [[시간 복잡도]] $O(1)$, case 개수와 무관

### 구조
| address | jump target | case | 비고 |
| --- | --- | --- | --- |
| 0x402008 | 0x401113 | case 0 |  |
| 0x402010 | 0x401119 | case 1 | fall-through |
| 0x402018 | 0x40111d | case 2 |  |
| 0x402020 | 0x401127 | case 3 | default |
| 0x402028 | 0x401122 | case 4 | multiple label |
| 0x402030 | 0x401122 | case 5 | multiple label |

- 존재 X 인 case -> default 주소로 채움
- multiple label -> 동일 target 주소 중복 기입

### 간접 분기
``` nasm
0x401106 <+0>:  cmp $0x5,%rdi
; defalut 이동
0x40110a <+4>:  ja 0x401127 <switch_ex+31>
; jump table 이동
0x40110c <+6>:  jmp *0x402008(,%rdi,8)
...
0x401127 <+33>: mov $0x1,%eax
0x40112c <+38>: ret
```
- base `0x402008` + index `%rdi` × ==8== -> 64-bit 엔트리 주소
- table 진입 전 범위 검사 필수 -> 미검사 시 임의 주소 분기

### 정규화
- case 값 연속 · 밀집 -> base 값 빼서 0 기준 index 로 변환
- ==ex)== case 101 ~ 107
``` nasm
; x = eax
sub  eax, 101          ; 정규화 : eax = x - 101 (0 ~ 6 범위로 변환)
cmp  eax, 6            ; 범위 초과 검사
ja   .default          ; eax > 6이면 default로
jmp  [table + eax * 8] ; 점프 테이블 인덱싱 (64-bit : *8)

.table:
    dq .case101
    dq .case102
    dq .case103
    dq .case104
    dq .case105
    dq .case106
    dq .case107
```
- 음수 포함해도 정규화만 하면 동일 적용 O
- ==ex)== case -2 ~ 5
``` nasm
; x = eax
sub  eax, -2           ; 즉, add eax, 2 → 정규화 (0 ~ 7 범위)
cmp  eax, 7
ja   .default
jmp  [table + eax * 8]
```
