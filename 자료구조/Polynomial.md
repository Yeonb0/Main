---
aliases:
  - 다항식
---
## [[ADT]]
### [[객체|Objects]]
$P(x) a_{1}x^{e_{1}} + a_{n}x^{e_{n}}$
- $\langle e_{i}, a_{i} \rangle$의 순서쌍으로 된 집합
- $a_{i}$ : Coefficient (계수)
- $e_{i}$ : Exponent (지수) ≥ 0

### [[함수|Functions]]
$\forall$ poly $\in$ `Polynomial`, coef $\in$ `Codefficients`, expon $\in$ `Exponents`

- `Polynomial` `Zero()`
	- `return` $p(x) = 0$

- `Boolean` `IsZero(poly)`
	- `if` (poly)
		- `return` FALSE (존재하면)
		- `else return` TRUE (존재 안하면)

- `Coefficient` `Coef(poly, expon)`
	- `if` (expon $\in$ poly)
		- `return` 계수 (Coefficient) 
		- `else return` ()
	- 지수 정보로 계수 얻기

- `Exponent` `LeadExp(poly)`
	- `return` poly 에서 가장 큰 지수

- `Polynomial` `Attach(poly, expon)`
	- `if` (expon $\in$ poly)  
		- `return` error -> 이미 있으면 에러
		- `else return` $\langle$coef, exp$\rangle$  항이 삽입된 다항식 poly

- `Polynomial` `Attach(poly, expon)`
	- `if` (expon $\in$ poly)  
		- `return` 지수가 expon 잉 항이 삭제된 다항식 poly
		- `else return` error -> 이미 없으면 에러

- `Polynomial` `SingleMult(poly, coef, expon)`
	- `return` 다항식 $\text{poly} · \text{coef} · x^{\text{expon}}$

- `Polynomial` `Add(poly1, poly2)`
	- `return` 다항식 poly1 + poly2

- `Polynomial` `Mult(poly1, poly2)`
	- `return` 다항식 poly1 · poly2