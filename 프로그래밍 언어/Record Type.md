---
aliases:
  - 레코드 타입
  - Record Type(레코드 타입)
---

- 서로 다른 type 의 [[데이터]]를 모은 타입
	- ↔ [[배열]] : 같은 type 데이터를 모음
- 원소 접근 -> [[이름]] ==(name)== 사용
	- ==ex)== `employee.name.first`

### 예시
- COBOL -> nested record
``` sql
01 EMPLOYEE-RECORD.
   02 EMPLOYEE-NAME.
      05 FIRST          PICTURE IS X(20).
      05 MIDDLE         PICTURE IS X(10).
      05 LAST           PICTURE IS X(20).
   02 HOURLY-RATE       PICTURE IS 99V99.
```
- `MOVE CORRESPONDING` : 두 레코드에서 같은 이름 필드끼리만 자동 복사

### 구현
- 각 [[필드]] -> 인접 memory 공간에 ==순서대로== 저장
- word alignment : 성능 위해 memory 주소가 4의 배수 ==(8 byte type 이면 8의 배수)== 되도록 padding 삽입
- ==ex)==
``` c
struct aa {
	char c; // 1 byte
	int i; // 4 byte
} a;
```

| 1000 | 1001 | 1002 | 1003 | 1004 | 1005 | 1006 | 1007 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| c | pad | pad | pad | i | i | i | i |

- 실행 속도↑, 프로그램 실행 자체에는 문제 X
