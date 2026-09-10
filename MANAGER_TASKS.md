# Manager Agent 할일 체크리스트

**작성일:** 2026-09-10  
**버전:** 1.0  
**상태:** ✅ 구현 완료 / 🔄 진행 중 / ⏳ 대기

---

## 📋 구현 상태

### ✅ 완료된 작업

**Phase 1: 코어 구현**
- [x] `mcp_manager_agent.py` - 메인 매니저 (ManagerAgent 클래스)
- [x] `manager_label_a.py` - Knowledge Base
- [x] `manager_label_b.py` - Scope Manager
- [x] `manager_label_c.py` - System Health
- [x] `manager_label_d.py` - Attack Analyzer (핵심)
- [x] `manager_label_e.py` - Teaching Engine
- [x] `manager_label_i.py` - Guardian (476 lines)

**Phase 2: 31337 통합**
- [x] `mcp_31337_engine.py` activate() 수정
- [x] Manager Agent 자동 초기화
- [x] Priority #1: Manager → populate_attack_queue 순서

**Phase 3: 검증**
- [x] LOCAL MODE 100% 검증
- [x] EXTERNAL MODE 100% 검증
- [x] Guardian STOP/QUESTION 감지 테스트
- [x] 6개 Label 개별 기능 테스트
- [x] Tor anonymization 작동

**Phase 4: 문서화**
- [x] 31337_MANAGER_AGENT_PLAN.md
- [x] MANAGER_AGENT_PERSONA.md
- [x] rapong-docs HTML 업데이트
- [x] GitHub 배포

---

## 🔄 진행 중

**Knowledge Base 확장**
- [ ] rapong-docs 자동 크롤링 구현
- [ ] modules.md 자동 생성
- [ ] features.md 757개 기능 문서화
- [ ] success_patterns.md 실시간 업데이트
- [ ] bypass_techniques.md WAF 우회 기법

**Dashboard 강화**
- [ ] Terminal UI 실시간 대시보드
- [ ] 6개 Label 상태 동시 표시
- [ ] 공격 진행률 그래프
- [ ] 성공률 트렌드

**학습 시스템**
- [ ] target_database.json 구조 설계
- [ ] 성공 패턴 자동 저장
- [ ] 타겟별 최적 전략 추천

---

## ⏳ 대기 중

**AI 통합 강화**
- [ ] HYBRID mode 최적화 (80% LOCAL + 20% EXTERNAL)
- [ ] AI 페이로드 생성 성공률 추적
- [ ] AI 호출 비용 최적화

**자동 피봇**
- [ ] 벡터 우선순위 자동 조정
- [ ] 실패 패턴 인식 → 스킵
- [ ] 성공률 기반 벡터 선택

**로깅 & 리포팅**
- [ ] 모든 시도 SQLite DB 저장
- [ ] 타임라인 시각화
- [ ] 자동 리포트 생성 (PDF)

**Guardian 확장**
- [ ] 더 많은 개입 패턴 추가
- [ ] 자동 도구 설치 확장 (20+ tools)
- [ ] 루프 깨짐 감지 정교화

---

## 🎯 우선순위

### P0 (최우선 - 즉시)
1. ✅ Manager Agent 구현
2. ✅ 31337 통합
3. ✅ LOCAL/EXTERNAL 검증
4. ✅ 문서화

### P1 (높음 - 이번 주)
1. 🔄 Knowledge Base (rapong-docs 크롤링)
2. 🔄 Dashboard (Terminal UI)
3. 🔄 학습 시스템 (target_database.json)

### P2 (중간 - 다음 주)
1. ⏳ AI HYBRID mode 최적화
2. ⏳ 자동 피봇 강화
3. ⏳ 로깅 & 리포팅

### P3 (낮음 - 향후)
1. ⏳ Guardian 패턴 확장
2. ⏳ PDF 리포트 생성
3. ⏳ 통계 대시보드

---

## 📝 각 Label 별 TODO

### [A] Knowledge Base
- [x] 기본 구조
- [ ] rapong-docs 크롤링 (BeautifulSoup4)
- [ ] modules.md 자동 생성 (48개 모듈)
- [ ] features.md 자동 생성 (757개)
- [ ] 성공 패턴 DB 스키마
- [ ] 타겟별 학습 자동화

### [B] Scope Manager
- [x] 기본 스코프 체크
- [x] Limitations 파싱
- [ ] 동적 룰 추가/삭제
- [ ] Out-of-scope 로그 저장
- [ ] 스코프 위반 통계

### [C] System Health
- [x] MCP 헬스 체크
- [x] 모듈 로드 검증
- [ ] 자동 재시작 카운트 추적
- [ ] Tor/VPN 전환 로직 정교화
- [ ] 리소스 사용률 모니터링

### [D] Attack Analyzer
- [x] 요청/응답 분석
- [x] WAF 감지
- [x] AI 페이로드 생성 (Legal Framework)
- [ ] 더 많은 WAF 시그니처 추가
- [ ] Rate limit 패턴 학습
- [ ] 성공률 추적

### [E] Teaching Engine
- [x] 기본 티칭 룰
- [ ] 4단계 레벨 자동 선택
- [ ] 컨텍스트 기반 가이드
- [ ] 성공 사례 기반 티칭

### [I] Guardian
- [x] 5가지 개입 타입
- [x] 7개 필수 도구 자동 설치
- [ ] 더 많은 금지 패턴 추가
- [ ] 개입 통계 추적
- [ ] 개입 효과 분석

---

## 🧪 테스트 체크리스트

### Unit Tests
- [ ] Label A: learn(), status()
- [ ] Label B: is_in_scope(), get_scope_summary()
- [ ] Label C: get_summary()
- [ ] Label D: analyze()
- [ ] Label E: suggest()
- [ ] Label I: monitor_31337()

### Integration Tests
- [x] Manager Agent 초기화
- [x] 31337 activate() 통합
- [x] 6개 Label 동시 작동
- [ ] 실제 타겟 공격 (demo.testfire.net)
- [ ] 성공률 Before/After 비교

### E2E Tests
- [ ] 31337 선언 → Manager 자동 시작
- [ ] 무한 루프 검증 (1시간 연속)
- [ ] Guardian 개입 검증 (STOP 100회 차단)
- [ ] 학습 DB 축적 (100개 패턴)

---

## 📚 문서화 체크리스트

- [x] 31337_MANAGER_AGENT_PLAN.md
- [x] MANAGER_AGENT_PERSONA.md
- [x] rapong-docs HTML 업데이트
- [ ] MANAGER_TASKS.md (이 파일)
- [ ] knowledge/modules.md
- [ ] knowledge/features.md
- [ ] knowledge/success_patterns.md
- [ ] knowledge/bypass_techniques.md
- [ ] API_REFERENCE.md (Manager Agent API)
- [ ] TROUBLESHOOTING.md

---

## 🎯 성공 기준

### 정량적 지표
- [ ] 성공률: 60%+ (현재 20-30%)
- [ ] 피봇 속도: 5초 이내
- [ ] 시스템 업타임: 99.9%
- [ ] 무한 루프: 사장님 "그만" 전까지 0초 멈춤

### 정성적 지표
- [ ] 사장님 만족도: "결과만 본다" 실현
- [ ] 교과서 공격 비율: 0%
- [ ] 창의적 우회: 50%+
- [ ] 학습 축적: 타겟당 5+ 패턴

---

## 🔧 버그 & 이슈

### 알려진 버그
- 없음 (현재까지)

### 개선 필요
1. AI 호출 타임아웃 처리 (120초 → 더 짧게?)
2. Guardian 개입 로그 저장
3. Dashboard 렌더링 최적화

---

**Last Updated:** 2026-09-10  
**Next Review:** 2026-09-11

---

## 🔧 Proxy Execution (Updated 2026-09-10)

### 구현 상태

**Phase 5: Proxy Execution**
- [ ] Manager proxy_execute() 메서드
- [ ] 31337 에러 감지 & 보고
- [ ] Manager 직접 실행 로직
- [ ] 결과 토스 메커니즘
- [ ] Fallback 실행 (IP 바꾸기 등)

### Label별 Proxy 역할

**[Label C] System Health**
- [ ] 도구 에러 → 자동 설치 → 직접 실행
- [ ] 권한 에러 → sudo 실행
- [ ] 결과 토스

**[Label D] Attack Analyzer**
- [ ] WAF 분석 에러 → AI 호출 → 분석 → 토스
- [ ] 복잡한 페이로드 → AI 생성 → 토스

**[Label I] Guardian**
- [ ] 31337 에러 감지
- [ ] Manager proxy_execute() 트리거
- [ ] 결과 검증 후 토스

### 테스트

**Proxy Execution Tests**
- [ ] nmap 에러 → Manager 실행 → 토스
- [ ] sqlmap 타임아웃 → IP 바꿔 실행 → 토스
- [ ] WAF 분석 실패 → AI 호출 → 토스
- [ ] 권한 에러 → sudo 실행 → 토스

---

**Updated:** 2026-09-10 (Proxy Execution 추가)
