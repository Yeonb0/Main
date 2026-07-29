- N-ary Tree 를 그려 분석
	- Substitution Method 보다 정확
- 과정
	1. root 부분에 Divide & Combine 부분을 넣는다
	2. root 에서 Conquer 횟수 만큼 child node 그리기
		- depth 가 +1 될때마다 size / node 갯수 구하기
		- depth i 에서 총 비용 = node 1 개의 비용 $\times$  node 갯수
	3. leaf 까지 내려간다
	4. Total cost 를 구한다
	5. 검증한다 -> [[Substitution Method]] 사용