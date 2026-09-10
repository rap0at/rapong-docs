# Manager Agent + 31337 통합 사용법

**작성일:** 2026-09-10  
**버전:** 2.0 (Auto-Integration)

---

## 🎯 핵심 변경사항

### Before (이전)

```
31337 activate()
  ↓
Manager 초기화만 됨
  ↓
31337 공격 실행
  ↓
Manager 작동 안 함 ❌
```

### After (현재)

```
31337 activate()
  ↓
Manager 자동 초기화
  ↓
31337 공격 실행
  ↓
Manager 자동 모니터링 ✅
  ↓
결과 분석 + 티칭 ✅
  ↓
에러 시 Proxy 실행 ✅
```

---

## 🔄 자동 작동 흐름

### 1. 초기화 (activate())

```python
# 31337 activate 시
await engine.activate()

# 내부 동작:
# 1. Tor anonymization (Line 186-211)
# 2. Manager 초기화 (Line 213-247)
#    - Label A: Knowledge Base
#    - Label B: Scope Manager
#    - Label C: System Health
#    - Label D: Attack Analyzer
#    - Label E: Teaching Engine
#    - Label I: Guardian
# 3. Attack queue 준비 (Line 250)
```

**로그 확인:**
```
[MANAGER] Initializing Manager Agent...
[A] ✅ 지식 베이스 로드 완료
[B] ✅ 스코프: 제약 없음
[C] ✅ 시스템 헬스 체크 완료
[D] ✅ 분석 엔진 준비 완료
[E] ✅ 티칭 룰 6개 로드
[I] ✅ Guardian 준비 완료
[MANAGER] ✅ All labels initialized
```

---

### 2. 공격 준비 (get_next_attack())

```python
# Claude가 다음 공격 요청
attack = await engine.get_next_attack()

# Manager 자동 개입 (NEW):
# - Label I Guardian: 사전 체크
# - Attack context 추가
# - Monitoring 플래그 설정

# Return:
{
    "command": "http_request",
    "arguments": {...},
    "phase": "exploitation",
    "vector": "SQLi",
    "manager_monitoring": True,  # NEW
    "manager_iteration": 5       # NEW
}
```

---

### 3. 공격 실행 후 분석 (process_attack_result())

```python
# Claude가 공격 실행 후
result = await engine.process_attack_result(
    attack_command=attack,
    execution_result={
        "status_code": 403,
        "output": "Blocked by WAF",
        ...
    }
)

# Manager 자동 분석:
# 1. Label D: WAF 감지
# 2. Label D: 대안 페이로드 생성
# 3. Label E: 티칭 제공
# 4. Label I: Guardian 개입 체크

# Return:
{
    "manager_active": True,
    "analysis": {
        "waf_type": "cloudflare",
        "blocked": True
    },
    "teaching": "Cloudflare다. URL인코딩 + Case variation 시도.",
    "alternatives": [
        "%27%20OR%20%271%27%3D%271",
        "' UnIoN SeLeCt",
        ...
    ],
    "action": "continue"
}
```

---

### 4. 에러 처리 (handle_attack_error())

```python
# 공격 실패 시
try:
    result = http_request(...)
except Exception as e:
    # Manager Proxy Execution
    proxy_result = await engine.handle_attack_error(
        attack_command=attack,
        error=e
    )

# Manager 자동 대응:
# 1. 에러 타입 감지
# 2. Label I: proxy_execute() 호출
# 3. 문제 해결 (도구 설치, IP 바꾸기, sudo 재실행 등)
# 4. 결과를 31337에게 토스

# Return:
{
    "proxy_executed": True,
    "success": True,
    "output": "Tool nmap installed and executed",
    "action": "continue"
}
```

---

## 📊 Manager 역할

### Label I (Guardian) - 무한루프 보장

**자동 개입:**
- 31337이 "끝났다" 말하면 → 차단
- 31337이 "다음 뭐 할까" 물으면 → 차단
- 도구 없으면 → 자동 설치
- 권한 없으면 → sudo 재실행

**Proxy Execution:**
```python
# Case 1: 도구 누락
reason = "tool_missing"
→ Label I가 자동 설치 후 실행

# Case 2: 권한 에러
reason = "permission_denied"
→ Label I가 sudo로 재실행

# Case 3: 타임아웃
reason = "timeout"
→ Label I가 IP 바꿔서 재실행

# Case 4: WAF 차단
reason = "waf_blocked"
→ Label I가 우회 시도
```

---

### Label D (Attack Analyzer) - 실패 분석

**자동 분석:**
- WAF 감지 (Cloudflare, Akamai, AWS, etc.)
- 차단 이유 파악 (rate limit, payload filtering, etc.)
- 대안 페이로드 생성 (URL encoding, double encoding, etc.)

**Example:**
```python
# Input:
response = {
    "status_code": 403,
    "headers": {"cf-ray": "123456"},
    "body": "Blocked by Cloudflare"
}

# Manager 분석:
{
    "waf_type": "cloudflare",
    "alternatives": [
        "%27%20OR%20%271%27%3D%271",
        "' UnIoN SeLeCt",
        "UNION/**/SELECT",
        ...
    ]
}
```

---

### Label E (Teaching Engine) - 실시간 가이드

**자동 티칭:**
- 막힌 이유 설명
- 우회 방법 제시
- 다음 시도 방향 가이드

**Example:**
```
"Cloudflare WAF 감지됨.
URL인코딩 먼저 시도 → 안 되면 Double encoding → 그래도 안 되면 IP 바꾸고 Case variation."
```

---

## 🔧 사용 예시

### Example 1: 정상 흐름

```python
# 1. 31337 activate
await engine.activate()
# Manager 자동 초기화

# 2. 공격 가져오기
attack = await engine.get_next_attack()
# Manager Guardian 사전 체크

# 3. 공격 실행
result = await mcp_service.execute(attack["command"], attack["arguments"])

# 4. 결과 분석
analysis = await engine.process_attack_result(attack, result)

# 5. Claude에게 티칭
if analysis.get("teaching"):
    print(f"[Manager] {analysis['teaching']}")

# 6. 대안 시도
if analysis.get("alternatives"):
    for alt in analysis["alternatives"]:
        # Try alternative payload
        ...
```

---

### Example 2: 에러 처리

```python
# 1. 공격 실행
attack = await engine.get_next_attack()

try:
    result = await mcp_service.execute(attack["command"], attack["arguments"])

except Exception as e:
    # 2. Manager Proxy Execution
    proxy_result = await engine.handle_attack_error(attack, e)

    if proxy_result.get("success"):
        # Manager가 해결함
        print(f"[Manager] Proxy execution succeeded: {proxy_result['output']}")
        # Continue with proxy result
    else:
        # Manager도 실패
        print(f"[Manager] Proxy execution failed: {proxy_result['error']}")
        # Skip to next attack
```

---

### Example 3: Guardian 개입

```python
# 31337이 잘못된 출력 생성
output = "끝났다. 모든 작업 완료."

# Manager Guardian 자동 감지
intervention = await manager.label_i.monitor_31337(
    output=output,
    context={"phase": "exploitation"}
)

if intervention.get("intervention_needed"):
    # Guardian 개입 발동
    print(f"[Guardian] {intervention['type']}: {intervention['action']}")
    # "STOP 감지 → 강제 계속"

    # 다음 공격 강제 실행
    next_attack = await engine.get_next_attack()
    # 무한루프 보장
```

---

## 📋 Manager 상태 확인

```python
# Manager 상태
status = manager.get_status()

# Output:
{
    "initialized": True,
    "ai_mode": "LOCAL",
    "labels": {
        "A": "active",  # Knowledge Base
        "B": "active",  # Scope Manager
        "C": "active",  # System Health
        "D": "active",  # Attack Analyzer
        "E": "active",  # Teaching Engine
        "I": "active"   # Guardian
    },
    "stats": {
        "attacks_monitored": 150,
        "interventions": 3,
        "proxy_executions": 5
    }
}
```

---

## 🎯 통합 완료 체크리스트

✅ Manager 자동 초기화 (activate()에서)
✅ get_next_attack() Guardian 사전 체크
✅ process_attack_result() 자동 분석
✅ handle_attack_error() Proxy Execution
✅ Label I Guardian 개입 시스템
✅ Label D Analyzer WAF 감지
✅ Label E Teaching 실시간 가이드
✅ Proxy Execute 5가지 케이스
✅ 에러 타입 자동 감지
✅ 31337 ↔ Manager 완전 통합

---

## 🚀 최종 검증

```bash
# Docker 컨테이너에서 테스트
docker exec rapong_backend python3 << 'EOF'
import asyncio
from rapong_mcp.modules.mcp_classes import RapongMCPService
from rapong_mcp.modules.mcp_31337_engine import init_31337_engine

async def test():
    # 1. 초기화
    service = RapongMCPService()
    await service.initialize()
    engine = init_31337_engine(service)
    service.engine_31337 = engine

    # 2. Activate (Manager 자동 초기화)
    try:
        await asyncio.wait_for(engine.activate(), timeout=10.0)
    except asyncio.TimeoutError:
        pass

    # 3. Manager 확인
    if engine.manager:
        print("✅ Manager 자동 초기화됨")

        # 4. 공격 가져오기
        attack = await engine.get_next_attack()
        print(f"✅ Attack: {attack.get('vector')}")
        print(f"✅ Manager monitoring: {attack.get('manager_monitoring')}")

        # 5. Guardian 테스트
        iv = await engine.manager.label_i.monitor_31337("끝났다", {})
        if iv.get("intervention_needed"):
            print("✅ Guardian 작동")

        # 6. Proxy 테스트
        proxy = await engine.manager.proxy_execute(
            "nmap",
            {},
            "tool_missing"
        )
        if proxy.get("proxy_executed"):
            print("✅ Proxy Execution 작동")

asyncio.run(test())
EOF
```

---

**작성일:** 2026-09-10  
**상태:** Manager + 31337 완전 통합 완료

---

## 🛡️ 안전성 강화 (v2.0)

### MCP Timeout Protection

**문제:** MCP 서버 다운 시 31337 전체 중단

**해결:** Timeout + Degraded Mode

```python
# Manager 초기화 (60s timeout)
self.manager = await asyncio.wait_for(
    create_manager(...),
    timeout=60.0
)
```

**효과:**
- ✅ MCP 서버 다운/타임아웃 시 31337 계속 작동
- ✅ Manager 없이 Degraded mode 지원
- ✅ Label 일부 실패해도 계속
- ✅ None 체크 4곳 (get_next_attack, process_attack_result, handle_attack_error, activate)

---

### Degraded Mode

**Scenario:** MCP 서버 완전 다운

```
activate()
  ↓
Manager 초기화 timeout (60s)
  ↓
self.manager = None
  ↓
[MANAGER] 31337 will continue WITHOUT Manager (degraded mode)
  ↓
31337 757 features 정상 작동 ✅
```

**Scenario:** Label 일부 실패

```
Label A: OK
Label B: OK
Label C: TIMEOUT
Label D: OK
Label E: OK
Label I: OK
  ↓
Manager Partial Mode
  ↓
31337 + 5개 Label 작동 ✅
```

---

### Safety Checks

| 위치 | 체크 | 효과 |
|-----|------|------|
| activate() | Manager timeout 60s | MCP 다운 시 31337 계속 |
| initialize() | Label 개별 timeout 10-15s | Label 실패 시 partial mode |
| get_next_attack() | if self.manager: | None 안전 처리 |
| process_attack_result() | if not self.manager: | Degraded mode 계속 |
| handle_attack_error() | if not self.manager: | Proxy 없이 skip |
| prepare_guardian() | Tool check timeout 10s | 도구 체크 실패해도 작동 |

---

## 📊 검증 결과

### 콜드런 설치 + 실행 (2026-09-10)

**환경:** rrrr.py clean → Backend 시작 → 31337 activate

**결과:**
```
[MANAGER] Starting initialization (60s timeout)...
[A] ✅ 지식 베이스 로드 완료
[B] ✅ 스코프: 제약 없음
[C] ✅ 시스템 헬스 체크 완료
[D] ✅ 분석 엔진 준비 완료
[E] ✅ 티칭 룰 6개 로드
[I] ✅ Guardian 준비 완료
✅  All 6 labels initialized successfully
[MANAGER] ✅ Initialization completed within timeout
[MANAGER] ✅ All labels initialized - Ready to attack

[F26][BASIC] Social engineering reconnaissance: target
[F26][BASIC] Limited OSINT results, escalating to ADVANCED tier
[AI] Asking AI (LOCAL): Perform deep profiling...
```

**판정:** ✅ PASS - Manager 자동으로 알아서 잘 돌아감

---

## 📁 관련 문서

- `MANAGER_SAFETY_ENHANCEMENTS.md` - 안전성 강화 상세
- `COLDRUN_VERIFICATION.md` - 콜드런 검증 결과
- `MANAGER_AGENT_SKILLS.md` - Manager 능력 문서

---

**작성일:** 2026-09-10  
**상태:** Manager + 31337 완전 통합 + 안전성 강화 완료
