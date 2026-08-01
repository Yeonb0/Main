---
aliases:
  - Instruction Set Architecture
  - 명령어 집합 구조
  - ISA(Instruction Set Architecture)
---

- [[CPU]] 가 따라야 하는 명령어의 집합
- 가능한 명령어 종류 · [[레지스터]] [[이름]] 규정
- high level & abstract level
- ==ex)== [[x86-64]], [[CISC]], [[RISC]]

### 추상화 단계
| 단계 | [[추상화]] 수준 | 대상 |
| --- | --- | --- |
| C language model | 가장 높음 | [[C]] 프로그래머 |
| ISA | 중간 | [[컴파일\|compiler]] 개발자 |
| [[마이크로아키텍처]] | 가장 낮음 | hardware-level 최적화 |

- ==ex)== C language model

```c
int main() {
	int i, n;
	for (i = 1; i <= n; ++i) {
		...
	}
}
```
