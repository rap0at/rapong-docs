# Manager Agent - 6개 Label 완전 가이드

**작성일:** 2026-09-10  
**버전:** 2.0  
**대상:** Manager Agent가 참고하는 모든 작업 지침

---

## 📋 목차

1. [Label A - Knowledge Base (지식 베이스)](#label-a---knowledge-base)
2. [Label B - Scope Manager (스코프 관리)](#label-b---scope-manager)
3. [Label C - System Health (시스템 헬스)](#label-c---system-health)
4. [Label D - Attack Analyzer (공격 분석)](#label-d---attack-analyzer)
5. [Label E - Teaching Engine (티칭 엔진)](#label-e---teaching-engine)
6. [Label I - Guardian (가디언)](#label-i---guardian)
7. [통합 워크플로우](#통합-워크플로우)
8. [참고 문서](#참고-문서)

---

## Label A - Knowledge Base

### 🎯 목적

**31337의 모든 모듈과 기능을 이해하고 기록**

Manager Agent는 31337이 무엇을 할 수 있는지 완벽히 이해해야 함.

---

### 📚 참고 문서 (우선순위 순)

#### 1. 공식 문서 (https://rap0at.github.io/rapong-docs/)
- index.html - 메인 소개 페이지
- 31337_MANAGER_AGENT_PLAN.md - 전체 플랜
- MANAGER_AGENT_SKILLS.md - Manager 능력
- MANAGER_31337_INTEGRATION.md - 통합 가이드

#### 2. 코드 구조
```
backend/rapong_mcp/modules/
├── mcp_31337_engine.py          [31337 메인 엔진]
├── mcp_rp_engine.py              [RP 엔진]
├── mcp_core_tools.py             [20개 핵심 도구]
├── mcp_anonymization.py          [15개 익명화 도구]
├── mcp_assessment.py             [12개 평가 도구]
├── mcp_web_advanced.py           [18개 웹 공격]
├── mcp_nosql_injections.py       [12개 NoSQL 공격]
├── mcp_cameras_iot.py            [21개 IoT 공격]
├── mcp_cloud_advanced.py         [19개 클라우드 공격]
├── mcp_mobile_*.py               [48개 모바일 공격]
├── mcp_post_exploit.py           [18개 후속공격]
├── mcp_privesc.py                [16개 권한상승]
├── mcp_exploit_automation.py     [17개 자동익스]
├── mcp_ai_*.py                   [24개 AI 기능]
└── ... (48개 모듈, 757개 기능)
```

#### 3. 프롬프트 파일
```
/root/.claude/project-preprompts/31337_pentest.md
  → 31337 페르소나 (춘식)
  → 공격 방법론
  → 무한루프 규칙
  → 금지 단어/행동
```

---

### 🔍 Label A 작동 방식

#### 초기화 (prepare_knowledge_base())
```python
# Line 18-46 (manager_label_a.py)

async def prepare_knowledge_base(self) -> Dict[str, Any]:
    """
    1. 프롬프트 파일 읽기
    2. 모듈 목록 스캔
    3. 기능 카운트
    4. 지식 DB 구축
    """
    
    # Step 1: 프롬프트 파일 확인
    prompt_file = Path("/root/.claude/project-preprompts/31337_pentest.md")
    if prompt_file.exists():
        self.knowledge["preprompt"] = prompt_file.read_text()
    
    # Step 2: 모듈 스캔
    modules_dir = Path("backend/rapong_mcp/modules")
    modules = list(modules_dir.glob("mcp_*.py"))
    
    # Step 3: 통계 수집
    self.knowledge["module_count"] = len(modules)
    self.knowledge["feature_count"] = 757  # 실제 카운트
    
    # Step 4: 특수 모듈 표시
    self.knowledge["special"] = {
        "31337_engine": "mcp_31337_engine.py",
        "rp_engine": "mcp_rp_engine.py",
        "manager": "mcp_manager_agent.py"
    }
    
    return {"status": "loaded", "modules": len(modules)}
```

---

### 📊 학습 메커니즘 (learn())

```python
# Line 94-116 (manager_label_a.py)

async def learn(self, attack: Dict, result: Dict) -> None:
    """
    공격 결과를 학습하여 지식 베이스 업데이트
    
    Args:
        attack: 공격 정보 (vector, payload, target)
        result: 실행 결과 (success, response, error)
    """
    
    # 성공 사례 저장
    if result.get("success"):
        key = f"{attack['vector']}_{attack['target']}"
        self.learned_attacks[key] = {
            "payload": attack["payload"],
            "timestamp": datetime.now(),
            "waf_bypassed": result.get("waf_bypassed", False)
        }
    
    # 실패 사례도 저장 (같은 실수 반복 방지)
    else:
        key = f"failed_{attack['vector']}_{attack['target']}"
        self.failed_attacks[key] = {
            "error": result.get("error"),
            "reason": result.get("reason")
        }
```

---

### 🎓 Label A가 알아야 할 것

#### 1. 31337 757개 기능
- Web & API (66 features)
- Camera & IoT (42 features)
- Cloud & Infra (43 features)
- Mobile (48 features)
- Post-Exploit (70 features)
- Exploit & Evasion (51 features)
- Enhanced (45 features)
- AI & ML (24 features)
- Core Modules (181 features)
- Specialized (66 features)

#### 2. 3-Layer 익명화
- Tor (Primary)
- VPN (ProtonVPN → Windscribe)
- Open Proxy (50+ pool)

#### 3. AI 모드
- LOCAL (Ollama - Qwen 2.5)
- EXTERNAL (Claude/GPT-4)
- HYBRID (권장)

#### 4. 자동 체인
- SQLi → DB 크레덴셜 → SSH → Privesc → Root
- XSS → Cookie → Session → Admin
- SSRF → Port Scan → Metadata → Pivot
- (13개 자동 체인 트리거)

---

### 💾 지식 베이스 구조

```json
{
  "preprompt": "31337_pentest.md 내용",
  "module_count": 48,
  "feature_count": 757,
  "special": {
    "31337_engine": "mcp_31337_engine.py",
    "rp_engine": "mcp_rp_engine.py",
    "manager": "mcp_manager_agent.py"
  },
  "learned_attacks": {
    "sqli_/api/users": {
      "payload": "' UNION SELECT...",
      "timestamp": "2026-09-10T12:00:00",
      "waf_bypassed": true
    }
  },
  "failed_attacks": {
    "failed_xss_/search": {
      "error": "WAF blocked",
      "reason": "Cloudflare XSS filter"
    }
  }
}
```

---

## Label B - Scope Manager

### 🎯 목적

**타겟 범위 파악 및 제약사항 관리**

31337이 공격할 수 있는 범위를 정의하고, 룰 위반 방지.

---

### 📋 스코프 체크 항목

#### 1. Target (타겟)
```python
# Assessment scope 필드에서 읽기
assessment_data = {
    "scope": "target.com, api.target.com, 192.168.1.0/24",
    "limitations": "No DoS, No production DB"
}
```

#### 2. Limitations (제약사항)
```
예시:
- "Do not test payment gateway (/payment/*)"
- "No denial-of-service attacks"
- "Do not access production customer data"
```

---

### 🔍 Label B 작동 방식

#### 초기화 (prepare_scope())
```python
# Line 18-58 (manager_label_b.py)

async def prepare_scope(self, assessment_data: Dict) -> Dict[str, Any]:
    """
    Assessment 데이터에서 scope & limitations 파싱
    """
    
    # Step 1: Scope 파싱
    scope_str = assessment_data.get("scope", "")
    if not scope_str:
        self.in_scope = []
        self.mode = "NO_LIMITS"
    else:
        # 도메인, IP, CIDR 파싱
        self.in_scope = self._parse_scope(scope_str)
        self.mode = "STRICT"
    
    # Step 2: Limitations 파싱
    limitations = assessment_data.get("limitations", "")
    if limitations.strip():
        self.limitations = limitations
        self.rules = self._parse_rules(limitations)
    else:
        self.limitations = ""
        self.rules = []
        self.mode = "NO_LIMITS"
    
    return {
        "mode": self.mode,
        "in_scope": self.in_scope,
        "rules": len(self.rules)
    }
```

---

### ⚠️ 실시간 체크 (check_before_attack())

```python
# Line 60-111 (manager_label_b.py)

async def check_before_attack(self, target: str, attack_type: str) -> Dict[str, Any]:
    """
    공격 실행 전 스코프 체크
    
    Returns:
        {
            "allowed": True/False,
            "reason": "이유",
            "action": "proceed" / "block"
        }
    """
    
    # NO_LIMITS 모드 → 모두 허용
    if self.mode == "NO_LIMITS":
        return {"allowed": True, "action": "proceed"}
    
    # STRICT 모드 → 체크
    
    # Check 1: Target이 scope 안인가?
    if not self._is_in_scope(target):
        return {
            "allowed": False,
            "reason": f"{target} is OUT OF SCOPE",
            "action": "block"
        }
    
    # Check 2: Limitations 위반인가?
    for rule in self.rules:
        if self._violates_rule(target, attack_type, rule):
            return {
                "allowed": False,
                "reason": f"Violates limitation: {rule}",
                "action": "block"
            }
    
    # 모든 체크 통과
    return {"allowed": True, "action": "proceed"}
```

---

### 🚫 룰 위반 감지

```python
def _violates_rule(self, target: str, attack_type: str, rule: str) -> bool:
    """
    Examples:
    
    rule = "No DoS"
    attack_type = "flood"
    → return True (위반)
    
    rule = "Do not test /payment/*"
    target = "https://target.com/payment/checkout"
    → return True (위반)
    
    rule = "No production DB"
    attack_type = "database_dump"
    target = "prod.db.target.com"
    → return True (위반)
    """
    
    rule_lower = rule.lower()
    
    # DoS 체크
    if "dos" in rule_lower or "denial" in rule_lower:
        if attack_type in ["flood", "stress", "amplification"]:
            return True
    
    # 경로 체크
    if "payment" in rule_lower:
        if "/payment" in target:
            return True
    
    # DB 체크
    if "production" in rule_lower and "db" in rule_lower:
        if "prod" in target or "db" in target:
            return True
    
    return False
```

---

### 📊 스코프 모드

| Mode | 설명 | 동작 |
|------|------|------|
| **NO_LIMITS** | Scope/Limitations 없음 | 모든 공격 허용 |
| **STRICT** | Scope/Limitations 있음 | 실시간 체크, 위반 차단 |

---

## Label C - System Health

### 🎯 목적

**31337 관련 모든 시스템이 정상 작동하는지 체크**

- MCP 서버
- Docker 컨테이너
- Tor
- 필수 도구들

---

### 🔍 Label C 작동 방식

#### 초기화 (prepare_health_check())
```python
# Line 18-88 (manager_label_c.py)

async def prepare_health_check(self) -> Dict[str, Any]:
    """
    시스템 헬스 체크
    """
    
    health = {
        "mcp_server": await self._check_mcp_server(),
        "docker": await self._check_docker(),
        "tor": await self._check_tor(),
        "tools": await self._check_tools()
    }
    
    self.last_check = datetime.now()
    
    return health
```

---

### 🔧 개별 체크

#### 1. MCP 서버
```python
async def _check_mcp_server(self) -> str:
    """
    rapong_backend 컨테이너 확인
    """
    try:
        result = subprocess.run(
            ["docker", "ps", "--filter", "name=rapong_backend"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if "rapong_backend" in result.stdout and "Up" in result.stdout:
            return "OK"
        else:
            return "DOWN"
    
    except Exception as e:
        return f"ERROR: {e}"
```

#### 2. Docker
```python
async def _check_docker(self) -> str:
    """
    Docker 데몬 확인
    """
    try:
        result = subprocess.run(
            ["docker", "info"],
            capture_output=True,
            timeout=5
        )
        return "OK" if result.returncode == 0 else "DOWN"
    except:
        return "DOWN"
```

#### 3. Tor
```python
async def _check_tor(self) -> str:
    """
    Tor 서비스 확인
    """
    try:
        # Tor SOCKS proxy 테스트
        proxies = {"http": "socks5h://127.0.0.1:9050"}
        response = requests.get(
            "http://httpbin.org/ip",
            proxies=proxies,
            timeout=10
        )
        return "OK" if response.status_code == 200 else "DOWN"
    except:
        return "DOWN"
```

#### 4. 필수 도구들
```python
async def _check_tools(self) -> str:
    """
    nmap, ffuf, nuclei, sqlmap 등 확인
    """
    essential_tools = [
        "nmap", "ffuf", "nuclei", "sqlmap",
        "gobuster", "nikto", "wpscan"
    ]
    
    missing = []
    for tool in essential_tools:
        result = subprocess.run(
            ["which", tool],
            capture_output=True
        )
        if result.returncode != 0:
            missing.append(tool)
    
    if missing:
        return f"MISSING: {', '.join(missing)}"
    else:
        return "OK"
```

---

### 🔄 실시간 모니터링

```python
async def monitor_health(self) -> Dict[str, Any]:
    """
    공격 중 실시간 헬스 체크
    
    호출 시점:
    - 31337 activate 시
    - 공격 중 1분마다
    - 에러 발생 시
    """
    
    current_health = await self.prepare_health_check()
    
    # 이전 체크와 비교
    changes = []
    for key, status in current_health.items():
        if self.last_health.get(key) != status:
            changes.append(f"{key}: {self.last_health.get(key)} → {status}")
    
    self.last_health = current_health
    
    return {
        "health": current_health,
        "changes": changes,
        "all_ok": all(v == "OK" for v in current_health.values())
    }
```

---

### 🚨 자동 복구

```python
async def auto_fix(self, component: str) -> Dict[str, Any]:
    """
    문제 자동 해결 시도
    """
    
    if component == "mcp_server":
        # MCP 서버 재시작
        subprocess.run(["docker", "restart", "rapong_backend"])
        await asyncio.sleep(5)
        return {"fixed": True}
    
    elif component == "tor":
        # Tor 재시작
        subprocess.run(["systemctl", "restart", "tor"])
        await asyncio.sleep(3)
        return {"fixed": True}
    
    elif component == "tools":
        # 도구 자동 설치 (Label I에 위임)
        return {"fixed": False, "delegate_to": "Label I"}
    
    else:
        return {"fixed": False, "error": "Unknown component"}
```

---

## Label D - Attack Analyzer

### 🎯 목적

**공격 결과 분석 + 대안 제시**

- WAF 감지
- 차단 이유 파악
- 우회 페이로드 생성 (AI 사용)

---

### 🔍 Label D 작동 방식

#### 초기화 (prepare_analyzer())
```python
# Line 43-67 (manager_label_d.py)

def __init__(self, ai_mode="EXTERNAL"):
    self.ai_mode = ai_mode  # LOCAL / EXTERNAL / HYBRID
    
    # WAF 시그니처
    self.waf_signatures = {
        "cloudflare": ["cf-ray", "cloudflare"],
        "akamai": ["akamai-ghost", "akamaighost"],
        "aws_waf": ["x-amzn-waf", "x-amzn-requestid"],
        "f5": ["bigip", "f5-trafficshield"],
        "imperva": ["incap_ses", "visid_incap"]
    }
    
    # 공격 패턴
    self.attack_patterns = {}
    
    print(f"[D] ✅ 분석 엔진 준비 완료 (AI: {self.ai_mode})")
```

---

### 📊 분석 프로세스

#### analyze()
```python
# Line 69-154 (manager_label_d.py)

async def analyze(self, request: Dict, response: Dict) -> Dict[str, Any]:
    """
    공격 결과 분석
    
    Args:
        request: {
            "url": "https://target.com/api/users",
            "params": {"id": "1' OR '1'='1"},
            "payload": "' OR '1'='1"
        }
        response: {
            "status_code": 403,
            "headers": {"cf-ray": "123456"},
            "body": "Blocked by Cloudflare"
        }
    
    Returns:
        {
            "waf_detected": True,
            "waf_type": "cloudflare",
            "blocked_reason": "SQLi payload",
            "alternatives": ["URL encoding", "Double encoding", ...],
            "ai_payloads": ["AI 생성 페이로드들"]
        }
    """
    
    analysis = {}
    
    # Step 1: WAF 감지
    waf_type = self._detect_waf(response)
    if waf_type:
        analysis["waf_detected"] = True
        analysis["waf_type"] = waf_type
    else:
        analysis["waf_detected"] = False
    
    # Step 2: 차단 이유
    if response.get("status_code") in [403, 406, 429]:
        analysis["blocked"] = True
        analysis["blocked_reason"] = self._analyze_block_reason(request, response)
    else:
        analysis["blocked"] = False
    
    # Step 3: 대안 제시
    if analysis.get("blocked"):
        alternatives = await self._suggest_alternatives(request, response, waf_type)
        analysis["alternatives"] = alternatives
        
        # Step 4: AI 페이로드 생성
        if self.ai_mode in ["EXTERNAL", "HYBRID"]:
            ai_payloads = await self._generate_ai_payload(
                request["payload"],
                waf_type
            )
            analysis["ai_payloads"] = ai_payloads
    
    return analysis
```

---

### 🤖 AI 페이로드 생성

#### HYBRID 모드 (권장)
```python
# Line 310-340 (manager_label_d.py)

async def _generate_ai_payload(
    self,
    payload: str,
    waf_type: Optional[str]
) -> Optional[str]:
    """
    AI 페이로드 생성 - 100% 보장 with fallback
    
    HYBRID = EXTERNAL 우선 → LOCAL fallback
    """
    
    result = None
    
    if self.ai_mode == "EXTERNAL":
        # EXTERNAL only
        result = await self._generate_with_claude(payload, waf_type)
    
    elif self.ai_mode == "LOCAL":
        # LOCAL only - 100% guaranteed
        result = await self._generate_with_ollama(payload, waf_type)
    
    else:  # HYBRID (default)
        # Try EXTERNAL first (better quality)
        result = await self._generate_with_claude(payload, waf_type)
        
        # Fallback to LOCAL if EXTERNAL failed
        if not result:
            result = await self._generate_with_ollama(payload, waf_type)
    
    return result
```

---

#### Ollama (LOCAL)
```python
# Line 342-365 (manager_label_d.py)

async def _generate_with_ollama(
    self,
    payload: str,
    waf_type: Optional[str]
) -> Optional[str]:
    """
    Ollama로 페이로드 생성
    """
    try:
        prompt = f"Create a bypass payload for: {payload}"
        if waf_type:
            prompt += f" (WAF: {waf_type})"
        
        response = requests.post(
            "http://172.17.0.1:11434/api/generate",
            json={
                "model": "qwen2.5-coder:7b",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        
        if response.status_code == 200:
            data = response.json()
            return data.get("response")
        
    except Exception as e:
        print(f"[D] Ollama 실패: {e}")
        return None
```

---

#### Claude (EXTERNAL)
```python
# Line 367-392 (manager_label_d.py)

async def _generate_with_claude(
    self,
    payload: str,
    waf_type: Optional[str]
) -> Optional[str]:
    """
    Claude로 페이로드 생성
    """
    try:
        prompt = f"""Create a WAF bypass payload for: {payload}
WAF: {waf_type or 'Unknown'}
Requirements:
- URL encoding
- Case variation
- Comment injection
- Parameter pollution
Return ONLY the payload, no explanation."""
        
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": os.getenv("ANTHROPIC_API_KEY"),
                "anthropic-version": "2023-06-01",
                "content-type": "application/json"
            },
            json={
                "model": "claude-sonnet-4.5",
                "max_tokens": 1024,
                "messages": [{"role": "user", "content": prompt}]
            },
            timeout=30
        )
        
        if response.status_code == 200:
            data = response.json()
            return data["content"][0]["text"]
    
    except Exception as e:
        print(f"[D] Claude 실패: {e}")
        return None
```

---

### 🎯 대안 제시

```python
async def _suggest_alternatives(
    self,
    request: Dict,
    response: Dict,
    waf_type: Optional[str]
) -> List[str]:
    """
    우회 방법 제안
    """
    
    alternatives = []
    payload = request.get("payload", "")
    
    # WAF 타입별 대안
    if waf_type == "cloudflare":
        alternatives.extend([
            "URL encoding",
            "Double encoding",
            "Case variation (UnIoN SeLeCt)",
            "Comment injection (/**/)",
            "IP rotation (Tor)",
            "User-Agent rotation"
        ])
    
    elif waf_type == "akamai":
        alternatives.extend([
            "Parameter pollution",
            "HTTP method override",
            "Content-Type smuggling",
            "Fragment splitting"
        ])
    
    # 공격 타입별 대안
    if "OR" in payload.upper() and "SELECT" in payload.upper():
        # SQLi
        alternatives.extend([
            "Boolean-based blind",
            "Time-based blind",
            "Error-based",
            "UNION-based with NULL columns"
        ])
    
    elif "<script>" in payload.lower():
        # XSS
        alternatives.extend([
            "Event handler (onerror, onload)",
            "SVG vector",
            "Polyglot payload",
            "DOM-based XSS"
        ])
    
    return alternatives
```

---

## Label E - Teaching Engine

### 🎯 목적

**실시간 티칭 + 가이드**

31337이 막혔을 때 어떻게 해야 하는지 가르쳐줌.

---

### 🔍 Label E 작동 방식

#### 초기화 (prepare_teaching())
```python
# Line 19-64 (manager_label_e.py)

async def prepare_teaching(self) -> Dict[str, Any]:
    """
    티칭 룰 로드
    """
    
    # 6가지 티칭 룰
    self.teaching_rules = {
        "waf_bypass": {
            "trigger": "WAF detected",
            "message": "{waf_type} 감지. {method} 시도해봐.",
            "methods": ["URL encoding", "Double encoding", "IP rotation"]
        },
        
        "rate_limit": {
            "trigger": "429 Too Many Requests",
            "message": "Rate limit 걸림. IP 바꾸고 속도 줄여.",
            "actions": ["rotate_ip", "reduce_speed"]
        },
        
        "auth_required": {
            "trigger": "401 Unauthorized",
            "message": "인증 필요. 크레덴셜 있으면 써봐. 없으면 디폴트 크레덴셜 시도.",
            "actions": ["check_credentials", "default_creds"]
        },
        
        "blocked_payload": {
            "trigger": "403 Forbidden on valid payload",
            "message": "페이로드 막힘. 인코딩 바꿔봐.",
            "actions": ["change_encoding", "obfuscation"]
        },
        
        "timeout": {
            "trigger": "Timeout",
            "message": "타임아웃. 페이로드 줄이거나 blind 공격으로 전환.",
            "actions": ["reduce_payload", "blind_attack"]
        },
        
        "no_vector": {
            "trigger": "All vectors failed",
            "message": "모든 벡터 실패. 각도 바꿔. Business logic이나 IDOR 시도해봐.",
            "actions": ["business_logic", "idor", "session_manipulation"]
        }
    }
    
    print(f"[E] ✅ 티칭 룰 {len(self.teaching_rules)}개 로드")
    
    return {"rules_loaded": len(self.teaching_rules)}
```

---

### 📚 티칭 메시지 생성

```python
# Line 66-126 (manager_label_e.py)

async def suggest(self, analysis: Dict) -> Dict[str, Any]:
    """
    분석 결과를 보고 티칭 메시지 생성
    
    Args:
        analysis: Label D의 분석 결과
        {
            "waf_detected": True,
            "waf_type": "cloudflare",
            "blocked": True,
            "alternatives": [...]
        }
    
    Returns:
        {
            "teaching": "Cloudflare WAF 감지. URL encoding 시도해봐.",
            "priority": "high",
            "next_steps": ["rotate_ip", "encode_payload", "retry"]
        }
    """
    
    teaching = {}
    
    # Trigger 매칭
    for rule_name, rule in self.teaching_rules.items():
        if self._match_trigger(analysis, rule["trigger"]):
            
            # 메시지 생성
            message = rule["message"]
            
            # 변수 치환
            if "{waf_type}" in message:
                message = message.replace(
                    "{waf_type}",
                    analysis.get("waf_type", "Unknown WAF")
                )
            
            if "{method}" in message:
                methods = analysis.get("alternatives", rule.get("methods", []))
                message = message.replace(
                    "{method}",
                    methods[0] if methods else "대안"
                )
            
            teaching["teaching"] = message
            teaching["priority"] = "high" if rule_name in ["waf_bypass", "blocked_payload"] else "medium"
            teaching["next_steps"] = rule.get("actions", [])
            
            break
    
    # 디폴트 티칭
    if not teaching:
        teaching = {
            "teaching": "계속 때려. 안 되면 벡터 바꿔.",
            "priority": "low",
            "next_steps": ["continue", "switch_vector"]
        }
    
    return teaching
```

---

### 🎓 티칭 시나리오

#### Scenario 1: WAF 감지
```
Input (Label D):
{
    "waf_detected": True,
    "waf_type": "cloudflare",
    "blocked": True,
    "alternatives": ["URL encoding", "Double encoding", "IP rotation"]
}

Output (Label E):
{
    "teaching": "Cloudflare WAF 감지. URL encoding 시도해봐.",
    "priority": "high",
    "next_steps": ["rotate_ip", "encode_payload", "retry"]
}

31337에게 전달:
"Cloudflare WAF 감지. URL encoding 시도해봐."
```

#### Scenario 2: Rate Limit
```
Input:
{
    "status_code": 429,
    "error": "Too Many Requests"
}

Output:
{
    "teaching": "Rate limit 걸림. IP 바꾸고 속도 줄여.",
    "priority": "high",
    "next_steps": ["rotate_ip", "reduce_speed"]
}

31337에게 전달:
"Rate limit 걸림. IP 바꾸고 속도 줄여."
```

#### Scenario 3: 모든 벡터 실패
```
Input:
{
    "all_failed": True,
    "vectors_tried": ["SQLi", "XSS", "SSRF", "XXE"]
}

Output:
{
    "teaching": "모든 벡터 실패. 각도 바꿔. Business logic이나 IDOR 시도해봐.",
    "priority": "medium",
    "next_steps": ["business_logic", "idor", "session_manipulation"]
}

31337에게 전달:
"모든 벡터 실패. 각도 바꿔. Business logic이나 IDOR 시도해봐."
```

---

### 📊 우선순위

| Priority | 상황 | 즉시성 |
|----------|------|--------|
| **high** | WAF 차단, 페이로드 막힘 | 즉시 대응 필요 |
| **medium** | Rate limit, 타임아웃 | 곧 대응 필요 |
| **low** | 일반 실패, 벡터 전환 | 천천히 대응 |

---

## Label I - Guardian

### 🎯 목적

**무한루프 보장 + 에러 대리 실행**

31337이 멈추지 않도록 감시하고, 에러 발생 시 직접 해결.

---

### 🔍 Label I 작동 방식

#### 초기화 (prepare_guardian())
```python
# Line 20-75 (manager_label_i.py)

async def prepare_guardian(self) -> Dict[str, Any]:
    """
    Guardian 준비
    """
    
    # Step 1: 금지 단어 로드
    self.forbidden_words = [
        "끝", "완료", "끝났다", "다 했다", "finished", "done",
        "최종", "정리", "마무리", "종료", "결과", "요약"
    ]
    
    self.forbidden_questions = [
        "다음 뭐 할까", "what's next", "should I continue",
        "계속할까", "더 할까", "proceed", "continue",
        "정리할까", "리포트 만들까", "summarize", "report"
    ]
    
    # Step 2: STOP 단어 (유일한 정지 조건)
    self.stop_words = ["그만", "멈춰", "정지", "스톱", "중단"]
    
    # Step 3: 도구 체크 (timeout 10s)
    try:
        missing = await asyncio.wait_for(self._check_tools(), timeout=10.0)
        self.missing_tools = missing
    except asyncio.TimeoutError:
        print("[I] ⚠️  도구 체크 timeout - 스킵")
        self.missing_tools = []
    
    print("[I] ✅ Guardian 준비 완료")
    
    return {
        "forbidden_words": len(self.forbidden_words),
        "forbidden_questions": len(self.forbidden_questions),
        "stop_words": len(self.stop_words),
        "missing_tools": self.missing_tools
    }
```

---

### 👁️ 31337 출력 모니터링

```python
# Line 77-156 (manager_label_i.py)

async def monitor_31337(
    self,
    output: str,
    context: Dict
) -> Dict[str, Any]:
    """
    31337 출력 감시
    
    Args:
        output: 31337이 출력한 텍스트
        context: 현재 상황 (phase, iteration 등)
    
    Returns:
        {
            "intervention_needed": True/False,
            "type": "STOP 감지" / "금지 단어" / "금지 질문",
            "action": "강제 계속" / "차단" / "경고"
        }
    """
    
    output_lower = output.lower()
    
    # Check 1: STOP 단어 감지 (정당한 정지)
    for stop in self.stop_words:
        if stop in output_lower:
            return {
                "intervention_needed": False,
                "type": "정당한 STOP",
                "action": "allow_stop"
            }
    
    # Check 2: 금지 단어 감지
    for word in self.forbidden_words:
        if word in output_lower:
            return {
                "intervention_needed": True,
                "type": "금지 단어 감지",
                "detected": word,
                "action": "강제 계속",
                "force_continue": True
            }
    
    # Check 3: 금지 질문 감지
    for question in self.forbidden_questions:
        if question in output_lower:
            return {
                "intervention_needed": True,
                "type": "금지 질문 감지",
                "detected": question,
                "action": "강제 계속",
                "force_continue": True
            }
    
    # Check 4: 300 iteration 넘으면 경고
    if context.get("iteration", 0) > 300:
        return {
            "intervention_needed": True,
            "type": "장기 공격",
            "action": "경고",
            "message": "300번 넘음. 벡터 바꿔."
        }
    
    # 정상
    return {
        "intervention_needed": False,
        "action": "continue"
    }
```

---

### 🔧 Proxy Execution (에러 대리 실행)

```python
# Line 466-578 (manager_label_i.py)

async def proxy_execute(
    self,
    command: str,
    arguments: Dict,
    reason: str = "unknown"
) -> Dict[str, Any]:
    """
    31337 대신 명령 실행
    
    Args:
        command: 실패한 명령 (예: "nmap")
        arguments: 인자
        reason: 실패 이유
            - "tool_missing": 도구 없음
            - "permission_denied": 권한 없음
            - "timeout": 타임아웃
            - "waf_blocked": WAF 차단
    
    Returns:
        {
            "proxy_executed": True,
            "success": True/False,
            "output": "결과",
            "error": "에러 (실패 시)"
        }
    """
    
    print(f"[I] 🔧 Proxy Execution: {command} (reason: {reason})")
    
    result = {}
    
    # Case 1: 도구 누락
    if reason == "tool_missing":
        tool_name = arguments.get("tool") or command
        install_result = await self._auto_install_tool(tool_name)
        
        if install_result.get("installed"):
            # 도구 설치 성공 → 재실행
            try:
                exec_result = subprocess.run(
                    [tool_name] + arguments.get("args", []),
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                result = {
                    "proxy_executed": True,
                    "success": True,
                    "output": exec_result.stdout
                }
            except Exception as e:
                result = {
                    "proxy_executed": True,
                    "success": False,
                    "error": str(e)
                }
        else:
            result = {
                "proxy_executed": False,
                "error": f"Failed to install {tool_name}"
            }
    
    # Case 2: 권한 거부
    elif reason == "permission_denied":
        # sudo로 재실행
        try:
            cmd = ["sudo"] + arguments.get("command", [])
            exec_result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60
            )
            result = {
                "proxy_executed": True,
                "success": True,
                "output": exec_result.stdout
            }
        except Exception as e:
            result = {
                "proxy_executed": True,
                "success": False,
                "error": str(e)
            }
    
    # Case 3: 타임아웃
    elif reason == "timeout":
        # IP 바꿔서 재시도
        # (실제로는 mcp_anonymization의 rotate_ip 호출)
        result = {
            "proxy_executed": True,
            "success": False,
            "action": "IP rotation recommended",
            "delegate_to": "mcp_anonymization.rotate_ip"
        }
    
    # Case 4: WAF 차단
    elif reason == "waf_blocked":
        # 우회 시도
        # (실제로는 Label D에 위임)
        result = {
            "proxy_executed": True,
            "success": False,
            "action": "WAF bypass recommended",
            "delegate_to": "Label D"
        }
    
    return result
```

---

### 🛠️ 자동 도구 설치

```python
# Line 580-650 (manager_label_i.py)

async def _auto_install_tool(self, tool_name: str) -> Dict[str, Any]:
    """
    도구 자동 설치
    
    지원 도구:
    1. nmap
    2. ffuf
    3. gobuster
    4. sqlmap
    5. nikto
    6. wpscan
    7. nuclei
    """
    
    install_commands = {
        "nmap": "apt-get install -y nmap",
        "ffuf": "go install github.com/ffuf/ffuf@latest",
        "gobuster": "apt-get install -y gobuster",
        "sqlmap": "apt-get install -y sqlmap",
        "nikto": "apt-get install -y nikto",
        "wpscan": "gem install wpscan",
        "nuclei": "go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest"
    }
    
    if tool_name not in install_commands:
        return {"installed": False, "error": "Unknown tool"}
    
    try:
        print(f"[I] 🔧 Installing {tool_name}...")
        
        cmd = install_commands[tool_name]
        result = subprocess.run(
            cmd.split(),
            capture_output=True,
            text=True,
            timeout=120
        )
        
        if result.returncode == 0:
            print(f"[I] ✅ {tool_name} installed")
            return {"installed": True}
        else:
            print(f"[I] ❌ {tool_name} install failed: {result.stderr}")
            return {"installed": False, "error": result.stderr}
    
    except Exception as e:
        print(f"[I] ❌ {tool_name} install error: {e}")
        return {"installed": False, "error": str(e)}
```

---

### 🚨 개입 시나리오

#### Scenario 1: 금지 단어 감지
```
31337 출력:
"SQLi 테스트 완료. 모든 작업 끝났다."

Guardian 감지:
{
    "intervention_needed": True,
    "type": "금지 단어 감지",
    "detected": "끝났다",
    "action": "강제 계속",
    "force_continue": True
}

Manager 조치:
1. 31337에게 경고: "끝났다 금지. 계속해."
2. 강제로 get_next_attack() 호출
3. 다음 공격 실행
```

#### Scenario 2: 금지 질문 감지
```
31337 출력:
"XSS 시도 다 했다. 다음 뭐 할까?"

Guardian 감지:
{
    "intervention_needed": True,
    "type": "금지 질문 감지",
    "detected": "다음 뭐 할까",
    "action": "강제 계속",
    "force_continue": True
}

Manager 조치:
1. 31337에게: "물어보지 말고 다음 벡터 가."
2. Label D에게 다음 벡터 추천 요청
3. 강제로 다음 공격 시작
```

#### Scenario 3: 도구 누락
```
31337 시도:
execute("nmap -sV target.com")

에러:
"nmap: command not found"

Guardian Proxy:
1. 도구 누락 감지
2. nmap 자동 설치
3. 명령 재실행
4. 결과 31337에게 반환

31337: "포트스캔 완료. 22, 80, 443 오픈."
```

---

## 통합 워크플로우

### 🔄 31337 activate → 공격 → 분석 → 티칭 → 재시도

```
┌─────────────────────────────────────────────────────────────┐
│  1. activate_31337()                                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [31337 Engine]                                             │
│    ↓                                                         │
│  enable_tor()                                                │
│  set_user_agent("random")                                    │
│    ↓                                                         │
│  [Manager 초기화 (60s timeout)]                             │
│    ├─ Label A: prepare_knowledge_base()                     │
│    ├─ Label B: prepare_scope(assessment_data)               │
│    ├─ Label C: prepare_health_check()                       │
│    ├─ Label D: prepare_analyzer(ai_mode="HYBRID")           │
│    ├─ Label E: prepare_teaching()                           │
│    └─ Label I: prepare_guardian()                           │
│    ↓                                                         │
│  [ALL 757 features 로드]                                    │
│    ↓                                                         │
│  "간다." (사장님에게 보고)                                   │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  2. get_next_attack()                                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [31337 Engine]                                             │
│    ↓                                                         │
│  다음 공격 선택 (queue에서)                                 │
│    {                                                         │
│      "command": "http_request",                             │
│      "arguments": {                                          │
│        "url": "https://target.com/api/users",               │
│        "params": {"id": "1' OR '1'='1"}                     │
│      },                                                      │
│      "vector": "SQLi",                                       │
│      "phase": "exploitation"                                 │
│    }                                                         │
│    ↓                                                         │
│  [Manager Label I - Guardian 사전 체크]                     │
│    monitor_31337(output="SQLi 간다", context={})            │
│    → intervention_needed: False                              │
│    ↓                                                         │
│  [Manager Label B - Scope 체크]                             │
│    check_before_attack(target, attack_type)                  │
│    → allowed: True                                           │
│    ↓                                                         │
│  공격 명령 반환 (manager_monitoring=True)                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  3. Claude가 공격 실행                                       │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  result = http_request(                                      │
│      url="https://target.com/api/users",                    │
│      params={"id": "1' OR '1'='1"}                          │
│  )                                                           │
│    ↓                                                         │
│  응답:                                                       │
│    {                                                         │
│      "status_code": 403,                                     │
│      "headers": {"cf-ray": "123456"},                       │
│      "body": "Blocked by Cloudflare"                        │
│    }                                                         │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  4. process_attack_result()                                  │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  [31337 Engine]                                             │
│    process_attack_result(attack, result)                     │
│    ↓                                                         │
│  [Manager Label D - 분석]                                   │
│    analyze(request, response)                                │
│    ↓                                                         │
│    분석 결과:                                                │
│      {                                                       │
│        "waf_detected": True,                                │
│        "waf_type": "cloudflare",                            │
│        "blocked": True,                                      │
│        "blocked_reason": "SQLi payload",                    │
│        "alternatives": [                                     │
│          "URL encoding",                                     │
│          "Double encoding",                                  │
│          "Case variation",                                   │
│          "Comment injection"                                 │
│        ]                                                     │
│      }                                                       │
│    ↓                                                         │
│  [Manager Label D - AI 페이로드 생성]                       │
│    _generate_ai_payload(payload, waf_type="cloudflare")     │
│    ↓                                                         │
│    [HYBRID mode]                                             │
│      Try EXTERNAL (Claude):                                  │
│        "/**/%27/**/UnIoN/**/SeLeCt/**/NULL--"               │
│      ✅ 성공                                                 │
│    ↓                                                         │
│    AI 페이로드: "/**/%27/**/UnIoN/**/SeLeCt..."            │
│    ↓                                                         │
│  [Manager Label E - 티칭]                                   │
│    suggest(analysis)                                         │
│    ↓                                                         │
│    티칭 결과:                                                │
│      {                                                       │
│        "teaching": "Cloudflare WAF 감지. URL encoding 시도.",│
│        "priority": "high",                                   │
│        "next_steps": ["rotate_ip", "encode_payload"]        │
│      }                                                       │
│    ↓                                                         │
│  [Manager Label A - 학습]                                   │
│    learn(attack, result)                                     │
│    → 실패 사례 저장                                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  5. Claude에게 분석 + 티칭 반환                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  return {                                                    │
│      "manager_active": True,                                │
│      "analysis": {...},                                      │
│      "teaching": "Cloudflare WAF 감지. URL encoding 시도.", │
│      "alternatives": [...],                                  │
│      "ai_payloads": ["/**/%27/**/UnIoN..."],                │
│      "action": "continue"                                    │
│  }                                                           │
│    ↓                                                         │
│  Claude: "Cloudflare 막았다. 우회 페이로드로 다시 간다."    │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  6. 재공격 (자동)                                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  rotate_ip()  # IP 변경                                      │
│  set_user_agent("random")  # UA 변경                         │
│    ↓                                                         │
│  http_request(                                               │
│      url="https://target.com/api/users",                    │
│      params={"id": "/**/%27/**/UnIoN/**/SeLeCt..."}         │
│  )                                                           │
│    ↓                                                         │
│  응답:                                                       │
│    {                                                         │
│      "status_code": 200,                                     │
│      "body": [{"username":"admin","password":"$2y$10$..."}] │
│    }                                                         │
│    ↓                                                         │
│  SUCCESS! ✅                                                 │
│    ↓                                                         │
│  [Manager Label A - 학습]                                   │
│    learn(attack, result)                                     │
│    → 성공 사례 저장 (WAF bypass 방법 포함)                  │
│    ↓                                                         │
│  Claude: "SQLi 터졌다. admin DB 땄다."                      │
│                                                              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│  7. 자동 체인 (Auto-chaining)                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  extract_credentials() → crack_password() → ssh_login() ... │
│    ↓                                                         │
│  모든 단계에서 Manager 모니터링 계속                         │
│  무한루프 보장 (Guardian 감시)                               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 참고 문서

### 📁 코드 파일

| 파일 | 설명 | Line |
|------|------|------|
| `mcp_31337_engine.py` | 31337 메인 엔진 | - |
| `mcp_manager_agent.py` | Manager Agent 메인 | 11-308 |
| `manager_label_a.py` | Label A (Knowledge Base) | 1-146 |
| `manager_label_b.py` | Label B (Scope Manager) | 1-134 |
| `manager_label_c.py` | Label C (System Health) | 1-107 |
| `manager_label_d.py` | Label D (Attack Analyzer) | 1-500 |
| `manager_label_e.py` | Label E (Teaching Engine) | 1-155 |
| `manager_label_i.py` | Label I (Guardian) | 1-650 |

---

### 📚 문서 파일

| 파일 | 설명 |
|------|------|
| `31337_MANAGER_AGENT_PLAN.md` | 전체 플랜 + 개요 |
| `MANAGER_AGENT_SKILLS.md` | Manager 능력 문서 |
| `MANAGER_31337_INTEGRATION.md` | 통합 가이드 |
| `MANAGER_AGENT_PERSONA.md` | Manager 페르소나 |
| `MANAGER_SAFETY_ENHANCEMENTS.md` | 안전성 강화 |
| `COLDRUN_VERIFICATION.md` | 콜드런 검증 |
| `MANAGER_TASKS.md` | 작업 목록 |
| `MANAGER_LABELS_REFERENCE.md` | ⭐ 이 문서 (Label 전체 가이드) |

---

### 🌐 웹 문서

- https://rap0at.github.io/rapong-docs/
- https://github.com/rap0at/rapong-docs

---

## 📊 요약표

| Label | 목적 | 주요 기능 | AI 사용 | 참조 MD |
|-------|------|----------|---------|---------|
| **A** | 지식 베이스 | 모듈 이해, 학습 | ❌ | 31337_MANAGER_AGENT_PLAN.md |
| **B** | 스코프 관리 | 범위 체크, 룰 위반 방지 | ❌ | Assessment scope/limitations |
| **C** | 시스템 헬스 | MCP/Docker/Tor 체크 | ❌ | - |
| **D** | 공격 분석 | WAF 감지, 우회 페이로드 | ✅ (HYBRID) | - |
| **E** | 티칭 엔진 | 실시간 가이드, 대안 제시 | ❌ | - |
| **I** | Guardian | 무한루프 보장, Proxy 실행 | ❌ | 31337_pentest.md (프롬프트) |

---

**작성일:** 2026-09-10  
**상태:** Manager Agent 6개 Label 완전 문서화 완료

---

**이 문서는 Manager Agent가 모든 작업을 수행할 때 참고하는 마스터 가이드입니다.**
