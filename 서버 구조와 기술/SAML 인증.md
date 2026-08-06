---
aliases:
  - SAML
  - Security Assertion Markup Language
  - SAML 인증(SAML Authentication)
---

- SAML 지원 웹 사이트 간 [[인증]] 정보 or [[인가]] 정보 전달 방식
- [[SSO]] 구현 기술

### 구조
- SP (Service Provider) : 서비스 제공 측
- IdP (ID Provider) : 인증 정보 제공 측

### 절차
1. 접속 [[서버]]에 SP 설정
2. IdP 가 SAML 지원하는 [[인증 서버]]에서 [[클라이언트]] 인증 & 인증 어설션 발행
3. 발행 정보를 SP 가 검증
4. 서비스 제공

![[서버-운용을-알아보자-02.png]]
