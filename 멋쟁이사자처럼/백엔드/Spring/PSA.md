---
aliases:
  - Portable Service Abstraction
---
- 다양한 기술을 일관된 방식으로 처리하도록 [[추상화]]

```java
@Transactional
public void order() {
    System.out.println("주문하기");
}
```