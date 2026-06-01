"""
Cloud Orbit — Smoke test suite
Run from repo root while Flask is running on port 5001.
Covers: Phase 3b animations, multi-platform routing (K8s/Docker), import check.
"""
import urllib.request
import sys

PORT = 5001
BASE = f"http://127.0.0.1:{PORT}"


def fetch(path, timeout=5):
    try:
        resp = urllib.request.urlopen(BASE + path, timeout=timeout)
        return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as e:
        return e.code, ""
    except Exception as e:
        return 0, str(e)


# ── SECTION 1: Home / adventure map ──────────────────────────────────────────
status, html = fetch("/")
map_checks = [
    ("GET / → HTTP 200",            status == 200),
    ("nodeEntrance keyframe",        "nodeEntrance" in html),
    ("node-entering class",          "node-entering" in html),
    ("node-visible class",           "node-visible" in html),
    ("title-visible class",          "title-visible" in html),
    ("sector-title transition",      "transition: opacity 0.4s" in html),
    ("animationend handler",         "animationend" in html),
    ("60ms stagger",                 "* 60" in html),
    ("lesson circles present",       "lesson-circle" in html),
    ("Compute Sector present",       "Compute Sector" in html),
    ("no old console.log",           "Minimal Working Duolingo Map" not in html),
    ("page-enter transition CSS",    "pageEnter" in html),
    ("page-exit transition CSS",     "pageExit" in html),
]

# ── SECTION 2: AWS lessons (IDs 1-24) ────────────────────────────────────────
s1, h1 = fetch("/lesson/1")
s24, h24 = fetch("/lesson/24")
aws_checks = [
    ("GET /lesson/1 → HTTP 200",     s1 == 200),
    ("Lesson 1 has title",           "CloudWatch" in h1 or "Lesson" in h1),
    ("GET /lesson/24 → HTTP 200",    s24 == 200),
]

# ── SECTION 3: Kubernetes lessons (IDs 101-120) ───────────────────────────────
s101, h101 = fetch("/lesson/101")
s120, h120 = fetch("/lesson/120")
k8s_checks = [
    ("GET /lesson/101 → HTTP 200",   s101 == 200),
    ("K8s lesson 101 has content",   "Pod" in h101 or "Kubernetes" in h101 or "container" in h101.lower()),
    ("GET /lesson/120 → HTTP 200",   s120 == 200),
    ("K8s lesson 120 has content",   "CIS" in h120 or "audit" in h120.lower() or "cluster" in h120.lower()),
]

# ── SECTION 4: Docker lessons (IDs 201-210) ───────────────────────────────────
s201, h201 = fetch("/lesson/201")
s210, h210 = fetch("/lesson/210")
docker_checks = [
    ("GET /lesson/201 → HTTP 200",   s201 == 200),
    ("Docker lesson 201 has content","Docker" in h201 or "layer" in h201.lower() or "npm" in h201),
    ("GET /lesson/210 → HTTP 200",   s210 == 200),
    ("Docker lesson 210 has content","cap" in h210.lower() or "security" in h210.lower()),
]

# ── SECTION 5: Other routes ───────────────────────────────────────────────────
sp, _  = fetch("/progress")
sb, _  = fetch("/badges")
s404, _ = fetch("/lesson/9999")
other_checks = [
    ("GET /progress → HTTP 200",     sp == 200),
    ("GET /badges → HTTP 200",       sb == 200),
    ("GET /lesson/9999 → HTTP 404",  s404 == 404),
]

# ── SECTION 6: Content schema validation ─────────────────────────────────────
schema_ok = True
schema_errors = []
try:
    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))
    from kubernetes_data import get_lessons as k8s_lessons
    from docker_data import get_lessons as docker_lessons
    from improved_data import get_lessons as aws_lessons

    required = ["id", "title", "question", "options", "answer", "explanation",
                "room_type", "difficulty", "content"]
    for platform, fn in [("AWS", aws_lessons), ("K8s", k8s_lessons), ("Docker", docker_lessons)]:
        for lesson in fn():
            for field in required:
                if field not in lesson:
                    schema_errors.append(f"{platform} lesson {lesson.get('id')}: missing '{field}'")
                    schema_ok = False
            if len(lesson.get("options", [])) != 4:
                schema_errors.append(f"{platform} lesson {lesson['id']}: expected 4 options")
                schema_ok = False
            if lesson.get("answer") not in lesson.get("options", []):
                schema_errors.append(
                    f"{platform} lesson {lesson['id']}: answer not in options"
                )
                schema_ok = False
except Exception as e:
    schema_errors.append(str(e))
    schema_ok = False

schema_checks = [
    ("Content schema valid (all platforms)", schema_ok),
]
if schema_errors:
    for err in schema_errors[:5]:
        print(f"  SCHEMA ERR: {err}")

# ── PRINT RESULTS ─────────────────────────────────────────────────────────────
all_sections = [
    ("Adventure Map (Phase 3b)",  map_checks),
    ("AWS Lessons",               aws_checks),
    ("Kubernetes Lessons",        k8s_checks),
    ("Docker Lessons",            docker_checks),
    ("Other Routes",              other_checks),
    ("Content Schema",            schema_checks),
]

all_pass = True
for section_name, checks in all_sections:
    print(f"\n-- {section_name} --")
    for name, result in checks:
        icon = "PASS" if result else "FAIL"
        print(f"  [{icon}] {name}")
        if not result:
            all_pass = False

print()
print("=" * 40)
print("ALL CHECKS PASSED" if all_pass else "SOME CHECKS FAILED")
print("=" * 40)
input("\nPress Enter to close...")
