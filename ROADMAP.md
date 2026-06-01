# 🚀 Cloud Orbit — 8-Week App Store Roadmap

> Goal: Production-ready iOS + Android release in ~8 weeks.
> All work targets `CloudOpsTestApp/` only. AWS_Orbit_RPG is archived.

---

## 🏢 The Team (GitOps Model)

Each role owns specific files and acceptance criteria. All changes go through Git (feature branches → PR → main). GitGuardian scans every push for secrets.

| Role | Owns |
|---|---|
| **Product Owner** | `ROADMAP.md`, backlog priorities, acceptance criteria |
| **Solutions Architect** | `capacitor.config.json`, CI/CD workflows, API design |
| **UX/UI Designer** | Design system in `styles.css`, animation specs, onboarding flow |
| **Frontend Developer** | Templates, JS animations, PWA |
| **Backend Developer** | `app.py`, `progress.py`, new API endpoints |
| **QA Engineer** | `test_*.py`, regression suite, pre/post push checks |
| **Security Engineer** | GitGuardian config, `.github/workflows/`, secrets audit |
| **Data Engineer** | `improved_data.py`, `kubernetes_data.py`, `docker_data.py`, content pipeline |

---

## 🎮 Design Philosophy

Drawing from the best in the industry:

### Learning Apps
- **Mimo** — Interactive fill-in exercises (not just MCQ), instant in-context feedback,
  AI error explanations, short 2-3 min sessions, clear linear path
- **Duolingo** — Hearts/lives, fire streaks, gem currency, league tables,
  daily XP goals, practice-weak-spots mode, animations on every correct answer

### Games
- **Slay the Spire** — Card drafting between fights, relic synergies that change
  playstyle, multiple viable builds, Ascension levels, seeded daily runs
- **Baldur's Gate 3 (Larian)** — Reward creativity and exploration; no single
  "correct" path; iterative post-launch content; player agency; fuel player
  exploits rather than blocking them ("let them have it, it's awesome")
- **Valve** — Long-tail quality obsession; Workshop/community content model;
  never ship until it feels right
- **Pearl Abyss** — Visual fidelity as a product differentiator; live-service cadence;
  weekly/seasonal content drops keep the world alive

### Cloud Orbit's Formula
`Mimo interactivity + Duolingo streaks/polish + Slay the Spire roguelite depth
+ Larian player agency + Valve quality bar + Pearl Abyss live-service cadence`

---

## 📅 8-Week Sprint Plan

### ✅ Done (Phases 1–3b)
- Full lesson→battle→result flow, energy shields, XP, audio, sound toggle
- Cloud Orbit rebrand, progress dashboard, GitHub Pages landing page
- Zap mascot animated states (thinking/celebrate/hurt)
- Map entrance animations — nodes + sector titles (Phase 3b) ✅ 2026-05-31

---

### 🔄 Week 1 — UI Polish Sprint (Phases 3c–3e)
**Owner: Frontend Developer + UX Designer**

- [x] Phase 3b — Map entrance animations ✅ 2026-05-31
- [ ] Phase 3c — Page transition fade+slide (map→lesson→battle→result→map)
- [ ] Phase 3d — Shield pip pop/crack animation on loss/gain
- [ ] Phase 3e — XP counter animates from 0 on progress dashboard load
- [ ] Accessibility: `prefers-reduced-motion` respected on all animations
- [ ] Mobile audit: all pages 375px-clean, no horizontal overflow

**Acceptance criteria:** Zero console errors on page load. All animations ≤500ms.
Reduced-motion degrades gracefully. All routes HTTP 200.

---

### 🔄 Week 2 — Content Expansion (Phases 4a–4b)
**Owner: Data Engineer**

- [ ] Phase 4a — Kubernetes platform: 20 lessons → `kubernetes_data.py`
  (Core Concepts / Workloads / Networking / Security)
- [ ] Phase 4b — Docker platform: 10 lessons → `docker_data.py`
  (Basics / Images & Builds / Compose / Registry & Security)
- [ ] Multi-platform lesson routing in `app.py` (lesson_id dispatch by range)
- [ ] Adventure map renders platform-specific sectors from `platforms_data.py`
- [ ] Progress dashboard shows per-platform XP rings

**Acceptance criteria:** `/lesson/101` → HTTP 200, K8s lesson renders.
All 30 lessons: 3 questions, correct answer, explanation. CKA/CKAD quality.

---

### 🔄 Week 3 — Content + Onboarding (Phases 4c–4d)
**Owner: Data Engineer + UX Designer**

- [ ] Phase 4c — Ansible platform: 12 lessons → `ansible_data.py`
- [ ] Phase 4d — Terraform platform: 12 lessons → `terraform_data.py`
- [ ] Onboarding flow: platform picker on first launch (Duolingo-style path select)
- [ ] Daily challenge: seeded 5-question daily run, bonus XP (StS daily run model)
- [ ] Practice weak spots: re-queue questions answered incorrectly (Duolingo model)

---

### 🔄 Week 4 — Roguelite Depth (Phase 5)
**Owner: Backend Developer + Frontend Developer**

- [ ] Card system: earn technique cards between battles, play to modify challenge (StS)
- [ ] Active relics: relics affect gameplay (CloudWatch Lens = hint on first wrong answer)
- [ ] Ascension levels: unlocked after platform completion, increases difficulty
- [ ] Weekly challenge dungeon: 5-question gauntlet with leaderboard (Pearl Abyss live model)
- [ ] Gem currency: earned by streaks, spent on shield refills / hints (Duolingo model)
- [ ] Multiple build paths: "SysOps route" vs "Developer route" through AWS content (Larian agency)

---

### 🔄 Week 5 — Mobile / Ionic Build
**Owner: Solutions Architect + Backend Developer**

- [ ] Audit Capacitor config (`appId: com.cloudorbit.app`, splash, icons)
- [ ] Static build pipeline: Frozen-Flask export OR migrate to JSON API + SPA
- [ ] Ionic wrapper: Android + iOS targets
- [ ] Push notifications: streak reminders via Capacitor Local Notifications
- [ ] Offline mode: service worker caches all lesson content
- [ ] Android APK CI: GitHub Actions `build-apk.yml`

---

### 🔄 Week 6 — Quality & Security Sprint
**Owner: QA Engineer + Security Engineer**

- [ ] Regression suite: `tests/test_routes.py` — all 8 routes, HTTP 200, template check
- [ ] Content validation: `tests/test_content.py` — all lessons have required fields
- [ ] GitGuardian: `.gitguardian.yml` policy, confirm scanning active on main
- [ ] OWASP audit: no XSS in Jinja2 templates (`|e` filter on all user input)
- [ ] Lighthouse score ≥90 on mobile
- [ ] 404 + 500 error pages with Zap sad state
- [ ] Privacy Policy + Terms of Service pages (app store requirement)

---

### 🔄 Week 7 — App Store Assets + Beta
**Owner: UX Designer + Product Owner**

- [ ] App icon: 1024×1024 master + all required platform sizes
- [ ] Splash screens: light/dark, all device sizes
- [ ] App Store screenshots: 6.7" iPhone, 12.9" iPad, Android 16:9
- [ ] App Store description, keywords, ratings prompt (post first lesson completion)
- [ ] Beta: TestFlight (iOS) + Firebase App Distribution (Android)
- [ ] Community content model: GitHub Discussions for lesson PRs (Valve Workshop)

---

### 🔄 Week 8 — Launch
**Owner: Product Owner + Solutions Architect**

- [ ] App Store Connect submission (iOS)
- [ ] Google Play Console submission (Android)
- [ ] Landing page updated with app store badges
- [ ] Analytics: Capacitor + Firebase
- [ ] Post-launch cadence plan: weekly content drops, monthly platform additions
- [ ] v1.0 tag on GitHub

---

## 🔁 GitOps Workflow

```
feature/phase-3c-transitions
    → PR to main
    → GitHub Actions: python import check + test suite
    → GitGuardian: secrets scan on push
    → Merge to main
    → Auto-build APK (Week 5+)
    → Deploy web demo to GitHub Pages
```

Branch naming: `feature/phase-Xn-desc`, `fix/desc`, `content/platform-name`

---

## 🧪 Testing Protocol (every push)

1. `python -c "from app import app; print('OK')"` — import check
2. `python test_phase3b.py > test_results.txt 2>&1` — functional checks
3. All new routes: HTTP 200 verified
4. 375px viewport: no horizontal overflow
5. Zero console errors on page load

---

## 📊 App Store Success Metrics

| Metric | Target |
|---|---|
| Lesson completion rate | >60% |
| Day 1 retention | >40% |
| Day 7 retention | >20% |
| Avg session length | 8–12 min |
| Crash-free sessions | >99.5% |
| App Store rating | ≥4.3 ★ |
| Lighthouse mobile | ≥90 |

---

## 🛡️ Security Checklist

- [ ] No API keys / secrets in source code (GitGuardian active)
- [ ] `progress.json` gitignored in production builds
- [ ] All Jinja2 user output escaped with `|e`
- [ ] HTTPS enforced in production
- [ ] Capacitor plugins: principle of least privilege
- [ ] `pip audit` clean on CI

---

*Last updated: 2026-06-01 — Claude Sonnet 4.6 (Lead Developer)*
