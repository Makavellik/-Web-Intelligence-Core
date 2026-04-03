import requests
import ssl
import socket
import re
import hashlib
from urllib.parse import urlparse
from datetime import datetime
from collections import Counter
import math
import asyncio
from playwright.async_api import async_playwright
import dns.resolver
import string
import random
import time
from urllib.parse import urlparse
import sys
import threading
from rich.text import Text
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

console = Console()

# ===========================
# 🧬 BANNER MINIMAL VIVO
# ===========================
def typewriter_slow(text, style="bold", base_delay=0.03):
    buffer = Text("", style=style)

    for c in text:
        buffer.append(c)
        console.print(buffer, end="\r")  # sobrescribe línea

        delay = base_delay + random.uniform(0.005, 0.04)

        # pausas raras pero suaves
        if random.random() < 0.06:
            time.sleep(random.uniform(0.1, 0.3))

        time.sleep(delay)

    console.print(buffer)  


def subtle_glitch(text):
    if random.random() < 0.15:
        glitched = list(text)
        i = random.randint(0, len(text)-1)
        glitched[i] = random.choice(["#", "%", "&", "@"])
        return "".join(glitched)
    return text


# ===========================
# 👁️ MENSAJES FANTASMA
# ===========================
def ghost_message():
    messages = [
        "…observando patrones",
        "…esto no es aleatorio",
        "…hay algo más aquí",
        "…sincronización externa",
        "…frecuencia alterada",
    ]

    if random.random() < 0.18:
        msg = random.choice(messages)
        console.print(f"[dim red]{msg}[/dim red]")
        time.sleep(random.uniform(0.3, 0.8))


# ===========================
# 🧬 BANNER PERTURBADOR
# ===========================
def render_perturbador_banner():
    console.print("\n")

    console.print("[blue]┌──────────────────────────────┐[/blue]")

    # 🔥 IMPORTANTE: construir línea completa
    line1 = subtle_glitch("BYMAKAVELI")
    line2 = "core online"
    line3 = "presence detected..."

    # render limpio (sin romper bordes)
    console.print("[blue]│[/blue] ", end="")
    typewriter_slow(line1, style="bold red", base_delay=0.035)

    console.print("[blue]│[/blue] ", end="")
    typewriter_slow(line2, style="dim cyan", base_delay=0.025)

    console.print("[blue]│[/blue] ", end="")
    typewriter_slow(line3, style="dim red", base_delay=0.02)

    console.print("[blue]└──────────────────────────────┘[/blue]\n")

    ghost_message()

# ===========================
# ⚡ EFECTO PARPADEO
# ===========================
class Blink:
    def __init__(self):
        self.state = True

    def toggle(self):
        self.state = not self.state
        return "█" if self.state else " "

# ---------------------------
# 🌍 REGIONES (idioma coherente)
# ---------------------------
LANG_PROFILES = [
    "en-US,en;q=0.9",
    "es-ES,es;q=0.9,en;q=0.8",
    "fr-FR,fr;q=0.9,en;q=0.7",
    "de-DE,de;q=0.9,en;q=0.7"
]

# ---------------------------
# 🌐 REFERERS REALISTAS
# ---------------------------
REFERERS = [
    "https://www.google.com/",
    "https://www.bing.com/",
    "https://duckduckgo.com/",
    "https://news.ycombinator.com/"
]

# ---------------------------
# 🧠 USER AGENTS REALES
# ---------------------------
USER_AGENTS = [
    # 🪟 Windows - Chrome
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/121.0.0.0 Safari/537.36",

    # 🍎 macOS - Chrome / Safari
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_0) AppleWebKit/537.36 Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5) AppleWebKit/605.1.15 Version/17.0 Safari/605.1.15",

    # 📱 Mobile - Android
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 Chrome/120.0.0.0 Mobile Safari/537.36",

    # 📱 Mobile - iPhone
    "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 Version/16.0 Mobile/15E148 Safari/604.1"
]


# ---------------------------
# 🧬 GENERADOR DE HEADERS
# ---------------------------
def generate_headers(session_state):
    ua = random.choice(USER_AGENTS)

    # 🧠 detectar tipo de dispositivo
    is_mobile = "Mobile" in ua or "Android" in ua or "iPhone" in ua

    headers = {
        "User-Agent": ua,

        # Accept más realista con ligera mutación
        "Accept": random.choice([
            "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "text/html,application/xml;q=0.9,image/webp,*/*;q=0.8",
        ]),

        "Accept-Language": random.choice(LANG_PROFILES),

        # encoding adaptable
        "Accept-Encoding": random.choice([
            "gzip, deflate, br",
            "gzip, deflate"
        ]),

        "Connection": "keep-alive",
    }

    # ---------------------------
    # 🔥 REFERER DINÁMICO
    # ---------------------------
    if session_state.get("last_url") and random.random() > 0.2:
        headers["Referer"] = session_state["last_url"]
    else:
        headers["Referer"] = random.choice(REFERERS)

    # ---------------------------
    # 🧠 DNT (no siempre presente)
    # ---------------------------
    if random.random() > 0.6:
        headers["DNT"] = "1"

    # ---------------------------
    # 🧬 UPGRADE-INSECURE (navegadores modernos)
    # ---------------------------
    if random.random() > 0.5:
        headers["Upgrade-Insecure-Requests"] = "1"

    # ---------------------------
    # 📱 HEADERS MÓVILES
    # ---------------------------
    if is_mobile:
        headers["Viewport-Width"] = str(random.choice([360, 390, 412]))
        headers["Sec-CH-UA-Mobile"] = "?1"

    # ---------------------------
    # 🧠 HEADERS TIPO CHROME (ligero fingerprint realista)
    # ---------------------------
    if "Chrome" in ua and random.random() > 0.5:
        headers["Sec-Fetch-Site"] = random.choice(["none", "same-origin", "cross-site"])
        headers["Sec-Fetch-Mode"] = "navigate"
        headers["Sec-Fetch-Dest"] = "document"

    return headers

# ---------------------------
# 🧠 SESIÓN HUMANA
# ---------------------------
class HumanSession:
    def __init__(self):
        self.session = requests.Session()

        # 🔥 Adapter para mayor estabilidad (reintentos suaves)
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,
            pool_maxsize=10,
            max_retries=1  # leve, no agresivo
        )
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        self.state = {
            "last_url": None,
            "history": []
        }

    def think_time(self):
        # ⏱️ delay humano más natural (con micro-variación)
        base = random.uniform(0.8, 2.2)
        jitter = random.uniform(0.0, 0.4)
        time.sleep(base + jitter)

    def visit(self, url):
        headers = generate_headers(self.state)

        # 🔄 reset limpio de headers
        self.session.headers.clear()
        self.session.headers.update(headers)

        self.think_time()

        try:
            r = self.session.get(
                url,
                timeout=(4, 10),  # 🔥 mejor control: conexión + lectura
                allow_redirects=True
            )

            # 🔍 validación silenciosa de respuesta
            if not r or not hasattr(r, "status_code"):
                return None

            # 🧬 actualizar estado SOLO si hay respuesta válida
            self.state["last_url"] = url

            # evitar crecimiento infinito del historial
            if len(self.state["history"]) > 20:
                self.state["history"].pop(0)

            self.state["history"].append(url)

            return r

        except requests.exceptions.Timeout:
            return None

        except requests.exceptions.ConnectionError:
            return None

        except requests.exceptions.RequestException:
            return None

        except Exception:
            return None

    def warmup(self, base_url):
        """
        🔥 Simula navegación previa real antes del análisis
        (misma lógica, más coherente internamente)
        """
        base = base_url.rstrip("/")

        paths = ["", "/", "/home", "/index.html"]

        # ligera variación en profundidad
        steps = random.randint(1, 3)

        for _ in range(steps):
            path = random.choice(paths)

            # evitar duplicados consecutivos (detalle fino)
            if self.state["history"] and self.state["history"][-1].endswith(path):
                continue

            url = base + path

            r = self.visit(url)

            # 🔥 micro pausa adicional si hay redirecciones (simula lectura)
            try:
                if r and len(r.history) > 0:
                    time.sleep(random.uniform(0.2, 0.6))
            except:
                pass

# ---------------------------
# 🌐 FETCH MULTI-SIGNAL
# ---------------------------
def fetch(url):
    hs = HumanSession()

    # 🧠 navegación previa (clave)
    hs.warmup(url)

    response = hs.visit(url)
    if not response:
        return None

    r = response

    return {
        "html": r.text[:200000],
        "headers": r.headers,
        "status": r.status_code,
        "size": len(r.content),
        "time_total": r.elapsed.total_seconds(),
        "redirect_chain": [resp.status_code for resp in r.history],
        "history": hs.state["history"],
        "final_url": r.url
    }

# ---------------------------
# 🧠 TECH INFERENCE (WEIGHTED)
# ---------------------------
PATTERNS = {
    "React": {
        "strong": [
            r"__NEXT_DATA__",
            r"data-reactroot",
            r"react-dom"
        ],
        "weak": [
            r"react",
            r"_reactRootContainer"
        ],
        "context": [
            r"<div id=\"root\">",
            r"bundle.*\.js"
        ]
    },

    "Vue": {
        "strong": [
            r"data-v-[a-z0-9]+",
            r"__VUE_DEVTOOLS_GLOBAL_HOOK__"
        ],
        "weak": [
            r"vue",
            r"v-bind"
        ],
        "context": [
            r"id=\"app\"",
            r"vue\.runtime"
        ]
    },

    "Angular": {
        "strong": [
            r"ng-version",
            r"angular\.js"
        ],
        "weak": [
            r"ng-",
            r"angular"
        ],
        "context": [
            r"<app-root>",
            r"zone\.js"
        ]
    },

    "WordPress": {
        "strong": [
            r"wp-content",
            r"wp-includes"
        ],
        "weak": [
            r"wordpress",
            r"wp-json"
        ],
        "context": [
            r"xmlrpc\.php",
            r"wp-admin"
        ]
    },

    "Laravel": {
        "strong": [
            r"laravel_session",
            r"csrf-token"
        ],
        "weak": [
            r"laravel",
            r"framework"
        ],
        "context": [
            r"/vendor/laravel",
            r"csrf_token"
        ]
    },

    "Django": {
        "strong": [
            r"csrftoken",
            r"django"
        ],
        "weak": [
            r"csrfmiddlewaretoken"
        ],
        "context": [
            r"__admin__",
            r"/static/admin"
        ]
    }
}

# ---------------------------
# 🧠 PATTERN ANALYZER
# ---------------------------
def analyze_patterns(blob):
    results = {}

    for tech, layers in PATTERNS.items():
        score = 0
        evidence = []

        # 🔥 señales fuertes
        for p in layers["strong"]:
            if re.search(p, blob):
                score += 0.5
                evidence.append(f"strong:{p}")

        # ⚖️ señales débiles
        for p in layers["weak"]:
            if re.search(p, blob):
                score += 0.2
                evidence.append(f"weak:{p}")

        # 🧠 contexto
        for p in layers["context"]:
            if re.search(p, blob):
                score += 0.3
                evidence.append(f"context:{p}")

        if score > 0:
            confidence = min(score, 0.95)

            results[tech] = {
                "confidence": round(confidence, 2),
                "evidence": evidence
            }

    return results


# ---------------------------
# 🚀 INFER TECH (FUSIONADO)
# ---------------------------
def infer_tech(html, headers):
    blob = html.lower()
    h = {k.lower(): v.lower() for k, v in headers.items()}

    signals = {}
    weights = {}

    # ---------------------------
    # 🧠 SISTEMA DE REGISTRO
    # ---------------------------
    def add_signal(tech, weight, reason):
        if tech not in signals:
            signals[tech] = []
            weights[tech] = 0

        signals[tech].append(reason)
        weights[tech] += weight

    # ---------------------------
    # 🔥 NUEVO: PATTERN ENGINE
    # ---------------------------
    pattern_results = analyze_patterns(blob)

    for tech, data in pattern_results.items():
        confidence = data["confidence"]
        evidence = data["evidence"]

        # convertimos confianza → peso interno
        weight = confidence * 0.8

        for ev in evidence:
            add_signal(tech, weight, f"pattern:{ev}")

    # ---------------------------
    # 🧬 META TAGS (muy fiable)
    # ---------------------------
    generator = re.findall(r'<meta name=\"generator\" content=\"(.*?)\"', blob)
    for g in generator:
        if "wordpress" in g:
            add_signal("WordPress", 0.8, "meta:generator")

    # ---------------------------
    # 📡 HEADERS (infra/backend)
    # ---------------------------
    server = h.get("server", "")
    powered = h.get("x-powered-by", "")

    if "nginx" in server:
        add_signal("Nginx", 0.6, "header:server")

    if "apache" in server:
        add_signal("Apache", 0.6, "header:server")

    if "php" in powered:
        add_signal("PHP", 0.7, "header:powered")

    # ---------------------------
    # 🍪 COOKIES (muy revelador)
    # ---------------------------
    cookies = h.get("set-cookie", "")

    if "laravel_session" in cookies:
        add_signal("Laravel", 0.9, "cookie")

    if "csrftoken" in cookies:
        add_signal("Django", 0.9, "cookie")

    if "wordpress_logged_in" in cookies:
        add_signal("WordPress", 0.95, "cookie")

    # ---------------------------
    # 🧠 JS RUNTIME SIGNALS
    # ---------------------------
    if "__next_data__" in blob:
        add_signal("React (Next.js)", 0.85, "js-runtime")

    if "window.__NUXT__" in blob:
        add_signal("Vue (Nuxt)", 0.85, "js-runtime")

    # ---------------------------
    # 🧬 RUTAS / ESTRUCTURA
    # ---------------------------
    if "/wp-content/" in blob:
        add_signal("WordPress", 0.7, "path")

    if "/static/js/" in blob and "webpack" in blob:
        add_signal("Webpack", 0.5, "bundle")

    # ---------------------------
    # ⚖️ NORMALIZACIÓN INTELIGENTE
    # ---------------------------
    detected = {}

    for tech, total_weight in weights.items():
        evidence_count = len(signals[tech])

        confidence = min(0.25 + (total_weight * 0.6) + (evidence_count * 0.05), 0.98)

        detected[tech] = {
            "confidence": round(confidence, 2),
            "evidence": signals[tech]
        }

    return detected


def fusion_engine(html, headers, response_data, exposure_data): 
    blob = html.lower()
    h = {k.lower(): v.lower() for k, v in headers.items()}

    fusion = {}

    # ---------------------------
    # 🧠 REGISTRO CENTRAL
    # ---------------------------
    def add(tech, weight, source, detail):
        if tech not in fusion:
            fusion[tech] = {
                "score": 0,
                "sources": set(),       # 🔥 evitar duplicados
                "evidence": []
            }

        fusion[tech]["score"] += weight
        fusion[tech]["sources"].add(source)

        # 🔥 evitar evidencia duplicada
        if detail not in fusion[tech]["evidence"]:
            fusion[tech]["evidence"].append(detail)

    # ---------------------------
    # 🔬 1. PATTERNS (HTML)
    # ---------------------------
    for tech, layers in PATTERNS.items():
        for p in layers["strong"]:
            if re.search(p, blob):
                add(tech, 0.6, "html_strong", p)

        for p in layers["weak"]:
            if re.search(p, blob):
                add(tech, 0.2, "html_weak", p)

        for p in layers["context"]:
            if re.search(p, blob):
                add(tech, 0.3, "html_context", p)

    # ---------------------------
    # 📡 2. HEADERS
    # ---------------------------
    server = h.get("server", "")
    powered = h.get("x-powered-by", "")

    if "nginx" in server:
        add("Nginx", 0.7, "header", "server")

    if "apache" in server:
        add("Apache", 0.7, "header", "server")

    if "php" in powered:
        add("PHP", 0.8, "header", "x-powered-by")

    # ---------------------------
    # 🍪 3. COOKIES
    # ---------------------------
    cookies = h.get("set-cookie", "")

    if "laravel_session" in cookies:
        add("Laravel", 1.0, "cookie", "laravel_session")

    if "csrftoken" in cookies:
        add("Django", 1.0, "cookie", "csrftoken")

    if "wordpress_logged_in" in cookies:
        add("WordPress", 1.0, "cookie", "wp_login")

    # ---------------------------
    # 📂 4. EXPOSURE SIGNALS
    # ---------------------------
    for item in exposure_data:
        path = item["path"]

        if "wp-" in path:
            add("WordPress", 0.6, "exposure", path)

        if "api" in path:
            add("API Backend", 0.4, "exposure", path)

    # ---------------------------
    # 🧠 5. COMPORTAMIENTO (timing + redirects)
    # ---------------------------
    redirects = response_data.get("redirect_chain", [])
    time_total = response_data.get("time_total", 0)

    if len(redirects) > 1:
        add("CDN / Proxy Layer", 0.6, "behavior", "redirect_chain")

    if time_total > 2.5:
        add("Heavy Backend", 0.4, "behavior", "latency")

    # ---------------------------
    # ⚖️ NORMALIZACIÓN FINAL
    # ---------------------------
    results = {}

    for tech, data in fusion.items():
        raw_score = data["score"]
        evidence_count = len(data["evidence"])

        confidence = min(0.2 + (raw_score * 0.5) + (evidence_count * 0.05), 0.99)

        results[tech] = {
            "confidence": round(confidence, 2),
            "sources": list(data["sources"]),  # 🔥 ya sin duplicados
            "evidence": data["evidence"],      # 🔥 lista completa (no recortada aquí)
            "top_evidence": "\n".join(data["evidence"][:3])  # ✅ mejora aplicada
        }
    
    return results

# ---------------------------
# 🔐 HEADERS INTELIGENTE
# ---------------------------
def analyze_headers(headers):
    score = 0
    insights = []
    h = {k.lower(): str(v).lower() for k, v in headers.items()}

    # ---------------------------
    # 🧠 CONTENT SECURITY POLICY
    # ---------------------------
    csp = h.get("content-security-policy", "")

    if csp:
        csp_score = 0

        if "unsafe-inline" in csp or "unsafe-eval" in csp:
            insights.append("CSP permisivo (unsafe-inline/eval)")
            csp_score += 5
        else:
            csp_score += 20

        if "default-src" in csp:
            csp_score += 5

        if "*" in csp:
            insights.append("CSP demasiado abierto (*)")
            csp_score -= 5

        score += max(csp_score, 0)
    else:
        insights.append("Sin CSP")

    # ---------------------------
    # 🔐 HSTS (más profundo)
    # ---------------------------
    hsts = h.get("strict-transport-security", "")

    if hsts:
        if "max-age" in hsts:
            try:
                max_age = int(hsts.split("max-age=")[1].split(";")[0])

                if max_age >= 31536000:
                    score += 20
                elif max_age >= 86400:
                    score += 10
                    insights.append("HSTS bajo (duración corta)")
                else:
                    score += 5
                    insights.append("HSTS muy bajo")
            except:
                score += 5
        else:
            insights.append("HSTS sin max-age")
            score += 5
    else:
        insights.append("Sin HSTS")

    # ---------------------------
    # 🧪 X-CONTENT-TYPE
    # ---------------------------
    if h.get("x-content-type-options") == "nosniff":
        score += 10
    elif "x-content-type-options" in h:
        score += 5
        insights.append("X-Content-Type no estándar")
    else:
        insights.append("Sin X-Content-Type-Options")

    # ---------------------------
    # 🧠 X-FRAME-OPTIONS
    # ---------------------------
    xfo = h.get("x-frame-options", "")

    if xfo in ["deny", "sameorigin"]:
        score += 10
    elif xfo:
        score += 5
        insights.append("X-Frame-Options débil")
    else:
        insights.append("Sin X-Frame-Options")

    # ---------------------------
    # 🧬 REFERRER POLICY
    # ---------------------------
    ref = h.get("referrer-policy", "")

    if ref:
        if "no-referrer" in ref or "strict-origin" in ref:
            score += 5
        else:
            insights.append("Referrer-Policy débil")
    else:
        insights.append("Sin Referrer-Policy")

    # ---------------------------
    # 🛡️ PERMISOS (FEATURE POLICY)
    # ---------------------------
    perm = h.get("permissions-policy", "")

    if perm:
        score += 5
    else:
        insights.append("Sin Permissions-Policy")

    # ---------------------------
    # 📡 INFO EXPUESTA
    # ---------------------------
    if "server" in h:
        insights.append("Divulgación de servidor (Server header)")

    if "x-powered-by" in h:
        insights.append("Divulgación tecnológica (X-Powered-By)")

    # ---------------------------
    # ⚖️ NORMALIZACIÓN
    # ---------------------------
    return min(score, 100), insights

# ---------------------------
# 🛡️ PERIMETER SIGNALS
# ---------------------------

def detect_perimeter(headers):
    h = {k.lower(): str(v).lower() for k, v in headers.items()}
    signals = []

    # ---------------------------
    # 🧠 REGISTRO INTERNO
    # ---------------------------
    def add(name, confidence):
        signals.append((name, round(confidence, 2)))

    header_blob = " ".join(f"{k}:{v}" for k, v in h.items())

    # ---------------------------
    # ☁️ CLOUDFLARE (multiseñal real)
    # ---------------------------
    cf_hits = sum([
        "cf-ray" in h,
        "cf-cache-status" in h,
        "server" in h and "cloudflare" in h["server"]
    ])

    if cf_hits >= 2:
        add("Cloudflare", 0.95)
    elif cf_hits == 1:
        add("Cloudflare", 0.75)

    # ---------------------------
    # ☁️ AKAMAI
    # ---------------------------
    if any(s in header_blob for s in ["akamai", "akamaighost", "x-akamai"]):
        add("Akamai", 0.9)

    # ---------------------------
    # ☁️ FASTLY
    # ---------------------------
    if "x-served-by" in h and any(x in header_blob for x in ["fastly", "cache"]):
        add("Fastly CDN", 0.85)

    # ---------------------------
    # ☁️ AWS CLOUDFRONT
    # ---------------------------
    if any(k in h for k in ["x-amz-cf-id", "x-amz-cf-pop"]):
        add("AWS CloudFront", 0.9)

    # ---------------------------
    # ☁️ GENERIC CDN (mejor afinado)
    # ---------------------------
    cdn_headers = ["via", "x-cache", "x-cache-hits"]

    cdn_score = sum(1 for hdr in cdn_headers if hdr in h)

    if cdn_score >= 2:
        add("CDN Layer", 0.7)
    elif cdn_score == 1:
        add("CDN Layer", 0.55)

    # ---------------------------
    # 🔁 REVERSE PROXY (más real)
    # ---------------------------
    via = h.get("via", "")

    if via:
        if any(x in via for x in ["proxy", "gateway", "varnish"]):
            add("Reverse Proxy", 0.7)
        else:
            add("Proxy Layer", 0.55)

    # ---------------------------
    # 🛡️ WAF DETECTION (correlacional)
    # ---------------------------
    waf_hits = 0

    waf_patterns = [
        "x-sucuri",
        "x-firewall",
        "x-waf",
        "mod_security",
        "sucuri",
        "cloudflare"
    ]

    for p in waf_patterns:
        if p in header_blob:
            waf_hits += 1

    if waf_hits >= 2:
        add("WAF Layer", 0.85)
    elif waf_hits == 1:
        add("WAF Layer", 0.65)

    # ---------------------------
    # 🧬 CACHE BEHAVIOR (más preciso)
    # ---------------------------
    cache = h.get("cache-control", "")

    if "max-age" in cache:
        if "public" in cache:
            add("Edge Caching", 0.65)
        else:
            add("Cache Layer", 0.5)

    # ---------------------------
    # 🧠 INFERENCIA OCULTA (señales combinadas)
    # ---------------------------
    if "cloudflare" in header_blob and "nginx" in header_blob:
        add("Hidden Backend (behind CDN)", 0.7)

    # ---------------------------
    # ⚖️ LIMPIEZA + PRIORIZACIÓN
    # ---------------------------
    seen = {}
    for name, conf in signals:
        if name not in seen or conf > seen[name]:
            seen[name] = conf

    # ordenar por confianza
    clean = sorted(
        [(k, v) for k, v in seen.items()],
        key=lambda x: x[1],
        reverse=True
    )

    return clean

# ---------------------------
# 🌐 TLS ANALYSIS
# ---------------------------

def tls_analysis(domain):
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = True
        ctx.verify_mode = ssl.CERT_REQUIRED

        with socket.create_connection((domain, 443), timeout=5) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:

                cert = ssock.getpeercert()

                # ===========================
                # 📅 EXPIRACIÓN
                # ===========================
                exp_raw = cert.get("notAfter")
                if not exp_raw:
                    return None

                exp = datetime.strptime(exp_raw, "%b %d %H:%M:%S %Y %Z")
                days = (exp - datetime.utcnow()).days

                # ===========================
                # 🔐 PROTOCOLO
                # ===========================
                protocol = ssock.version() or "unknown"

                # ===========================
                # 🧬 CIPHER
                # ===========================
                cipher = ssock.cipher()
                cipher_name = cipher[0] if cipher else "unknown"

                # ===========================
                # 🧠 ANÁLISIS
                # ===========================
                weak_signals = 0

                if "TLSv1.0" in protocol or "TLSv1.1" in protocol:
                    weak_signals += 2
                elif "TLSv1.2" in protocol:
                    weak_signals += 0.5
                elif "TLSv1.3" in protocol:
                    weak_signals -= 1

                weak_keywords = ["rc4", "des", "3des", "md5", "null", "export"]
                strong_keywords = ["aes", "gcm", "chacha20"]

                if any(w in cipher_name.lower() for w in weak_keywords):
                    weak_signals += 2

                if any(s in cipher_name.lower() for s in strong_keywords):
                    weak_signals -= 0.5

                # ===========================
                # 🎯 CLASIFICACIÓN
                # ===========================
                if days < 0:
                    status = "expired"
                elif days < 15:
                    status = "critical"
                elif days < 45:
                    status = "warning"
                else:
                    status = "ok"

                if weak_signals >= 2:
                    strength = "weak"
                elif weak_signals <= -1:
                    strength = "strong"
                else:
                    strength = "moderate"

                return {
                    "days": max(days, 0),
                    "protocol": protocol,
                    "cipher": cipher_name,
                    "strength": strength,
                    "status": status
                }

    except Exception:
        return None

# ---------------------------
# 🧠 SIGNAL ENTROPY 
# ---------------------------
def signal_entropy(html):
    try:
        blob = html.lower()

        # ---------------------------
        # 🧠 LIMPIEZA BASE
        # ---------------------------
        text = re.sub(r"\s+", "", blob)

        if not text:
            return 0.0

        # ---------------------------
        # 🔬 ENTROPÍA GLOBAL
        # ---------------------------
        freq = Counter(text)
        total = len(text)

        base_entropy = -sum(
            (c/total) * math.log2(c/total)
            for c in freq.values() if c
        )

        # ---------------------------
        # 🧬 ENTROPÍA DE SCRIPTS (JS)
        # ---------------------------
        scripts = re.findall(r"<script.*?>(.*?)</script>", blob, re.DOTALL)
        script_entropy = 0

        if scripts:
            s_text = "".join(scripts)
            s_text = re.sub(r"\s+", "", s_text)

            if s_text:
                sf = Counter(s_text)
                st = len(s_text)

                script_entropy = -sum(
                    (c/st) * math.log2(c/st)
                    for c in sf.values() if c
                )

        # ---------------------------
        # 🧬 ENTROPÍA DE ATRIBUTOS (DOM)
        # ---------------------------
        attrs = re.findall(r"(id|class)=\"(.*?)\"", blob)
        attr_text = "".join(v for _, v in attrs)

        attr_entropy = 0

        if attr_text:
            af = Counter(attr_text)
            at = len(attr_text)

            attr_entropy = -sum(
                (c/at) * math.log2(c/at)
                for c in af.values() if c
            )

        # ---------------------------
        # ⚖️ FUSIÓN INTELIGENTE
        # ---------------------------
        # peso mayor al contenido real
        final_entropy = (
            base_entropy * 0.6 +
            script_entropy * 0.3 +
            attr_entropy * 0.1
        )

        # ---------------------------
        # 🧠 NORMALIZACIÓN SUAVE
        # ---------------------------
        return round(min(final_entropy, 8.0), 2)

    except:
        return 0.0

# ---------------------------
# 🧬 RESPONSE FINGERPRINT
# ---------------------------
def fingerprint(response):
    try:
        headers = response.get("headers", {})
        h = {k.lower(): str(v).lower() for k, v in headers.items()}

        # ===========================
        # 🧠 SEÑALES BASE
        # ===========================
        status = str(response.get("status", ""))
        size = str(response.get("size", "0"))
        time_val = float(response.get("time_total", response.get("time", 0)))

        # ===========================
        # 📡 HEADERS
        # ===========================
        server = h.get("server", "-")
        powered = h.get("x-powered-by", "-")
        content_type = h.get("content-type", "-")
        cache = h.get("cache-control", "-")

        # ===========================
        # 🔁 REDIRECCIONES
        # ===========================
        redirects = response.get("redirect_chain", [])
        redirect_sig = "-".join(map(str, redirects)) if redirects else "none"

        # ===========================
        # 🧬 COMPORTAMIENTO
        # ===========================
        latency_bucket = (
            "fast" if time_val < 0.5 else
            "medium" if time_val < 2 else
            "slow"
        )

        size_int = int(size) if str(size).isdigit() else 0

        size_bucket = (
            "small" if size_int < 50000 else
            "medium" if size_int < 300000 else
            "large"
        )

        # ===========================
        # 🧠 IDENTIDAD (EXPLICABLE)
        # ===========================
        identity_parts = {
            "status": status,
            "server": server,
            "powered": powered,
            "type": content_type,
            "cache": cache,
            "latency": latency_bucket,
            "size": size_bucket,
            "redirects": redirect_sig
        }

        identity_str = "|".join(identity_parts.values())

        # ===========================
        # 🔐 HASH
        # ===========================
        fp_hash = hashlib.sha256(identity_str.encode()).hexdigest()[:20]

        return {
            "hash": fp_hash,
            "identity": identity_str,
            "components": identity_parts
        }

    except Exception as e:
        return {
            "hash": "fingerprint_error",
            "identity": str(e),
            "components": {}
        }
# ---------------------------
# 🧠 CONTEXTUAL DRIFT 
# ---------------------------
def contextual_drift(tech):
    layers = {
        "frontend": {"React", "Vue", "Angular", "React (Next.js)", "Vue (Nuxt)"},
        "backend": {"Laravel", "Django", "PHP"},
        "infra": {"Nginx", "Apache"},
    }

    detected = {k: [] for k in layers}
    unknown = []

    # ---------------------------
    # 🧠 CLASIFICACIÓN
    # ---------------------------
    for t in tech:
        matched = False
        for layer, items in layers.items():
            if t in items:
                detected[layer].append(t)
                matched = True
        if not matched:
            unknown.append(t)

    drift = 0
    complexity = 0
    observations = []

    # ---------------------------
    # ⚖️ DRIFT POR CAPA (más inteligente)
    # ---------------------------
    for layer, items in detected.items():
        count = len(items)

        if count > 1:
            # penalización progresiva (no lineal)
            layer_drift = 8 + (count * 2)
            drift += layer_drift
            complexity += count

            observations.append(
                f"{layer}: múltiples tecnologías ({', '.join(items)})"
            )

    # ---------------------------
    # 🧬 COHERENCIA FRONTEND
    # ---------------------------
    fe = detected["frontend"]

    if "React" in fe and "Vue" in fe:
        drift += 10
        observations.append("mezcla React + Vue (arquitectura inconsistente)")

    if "Angular" in fe and len(fe) > 1:
        drift += 8
        observations.append("Angular combinado con otros frameworks")

    # ---------------------------
    # 🧬 COHERENCIA BACKEND
    # ---------------------------
    be = detected["backend"]

    if len(be) > 1:
        drift += 12
        observations.append("backend múltiple (posible proxying / microservicios)")

    # señal más quirúrgica
    if "Laravel" in be and "Django" in be:
        drift += 10
        observations.append("stack mixto PHP + Python (arquitectura compleja real)")

    # ---------------------------
    # 🧬 INFRA (más real)
    # ---------------------------
    infra = detected["infra"]

    if len(infra) > 1:
        drift += 10
        observations.append("infra múltiple (nginx + apache → posible reverse proxy)")

    # ---------------------------
    # 🧠 INTERACCIÓN ENTRE CAPAS
    # ---------------------------
    active_layers = [k for k, v in detected.items() if v]

    if len(active_layers) >= 3:
        drift += 6
        complexity += 2
        observations.append("stack completo multi-capa (frontend+backend+infra)")

    # ---------------------------
    # 🧬 PATRONES REALES (heurística avanzada)
    # ---------------------------
    # frontend moderno + backend legacy
    if ("React" in fe or "Vue" in fe) and "PHP" in be:
        drift += 6
        observations.append("frontend moderno sobre backend tradicional")

    # SSR frameworks
    if "React (Next.js)" in fe or "Vue (Nuxt)" in fe:
        complexity += 2
        observations.append("uso de SSR framework (mayor complejidad estructural)")

    # ---------------------------
    # 🔍 TECNOLOGÍAS DESCONOCIDAS
    # ---------------------------
    if unknown:
        penalty = min(len(unknown) * 2, 10)
        drift += penalty

        observations.append(
            f"tecnologías no clasificadas ({len(unknown)})"
        )

    # ---------------------------
    # ⚖️ NORMALIZACIÓN INTELIGENTE
    # ---------------------------
    drift = min(drift, 50)
    complexity = min(complexity, 12)

    return drift, complexity, {
        "layers": detected,
        "unknown": unknown,
        "observations": observations
    }

# ---------------------------
# 📡 EXPOSURE
# ---------------------------
COMMON = [
    "/robots.txt",
    "/sitemap.xml",
    "/.well-known/security.txt",
    "/.env",
    "/crossdomain.xml"
]

def exposure(url):
    hs = HumanSession()
    base = url.rstrip("/")

    results = []

    for path in COMMON:
        full_url = base + path

        r = hs.visit(full_url)
        if not r:
            continue

        if r.status_code == 200:
            content = r.text[:5000]  # no necesitas todo

            # ---------------------------
            # 🧠 ANÁLISIS CONTEXTUAL
            # ---------------------------
            signals = []

            # robots → rutas interesantes
            if path == "/robots.txt":
                matches = re.findall(r"Disallow:\s*(.*)", content)
                if matches:
                    signals.append({
                        "type": "hidden_paths",
                        "count": len(matches)
                    })

            # sitemap → volumen
            if path == "/sitemap.xml":
                urls = re.findall(r"<loc>(.*?)</loc>", content)
                signals.append({
                    "type": "url_count",
                    "count": len(urls)
                })

            # security.txt → madurez
            if "contact:" in content.lower():
                signals.append({
                    "type": "security_contact",
                    "present": True
                })

            # posible exposición accidental
            if any(x in content.lower() for x in ["password", "secret", "key"]):
                signals.append({
                    "type": "sensitive_keywords",
                    "risk": "medium"
                })

            # ---------------------------
            # 🧾 NUEVO: DETAILS (🔥 mejora)
            # ---------------------------
            details = []

            for s in signals:
                if s["type"] == "hidden_paths":
                    details.append(f"hidden:{s['count']}")
                elif s["type"] == "url_count":
                    details.append(f"urls:{s['count']}")
                elif s["type"] == "security_contact":
                    details.append("security.txt")
                elif s["type"] == "sensitive_keywords":
                    details.append("sensitive!")

            # ---------------------------
            # 📊 SCORE DE EXPOSICIÓN
            # ---------------------------
            signal_score = len(signals) * 5

            results.append({
                "path": path,
                "status": r.status_code,
                "size": len(r.content),
                "signals": signals,                  # 🔬 completo
                "details": details,                  # ✅ listo para UI
                "details_str": ", ".join(details),   # ✅ directo para print
                "score": signal_score
            })

    return results


async def analyze_js_runtime(url):
    result = {
        "scripts": [],
        "endpoints": [],
        "events": [],
        "storage": {}
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        context = await browser.new_context(
            ignore_https_errors=True,
            java_script_enabled=True
        )

        page = await context.new_page()

        # ===========================
        # 📡 INTERCEPTAR REQUESTS (más limpio)
        # ===========================
        seen_endpoints = set()

        def track_request(req):
            u = req.url
            if u not in seen_endpoints:
                seen_endpoints.add(u)
                result["endpoints"].append(u)

        page.on("request", track_request)

        # ===========================
        # 📥 RESPUESTAS JS + FILTRO REAL
        # ===========================
        seen_scripts = set()

        async def track_response(res):
            try:
                ctype = res.headers.get("content-type", "").lower()
                url_res = res.url

                if (
                    "javascript" in ctype or
                    url_res.endswith(".js")
                ):
                    if url_res not in seen_scripts:
                        seen_scripts.add(url_res)
                        result["scripts"].append(url_res)
            except:
                pass

        page.on("response", lambda res: asyncio.create_task(track_response(res)))

        # ===========================
        # 🧠 HOOK JS AVANZADO
        # ===========================
        await page.add_init_script("""
            (() => {
                window.__tracker = {
                    events: [],
                    endpoints: []
                };

                // -----------------------
                // 🔥 FETCH
                // -----------------------
                const originalFetch = window.fetch;
                window.fetch = function() {
                    try {
                        window.__tracker.events.push("fetch");
                        window.__tracker.endpoints.push(arguments[0]);
                    } catch(e){}
                    return originalFetch.apply(this, arguments);
                };

                // -----------------------
                // 🔥 XHR
                // -----------------------
                const originalOpen = XMLHttpRequest.prototype.open;
                XMLHttpRequest.prototype.open = function(method, url) {
                    try {
                        window.__tracker.events.push("xhr");
                        window.__tracker.endpoints.push(url);
                    } catch(e){}
                    return originalOpen.apply(this, arguments);
                };

                // -----------------------
                // 🔥 WEBSOCKET
                // -----------------------
                const OriginalWS = window.WebSocket;
                window.WebSocket = function(url) {
                    try {
                        window.__tracker.events.push("websocket");
                        window.__tracker.endpoints.push(url);
                    } catch(e){}
                    return new OriginalWS(url);
                };

                // -----------------------
                // 🔥 EVENT LISTENERS
                // -----------------------
                const originalAddEvent = EventTarget.prototype.addEventListener;
                EventTarget.prototype.addEventListener = function(type) {
                    try {
                        window.__tracker.events.push("event:" + type);
                    } catch(e){}
                    return originalAddEvent.apply(this, arguments);
                };

                // -----------------------
                // 🔥 STORAGE HOOK
                // -----------------------
                const originalSetItem = Storage.prototype.setItem;
                Storage.prototype.setItem = function(k, v) {
                    try {
                        window.__tracker.events.push("storage_set");
                    } catch(e){}
                    return originalSetItem.apply(this, arguments);
                };

            })();
        """)

        # ===========================
        # 🚀 NAVEGACIÓN CONTROLADA
        # ===========================
        await page.goto(url, wait_until="networkidle")

        # pequeña espera → captura comportamiento dinámico real
        await page.wait_for_timeout(1500)

        # ===========================
        # 💾 EXTRAER TRACKER
        # ===========================
        tracker = await page.evaluate("window.__tracker || {}")

        result["events"] = list(set(tracker.get("events", [])))

        # endpoints internos JS
        for ep in tracker.get("endpoints", []):
            if ep and ep not in result["endpoints"]:
                result["endpoints"].append(ep)

        # ===========================
        # 💾 STORAGE COMPLETO
        # ===========================
        try:
            storage = await page.evaluate("""
                (() => {
                    let data = {};
                    for (let i = 0; i < localStorage.length; i++) {
                        let k = localStorage.key(i);
                        data[k] = localStorage.getItem(k);
                    }
                    return data;
                })()
            """)
            result["storage"] = storage
        except:
            result["storage"] = {}

        await browser.close()

    return result


def infra_analysis(domain):
    result = {
        "ips": [],
        "asn": "unknown",
        "org": "unknown",
        "country": "unknown",
        "dns": {},
        "subdomains": []
    }

    # ===========================
    # 🌐 DNS RECORDS (limpio + señal real)
    # ===========================
    dns_data = {}

    for rtype in ["A", "AAAA", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, rtype, lifetime=4)
            values = list(set(str(r).strip() for r in answers if r))

            if values:
                dns_data[rtype] = values[:10]
        except:
            continue

    result["dns"] = dns_data

    # ===========================
    # 🌍 IP RESOLUTION (multi-path + robusto)
    # ===========================
    ips = set()

    try:
        ips.update(socket.gethostbyname_ex(domain)[2])
    except:
        pass

    try:
        answers = dns.resolver.resolve(domain, "A", lifetime=4)
        ips.update(str(r) for r in answers)
    except:
        pass

    result["ips"] = list(ips)

    # ===========================
    # 🧠 IP INTEL (más preciso + fallback)
    # ===========================
    if result["ips"]:
        ip = result["ips"][0]

        try:
            r = requests.get(
                f"http://ip-api.com/json/{ip}?fields=status,as,org,country,hosting",
                timeout=5
            ).json()

            if r.get("status") == "success":
                result["asn"] = r.get("as", "unknown")
                result["org"] = r.get("org", "unknown")
                result["country"] = r.get("country", "unknown")

                if r.get("hosting"):
                    result["org"] += " (hosting)"

        except:
            pass

    # ===========================
    # 🔍 SUBDOMAINS (filtrado quirúrgico)
    # ===========================
    subs = set()

    try:
        r = requests.get(
            f"https://crt.sh/?q=%25.{domain}&output=json",
            timeout=8
        )

        if r.status_code == 200:
            data = r.json()

            for entry in data:
                name = entry.get("name_value", "")

                for sub in name.split("\n"):
                    sub = sub.strip().lower()

                    if (
                        sub.endswith(domain)
                        and "*" not in sub
                        and len(sub) < 100
                        and not sub.startswith(".")
                    ):
                        subs.add(sub)

    except:
        pass

    result["subdomains"] = list(subs)[:25]

    # ===========================
    # 🧬 DETECCIÓN WILDCARD DNS
    # ===========================
    try:
        random_sub = "".join(random.choices(string.ascii_lowercase, k=12)) + "." + domain

        wildcard_ips = set()
        try:
            answers = dns.resolver.resolve(random_sub, "A", lifetime=3)
            wildcard_ips.update(str(r) for r in answers)
        except:
            pass

        if wildcard_ips and set(result["ips"]) & wildcard_ips:
            result["org"] += " | wildcard-dns"

    except:
        pass

    # ===========================
    # ⚖️ CORRELACIÓN AVANZADA
    # ===========================
    try:
        # 🌍 Infra distribuida real
        if len(result["ips"]) > 3:
            result["org"] += " | distributed"

        # 🔁 posible balanceo
        if 1 < len(result["ips"]) <= 3:
            result["org"] += " | load-balanced"

        # ☁️ CDN / edge por NS
        ns = " ".join(result["dns"].get("NS", [])).lower()

        cdn_hints = ["cloudflare", "akamai", "fastly", "awsdns", "edge"]

        if any(c in ns for c in cdn_hints):
            result["org"] += " | edge"

        # 🧠 TXT analysis (señales ocultas)
        txt_records = " ".join(result["dns"].get("TXT", [])).lower()

        if "spf" in txt_records:
            result["org"] += " | mail-config"

        if "google-site-verification" in txt_records:
            result["org"] += " | google-linked"

    except:
        pass

    return result

# ---------------------------
# 🧠 FINAL SCORING ENGINE
# ---------------------------
def scoring(header_score, perimeter, tls, exposure, drift, entropy):
    score = header_score

    # ===========================
    # 🛡️ PERÍMETRO
    # ===========================
    if perimeter:
        score += 8

        if len(perimeter) > 1:
            score += 4

    # ===========================
    # 🌐 TLS (🔥 FIX REAL)
    # ===========================
    if isinstance(tls, dict):
        tls_days = tls.get("days", 0)
        strength = tls.get("strength", "unknown")
        status = tls.get("status", "unknown")
    else:
        tls_days = 0
        strength = "unknown"
        status = "unknown"

    # vida del certificado
    if tls_days > 90:
        score += 12
    elif tls_days > 60:
        score += 10
    elif tls_days > 30:
        score += 6
    elif tls_days > 15:
        score += 3
    else:
        score -= 5

    # estado crítico (expirado o casi)
    if status == "expired":
        score -= 15
    elif status == "critical":
        score -= 10

    # fuerza criptográfica
    if strength == "weak":
        score -= 10
    elif strength == "moderate":
        score -= 3
    elif strength == "strong":
        score += 2

    # ===========================
    # 📂 EXPOSURE
    # ===========================
    exp_penalty = 0

    for e in exposure or []:  # 🔥 evita crash si es None
        path = e.get("path", "")
        signals = e.get("signals", [])

        if path in ["/robots.txt", "/sitemap.xml"]:
            exp_penalty += 2
        elif signals:
            exp_penalty += 6
        else:
            exp_penalty += 4

    score -= exp_penalty

    # ===========================
    # 🧩 DRIFT
    # ===========================
    if drift > 25:
        score -= drift * 0.8
    elif drift > 10:
        score -= drift * 0.5
    else:
        score -= drift * 0.3

    # ===========================
    # 🧠 ENTROPY
    # ===========================
    if entropy < 3.5:
        score -= 6
    elif 3.5 <= entropy <= 5.5:
        score += 2
    elif 5.5 < entropy <= 6.5:
        score += 5
    else:
        score += 2

    # ===========================
    # ⚖️ NORMALIZACIÓN
    # ===========================
    return max(min(round(score, 2), 100), 0)
# ---------------------------
# 🚀 ENGINE
# ---------------------------

def analyze(url):
    console.rule("[bold cyan]🧠 Web Intelligence[/bold cyan]")

    data = fetch(url)
    if not data:
        console.print("[bold red]❌ Error en conexión[/bold red]")
        return

    html = data["html"]
    headers = data["headers"]

    # ===========================
    # 🧾 RESUMEN INICIAL
    # ===========================
    status = data.get("status", "N/A")
    time_val = data.get("time_total", 0)  # 🔥 FIX REAL

    summary = (
        f"[green]✔ Status:[/green] {status}\n"
        f"[yellow]⏱ Tiempo:[/yellow] {round(time_val, 2)}s\n"
        f"[cyan]🌐 URL:[/cyan] {url}"
    )

    console.print(Panel(summary, title="📌 Resumen", border_style="cyan"))

    # ===========================
    # 📡 STACK TECNOLÓGICO
    # ===========================
    tech = infer_tech(html, headers)

    table_tech = Table(box=box.ROUNDED)
    table_tech.add_column("Tecnología", style="bold cyan")
    table_tech.add_column("Confianza", justify="center", style="green")
    table_tech.add_column("Evidencia", style="yellow")

    for t, v in sorted(tech.items(), key=lambda x: x[1]["confidence"], reverse=True):
        table_tech.add_row(
            t,
            f"{v['confidence']*100:.0f}%",
            "\n".join(v["evidence"]) if v["evidence"] else "-"
        )

    console.print(Panel(table_tech, title="📡 Stack Tecnológico", border_style="cyan"))

    # ===========================
    # 🔐 HEADERS
    # ===========================
    header_score, insights = analyze_headers(headers)

    header_text = (
        "\n".join(f"[yellow]• {i}[/yellow]" for i in insights)
        if insights else "[green]✔ Configuración sólida[/green]"
    )

    console.print(
        Panel(
            header_text,
            title=f"🔐 Headers Score: [bold]{header_score}[/bold]",
            border_style="blue"
        )
    )

    # ===========================
    # 🛡️ PERÍMETRO
    # ===========================
    perimeter = detect_perimeter(headers)
    if perimeter:
        lines = []

        for name, conf in perimeter:
    
            if conf >= 0.85:
                color = "green"
            elif conf >= 0.65:
                color = "yellow"
            else:
                color = "red"

            # 🔥 barra visual simple
            bar = "█" * int(conf * 10)

        lines.append(
            f"[{color}]• {name}[/{color}] "
            f"[cyan]{conf:.2f}[/cyan] "
            f"[{color}]{bar}[/{color}]"
        )

        p_text = "\n".join(lines)

    else:
        p_text = "[red]No evidente[/red]"

    console.print(Panel(p_text, title="🛡️ Protección Perimetral", border_style="green"))

    # ===========================
    # 🌐 TLS
    # ===========================
    domain = urlparse(url).netloc
    tls = tls_analysis(domain)
    

    if tls:
        color = (
            "green" if tls["status"] == "ok" else
            "yellow" if tls["status"] == "warning" else
            "red"
    )

        tls_text = (
            f"[cyan]Días:[/cyan] {tls['days']}\n"
            f"[blue]Protocolo:[/blue] {tls['protocol']}\n"
            f"[magenta]Cipher:[/magenta] {tls['cipher']}\n"
            f"[yellow]Fuerza:[/yellow] {tls['strength']}"
        )
    else:
        color = "red"
        tls_text = "[red]No disponible[/red]"

    console.print(
        Panel(
            tls_text,
            title="🌐 TLS",
            border_style=color
    )
    )

    # ===========================
    # 📂 SUPERFICIE (🔥 FIX)
    # ===========================
    exp = exposure(url)

    if exp:
        exp_table = Table(box=box.SIMPLE)
        exp_table.add_column("Ruta", style="yellow")
        exp_table.add_column("Detalles", justify="left", style="red")

        for e in exp:
            exp_table.add_row(
                e["path"],
                f"{e['score']} | {e.get('details_str', '')}"
            )

        console.print(Panel(exp_table, title="📂 Superficie Expuesta", border_style="yellow"))
    else:
        console.print(Panel("[green]Superficie mínima[/green]", title="📂 Superficie", border_style="yellow"))

    # ===========================
    # 🧠 SEÑALES AVANZADAS
    # ===========================
    entropy = signal_entropy(html)
    fp = fingerprint(data)

    fp_text = (
        f"[blue]Hash:[/blue] {fp['hash']}\n"
        f"[cyan]Perfil:[/cyan]\n"
        + "\n".join(f"• {k}: {v}" for k, v in fp["components"].items())
    )

    adv = (
       f"[magenta]Entropy:[/magenta] {entropy}\n\n"
       f"{fp_text}"
    )

    console.print(Panel(adv, title="🧠 Señales Avanzadas", border_style="magenta"))

    # ===========================
    # 🧬 FUSIÓN (🔥 FIX REAL)
    # ===========================
    fusion = fusion_engine(html, headers, data, exp)

    fusion_table = Table(box=box.MINIMAL_DOUBLE_HEAD)
    fusion_table.add_column("Tech", style="cyan")
    fusion_table.add_column("Confianza", style="green")
    fusion_table.add_column("Evidencia", style="yellow")

    for t, v in sorted(fusion.items(), key=lambda x: x[1]["confidence"], reverse=True):
        fusion_table.add_row(
            t,
            f"{v['confidence']*100:.0f}%",
            v.get("top_evidence", "-")  # 🔥 USA TU MEJORA
        )

    console.print(Panel(fusion_table, title="🧬 Fusión de Señales", border_style="cyan"))

    # ===========================
    # 🧩 DRIFT (mejor legibilidad)
    # ===========================
  
    try:
        drift, complexity, ctx = contextual_drift(list(tech.keys()))

        layers = ctx.get("layers", {})
        unknown = ctx.get("unknown", [])
        observations = ctx.get("observations", [])

        # ---------------------------
        # 🧱 CAPAS (ordenadas + limpias)
        # ---------------------------
        layer_lines = []
        for layer, items in layers.items():
            if items:
                layer_lines.append(
                    f"[cyan]{layer}:[/cyan] {', '.join(items)}"
                )

            layers_text = "\n".join(layer_lines) if layer_lines else "-"

        # ---------------------------
        # ❓ UNKNOWN
        # ---------------------------
        unknown_text = (
            ", ".join(unknown[:5]) + (" ..." if len(unknown) > 5 else "")
            if unknown else "-"
        )

        # ---------------------------
        # 🧠 OBSERVACIONES (🔥 clave)
        # ---------------------------
        obs_text = "\n".join(
            f"• {o}" for o in observations[:6]
        )   if observations else "-"

        # ---------------------------
        # 🎯 SCORE VISUAL
        # ---------------------------
        if drift > 30:
           drift_color = "red"
        elif drift > 15:
            drift_color = "yellow"
        else:
            drift_color = "green"

        # ---------------------------
        # 🧠 TEXTO FINAL
        # ---------------------------
        drift_text = (
            f"[bold {drift_color}]Drift:[/bold {drift_color}] {drift}/50\n"
            f"[bold]Complexity:[/bold] {complexity}/12\n\n"
            f"[bold magenta]Stack detectado:[/bold magenta]\n{layers_text}\n\n"
            f"[bold white]Unknown:[/bold white] {unknown_text}\n\n"
            f"[bold yellow]Observaciones:[/bold yellow]\n{obs_text}"
        )

    except Exception as e:
        drift_text = f"[red]Error contextual drift:[/red] {e}"

    console.print(
        Panel(
            drift_text,
            title="🧩 Contextual Drift",
            border_style="cyan",
            expand=True  # 🔥 evita cortes
        )
    )
    
    # ===========================
    # ⚙️ JS RUNTIME ANALYSIS
    # ===========================

    try:
        js_data = asyncio.run(analyze_js_runtime(url))

        # ---------------------------
        # 🔍 FORMATEO DETALLADO
        # ---------------------------
        top_scripts = "\n".join(
        f"• {s}" for s in js_data.get("scripts", [])[:5]
        )or "-"

        # filtrar endpoints interesantes (🔥 mejora real)
        interesting_endpoints = [
        e for e in js_data.get("endpoints", [])
        if any(x in e.lower() for x in ["api", "auth", "login", "graphql"])
        ]

        top_endpoints = "\n".join(
        f"• {e}" for e in (interesting_endpoints[:5] or js_data.get("endpoints", [])[:5])
        )or "-"

        top_events = "\n".join(
        f"• {ev}" for ev in js_data.get("events", [])[:10]
        ) or "-"

        storage_items = "\n".join(
        f"• {k}: {str(v)[:40]}"
        for k, v in js_data.get("storage", {}).items()
        ) or "-"

       # ---------------------------
       # 🧠 TEXTO FINAL
       # ---------------------------
        js_text = (
            f"[cyan]Scripts ({len(js_data.get('scripts', []))}):[/cyan]\n{top_scripts}\n\n"
            f"[yellow]Endpoints ({len(js_data.get('endpoints', []))}):[/yellow]\n{top_endpoints}\n\n"
            f"[magenta]Eventos JS ({len(js_data.get('events', []))}):[/magenta]\n{top_events}\n\n"
            f"[green]LocalStorage ({len(js_data.get('storage', {}))}):[/green]\n{storage_items}"
        )

    except Exception as e:
        js_text = f"[red]Error JS analysis:[/red] {e}"

    console.print(
        Panel(js_text, title="⚙️ JavaScript Runtime", border_style="magenta")
    )
    
    # ===========================
    # 🌍 INFRASTRUCTURE ANALYSIS
    # ===========================
    try:
        domain = urlparse(url).netloc
        infra = infra_analysis(domain)

        # ---------------------------
        # 🌐 DNS (bonito + limpio)
        # ---------------------------
        dns_lines = []
        for rtype, values in infra.get("dns", {}).items():
            vals = ", ".join(values[:3])
            dns_lines.append(f"[cyan]{rtype}:[/cyan] {vals}")

        dns_text = "\n".join(dns_lines) if dns_lines else "-"

        # ---------------------------
        # 🌍 IPs
        # ---------------------------
        ip_text = "\n".join(
            f"• {ip}" for ip in infra.get("ips", [])[:5]
        ) or "-"

        # ---------------------------
        # 🔍 SUBDOMINIOS (filtrado útil)
        # ---------------------------
        interesting_subs = [
            s for s in infra.get("subdomains", [])
            if any(x in s for x in ["api", "dev", "staging", "admin", "test"])
        ]

        sub_list = interesting_subs if interesting_subs else infra.get("subdomains", [])

        sub_text = "\n".join(
            f"• {s}" for s in sub_list[:10]
        ) or "-"

        # ---------------------------
        # 🧠 TEXTO FINAL
        # ---------------------------
        infra_text = (
            f"[bold cyan]IP(s):[/bold cyan]\n{ip_text}\n\n"
            f"[bold yellow]ASN / Org:[/bold yellow]\n{infra.get('asn')} \n{infra.get('org')}\n\n"
            f"[bold green]País:[/bold green] {infra.get('country')}\n\n"
            f"[bold magenta]DNS:[/bold magenta]\n{dns_text}\n\n"
            f"[bold white]Subdominios ({len(infra.get('subdomains', []))}):[/bold white]\n{sub_text}"
        )

    except Exception as e:
        infra_text = f"[red]Error infra analysis:[/red] {e}"

    console.print(
        Panel(
            infra_text,
            title="🌍 Infraestructura",
            border_style="blue",
            expand=True  # 🔥 clave para que no se corte
       )
    )
    
    # ===========================
    # 📊 SCORE FINAL
    # ===========================
    final = scoring(header_score, perimeter, tls, exp, drift, entropy)

    color = "green" if final > 80 else "yellow" if final > 50 else "red"

    console.print(
        Panel(
            f"[bold {color}]{final}/100[/bold {color}]",
            title="📊 Índice de Madurez",
            border_style=color
        )
    )

    console.rule("[bold cyan]END REPORT[/bold cyan]")

# ===========================
# 💓 LATIDO DEL SISTEMA
# ===========================
class Heartbeat:
    def __init__(self):
        self.running = True
        self.frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
        self.index = 0

    def pulse(self):
        while self.running:
            self.index = (self.index + 1) % len(self.frames)
            time.sleep(0.08)  # más fluido

    def frame(self):
        return self.frames[self.index]


# ===========================
# 🧠 SISTEMA NEURAL VIVO
# ===========================
class NeuralPulse:
    def __init__(self):
        self.energy = 0
        self.lock = threading.Lock()
        self.thoughts = [
            "sincronizando conciencia...",
            "analizando patrones invisibles...",
            "detectando resonancia...",
            "ajustando frecuencia...",
            "interpretando señales...",
            "explorando superficie lógica...",
            "expandiendo percepción..."
        ]

    def react(self, value):
        with self.lock:
            self.energy += len(value) % 5

    def state(self):
        levels = ["mínima", "estable", "activa", "intensa", "crítica"]
        with self.lock:
            return levels[self.energy % len(levels)]

    def whisper(self):
        if random.random() < 0.35:
            return random.choice(self.thoughts)
        return None


# ===========================
# ✍️ EFECTO ESCRITURA SEGURO
# ===========================
def typewriter(text, delay=0.008):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()


# ===========================
# 🚀 EJECUCIÓN SEGURA
# ===========================
def safe_analyze(target):
    try:
        analyze(target) 
    except KeyboardInterrupt:
        console.print("\n[bold red]⛔ Interrumpido por el usuario[/bold red]")
    except Exception as e:
        console.print(f"\n[bold red]❌ Error:[/bold red] {str(e)}")


# ===========================
# 🧠 RENDER DINÁMICO
# ===========================
def render_header(hb, neural):
    banner = Text()
    banner.append("\n🧠 WEB INTELLIGENCE CORE\n", style="bold cyan")
    banner.append("Sistema de análisis pasivo multidimensional\n", style="dim")
    banner.append("Estado: ", style="white")
    banner.append("ACTIVO\n", style="bold green")
    banner.append("Estado cognitivo: ", style="white")
    banner.append(f"{neural.state()}\n", style="bold magenta")
    banner.append("Frecuencia: ", style="white")
    banner.append(f"{hb.frame()}\n\n", style="bold cyan")

    return Panel(banner, border_style="cyan")


def run():
    hb = Heartbeat()
    neural = NeuralPulse()

    t = threading.Thread(target=hb.pulse, daemon=True)
    t.start()

    console.clear()
    render_perturbador_banner()
    console.print(render_header(hb, neural))
    ghost_message()
    console.print(
        f"[bold blue]{hb.frame()}[/bold blue] "
        "[dim red]>[/dim red] ",
    end=""
    )
    while True:
        try:
            console.print(
                f"[bold magenta]{hb.frame()}[/bold magenta] "
                "[bold cyan]Ingrese objetivo (https://ejemplo.com; [/bold cyan] "
                "[dim](exit para salir):[/dim] ",
                end=""
            )

            target = input().strip()

            # ---------------------------
            # 🚪 SALIDA CONTROLADA
            # ---------------------------
            if target.lower() in ["exit", "quit", "salir"]:
                console.print("\n[bold red]Apagando sistema...[/bold red]")
                break

            if not target:
                continue

            # ---------------------------
            # 🧠 REACCIÓN NEURAL
            # ---------------------------
            neural.react(target)

            # ---------------------------
            # ⚡ EFECTO ACTIVACIÓN
            # ---------------------------
            typewriter("\n[+] Inicializando módulos...")
            time.sleep(0.15)

            thought = neural.whisper()
            if thought:
                console.print(f"[dim cyan]🧠 {thought}[/dim cyan]")

            typewriter("[+] Sincronizando señales...")
            time.sleep(0.15)

            typewriter("[+] Ejecutando análisis...\n")

            # ---------------------------
            # 🔍 EJECUCIÓN
            # ---------------------------
            safe_analyze(target)

            # ---------------------------
            # 🧬 ESTADO FINAL
            # ---------------------------
            console.print(
                f"\n[bold magenta]⚡ Estado del núcleo:[/bold magenta] {neural.state()}"
            )

            console.print("\n" + "-" * 60 + "\n")

        except KeyboardInterrupt:
            console.print("\n[bold red]⛔ Interrupción detectada[/bold red]")
            break

    hb.running = False
    console.print("[dim]Sistema detenido.[/dim]")


    
if __name__ == "__main__":
    run()    