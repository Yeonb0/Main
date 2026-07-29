---
aliases:
  - Plain Old Java Project
---

- 순수 [[Java]] 만을 통해서 생성한 [[객체]]
```java
// 기본적인 POJO의 예시
public class Member {

    private String name;
    private int age;

    public Member(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
    
}
```
- [[Spring|스프링]] 전용 [[클래스]] [[상속]] X
- 특별한 규칙에 강하게 묶여있지 않음
- 비즈니스 로직 구현 시 [[OOP|객체 지향 프로그래밍]] 설계를 제한 없이 적용 가능
- 코드가 단순해져 [[테스트]] & [[디버깅]] 쉬워짐 