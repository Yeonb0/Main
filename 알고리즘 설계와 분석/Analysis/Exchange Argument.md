- [[Greedy Algorithm#^4cf760|Greedy-Choice Property]] 를 가지는가?
- 임의의 최적해 (Optimal solution) 을 가져와서 greedt 가 고른 원소로 하나를 바꾸어도 해가 나빠지지 않음

### 과정
1. 최적해 가정 : 문제의 임의의 최적해 가정
2. 비교 : greedy 를 통해 선택 원소가 A 에 이미 있으면 증명 끝, 없으면
3. 교환 : A 안의 어떤 원소를 greedy 선택 원소로 바꿔 A' 를 만듬
4. 검증 : A' 도 요전히 유효하고, 크기 (혹은 값)가 A 와 같거나 더 좋음 
   -> A' 도 최적해