# Cloud Orbit — Quickstart Guide

## Which path?

| You want to... | Go to |
|----------------|-------|
| Install on Android | [Android User](#android-user) |
| Play in browser | [Web User](#web-user) |
| Contribute code | [Developer](#developer) |
| Build the APK | [Build APK](#build-apk) |

---

## Android User

1. Go to [Releases](https://github.com/Cybranfox/CloudOpsTestApp/releases)
2. Download the latest `cloud-orbit-v1.0-debug.apk`
3. On your Android device: **Settings > Security > Install Unknown Apps** — enable for your browser or file manager
4. Open the downloaded APK to install
5. Launch **Cloud Orbit** from your app drawer

**No account needed. No internet needed after install. All progress stays on your device.**

---

## Web User

Visit the landing page: [cybranfox.github.io/CloudOpsTestApp/landing.html](https://cybranfox.github.io/CloudOpsTestApp/landing.html)

Or run locally:

```bash
git clone https://github.com/Cybranfox/CloudOpsTestApp.git
cd CloudOpsTestApp
pip install -r requirements.txt
python app.py
# Open http://localhost:5001
```

---

## Developer

### Prerequisites
- Python 3.11+
- Node.js 20+ (for APK builds)
- Git

### Setup
```bash
git clone https://github.com/Cybranfox/CloudOpsTestApp.git
cd CloudOpsTestApp
pip install -r requirements.txt
python app.py
```

### Run Tests
```bash
# All tests (86 tests, ~0.3s)
python -m pytest tests/ -q

# Specific test file
python -m pytest tests/test_routes.py -v

# With coverage
pip install pytest-cov
python -m pytest tests/ --cov=. --cov-report=term-missing
```

### Lint & Format
```bash
# Auto-format all Python files
pip install black
black *.py --line-length 88

# Check linting
pip install flake8
flake8 *.py --max-line-length=88 --extend-ignore=E203,W503,E501,E731,E741

# Security scan
python security_check.py
```

### Static Build (for Capacitor)
```bash
python freeze.py
# Output: dist/ directory with all 78 lessons rendered as static HTML
```

### Project Structure
```
CloudOpsTestApp/
├── app.py                   # Flask routes (multi-platform dispatch)
├── progress.py              # Game engine (XP, shields, cards, relics, gems)
├── improved_data.py         # AWS lesson bank (24 lessons)
├── kubernetes_data.py       # K8s lesson bank (20 lessons)
├── docker_data.py           # Docker lesson bank (10 lessons)
├── ansible_data.py          # Ansible lesson bank (12 lessons)
├── terraform_data.py        # Terraform lesson bank (12 lessons)
├── platforms_data.py        # Platform definitions + lesson IDs
├── freeze.py                # Frozen-Flask static build
├── tests/
│   ├── test_routes.py       # Route + content quality tests
│   └── test_app.py          # Template + feature verification tests
├── static/
│   ├── styles.css           # Design system
│   ├── zap_animator.js      # Mascot animation controller
│   ├── audio_integration.js # Web Audio synthesiser
│   ├── notifications.js     # Capacitor push notifications
│   └── sw.js                # PWA service worker
├── templates/               # 15 Jinja2 templates
├── .github/workflows/
│   ├── ci-cd.yml            # Main CI (lint, test, security scan)
│   └── build-apk.yml        # Android APK build
└── ROADMAP.md               # 8-week sprint plan
```

---

## Build APK

### Option 1: GitHub Actions (recommended)
1. Go to [Actions > Build Android APK](https://github.com/Cybranfox/CloudOpsTestApp/actions/workflows/build-apk.yml)
2. Click **Run workflow** > **Run workflow**
3. Wait ~2 minutes
4. Download the APK artifact

### Option 2: Local build
```bash
# Prerequisites: Android SDK, Java 17, Node.js 20+
npm install                     # Install Capacitor + plugins
python freeze.py                # Build static dist/
npx cap init "Cloud Orbit" "com.cloudorbit.app" --web-dir dist
npx cap add android
npx cap sync android
cd android && ./gradlew assembleDebug
# APK at: android/app/build/outputs/apk/debug/app-debug.apk
```

---

## Troubleshooting

### `ModuleNotFoundError: No module named 'dotenv'`
```bash
pip install -r requirements.txt
```

### `Address already in use` (port 5001)
```bash
# Kill stale Flask processes
taskkill /F /IM python.exe   # Windows
kill $(lsof -t -i:5001)       # macOS/Linux
```

### Tests fail with 302 instead of 200
Normal — the app redirects new players to `/onboarding`. Reset progress:
```bash
cp progress.example.json progress.json
```

### APK build fails with `npm ci` error
The workflow uses `npm install` (not `npm ci`). If running locally, use `npm install`.

---

## Contributing

1. Fork the repo
2. Create a feature branch: `feature/your-feature`
3. Write tests for your changes
4. Run `python -m pytest tests/ -q` — all 86 must pass
5. Run `black *.py --line-length 88` on changed files
6. Open a PR against `main`

Content PRs (new lessons, platforms, questions) are especially welcome. See `kubernetes_data.py` for the lesson format.

[Full roadmap](ROADMAP.md) · [Report a bug](https://github.com/Cybranfox/CloudOpsTestApp/issues) · [Privacy Policy](/privacy) · [Terms](/terms)
