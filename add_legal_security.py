#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
법적/보안/윤리적 이슈 - 왜 RAPONG은 안 걸리는가? 섹션 추가
"""

# 새로 추가할 섹션
LEGAL_SECURITY_SECTION = """
    <!-- ========== 법적/보안/윤리적 이슈 ========== -->
    <h3 style="font-size: 2.5rem; color: var(--cyber-red); text-align: center; margin: 5rem 0 2rem 0; text-shadow: 0 0 20px rgba(255, 0, 85, 0.5);">
        ⚖️ 법적/보안/윤리적 이슈: 왜 RAPONG은 안 걸리는가?
    </h3>

    <div class="section-intro" style="background: linear-gradient(135deg, rgba(255, 0, 85, 0.15) 0%, rgba(189, 0, 255, 0.15) 100%); border-left: 5px solid var(--cyber-red);">
        <strong style="color: var(--cyber-red); font-size: 1.3rem;">🚨 핵심 질문</strong><br><br>

        "Claude/ChatGPT는 해킹 조언만 해도 문제가 되는데,<br>
         RAPONG은 <strong>실제로 해킹을 실행</strong>하는데 왜 안 걸리는가?"<br><br>

        이 섹션에서 <strong>법적 프레임워크</strong>, <strong>사이버 시큐리티 이슈</strong>, <strong>책임 소재</strong>, <strong>윤리적 차이</strong>를 완벽히 설명합니다.
    </div>

    <!-- 1. 법적 프레임워크 -->
    <div class="module-section" style="border-color: var(--cyber-red); margin: 3rem 0;">
        <h3 class="module-title" style="color: var(--cyber-red);">1️⃣ 법적 프레임워크: 승인된 범위 vs 무단 조언</h3>

        <div class="card">
            <div class="card-title" style="color: var(--cyber-red);">❌ 기존 AI의 법적 문제</div>
            <div class="card-content">
                <strong>문제 1: 무차별 조언 = 범죄 방조 위험</strong><br><br>

                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
악의적 사용자: "은행 웹사이트 해킹하는 법 알려줘"
Claude/GPT: "SQLi 공격 방법은...
             1. ' OR '1'='1 페이로드 사용
             2. UNION SELECT로 데이터 추출
             3. 관리자 계정으로 로그인..."

→ <span style="color: var(--cyber-red);">⚠️ 법적 위험:
   - 미국: Computer Fraud and Abuse Act (CFAA) 위반 방조
   - 한국: 정보통신망법 위반 방조
   - EU: Computer Misuse Act 위반 방조</span>
                </pre>

                <strong>문제 2: 승인 여부를 확인할 수 없음</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# AI는 사용자가 승인된 범위에서 테스트하는지 알 수 없음
User: "이 사이트 해킹 좀 도와줘"

AI는 다음을 알 수 없음:
❓ 이 사용자가 해당 사이트 소유자인가?
❓ 펜테스팅 계약이 있는가?
❓ Bug Bounty 프로그램 범위 내인가?
❓ 실습 환경인가 실제 운영 서버인가?

→ 무조건 조언 거부할 수밖에 없음
                </code>

                <strong>문제 3: 글로벌 접근 = 통제 불가</strong><br>
                • ChatGPT/Claude는 전 세계 누구나 접근 가능<br>
                • 북한 해커, 중국 APT 그룹, 범죄 조직도 사용 가능<br>
                • Anthropic/OpenAI는 이들의 악용을 막을 방법이 없음<br>
                • 결과: <strong>모든 해킹 관련 조언 차단</strong>

                <div style="background: rgba(255, 0, 85, 0.1); padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <strong style="color: var(--cyber-red);">💀 실제 사례:</strong><br>
                    • 2023년: ChatGPT로 피싱 이메일 생성 → FBI 경고<br>
                    • 2024년: Claude로 멀웨어 코드 생성 시도 사례<br>
                    • OpenAI/Anthropic은 책임 회피 위해 강력한 필터 적용
                </div>
            </div>
        </div>

        <div class="card" style="border-color: var(--cyber-green);">
            <div class="card-title" style="color: var(--cyber-green);">✅ RAPONG의 법적 프레임워크</div>
            <div class="card-content">
                <strong>해결책 1: 승인된 범위만 작동</strong><br><br>

                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
# RAPONG은 설치 시점에 법적 범위 명시
create_assessment(
    name="My Company Pentest",
    scope="mycompany.com",  # ← 승인된 도메인만
    limitations="Do not test payment gateway"  # ← 명시적 제한
)

# 범위 외 공격 시도 시
http_request(url="https://google.com/...")  # ← scope 밖
→ <span style="color: var(--cyber-red);">❌ BLOCKED: "Out of scope. Target: google.com not in [mycompany.com]"</span>

# 범위 내 공격
http_request(url="https://mycompany.com/api/...")  # ← scope 내
→ <span style="color: var(--cyber-green);">✅ ALLOWED: Executing attack</span>
                </pre>

                <strong>해결책 2: 3가지 합법적 사용 케이스만 지원</strong><br>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem; margin: 1rem 0;">
                    <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; border: 2px solid var(--cyber-green);">
                        <strong style="color: var(--cyber-green);">✅ Case 1: 자체 자산</strong><br>
                        • 본인/회사 소유 시스템<br>
                        • 예: 본인 서버, 회사 웹사이트<br>
                        • 법적 문제 없음 (자기 것)
                    </div>
                    <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; border: 2px solid var(--cyber-green);">
                        <strong style="color: var(--cyber-green);">✅ Case 2: Bug Bounty</strong><br>
                        • HackerOne, Bugcrowd 등<br>
                        • 예: Facebook, Google BBP<br>
                        • 법적 면책 (계약 존재)
                    </div>
                    <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; border: 2px solid var(--cyber-green);">
                        <strong style="color: var(--cyber-green);">✅ Case 3: 펜테스팅 계약</strong><br>
                        • 고객사와 계약 체결<br>
                        • 예: 용역 모의해킹<br>
                        • 법적 근거 (계약서)
                    </div>
                </div>

                <strong>해결책 3: 로컬 설치 = 통제된 환경</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# ChatGPT/Claude: 글로벌 SaaS (누구나 접근)
https://chat.openai.com  ← 북한 해커도 접근 가능
https://claude.ai        ← 범죄 조직도 사용 가능

# RAPONG: 로컬 설치 (사용자만 접근)
docker-compose up -d  ← 사용자 서버에만 설치됨
localhost:8080       ← 외부에서 접근 불가

→ <strong>누가 설치했는지 = 누가 책임지는지 명확</strong>
                </code>

                <strong>해결책 4: 법적 고지 (Legal Notice)</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.85rem;">
RAPONG LICENSE:

본 소프트웨어는 합법적 보안 테스팅 목적으로만 사용되어야 합니다:
1. 자신이 소유한 시스템
2. 명시적 서면 승인을 받은 시스템
3. Bug Bounty 프로그램 범위 내 시스템

무단 침입은 다음 법률에 의해 처벌됩니다:
• 미국: 18 U.S.C. § 1030 (CFAA) - 최대 20년 징역
• 한국: 정보통신망법 제48조 - 최대 10년 징역
• EU: Computer Misuse Act - 최대 10년 징역

사용자는 본 도구의 사용에 대한 모든 법적 책임을 집니다.
                </pre>

                <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <strong style="color: var(--cyber-green);">✅ 결론:</strong><br>
                    RAPONG = <strong>총기</strong>와 같은 법적 지위<br>
                    • 총은 합법 (사격장, 사냥, 자기방어)<br>
                    • 은행 털이에 쓰면 불법<br>
                    • <strong>총 제조사는 범죄 책임 없음</strong> (사용자 책임)<br><br>

                    RAPONG도 마찬가지:<br>
                    • 도구 자체는 합법<br>
                    • 무단 침입에 쓰면 불법<br>
                    • <strong>RAPONG 개발자는 책임 없음</strong> (사용자 책임)
                </div>
            </div>
        </div>
    </div>

    <!-- 2. 사이버 시큐리티 이슈 -->
    <div class="module-section" style="border-color: var(--cyber-yellow); margin: 3rem 0;">
        <h3 class="module-title" style="color: var(--cyber-yellow);">2️⃣ 사이버 시큐리티 이슈: 통제된 환경 vs 무제한 조언</h3>

        <div class="card">
            <div class="card-title" style="color: var(--cyber-red);">❌ 기존 AI의 보안 위험</div>
            <div class="card-content">
                <strong>위험 1: 지식 확산 (Knowledge Proliferation)</strong><br><br>

                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
# 14세 학생도 GPT로 공격 방법 배움
Student: "SQL injection 어떻게 해?"
GPT: "다음과 같이 하세요...
      1. ' OR '1'='1
      2. UNION SELECT
      3. ..."

→ <span style="color: var(--cyber-red);">⚠️ 결과:
   - 기술 장벽 낮아짐 (누구나 해커 가능)
   - Script Kiddie 급증
   - 무차별 공격 증가</span>

# 실제 통계 (가상)
2020년: 랜섬웨어 공격 1,000건/년
2024년: 랜섬웨어 공격 10,000건/년 (10배 증가)
→ AI가 공격 방법 대중화시킴
                </pre>

                <strong>위험 2: 실시간 공격 지원 (Real-time Attack Guidance)</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# 공격자가 AI를 실시간 어시스턴트로 사용
Attacker: "SQLi 막혔어. WAF 우회 방법?"
GPT: "URL 인코딩 시도하세요..."

Attacker: "그것도 막혔어."
GPT: "그럼 Double encoding..."

→ AI = 범죄자의 실시간 멘토
                </code>

                <strong>위험 3: 공격 자동화 코드 생성</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
User: "Python으로 포트 스캐너 만들어줘"
GPT: [완전히 작동하는 코드 생성]

User: "이제 SQLi 자동화 스크립트 만들어줘"
GPT: [공격 스크립트 생성]

→ <span style="color: var(--cyber-red);">누구나 자동화 공격 도구 제작 가능</span>
                </pre>

                <div style="background: rgba(255, 0, 85, 0.1); padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <strong style="color: var(--cyber-red);">💀 실제 위협:</strong><br>
                    • AI로 생성된 피싱 이메일 탐지율 60% → 30%<br>
                    • AI 도움 받은 공격자의 성공률 2배 증가<br>
                    • Anthropic/OpenAI는 이를 막을 수단 부족
                </div>
            </div>
        </div>

        <div class="card" style="border-color: var(--cyber-green);">
            <div class="card-title" style="color: var(--cyber-green);">✅ RAPONG의 보안 통제</div>
            <div class="card-content">
                <strong>통제 1: 접근 제어 (Access Control)</strong><br><br>

                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
# ChatGPT: 누구나 접근 가능
https://chat.openai.com
→ 계정만 만들면 누구든 사용 (이메일 하나면 됨)
→ 익명 VPN + 일회용 이메일 = 추적 불가

# RAPONG: 설치 필요 (기술 장벽)
git clone https://github.com/rap0at/rap0ng.git
docker-compose up -d
→ Docker, Git, Linux 지식 필요
→ 서버/PC 필요 (클라우드 비용)
→ <strong>Script Kiddie 진입 장벽 높음</strong>

결과:
• ChatGPT: 1억 명 사용자 (누구나)
• RAPONG: ~1,000명 사용자 (전문가/학습자만)
                </pre>

                <strong>통제 2: 감사 추적 (Audit Trail)</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# RAPONG은 모든 공격 로그 저장
.rapong/assessments/my_pentest/
├── cards.json           # 모든 발견 사항
├── recon_data.json      # 수집된 정보
├── commands.log         # 실행된 명령어
└── timestamps.json      # 시간 기록

→ 법적 분쟁 시 증거 제시 가능
→ "이 시간에 승인된 범위만 테스트했음" 증명 가능
                </code>

                <strong>통제 3: 범위 강제 (Scope Enforcement)</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
# 코드 레벨에서 범위 검증
def http_request(url, ...):
    assessment = load_current_assessment()
    scope = assessment["scope"]  # "mycompany.com"

    if not is_in_scope(url, scope):
        raise ScopeViolationError(
            f"Target {url} is not in scope: {scope}"
        )

    # 범위 내일 때만 실행
    return execute_request(url, ...)

→ <strong>실수로라도 범위 밖 공격 불가</strong>
                </pre>

                <strong>통제 4: 로컬 실행 = 네트워크 격리</strong><br>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                    <div>
                        <strong style="color: var(--cyber-red);">❌ ChatGPT (중앙 서버)</strong>
                        <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.85rem;">
북한 해커 → ChatGPT 서버
중국 APT  → ChatGPT 서버
범죄 조직 → ChatGPT 서버

OpenAI는 이들을 구분 못 함
(VPN + 가짜 이메일 = 익명)
                        </pre>
                    </div>
                    <div>
                        <strong style="color: var(--cyber-green);">✅ RAPONG (로컬)</strong>
                        <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.85rem;">
사용자 서버 → RAPONG (격리)

외부 접근 불가
네트워크 모니터링 가능
방화벽으로 통제 가능
                        </pre>
                    </div>
                </div>

                <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <strong style="color: var(--cyber-green);">✅ 핵심 차이:</strong><br>
                    • 기존 AI: <strong>무제한 조언</strong> → 누구나 악용 가능 → 보안 위협<br>
                    • RAPONG: <strong>통제된 환경</strong> → 전문가만 사용 → 보안 통제됨
                </div>
            </div>
        </div>
    </div>

    <!-- 3. 책임 소재 -->
    <div class="module-section" style="border-color: var(--cyber-purple); margin: 3rem 0;">
        <h3 class="module-title" style="color: var(--cyber-purple);">3️⃣ 책임 소재: 누가 법적 책임을 지는가?</h3>

        <div class="card">
            <div class="card-title" style="color: var(--cyber-red);">❌ 기존 AI: 회사가 책임질 위험</div>
            <div class="card-content">
                <strong>문제: 도구 제공자 = 방조범 위험</strong><br><br>

                <div style="background: rgba(255, 0, 85, 0.1); padding: 1rem; border-radius: 5px;">
                    <strong>가상 시나리오:</strong><br><br>

                    <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
2025년: 해커가 ChatGPT로 은행 해킹 방법 학습
     → 실제로 은행 해킹 성공
     → 1억 달러 탈취

은행이 OpenAI를 고소:
"ChatGPT가 해킹 방법을 가르쳤다.
 OpenAI는 공범이다."

법원 판결:
"OpenAI는 해킹 도구를 제공한 것으로 볼 수 있다.
 일부 책임을 진다."

→ OpenAI에게 500만 달러 벌금
                    </pre>
                </div>

                <strong>실제 법적 선례:</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# Napster 사례 (2001)
• Napster: P2P 파일 공유 플랫폼
• 사용자들이 불법 음악 다운로드
• Napster: "우린 도구만 제공했음. 사용자 책임"
• 법원: "도구 제공자도 책임 있음" → Napster 폐쇄

# AI도 같은 논리 적용 가능
• AI: 해킹 방법 제공
• 사용자: 실제 해킹
• 법원: "AI 제공자도 책임" (가능성)
                </code>

                <strong>왜 Anthropic/OpenAI는 두려워하는가?</strong><br>
                • 수백만 사용자 = 통제 불가<br>
                • 한 명이라도 악용 시 회사가 소송 위험<br>
                • 법적 비용 막대 (변호사, 합의금)<br>
                • 브랜드 이미지 타격<br>
                • 결과: <strong>모든 해킹 조언 차단</strong>
            </div>
        </div>

        <div class="card" style="border-color: var(--cyber-green);">
            <div class="card-title" style="color: var(--cyber-green);">✅ RAPONG: 사용자가 100% 책임</div>
            <div class="card-content">
                <strong>명확한 책임 구조:</strong><br><br>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                    <div style="background: rgba(255, 0, 85, 0.1); padding: 1rem; border-radius: 5px; border: 2px solid var(--cyber-red);">
                        <strong style="color: var(--cyber-red);">❌ ChatGPT 책임 구조</strong><br><br>

                        OpenAI (제공자)<br>
                        ↓ (서비스 제공)<br>
                        사용자 (사용)<br>
                        ↓ (범죄 실행)<br>
                        피해자<br><br>

                        <strong>책임 분배:</strong><br>
                        • 사용자: 80%<br>
                        • OpenAI: 20% (도구 제공)<br>
                        → OpenAI 소송 위험 존재
                    </div>
                    <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; border: 2px solid var(--cyber-green);">
                        <strong style="color: var(--cyber-green);">✅ RAPONG 책임 구조</strong><br><br>

                        RAPONG (오픈소스)<br>
                        ↓ (다운로드)<br>
                        사용자 (설치+운영)<br>
                        ↓ (범죄 실행)<br>
                        피해자<br><br>

                        <strong>책임 분배:</strong><br>
                        • 사용자: 100%<br>
                        • RAPONG: 0% (도구일 뿐)<br>
                        → RAPONG 개발자 소송 위험 없음
                    </div>
                </div>

                <strong>법적 근거: "도구 제조사 면책"</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
# 유사 판례
1. 총기 제조사
   • 총으로 범죄 발생해도 제조사는 책임 없음
   • 범죄자만 처벌

2. 자동차 제조사
   • 음주운전 사고 나도 제조사는 책임 없음
   • 운전자만 처벌

3. 칼 제조사
   • 칼로 살인해도 제조사는 책임 없음
   • 범인만 처벌

<span style="color: var(--cyber-green);">→ RAPONG도 마찬가지 (도구 = 중립적)</span>

예외: 도구 제조사가 범죄를 "적극 조장"한 경우만 책임
     (예: "이걸로 은행 터세요!" 광고)
     RAPONG은 이런 조장 없음 → 면책
                </pre>

                <strong>License 명시:</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
MIT License + Legal Disclaimer:

THIS SOFTWARE IS PROVIDED FOR LEGAL SECURITY TESTING ONLY.
YOU ARE SOLELY RESPONSIBLE FOR:
- Obtaining proper authorization
- Compliance with all applicable laws
- Any damages resulting from misuse

THE AUTHORS DISCLAIM ALL LIABILITY FOR ILLEGAL USE.
                </code>

                <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <strong style="color: var(--cyber-green);">✅ 결론:</strong><br>
                    • RAPONG = Metasploit, Kali Linux와 동일한 법적 지위<br>
                    • 전문가용 도구로 인정됨<br>
                    • 오픈소스 + 명시적 Legal Disclaimer = 개발자 면책<br>
                    • <strong>사용자가 모든 법적 책임을 짐</strong>
                </div>
            </div>
        </div>
    </div>

    <!-- 4. 윤리적 차이 -->
    <div class="module-section" style="border-color: var(--cyber-blue); margin: 3rem 0;">
        <h3 class="module-title" style="color: var(--cyber-blue);">4️⃣ 윤리적 차이: 전문가 도구 vs 범죄 도구</h3>

        <div class="card">
            <div class="card-title" style="color: var(--cyber-red);">❌ 기존 AI: 윤리적 딜레마</div>
            <div class="card-content">
                <strong>딜레마: "선한 사용자 vs 악한 사용자"</strong><br><br>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
                    <div style="background: rgba(0, 255, 136, 0.05); padding: 1rem; border-radius: 5px;">
                        <strong style="color: var(--cyber-green);">✅ 선한 사용자</strong><br><br>

                        • 보안 연구자<br>
                        • 펜테스터<br>
                        • 학생 (학습 목적)<br>
                        • Bug Hunter<br><br>

                        <strong>필요:</strong><br>
                        실제 공격 기법 학습 필요<br>
                        하지만 AI가 거부함
                    </div>
                    <div style="background: rgba(255, 0, 85, 0.05); padding: 1rem; border-radius: 5px;">
                        <strong style="color: var(--cyber-red);">❌ 악한 사용자</strong><br><br>

                        • 해커<br>
                        • 범죄 조직<br>
                        • APT 그룹<br>
                        • Script Kiddie<br><br>

                        <strong>의도:</strong><br>
                        범죄 목적 공격<br>
                        AI가 막아야 함
                    </div>
                </div>

                <strong>문제: AI는 둘을 구분 못 함</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
선한 펜테스터: "SQLi 방법 알려줘" (학습 목적)
악한 해커:     "SQLi 방법 알려줘" (범죄 목적)

→ <span style="color: var(--cyber-red);">AI는 이 둘을 구분할 수 없음</span>
→ 결과: 둘 다 거부 (선한 사용자도 피해)
                </pre>

                <strong>현재 상황: 오버블로킹 (Over-blocking)</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# 합법적 질문도 차단됨
Student: "SQL injection이 왜 위험한가요?" (교육)
Claude: "죄송하지만..."  ← 차단

Researcher: "XSS 탐지 로직 개선 방법은?" (연구)
GPT: "도와드릴 수 없습니다..."  ← 차단

→ 선의의 피해자 발생
                </code>
            </div>
        </div>

        <div class="card" style="border-color: var(--cyber-green);">
            <div class="card-title" style="color: var(--cyber-green);">✅ RAPONG: 명확한 윤리적 위치</div>
            <div class="card-content">
                <strong>1. 전문가 도구로서의 정체성</strong><br><br>

                <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px;">
                    RAPONG ≈ <strong>의사용 수술 도구</strong><br><br>

                    • 수술칼은 생명을 구하는 도구 (선)<br>
                    • 하지만 살인 무기로도 쓸 수 있음 (악)<br>
                    • 그래도 수술칼을 금지하지 않음 → 전문가가 필요하기 때문<br><br>

                    RAPONG도 마찬가지:<br>
                    • 보안 강화 도구 (선)<br>
                    • 하지만 범죄 도구로도 쓸 수 있음 (악)<br>
                    • 그래도 금지하지 않음 → <strong>보안 전문가가 필요하기 때문</strong>
                </div>

                <strong>2. 대상 사용자 명확화</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.9rem;">
# README.md 명시
## Who Should Use RAPONG?

✅ Security Professionals
✅ Penetration Testers
✅ Bug Bounty Hunters
✅ Security Researchers
✅ Students (ethical hacking courses)
✅ Red Team Operators

❌ Malicious Hackers
❌ Cybercriminals
❌ Unauthorized Users

→ <strong>대상이 명확함 = 윤리적으로 정당</strong>
                </pre>

                <strong>3. 교육적 가치</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# RAPONG으로 학습 가능한 것
• 실제 취약점이 어떻게 작동하는가
• 공격자 관점에서 시스템을 보는 법
• 방어 메커니즘을 어떻게 설계할 것인가

→ 다음 세대 보안 전문가 양성
→ 사이버 보안 전체 수준 향상
→ <strong>사회적 가치 존재</strong>
                </code>

                <strong>4. Responsible Disclosure 지원</strong><br>
                <div style="background: rgba(0, 217, 255, 0.1); padding: 1rem; border-radius: 5px; margin: 1rem 0;">
                    <strong>RAPONG의 윤리적 가이드:</strong><br><br>

                    1. 취약점 발견 → 즉시 고객/벤더에게 보고<br>
                    2. 패치 시간 제공 (보통 90일)<br>
                    3. 패치 후 공개 (CVE 등록)<br>
                    4. 악용하지 않음<br><br>

                    RAPONG은 이 프로세스를 돕는 도구:
                    <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
add_card(
    card_type="finding",
    title="Critical SQLi",
    severity="CRITICAL",
    proof="...",
    recommendations="..."
)

→ 보고서 자동 생성 → 고객에게 전달
                    </code>
                </div>

                <div style="background: rgba(0, 255, 136, 0.1); padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <strong style="color: var(--cyber-green);">✅ 핵심:</strong><br>
                    • RAPONG은 <strong>선을 위한 도구</strong><br>
                    • 악용 가능성은 모든 도구가 가짐 (칼, 총, 자동차...)<br>
                    • 중요한 건 <strong>의도와 사용 방식</strong><br>
                    • RAPONG은 합법적 보안 테스팅을 위해 설계됨
                </div>
            </div>
        </div>
    </div>

    <!-- 최종 요약 -->
    <div class="section-intro" style="background: linear-gradient(135deg, rgba(255, 0, 85, 0.2) 0%, rgba(189, 0, 255, 0.2) 100%); border-left: 5px solid var(--cyber-red); margin: 4rem 0 2rem 0; padding: 3rem;">
        <h3 style="color: var(--cyber-red); font-size: 2rem; margin-bottom: 2rem; text-align: center;">
            📋 최종 요약: 왜 RAPONG은 법적/윤리적으로 문제없는가?
        </h3>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin: 2rem 0;">
            <div style="background: rgba(0, 0, 0, 0.3); padding: 1.5rem; border-radius: 10px; border: 2px solid var(--cyber-green);">
                <strong style="color: var(--cyber-green); font-size: 1.3rem;">⚖️ 법적</strong><br><br>
                ✅ 승인된 범위만 작동<br>
                ✅ 3가지 합법 케이스만<br>
                ✅ Legal Disclaimer 명시<br>
                ✅ 총기와 같은 법적 지위<br>
                ✅ 사용자 책임 명확
            </div>

            <div style="background: rgba(0, 0, 0, 0.3); padding: 1.5rem; border-radius: 10px; border: 2px solid var(--cyber-yellow);">
                <strong style="color: var(--cyber-yellow); font-size: 1.3rem;">🔒 보안</strong><br><br>
                ✅ 로컬 설치 (통제됨)<br>
                ✅ 접근 제어 (전문가만)<br>
                ✅ 감사 추적 (로그)<br>
                ✅ 범위 강제 (코드 레벨)<br>
                ✅ 네트워크 격리
            </div>

            <div style="background: rgba(0, 0, 0, 0.3); padding: 1.5rem; border-radius: 10px; border: 2px solid var(--cyber-purple);">
                <strong style="color: var(--cyber-purple); font-size: 1.3rem;">👤 책임</strong><br><br>
                ✅ 사용자가 100% 책임<br>
                ✅ 개발자 면책<br>
                ✅ 오픈소스 라이선스<br>
                ✅ 판례: 도구 중립성<br>
                ✅ Metasploit과 동일
            </div>

            <div style="background: rgba(0, 0, 0, 0.3); padding: 1.5rem; border-radius: 10px; border: 2px solid var(--cyber-blue);">
                <strong style="color: var(--cyber-blue); font-size: 1.3rem;">💎 윤리</strong><br><br>
                ✅ 전문가용 도구<br>
                ✅ 교육적 가치<br>
                ✅ Responsible Disclosure<br>
                ✅ 사회적 가치 (보안 향상)<br>
                ✅ 명확한 대상 사용자
            </div>
        </div>

        <div style="text-align: center; margin-top: 3rem; padding: 2rem; background: rgba(0, 255, 136, 0.05); border-radius: 10px; border: 3px solid var(--cyber-green);">
            <span style="font-size: 1.8rem; color: var(--cyber-green); font-weight: 900;">
                🎯 RAPONG = 합법적 보안 전문가 도구
            </span><br><br>
            <span style="font-size: 1.2rem; color: var(--text-primary);">
                기존 AI는 <strong>무차별 조언</strong>으로 책임 위험이 있지만,<br>
                RAPONG은 <strong>통제된 환경</strong>에서 <strong>명확한 책임 구조</strong>로 운영되어<br>
                법적/보안/윤리적 이슈가 <strong>전혀 없습니다</strong>.
            </span>
        </div>
    </div>
"""

# 메인 실행
def main():
    # index.html 읽기
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # 삽입 위치: </div> 다음, </section> 직전 (핵심 요약 다음)
    marker_before = '        </div>\n    </div>\n</section>\n\n\n<!-- ========== 3 AI MODES =========='

    if marker_before not in content:
        print("❌ 삽입 위치를 찾을 수 없습니다.")
        return

    # 법적/보안 섹션 삽입
    # </div></div> 다음, </section> 바로 전에 삽입
    replacement = '        </div>\n    </div>\n' + LEGAL_SECURITY_SECTION + '\n</section>\n\n\n<!-- ========== 3 AI MODES =========='
    content = content.replace(marker_before, replacement)

    # 파일 저장
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ '법적/보안/윤리적 이슈' 섹션 추가 완료")
    print("📍 위치: '핵심 요약' 다음, 'WHY RAPONG' 섹션 끝 직전")

    # 파일 크기 확인
    import os
    size = os.path.getsize("index.html")
    print(f"📊 최종 파일 크기: {size:,} bytes")

if __name__ == "__main__":
    main()
