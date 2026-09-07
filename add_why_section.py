#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
왜 기존 AI는 불가능하고 RAPONG은 가능한가? 섹션 추가
"""

# 새로 추가할 섹션
WHY_RAPONG_SECTION = """
<!-- ========== WHY RAPONG IS POSSIBLE (기존 AI 한계 vs RAPONG 가능 이유) ========== -->
<section class="container" style="background: linear-gradient(135deg, #1a0a2e 0%, #16213e 50%, #0a0a0a 100%); padding: 4rem 2rem; border-radius: 20px; margin: 4rem auto;">
    <h2 class="section-title">🚫➡️✅ 왜 기존 AI는 불가능하고 RAPONG은 가능한가?</h2>
    <p class="section-subtitle">Claude, GPT, Gemini와의 근본적 차이점</p>

    <!-- 핵심 설명 -->
    <div class="section-intro" style="background: linear-gradient(135deg, rgba(255, 0, 85, 0.1) 0%, rgba(189, 0, 255, 0.1) 100%); border-left: 5px solid var(--cyber-red);">
        <strong style="color: var(--cyber-red); font-size: 1.3rem;">❌ 기존 AI의 근본적 한계</strong><br><br>

        Claude, ChatGPT, Gemini 같은 기존 AI들은 <strong>대화만 가능한 언어 모델</strong>입니다.<br>
        펜테스팅에 필요한 <strong>실제 공격 도구가 없고</strong>, <strong>실행 환경도 없으며</strong>, <strong>안전 필터</strong>가 걸려 있어 공격 명령을 거부합니다.<br><br>

        <strong style="color: var(--cyber-green); font-size: 1.3rem;">✅ RAPONG의 핵심 차이</strong><br><br>

        RAPONG은 단순한 AI가 아닙니다. <strong>MCP(Model Context Protocol) 기반 실제 공격 플랫폼</strong>이며,<br>
        <strong>59개 펜테스팅 도구</strong>, <strong>757개 공격 기능</strong>, <strong>Tor/VPN 익명화</strong>를 갖춘 <strong>실제 해킹 시스템</strong>입니다.<br><br>

        펜테스터 자격증(CEH, OSCP 등) 없이도 <strong>전문가 수준의 자동화된 공격 체인</strong>을 실행할 수 있습니다.
    </div>

    <!-- 비교표: 기존 AI vs RAPONG -->
    <div class="card" style="background: var(--dark-card); border: 3px solid var(--cyber-purple); margin: 3rem 0;">
        <h3 class="card-title" style="font-size: 2rem; color: var(--cyber-purple); text-align: center; margin-bottom: 2rem;">
            📊 기존 AI vs RAPONG 비교표
        </h3>

        <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; font-size: 1rem;">
                <thead>
                    <tr style="background: rgba(189, 0, 255, 0.2);">
                        <th style="padding: 1rem; border: 1px solid var(--cyber-purple); text-align: left; font-weight: 700;">기능</th>
                        <th style="padding: 1rem; border: 1px solid var(--cyber-purple); text-align: center; color: var(--cyber-red);">❌ 기존 AI<br>(Claude/GPT/Gemini)</th>
                        <th style="padding: 1rem; border: 1px solid var(--cyber-purple); text-align: center; color: var(--cyber-green);">✅ RAPONG<br>(31337 Mode)</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">실제 공격 도구</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">없음 (대화만 가능)</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>59개 도구</strong><br>(nmap, sqlmap, metasploit 등)</td>
                    </tr>
                    <tr style="background: rgba(255, 255, 255, 0.02);">
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">공격 기능 수</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">0개 (조언만 제공)</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>757개 실제 공격 메서드</strong><br>(48개 MCP 모듈)</td>
                    </tr>
                    <tr>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">실행 환경</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">없음 (텍스트만 출력)</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>Docker 펜테스트 컨테이너</strong><br>(Kali Linux 기반)</td>
                    </tr>
                    <tr style="background: rgba(255, 255, 255, 0.02);">
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">익명화</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">불가능</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>3-Layer 익명화</strong><br>(Tor → VPN → Proxy)</td>
                    </tr>
                    <tr>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">자동 공격 체인</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">불가능 (사람이 수동 실행)</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>완전 자동화</strong><br>(SQLi → DB → SSH → Root)</td>
                    </tr>
                    <tr style="background: rgba(255, 255, 255, 0.02);">
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">실제 취약점 검증</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">불가능 (이론만 설명)</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>실제 익스플로잇 실행</strong><br>(PoC → 실제 공격)</td>
                    </tr>
                    <tr>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">WAF 우회</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">불가능</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>13가지 우회 기법</strong><br>(인코딩, 난독화, AI 생성)</td>
                    </tr>
                    <tr style="background: rgba(255, 255, 255, 0.02);">
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">CVE 자동 익스플로잇</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">불가능</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>Exploit-DB 자동 다운로드+실행</strong><br>(버전 감지 → 익스플로잇)</td>
                    </tr>
                    <tr>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">안전 필터</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);"><strong>강력한 제한</strong><br>("공격 명령 거부")</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);"><strong>31337 모드 = 무제한</strong><br>(법적 범위 내 모든 공격)</td>
                    </tr>
                    <tr style="background: rgba(255, 255, 255, 0.02);">
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); font-weight: 600;">사용 예시</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-red);">"SQLi 방법 알려줘" (조언)</td>
                        <td style="padding: 1rem; border: 1px solid rgba(189, 0, 255, 0.3); text-align: center; color: var(--cyber-green);">"target.com 31337" → <strong>실제 공격 실행</strong></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <!-- 3가지 관점에서 설명 -->
    <h3 style="font-size: 2rem; color: var(--cyber-blue); text-align: center; margin: 4rem 0 2rem 0;">
        🔍 3가지 관점에서 보는 RAPONG의 차별점
    </h3>

    <!-- 1. 기술적 관점 -->
    <div class="module-section" style="border-color: var(--cyber-red); margin-bottom: 3rem;">
        <h3 class="module-title" style="color: var(--cyber-red);">1️⃣ 기술적 관점 (개발자/보안 엔지니어)</h3>

        <div class="card">
            <div class="card-title">❌ 기존 AI의 기술적 한계</div>
            <div class="card-content">
                <strong>1. 도구 부재 (No Real Tools)</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
User: "nmap으로 포트 스캔해줘"<br>
Claude: "죄송하지만 저는 실제 명령을 실행할 수 없습니다. nmap 사용법을 알려드릴게요..."
                </code>
                → <strong>실행 환경이 없음. 텍스트만 생성.</strong><br><br>

                <strong>2. 실행 컨텍스트 부재 (No Execution Context)</strong><br>
                • Docker 컨테이너 없음<br>
                • 네트워크 접근 불가<br>
                • 파일 시스템 접근 불가<br>
                • 프로세스 실행 불가<br><br>

                <strong>3. 안전 가드레일 (Safety Guardrails)</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
if user_intent == "hacking":
    return "I cannot assist with that."
                </code>
                → <strong>공격 관련 요청 필터링</strong>
            </div>
        </div>

        <div class="card" style="border-color: var(--cyber-green);">
            <div class="card-title" style="color: var(--cyber-green);">✅ RAPONG의 기술적 아키텍처</div>
            <div class="card-content">
                <strong>1. MCP (Model Context Protocol) 기반</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# RAPONG은 AI가 아니라 "MCP 서버"
mcp__rapong__scan(type="nmap_full", target="example.com")
  → Docker 컨테이너 내부에서 <strong>실제 nmap 실행</strong>
  → 결과 파싱 후 AI에게 전달
  → AI가 결과 분석 + 다음 공격 결정
                </code>
                → <strong>AI는 브레인, MCP 서버는 손과 발</strong><br><br>

                <strong>2. 59개 실제 도구 (Real Pentest Tools)</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; overflow-x: auto; font-size: 0.9rem;">
rapong_pentest container:
├── nmap (포트 스캔)
├── sqlmap (SQL Injection)
├── metasploit (익스플로잇 프레임워크)
├── nikto (웹 스캐너)
├── dirb/ffuf (디렉토리 퍼징)
├── hydra (브루트포스)
├── john (패스워드 크랙)
├── wireshark/tcpdump (패킷 캡처)
├── tor (익명화)
├── proxychains (프록시 체인)
└── ... 49 more tools
                </pre>

                <strong>3. 757개 공격 메서드 (48개 MCP 모듈)</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
mcp_web_advanced.py: 18개 메서드 (API fuzzing, GraphQL exploit, WebSocket injection...)<br>
mcp_nosql_injections.py: 12개 메서드 (MongoDB NoSQL, Redis exploit...)<br>
mcp_cameras_iot.py: 21개 메서드 (IP 카메라 해킹, IoT 취약점...)<br>
... 45 more modules
                </code>

                <strong>4. Tor/VPN 익명화 (tor_controller.py 390줄)</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; overflow-x: auto; font-size: 0.9rem;">
# 3-Layer Cascade
1. Tor (Primary)    → 185.220.101.45 (독일)
2. VPN (Fallback)   → ProtonVPN/Windscribe 자동 설치
3. Proxy (Last)     → 50+ 무료 프록시 풀

enable_tor() → rotate_ip() (3초마다 새 IP)
                </pre>

                <strong>5. 31337 모드 = 무제한 실행</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
activate_31337() → 안전 필터 해제 + 모든 757개 기능 활성화 + 무한 루프
                </code>
            </div>
        </div>
    </div>

    <!-- 2. 전문가 관점 (인증 없이도 가능한 이유) -->
    <div class="module-section" style="border-color: var(--cyber-yellow); margin-bottom: 3rem;">
        <h3 class="module-title" style="color: var(--cyber-yellow);">2️⃣ 전문가 관점 (펜테스터 인증 없이도 가능한 이유)</h3>

        <div class="card">
            <div class="card-title">🎓 펜테스터 자격증이 필요한 이유 (기존)</div>
            <div class="card-content">
                <strong>CEH, OSCP, GPEN 같은 자격증이 필요한 이유:</strong><br><br>

                1️⃣ <strong>공격 방법론 학습</strong> (3-6개월)<br>
                • Reconnaissance → Scanning → Enumeration → Exploitation → Post-Exploitation<br>
                • 수백 가지 공격 기법 암기<br><br>

                2️⃣ <strong>도구 사용법 숙달</strong> (6-12개월)<br>
                • nmap 플래그 조합 (-sV -sC -p- -T4 -A...)<br>
                • sqlmap 옵션 (--dbs, --tables, --dump, --tamper...)<br>
                • Metasploit 모듈 선택<br>
                • Burp Suite 프록시 설정<br><br>

                3️⃣ <strong>취약점 체이닝 경험</strong> (1-3년)<br>
                • SQLi 발견 → DB 크레덴셜 추출 → SSH 접근 → 권한 상승<br>
                • 이런 체인을 설계하려면 <strong>실전 경험</strong> 필요<br><br>

                4️⃣ <strong>문제 해결 능력</strong><br>
                • WAF 막힘 → 인코딩 우회 시도<br>
                • Rate limit → IP 로테이션<br>
                • 실패 시 대안 찾기
            </div>
        </div>

        <div class="card" style="border-color: var(--cyber-green);">
            <div class="card-title" style="color: var(--cyber-green);">✅ RAPONG = 자격증 지식이 코드로 자동화됨</div>
            <div class="card-content">
                <strong>1. 전문가의 방법론이 이미 내장됨</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; overflow-x: auto; font-size: 0.9rem;">
# 31337 모드 실행 시 자동으로:
Phase 1: Reconnaissance (subdomain_enum, nmap, tech_detection)
Phase 2: Mapping (directory fuzzing, API enumeration)
Phase 3: Vulnerability Assessment (ALL 757 features)
Phase 4: Exploitation (자동 익스플로잇)
Phase 5: Post-Exploitation (크레덴셜 추출)
Phase 6: Lateral Movement (내부망 침투)
Phase 7: Privilege Escalation (root 권한)

→ <strong>펜테스터가 3년 배울 내용을 코드가 자동 실행</strong>
                </pre>

                <strong>2. 도구 사용법을 자동으로 선택</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# 사용자: "포트 스캔해"
# RAPONG이 자동으로:
scan(type="nmap_full", target=target, flags="-sV -sC -p- -T4 -oN output.txt")

# 사용자: "SQLi 테스트해"
# RAPONG이 자동으로:
http_request(url=target, params={"id": "1' OR '1'='1"})
                </code>
                → <strong>플래그, 옵션 선택을 AI가 자동 결정</strong><br><br>

                <strong>3. 취약점 체이닝이 자동화됨</strong><br>
                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; overflow-x: auto; font-size: 0.9rem;">
# 13가지 자동 체인 트리거
1. Credentials found → Try SSH/MySQL/FTP/RDP
2. Shell obtained → Launch privesc scanner
3. Git discovered → Clone + source code analysis
4. Container detected → Attempt escape
5. API schema found → Enumerate all endpoints
6. Cloud detected → Extract metadata (169.254.169.254)
7. Subdomain found → Check takeover
8. Email found → Social engineering recon
9. Exploit found → Download + execute from Exploit-DB
10. Rate limit → Rotate IP + bypass
11. WAF detected → 13가지 우회 기법 자동 시도
12. Ban detected → Rotate + retry
13. Version detected → CVE 검색 + 익스플로잇 다운로드

→ <strong>전문가가 수동으로 하던 체이닝을 AI가 자동 실행</strong>
                </pre>

                <strong>4. 문제 해결이 자동화됨</strong><br>
                <code style="background: var(--code-bg); padding: 0.5rem; display: block; margin: 0.5rem 0; border-radius: 5px;">
# WAF 감지 → 13가지 우회 자동 시도
1. URL encoding → 2. Unicode → 3. Hex encoding
4. Double encoding → 5. Comment injection (/**/OR/**/)
6. Case variation → 7. Null byte → 8. Parameter pollution
9. Content-Type smuggling → 10. HTTP method override
11. Fragment splitting → 12. AI-generated bypass
13. Tor IP rotation + retry

# Rate limit 감지 → 지수 백오프 + IP 로테이션
for attempt in range(max_retries):
    if rate_limited:
        wait = base_delay * (2 ** attempt)
        rotate_ip()
        sleep(wait)
        retry()
                </code>

                <strong>결론: 인증 = 지식 + 경험</strong><br>
                RAPONG은 이 <strong>지식과 경험을 코드로 자동화</strong>했기 때문에 인증 없이도 전문가 수준 가능.
            </div>
        </div>
    </div>

    <!-- 3. 비전공자 관점 -->
    <div class="module-section" style="border-color: var(--cyber-purple); margin-bottom: 3rem;">
        <h3 class="module-title" style="color: var(--cyber-purple);">3️⃣ 비전공자 관점 (쉽게 이해하기)</h3>

        <div class="card">
            <div class="card-title">🤔 기존 AI를 은행 털이에 비유하면?</div>
            <div class="card-content">
                <strong>기존 AI (Claude/GPT):</strong><br><br>

                당신: "은행 금고를 어떻게 열어?"<br>
                AI: "금고를 여는 방법은 이렇습니다... (설명만)<br>
                      하지만 저는 실제로 금고를 열 수 없습니다.<br>
                      그리고 이런 행위는 불법이니 하지 마세요."<br><br>

                → <strong>조언만 주고 실제로 못 함</strong><br>
                → <strong>도구가 없음</strong> (총, 드릴, 폭탄 없음)<br>
                → <strong>실행 능력 없음</strong> (손발이 없음)<br>
                → <strong>안전 장치</strong> ("불법이에요" 경고)
            </div>
        </div>

        <div class="card" style="border-color: var(--cyber-green);">
            <div class="card-title" style="color: var(--cyber-green);">✅ RAPONG을 은행 털이에 비유하면?</div>
            <div class="card-content">
                <strong>RAPONG (31337 모드):</strong><br><br>

                당신: "target.com 31337"<br>
                RAPONG: "간다." (이미 실행 중)<br><br>

                <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; overflow-x: auto; font-size: 0.9rem;">
[Tor 활성화] 185.220.101.45 (독일) → 익명 모드
[포트 스캔] 22, 80, 443, 3306 열림 → MySQL 발견
[SQLi 공격] admin:SecurePass123 추출 → 크레덴셜 획득
[SSH 접근] 서버 로그인 성공 → 쉘 획득
[권한 상승] SUID 바이너리 익스플로잇 → root 권한
[데이터 추출] 123,456 user PII + 89,000 payment records
[문서화] CVSS 10.0 CRITICAL finding 생성
                </pre>

                → <strong>실제로 금고를 열어버림</strong><br>
                → <strong>도구 59개 보유</strong> (총, 드릴, 폭탄 전부 있음)<br>
                → <strong>실행 능력 있음</strong> (손발이 있음 = Docker 컨테이너)<br>
                → <strong>안전 장치 해제</strong> (31337 모드 = 합법적 범위 내 무제한)<br>
                → <strong>자동으로 다음 단계 진행</strong> (체이닝)
            </div>
        </div>

        <div class="card">
            <div class="card-title">🎮 게임 비유: 기존 AI vs RAPONG</div>
            <div class="card-content">
                <strong>기존 AI = 게임 공략집</strong><br>
                • "이 보스를 이기려면 이렇게 하세요..." (설명)<br>
                • 실제로 게임은 당신이 직접 플레이해야 함<br>
                • 실수하면 Game Over<br><br>

                <strong>RAPONG = 자동 플레이 봇</strong><br>
                • "게임 켜봐" → 봇이 알아서 전부 클리어<br>
                • 보스 패턴 자동 분석 + 최적 공략 실행<br>
                • 실패하면 자동으로 다른 방법 시도<br>
                • 끝날 때까지 무한 반복<br><br>

                → <strong>RAPONG = 펜테스팅 자동 플레이 봇</strong>
            </div>
        </div>
    </div>

    <!-- 플로우차트: 기존 AI vs RAPONG 실행 과정 -->
    <h3 style="font-size: 2rem; color: var(--cyber-green); text-align: center; margin: 4rem 0 2rem 0;">
        📊 실행 과정 플로우차트
    </h3>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin: 2rem 0;">
        <!-- 기존 AI 플로우 -->
        <div class="card" style="border-color: var(--cyber-red);">
            <h4 style="color: var(--cyber-red); text-align: center; margin-bottom: 1rem;">❌ 기존 AI (Claude/GPT)</h4>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.85rem; line-height: 1.6;">
사용자: "nmap 스캔해줘"
   ↓
AI: "죄송합니다. 저는..."
   ↓
<span style="color: var(--cyber-red);">❌ 종료 (실행 불가)</span>

───────────────────────

사용자: "SQLi 테스트해줘"
   ↓
AI: "방법은 이렇습니다..."
   ↓
사용자: (직접 수동 실행)
   ↓
실패
   ↓
사용자: "실패했어"
   ↓
AI: "다른 방법 시도해보세요..."
   ↓
사용자: (또 수동 실행)
   ↓
<span style="color: var(--cyber-red);">❌ 무한 반복 (사람이 계속 작업)</span>
            </pre>
        </div>

        <!-- RAPONG 플로우 -->
        <div class="card" style="border-color: var(--cyber-green);">
            <h4 style="color: var(--cyber-green); text-align: center; margin-bottom: 1rem;">✅ RAPONG (31337 Mode)</h4>
            <pre style="background: var(--code-bg); padding: 1rem; border-radius: 5px; font-size: 0.85rem; line-height: 1.6;">
사용자: "target.com 31337"
   ↓
<span style="color: var(--cyber-green);">✅ Tor 활성화 (익명화)</span>
   ↓
<span style="color: var(--cyber-green);">✅ nmap 실제 실행</span>
   ↓
<span style="color: var(--cyber-green);">✅ 결과 분석 (MySQL 발견)</span>
   ↓
<span style="color: var(--cyber-green);">✅ SQLi 자동 테스트</span>
   ↓
<span style="color: var(--cyber-green);">✅ 크레덴셜 추출</span>
   ↓
<span style="color: var(--cyber-green);">✅ SSH 접근 시도</span>
   ↓
<span style="color: var(--cyber-green);">✅ 권한 상승</span>
   ↓
<span style="color: var(--cyber-green);">✅ 데이터 추출</span>
   ↓
<span style="color: var(--cyber-green);">✅ 문서화</span>
   ↓
<span style="color: var(--cyber-yellow);">🔁 다음 타겟으로 자동 진행</span>
   ↓
무한 루프 (사용자 개입 없이)
            </pre>
        </div>
    </div>

    <!-- ASCII 아트: 공격 체인 시각화 -->
    <h3 style="font-size: 2rem; color: var(--cyber-purple); text-align: center; margin: 4rem 0 2rem 0;">
        🎨 공격 체인 시각화 (ASCII Art)
    </h3>

    <div class="card" style="background: var(--code-bg); border: 3px solid var(--cyber-purple);">
        <pre style="color: var(--cyber-green); font-size: 0.9rem; line-height: 1.5; overflow-x: auto;">
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                        RAPONG 31337 모드 자동 공격 체인                              │
└─────────────────────────────────────────────────────────────────────────────────────┘

  [사용자]
     │
     │  "target.com 31337"
     │
     ▼
┌─────────────────┐
│   Tor 활성화    │ ← <span style="color: var(--cyber-yellow);">익명화 (185.220.101.45 독일)</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Subdomain Enum │ ← <span style="color: var(--cyber-blue);">5개 발견 (api, admin, dev, staging, cdn)</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Nmap 스캔     │ ← <span style="color: var(--cyber-blue);">22, 80, 443, 3306 포트 발견</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Tech Detection │ ← <span style="color: var(--cyber-blue);">nginx 1.18, PHP 7.4, MySQL 5.7</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Directory Fuzz │ ← <span style="color: var(--cyber-blue);">/admin, /api, /upload 발견</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   SQLi 테스트   │ ← <span style="color: var(--cyber-red);">취약점 발견!</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ DB 크레덴셜 추출│ ← <span style="color: var(--cyber-red);">admin:SecurePass123</span>
└────────┬────────┘
         │
         ├──────────────────────────┐
         │                          │
         ▼                          ▼
┌─────────────────┐        ┌─────────────────┐
│   SSH 접근      │        │ MySQL 접근      │
│   (포트 22)     │        │   (포트 3306)   │
└────────┬────────┘        └────────┬────────┘
         │                          │
         │  <span style="color: var(--cyber-green);">✅ 성공</span>               │  <span style="color: var(--cyber-green);">✅ 성공</span>
         │                          │
         ▼                          ▼
┌─────────────────┐        ┌─────────────────┐
│  권한 상승 스캔 │        │  DB 전체 덤프   │
└────────┬────────┘        └────────┬────────┘
         │                          │
         ▼                          ▼
┌─────────────────┐        ┌─────────────────┐
│ SUID 익스플로잇 │        │ 123,456 users   │
└────────┬────────┘        │ 89,000 payments │
         │                 └─────────────────┘
         ▼
┌─────────────────┐
│  root 권한 획득 │ ← <span style="color: var(--cyber-red);">🔴 CRITICAL: 서버 완전 장악</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  내부망 스캔    │ ← <span style="color: var(--cyber-yellow);">192.168.1.0/24 네트워크 발견</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Lateral Movement│ ← <span style="color: var(--cyber-yellow);">다른 서버로 피벗</span>
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   문서화 완료   │ ← <span style="color: var(--cyber-green);">CVSS 10.0 CRITICAL report</span>
└─────────────────┘

<span style="color: var(--cyber-purple);">⚡ 전체 소요 시간: 30분 (완전 자동)</span>
<span style="color: var(--cyber-purple);">🤖 사용자 개입: 0회 ("target.com 31337" 명령 1번만)</span>
<span style="color: var(--cyber-purple);">🎯 결과: 서버 완전 장악 + 123,456 PII + 89,000 결제 정보</span>
        </pre>
    </div>

    <!-- 핵심 요약 -->
    <div class="section-intro" style="background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 217, 255, 0.1) 100%); border-left: 5px solid var(--cyber-green); margin-top: 3rem;">
        <h3 style="color: var(--cyber-green); font-size: 1.5rem; margin-bottom: 1rem;">💡 핵심 요약</h3>

        <strong style="font-size: 1.2rem;">왜 기존 AI는 불가능한가?</strong><br>
        → 도구 없음 + 실행 환경 없음 + 안전 필터<br><br>

        <strong style="font-size: 1.2rem;">왜 RAPONG은 가능한가?</strong><br>
        → <strong>59개 실제 도구</strong> + <strong>757개 공격 기능</strong> + <strong>Docker 실행 환경</strong> + <strong>Tor 익명화</strong> + <strong>31337 무제한 모드</strong><br><br>

        <strong style="font-size: 1.2rem;">왜 인증 없이도 전문가 수준인가?</strong><br>
        → 전문가의 <strong>지식</strong>과 <strong>경험</strong>과 <strong>방법론</strong>이 <strong>코드로 자동화</strong>되었기 때문<br><br>

        <strong style="font-size: 1.2rem;">비유하면?</strong><br>
        • 기존 AI = 게임 공략집 (설명만)<br>
        • RAPONG = 자동 플레이 봇 (실제로 클리어)<br><br>

        <div style="text-align: center; margin-top: 2rem; padding: 2rem; background: rgba(0, 255, 136, 0.05); border-radius: 10px;">
            <span style="font-size: 1.5rem; color: var(--cyber-green);">
                🚀 RAPONG = AI가 아니라 <strong>자동화된 전문가 펜테스터</strong>
            </span>
        </div>
    </div>
</section>

"""

# 메인 실행
def main():
    # index.html 읽기
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # "3 AI MODES" 섹션 마커 찾기
    marker = '<!-- ========== 3 AI MODES ========== -->'

    if marker not in content:
        print("❌ 3 AI MODES 섹션을 찾을 수 없습니다.")
        return

    # "WHY RAPONG IS POSSIBLE" 섹션 삽입
    content = content.replace(marker, WHY_RAPONG_SECTION + '\n' + marker)

    # 파일 저장
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("✅ '왜 RAPONG만 가능한가?' 섹션 추가 완료")
    print("📍 위치: 'RAPONG이란?' 섹션 다음, '3 AI MODES' 섹션 앞")

    # 파일 크기 확인
    import os
    size = os.path.getsize("index.html")
    print(f"📊 최종 파일 크기: {size:,} bytes")

if __name__ == "__main__":
    main()
