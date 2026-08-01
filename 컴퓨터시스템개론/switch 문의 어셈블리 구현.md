---
aliases:
  - Switch Statement
  - switch 문의 어셈블리 구현(Switch Statement)
---

- [[switch]] 문 -> 범위 검사 + [[Jump Table]] 간접 분기로 변환
- single solution X -> case 값 분포에 따라 컴파일러가 [[Strategy|전략]] 선택

### 원본 코드
``` c
long switch_ex(long x, long y) {
	long z = y;
	switch (x) {
		case 0:
			z = 5;
			break;
		case 1:
			z += 1;
		case 2:
			z -= 2;
			break;
		case 4:
		case 5:
			z *= 3;
			break;
		default:
			z + 1;
		}
		return z;
	}
}
```

| case | 내용 |
| --- | --- |
| case 0 | 일반적인 switch-case 문 |
| case 1 -> case 2 | fall-through |
| case 3 | 존재 X -> default |
| case 4 & case 5 | multiple labels |
| default | case 이외 경우 |

### 어셈블리 코드
``` nasm
0x401106 <+0>:  cmp $0x5,%rdi
0x40110a <+4>:  ja 0x401127 <switch_ex+33>
0x40110c <+6>:  jmp *0x402008(,%rdi,8)
0x401113 <+13>: mov $0x5,%eax
0x401118 <+18>: ret
0x401119 <+19>: add $0x1,%rsi
0x40111d <+23>: lea -0x2(%rsi),%rax
0x401121 <+27>: ret
0x401122 <+28>: lea (%rsi,%rsi,2),%rax
0x401126 <+32>: ret
0x401127 <+33>: mov $0x1,%eax
0x40112c <+38>: ret
```
- `cmp $0x5,%rdi` : case 최댓값 ==5== -> `x > 5` 검사
- `ja` : unsigned 초과 -> default 로 jump
- `jmp *0x402008(,%rdi,8)` : [[Jump Table]] 간접 분기
``` nasm
0x401106 <+0>:  cmp $0x5,%rdi
; case 가 5 까지 있으므로 x > 5 check
0x40110a <+4>:  ja 0x401127 <switch_ex+33>
; x > 5 면 defalut 로 jump

...
defalut: 
0x401127 <+33>: mov $0x1,%eax
; z = 1 
```

### case 별 코드
- case 0 -> 독립 블록, `ret` 로 종료
``` nasm
case_0:
0x401113 <+13>: mov $0x5,%eax
0x401118 <+18>: ret
```
- case 1 & 2 -> fall-through, case 1 끝에 `ret` 없음 -> case 2 로 연속 실행
``` nasm
case_1:
0x401119 <+19>: add $0x1,%rsi
; 끝에 ret 없음
case_2:
0x40111d <+23>: lea -0x2(%rsi),%rax
0x401121 <+27>: ret
```
- case 3 -> 존재 X -> jump table 에서 default 로 jump
``` nasm
default:
0x401127 <+33>: mov $0x1,%eax
0x40112c <+38>: ret
```
- case 4 & 5 -> multiple labels, 동일 target 주소 공유
``` nasm
case_4:
case_5:
0x401122 <+28>: lea (%rsi,%rsi,2),%rax
0x401126 <+32>: ret
```

### 구현 전략
| 상황 | 전략 | 기준 |
| --- | --- | --- |
| case 101 ~ 107 | [[Jump Table]] | 연속 범위 -> $O(1)$ |
| case -2 ~ 5 | [[Jump Table]] | 음수 포함 연속 범위, 정규화 후 $O(1)$ |
| case 1, 48, 105, ... 306 | [[Binary Search]] | sparse -> $O(\log n)$ |
| case 2 ~ 3개 | Linear Search | 개수 적음 -> 단순 비교 |

- sparse case 에 jump table -> 미사용 엔트리 다수 -> [[메모리]] 낭비
- ==ex)== [[Binary Search]] : 중간값 비교 재귀 수행
``` nasm
; case 값들 : 1, 48, 105, 189, 230, 270, 306 (예시)
; 중간값 = 189

cmp  eax, 189
je   .case189
jl   .left_half        ; eax < 189 → 왼쪽 절반 탐색
jg   .right_half       ; eax > 189 → 오른쪽 절반 탐색

.left_half:
    cmp  eax, 48
    je   .case48
    jl   .ll_half      ; 1 탐색
    jg   .lr_half      ; 105 탐색
; ...
```
- ==ex)== Linear Search : case 3 ~ 4개 이하 -> 오버헤드 X
``` nasm
cmp  eax, 1
je   .case1
cmp  eax, 48
je   .case48
cmp  eax, 105
je   .case105
jmp  .default
```
