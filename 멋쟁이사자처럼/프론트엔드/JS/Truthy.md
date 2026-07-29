---
aliases:
  - Truthy
  - truthy
---


- [[boolean]] 으로 평가되는 상황에서 `true`로 취급되는 값
- [[Falsy]]를 제외한 모든 값이 [[Truthy]]

```js
// truthy
if (true)
if ({})
if ([])
if (42)
if ("0")
if ("false")
if (new Date())
if (-42)
if (12n)
if (3.14)
if (-3.14)
if (Infinity)
if (-Infinity)
```