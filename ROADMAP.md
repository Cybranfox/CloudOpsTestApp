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
- [x] Phase 3c — Page transition fade+slide (map→lesson→battle→result→map) (2026-06-01)
- [ ] Phase 3d — Shield pip pop/crack animation on loss/gain
- [ ] Phase 3e — XP counter animates from 0 on progress dashboard load
- [ ] Accessibility: `prefe