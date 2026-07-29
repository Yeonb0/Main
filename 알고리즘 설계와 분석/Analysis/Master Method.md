- 조건 : $T(n) = aT\left( \frac{n}{b} \right) + f(n) \ \text{and} \ a \geq 1 \ \text{and} \ b > 1$

- 방법 : Driving function vs Watershed function
	- Driving function : $f(n)$
		- Didive & combine 비용
	- Watershed function : $n^{\log_{b}a}$
		- recursion tree 의 leaf node 비용
	-> 어떤 쪽이 더 dominant 한가?

- 경우
	- Case 1) Watershed Function 우위
		- $f(n) < O(n^{\log_{b}a})$ -> $T(n) = \Theta(n^{\log_{b}a})$
	- Case 2) 두 function 이 유사
		- $f(n) = \Theta(n^{\log_{b}a}\lg^kn)$ ->  $T(n) = \Theta(n^{\log_{b}a}\lg^{k+1}n)$
	- Case 3) Driving Function 우위
		- $f(n) > O(n^{\log_{b}a})$ -> $T(n) = \Theta(f(n))$
