# ☁️ Cloud Orbit — Learn DevOps Through Adventure

> A gamified learning platform that turns cloud and DevOps mastery into an RPG. Battle through real-world scenarios, earn XP, collect relics, and unlock the full stack. **78 lessons across 5 live platforms.**

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![PWA](https://img.shields.io/badge/PWA-Ready-5A0FC8?logo=pwa&logoColor=white)](https://web.dev/progressive-web-apps/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Release](https://img.shields.io/badge/Release-v1.0_β-7B42BC)](https://github.com/Cybranfox/CloudOpsTestApp/releases)
[![Tests](https://img.shields.io/badge/Tests-86/86-4CAF50)](https://github.com/Cybranfox/CloudOpsTestApp/actions)
[![Android](https://img.shields.io/badge/Android-APK_Available-32b8c6?logo=android)](https://github.com/Cybranfox/CloudOpsTestApp/releases/tag/v1.0)

---

## 🎮 What is Cloud Orbit?

Cloud Orbit is an RPG-style learning platform for cloud engineers, DevOps practitioners, and anyone studying for AWS / Kubernetes / Docker certifications. Instead of reading docs, you **battle** through scenario-based challenges guided by **Zap** — your animated AI mascot.

**Inspired by:** Duolingo (streaks), Slay the Spire (relics/energy), MIMO (interactive), BG3 (player agency), Valve (quality obsession).

---

## 🚀 Current Features

### 🗺️ Adventure Map
- Dynamic platform-driven sectors rendered from `platforms_data.py` — AWS, Kubernetes, Docker
- Colour-coded node states (completed / current / available / locked)
- **Entrance animations** — nodes fade + slide in with spring-easing, staggered 60 ms apart
- **Page transitions** — fade+slide on every route change (map to lesson to quiz to result to map), 300ms enter, 250ms exit
- Sector headers animate in before each sector's nodes

### ⚔️ Battle System (Slay the Spire mechanics)
- **Energy Shields** — displayed as pip icons, lose one on wrong answer, gain one on correct
- **Shield pip animations** (Phase 3d) — `pipPop` burst on gain, `pipCrack` shake on loss
- **Room types** — standard battles, elite challenges, boss fights with escalating difficulty
- **Relics** — permanent passive bonuses (Guardian's Shield, CloudWatch Lens, etc.)
- **Potions** — consumable shield refills

### 📊 Progress Dashboard
- **Hero card** — animated SVG XP ring with 1200ms ease-out count-up from zero (Phase 3e)
- **Streak tracker** — day streak with fire indicator
- **Battle statistics** — accuracy, battles won, elites slain, bosses felled
- **Per-platform progress** — AWS, Kubernetes, Docker progress bars with completion %
- **Relics shelf** — hover tooltips on each collected relic
- **Achievements grid** — 8 milestone achievements with locked/unlocked states

### 🔊 Sound System
- Web Audio API synthesiser — no external files needed
- Procedural: correct chime, wrong buzz, shield loss/gain, level-up fanfare, badge ding, click
- Mute toggle in navbar, audio synced with shield pip animations

### ⚡ Zap — Your Mascot
- Context-aware speech bubbles (battle stations, encouraging, explaining)
- Four animated states: `thinking` (question), `celebrate` (correct), `hurt` (wrong), `idle`
- Quiz-wired CSS animations driven by `zap_animator.js`

### Accessibility
- `prefers-reduced-motion` respected on ALL animations across every page
- Responsive layout down to 375 px — zero horizontal overflow
- Mobile-audited: all pages 375px-clean

### 💎 Roguelite Depth (Week 4)
- **Gem Currency** — Earn gems from correct answers and streaks. Spend on hints (5 gems) and shield refills (10 gems).
- **Technique Cards** — Earn between battles (20-100% chance based on room type). 5 card types: Double XP, Iron Shield, Wisdom Discount, Oracle's Glimpse, Gem Magnet.
- **Active Relics** — CloudWatch Lens reveals hints on wrong answers. Guardian's Shield blocks one energy loss per question.
- **Ascension Levels** — Unlock after platform completion. Higher ascension = less XP, more energy loss (increasing difficulty).
- **Daily Challenge** — Seeded 5-question run. Same questions for all players each day. Determined by date hash.
- **Weekly Dungeon** — 5-question gauntlet with personal best tracking. New dungeon every Monday.
- **Practice Weak Spots** — Re-queue questions answered incorrectly (Duolingo model). Clear them by answering correctly.
- **Build Paths** — Choose SysOps or Developer route through AWS content (Larian agency model). 12 lessons per path.

### Beta Program
- **In-app feedback** — Report bugs directly from the dashboard (links to GitHub Issues)
- **Push notifications** — Streak reminders (6pm daily) and inactive nudges (3 days)
- **Privacy-first** — No accounts, no tracking, no data collection. All progress stored locally.
- **Landing page** — [cybranfox.github.io/CloudOpsTestApp/landing.html](https://cybranfox.github.io/CloudOpsTestApp/landing.html)

---

## 🗺️ Platform Roadmap

| Platform | Status | Lessons | Sectors |
|---|---|---|---|
| AWS | Active | 24 | Compute, Storage, Security, Network, Database, DevOps |
| Kubernetes | Active | 20 | Core Concepts, Workloads, Networking, Security |
| Docker | Active | 10 | Basics, Images & Builds, Compose, Registry & Security |
| Ansible | Week 3 | 12 | Playbooks, Roles, Inventory, Vault |
| Terraform | Week 3 | 12 | HCL Basics, Providers, State & Backend, Modules |

---

## 🛠️ Tech Stack

| Layer | Tech |
|---|---|
| Backend | Python 3.11+ . Flask 3.x . Jinja2 |
| Frontend | Vanilla JS . CSS3 (dark theme design system) . Web Audio API |
| Data | JSON flat-file progress store (`progress.json`) |
| Content | 3 platform modules: `improved_data.py` (AWS), `kubernetes_data.py`, `docker_data.py` |
| Mobile | Capacitor (Android APK) |
| PWA | Service Worker . Web App Manifest |
| CI/CD | GitHub Actions (lint, security scan, build) . GitGuardian secrets detection |

---

## Quickstart

### Android (APK)
1. Download the latest APK from [Releases](https://github.com/Cybranfox/CloudOpsTestApp/releases)
2. Enable "Install from Unknown Sources" in Android Settings
3. Open the APK to install

### Web (Local)
```bash
# 1. Clone
git clone https://github.com/Cybranfox/CloudOpsTestApp.git
cd CloudOpsTestApp

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run
python app.py
# -> http://localhost:5001
```

No database required. Flat-file progress storage. Works out of the box.

---

## 📁 Project Structure

```
CloudOpsTestApp/
├── app.py                   # Flask routes + multi-platform dispatch (ID range routing)
├── progress.py              # Game state engine (XP, shields, relics, achievements)
├── improved_data.py         # AWS lesson bank (24 lessons, IDs 1-24)
├── kubernetes_data.py       # Kubernetes lesson bank (20 lessons, IDs 101-120)
├── docker_data.py           # Docker lesson bank (10 lessons, IDs 201-210)
├── platforms_data.py        # Platform registry (AWS/K8s/Docker/Ansible/Terraform)
├── progress.json            # Persisted player state
├── requirements.txt         # Python dependencies
├── ROADMAP.md               # 8-week sprint plan
├── static/
│   ├── styles.css           # Design system (CSS custom properties, dark theme)
│   ├── audio_integration.js # Web Audio synthesiser (all sounds procedural)
│   ├── zap_animator.js      # Mascot animation controller
│   ├── space_adventure_enhanced.js  # Map interaction logic
│   ├── sw.js                # Service worker (PWA offline cache)
│   └── manifest.json        # PWA manifest
├── templates/
│   ├── base.html                 # Nav, scripts, sound toggle, page transitions
│   ├── space_adventure_map.html  # Dynamic platform-driven adventure map
│   ├── lesson.html               # Pre-battle lesson card + page transitions
│   ├── quiz.html                 # Battle screen + shield pip animations (Phase 3d)
│   ├── progress_dashboard.html   # Full progress UI + XP counter animation (Phase 3e)
│   ├── reward_screen_orbit.html  # Milestone reward screen
│   └── badges_cosmic.html        # Badge collection + filter system
└── .github/
    └── workflows/
        └── ci-cd.yml        # CI/CD pipeline (lint, security, build)
```

---

## Content Coverage

All lessons are scenario-based, exam-quality questions. Each includes: scenario setup, question, 4 options, correct answer, detailed explanation, badge, and loot.

### AWS (IDs 1-24)
| Sector | Topics |
|---|---|
| Compute | CloudWatch + Auto Scaling, Multi-AZ, CodePipeline & Blue/Green, IAM + KMS |
| Storage | VPC Security, S3 Lifecycle, RDS Multi-AZ, DynamoDB |
| Security | GuardDuty + Security Hub, CloudTrail, Secrets Manager, WAF + Shield |
| Network | Transit Gateway, Route 53, CloudFront, Direct Connect |
| Database | Step Functions, Kinesis, ElastiCache, Aurora Serverless |
| DevOps | Lambda + SAM, ECS + Fargate, CDK, AWS Organizations |

### Kubernetes (IDs 101-120)
| Sector | Topics |
|---|---|
| Core Concepts | Pods & Sidecar Patterns, Deployments & Rolling Updates, Services, ConfigMaps & Secrets, Namespaces & Resource Quotas |
| Workloads | DaemonSets, StatefulSets, HPA & KEDA, Jobs & CronJobs, Resource Requests & QoS |
| Networking | Ingress & TLS, NetworkPolicy (Zero-Trust), CoreDNS & Service Discovery |
| Security | RBAC, IRSA & Pod Identity, PodSecurityContext, OPA Gatekeeper, CIS Benchmarks |

### Docker (IDs 201-210)
| Sector | Topics |
|---|---|
| Basics | Dockerfile Best Practices & Layer Caching, Multi-Stage Builds, Container Security (Non-Root) |
| Compose | Service Dependencies & Health Checks, Volumes & Bind Mounts, Networking & Service Discovery, Environment Variables |
| Registry & Security | Image Scanning & CVE Remediation, Private Registry & Image Promotion, Runtime Defences |

---

## Contributing

Content PRs welcome — especially for the upcoming Ansible and Terraform tracks. See `platforms_data.py` for the sector structure and `kubernetes_data.py` for the lesson format to follow.

---

*Copyright 2026 Cloud Orbit — Master the Cloud Through Adventure*
