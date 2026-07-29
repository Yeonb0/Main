- 알고리즘 성능 측정에 주로 많이 사용
- Upper bound (상한) : 아무리 시간이 많이 걸려도 이 시간을 넘진 않음

> [!example] 
> $f(n) = 7n^3 + 100n^2 - 20n + 6$
> -> $O(n^3)$

- 보통 가장 높은 차수를 따름. (계수 무시)
- 상한 이므로 3차 이상의 차수도 괜찮음. 

### Formal Definition
> ![[Pasted image 20260629090837.png]]
> ![[Pasted image 20260629090859.png]]
> - $n_0$ 이후에서 항상 $f(n)$ 의 위쪽에 존재
> - $g(n)$ 은 $f(n)$ 의 점근적 상한 (asymtotic upper bound)


> [!Example] 
> ![[Pasted image 20260629091350.png]]
> - $O(n^3)$ 은 $n_0 = 2$ 이후 부터 모든 $O(n^2)$ 함수보다 크다.



