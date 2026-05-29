# ☁️ Cloud Orbit — Learn DevOps Through Adventure

> A gamified learning platform that turns cloud and DevOps mastery into an RPG. Battle through real-world scenarios, earn XP, collect relics, and unlock the full stack.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![PWA](https://img.shields.io/badge/PWA-Ready-5A0FC8?logo=pwa&logoColor=white)](https://web.dev/progressive-web-apps/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 🎮 What is Cloud Orbit?

Cloud Orbit is an RPG-style learning platform for cloud engineers, DevOps practitioners, and anyone studying for AWS / Kubernetes / Docker / Ansible certifications. Instead of reading docs, you **battle** through scenario-based challenges guided by **Zap** — your animated AI mascot.

**Inspired by:** Duolingo's streak mechanics, Slay the Spire's relic/energy system, MIMO's track-based progression.

---

## 🚀 Current Features

### 🗺️ Adventure Map
- Duolingo-style zigzag path with colour-coded node states (completed / current / available / locked)
- 6 AWS sectors × 4 battles each = 24 challenges to conquer

### ⚔️ Battle System (Slay the Spire mechanics)
- **Energy Shields** — lose one on a wrong answer, gain one on correct; manage resources carefully
- **Room types** — standard battles, elite challenges, boss fights, each with escalating difficulty
- **Relics** — permanent passive bonuses earned by defeating elites/bosses (Guardian's Shield, CloudWatch Lens, etc.)
- **Potions** — consumable boosts found along the way

### 📊 Progress Dashboard
- **Hero card** — animated SVG XP ring, current level, total XP
- **Streak tracker** — 🔥 day streak with fire indicator
- **Battle statistics** — Slay-the-Spire run-end grid: accuracy, battles won, elites slain, bosses felled
- **Learning Tracks** — MIMO-style per-platform progress bars (AWS active; K8s / Docker / Ansible / Terraform coming)
- **Relics shelf** — hover tooltips on each collected relic
- **Achievements grid** — locked/unlocked states across 8 milestone achievements

### 🔊 Sound System
- Web Audio API synthesiser — no external files needed
- Procedurally generated: correct chime, wrong buzz, shield loss/gain, level-up fanfare, badge ding, click
- Mute toggle (🔊/🔇) in navbar, persists per session

### ⚡ Zap — Your Mascot
- Context-aware speech bubbles (battle stations, encouraging, explaining)
- Animated states driven by `zap_animator.js`

### 📱 Mobile / PWA
- Full PWA manifest + service worker for offline use
- Capacitor config for Android APK builds
- Responsive layout down to 375 px

---

## 🗺️ Platform Roadmap

| Platform | Status | Sectors |
|---|---|---|
| ☁️ **AWS** | ✅ Active — 24 lessons | Compute, Storage, Security, Network, Database, DevOps |
| ⚙️ **Kubernetes** | 🔜 Coming soon | Core Concepts, Workloads, Networking, Security, Helm & GitOps |
| 🐳 **Docker** | 🔜 Coming soon | Basics, Images & Builds, Compose, Networking |
| 🔧 **Ansible** | 🔜 Coming soon | Playbooks, Roles, Inventory, Vault |
| 🏔️ **Terraform** | 🔜 Coming soon | HCL Basics, Providers, State & Backend, Modules |

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python 3.11 · Flask · Jinja2 |
| Frontend | Vanilla JS · CSS3 (dark theme design system) · Web Audio API |
| Data | JSON flat-file progress store (`progress.json`) |
| Mobile | Capacitor (Android APK) |
| PWA | Service Worker · Web App Manifest |

---

## ⚡ Quickstart

```bash
# 1. Clone
git clone https://github.com/Cybranfox/CloudOpsTestApp.git
cd CloudOpsTestApp/AWS_Orbit_RPG

# 2. Install dependencies
pip install flask

# 3. Run
python app.py
# → http://localhost:5001
```

No database, no environment variables, no build step. Works out of the box.

---

## 📁 Project Structure

```
AWS_Orbit_RPG/
├── app.py                  # Flask routes
├── progress.py             # Game state engine (XP, shields, relics, achievements)
├── improved_data.py        # AWS lesson + question bank (24 lessons)
├── platforms_data.py       # Multi-platform registry (AWS/K8s/Docker/Ansible/Terraform)
├── progress.json           # Persisted player state
├── static/
│   ├── styles.css          # Design system (CSS custom properties, dark theme)
│   ├── audio_integration.js # Web Audio synthesiser (all sounds procedural)
│   ├── zap_animator.js     # Mascot animation controller
│   └── sw.js               # Service worker (PWA offline cache)
└── templates/
    ├── base.html                # Nav, scripts, sound toggle
    ├── space_adventure_map.html # Duolingo-style adventure map
    ├── lesson.html              # Pre-battle lesson card
    ├── quiz.html                # Battle/quiz screen with energy shields
    ├── progress_dashboard.html  # Full progress UI (StS + Duolingo inspired)
    ├── reward_screen_orbit.html # Milestone reward screen
    └── badges_cosmic.html       # Badge collection screen
```

---

## 🎯 AWS Content Coverage

Lessons are scenario-based exam-style questions targeting **AWS SysOps** and **Developer Associate** certification topics.

| Sector | Topics Covered |
|---|---|
| ⚡ Compute | CloudWatch + Auto Scaling, Multi-AZ, CodePipeline & Blue/Green, IAM + KMS |
| 💾 Storage | VPC Security, S3 Lifecycle, RDS Multi-AZ, DynamoDB |
| 🛡️ Security | GuardDuty + Security Hub, CloudTrail, Secrets Manager, WAF + Shield |
| 🌐 Network | Transit Gateway, Route 53, CloudFront, Direct Connect |
| 🗄️ Database | Step Functions, Kinesis, ElastiCache, Aurora Serverless |
| 🚀 DevOps | Lambda + SAM, ECS + Fargate, CDK, AWS Organizations |

---

## 🤝 Contributing

Content PRs welcome — especially for the upcoming K8s / Docker / Ansible tracks. See `platforms_data.py` for the sector structure to follow.

---

*© 2025 Cloud Orbit — Master the Cloud Through Adventure*
