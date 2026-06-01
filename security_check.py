#!/usr/bin/env python3
"""
security_check.py -- CI gate for Cloud Orbit.

Fails the build (exit code 1) if:
  1. FLASK_DEBUG is set to a truthy value in environment
  2. app.secret_key is hardcoded as a string literal in app.py
  3. app.run(debug=True) is hardcoded in app.py
  4. progress.json is world-writable (Linux/macOS CI)
  5. .env is not listed in .gitignore

Run:  python security_check.py
Exit: 0 = all checks passed, 1 = one or more errors found
"""

import os
import re
import stat
import sys

ERRORS = []
WARNINGS = []

ROOT = os.path.dirname(os.path.abspath(__file__))
APP_PY = os.path.join(ROOT, "app.py")
PROGRESS_JSON = os.path.join(ROOT, "progress.json")
GITIGNORE = os.path.join(ROOT, ".gitignore")
REQUIREMENTS = os.path.join(ROOT, "requirements.txt")


def check_debug_mode():
    """FLASK_DEBUG must not be enabled."""
    flask_debug = os.environ.get("FLASK_DEBUG", "")
    flask_env = os.environ.get("FLASK_ENV", "")

    if flask_debug.lower() in ("1", "true", "yes"):
        ERRORS.append(
            "FAIL [debug-mode]: FLASK_DEBUG is set to a truthy value. "
            "Debug mode exposes the Werkzeug interactive debugger."
        )

    if flask_env == "production" and flask_debug.lower() in ("1", "true"):
        ERRORS.append(
            "FAIL [debug-mode]: FLASK_DEBUG is enabled while FLASK_ENV=production."
        )


def check_secret_key_not_hardcoded():
    """app.secret_key must not be a hardcoded string literal."""
    if not os.path.isfile(APP_PY):
        ERRORS.append(f"FAIL [secret-key]: Cannot find {APP_PY}")
        return

    with open(APP_PY, "r", encoding="utf-8") as f:
        source = f.read()

    # Match: app.secret_key = "anything" or app.secret_key = 'anything'
    pattern_direct = re.compile(
        r"app\.secret_key\s*=\s*[\"'][^\"']{4,}[\"']"
    )
    # Match: "SECRET_KEY": "anything" in a config dict
    pattern_config = re.compile(
        r"['\"]SECRET_KEY['\"]\s*:\s*[\"'][^\"']{4,}[\"']"
    )
    # Match: app.run(..., debug=True, ...)
    pattern_debug_hardcoded = re.compile(
        r"app\.run\s*\([^)]*debug\s*=\s*True[^)]*\)"
    )

    if pattern_direct.search(source):
        ERRORS.append(
            "FAIL [secret-key]: app.secret_key is set to a hardcoded string in app.py. "
            "Use: app.secret_key = os.environ['FLASK_SECRET_KEY']"
        )

    if pattern_config.search(source):
        ERRORS.append(
            "FAIL [secret-key]: SECRET_KEY appears hardcoded in a config dict in app.py."
        )

    if pattern_debug_hardcoded.search(source):
        ERRORS.append(
            "FAIL [debug-hardcoded]: app.run(debug=True) is hardcoded in app.py. "
            "Use: debug = os.environ.get('FLASK_ENV') == 'development'"
        )

    if "os.environ" not in source and "os.getenv" not in source:
        WARNINGS.append(
            "WARN [secret-key]: app.py does not reference os.environ or os.getenv. "
            "Verify FLASK_SECRET_KEY is loaded from the environment."
        )


def check_progress_json_permissions():
    """progress.json must not be world-writable."""
    if not os.path.isfile(PROGRESS_JSON):
        # Not present in CI (it is in .gitignore) -- skip
        return

    file_stat = os.stat(PROGRESS_JSON)
    mode = file_stat.st_mode

    if mode & stat.S_IWOTH:
        ERRORS.append(
            f"FAIL [file-perms]: {PROGRESS_JSON} is world-writable "
            f"(mode: {oct(stat.S_IMODE(mode))}). Run: chmod 640 progress.json"
        )

    if mode & stat.S_IROTH:
        WARNINGS.append(
            f"WARN [file-perms]: {PROGRESS_JSON} is world-readable "
            f"(mode: {oct(stat.S_IMODE(mode))}). Consider: chmod 640 progress.json"
        )


def check_env_in_gitignore():
    """.env must be listed in .gitignore."""
    if not os.path.isfile(GITIGNORE):
        WARNINGS.append("WARN [gitignore]: No .gitignore found.")
        return

    with open(GITIGNORE, "r", encoding="utf-8") as f:
        content = f.read()

    # Accept ".env", ".env.*", "*.env" as sufficient
    has_env_entry = bool(re.search(r"^\.env", content, re.MULTILINE))
    if not has_env_entry:
        ERRORS.append(
            "FAIL [gitignore]: .env is not listed in .gitignore. "
            "Add '.env' to prevent accidental secret commits."
        )


def check_requirements():
    """Warn if key security dependencies are missing."""
    if not os.path.isfile(REQUIREMENTS):
        WARNINGS.append("WARN [requirements]: requirements.txt not found.")
        return

    with open(REQUIREMENTS, "r", encoding="utf-8") as f:
        lines = [l.strip().lower() for l in f if l.strip() and not l.startswith("#")]

    if not any("flask-cors" in l for l in lines):
        WARNINGS.append(
            "WARN [requirements]: flask-cors not in requirements.txt. "
            "Required for Capacitor mobile app CORS."
        )

    if not any("python-dotenv" in l or "dotenv" in l for l in lines):
        WARNINGS.append(
            "WARN [requirements]: python-dotenv not in requirements.txt. "
            "Required to load FLASK_SECRET_KEY from .env."
        )


def main():
    print("=" * 60)
    print("Cloud Orbit -- Security Check")
    print("=" * 60)

    check_debug_mode()
    check_secret_key_not_hardcoded()
    check_progress_json_permissions()
    check_env_in_gitignore()
    check_requirements()

    if WARNINGS:
        print("\nWarnings (non-blocking):")
        for w in WARNINGS:
            print(f"  {w}")

    if ERRORS:
        print("\nErrors (build will FAIL):")
        for e in ERRORS:
            print(f"  {e}")
        print(
            f"\nResult: FAILED  --  {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)"
        )
        sys.exit(1)
    else:
        print(f"\nResult: PASSED  --  0 errors, {len(WARNINGS)} warning(s)")
        sys.exit(0)


if __name__ == "__main__":
    main()
