- 알고리즘 성능 측정에 주로 많이 사용
- Lower bound (하한) : 아무리 빨라져도 이만큼의 시간은 걸림

> [!example] 
> $f(n) = 7n^3 + 100n^2 - 20n + 6$
> -> $\Omega(n^3)$

- 보통 가장 높은 차수를 따름. (계수 무시)
- 하한 이므로 3차 이하의 차수도 괜찮음. 

### Formal Definition
> ![[Pasted image 20260629090837.png]
> ![[Pasted image 20260629091819.png]]
> ![[Pasted image 20260629091834.png]]
> - $n_0$ 이후에서 항상 $f(n)$ 의 아래쪽에 존재
> - $g(n)$ 은 $f(n)$ 의 점근적 하한 (asymtotic lower bound)


> [!Example] 
> ![[Pasted image 20260629091928.png]]
> - $\Omega(\lg n)$ 은 $n_0 = 16$ 이후 부터 모든 $\Omega(n^2)$ 함수보다 작다.



