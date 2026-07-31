---
aliases:
  - while 문
  - Logically Controlled Loop
  - logically controlled loop(while)
---

- boolean 표현식에 기반해 반복하는 [[반복문]]
- 반복 횟수 미확정, 조건 거짓 -> 종료

### 형태
- [[C]] : pretest · posttest 양쪽 제공
	- pretest -> `while`
	- posttest -> `do ... while` -> ==최소 1회== 실행
``` c
/* pretest */
scanf ("%d", &indat) ;
while (indat >= 0) {
    sum = sum + indat ;
    scanf("%d", &indat) ;
}

/* posttest */
do {
    indat = indat / 10;
    digits = digits + 1;
} while (indat>0);
```
