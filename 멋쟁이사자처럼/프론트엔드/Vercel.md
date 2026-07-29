---
aliases:
  - 배포
---

1. 프로젝트 루트 경로에서 [[Vercel]] 모듈 다운 받기
```bash
npm i vercel
```

2. [[Vercel]] 계정으로 로그인 
```bash
npx vercel login
```

3. 아래 명령어로 배포 시작
```bash
npx vercel
```

4. 아래 질문에 답하기
```bash
? Which team? yeonb0 (본인 계정 이름)

? Project? Create new project

? Name? 프로젝트명

? Customize settings? no

? Customize advanced settings? no

? Connect detected Git repository? yes
```


5. 아래 문구가 나오면 배포 완료
![[Pasted image 20260706092941.png]]


## 환경 변수 설정
1. 프로젝트 대시보드 -> Settings -> Environment variables 로 들어가기
2. `.env` 파일에 있는 Key - Value 를 넣고 Save
3. `Redeploy` 를 눌러서 재배포 및 업데이트