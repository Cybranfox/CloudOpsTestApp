# Cloud Orbit — Post-Launch Cadence Plan

## Weekly Content Drops (Pearl Abyss live-service model)

### Week 1-4: Stabilisation
- Monitor crash reports (target: >99.5% crash-free)
- Respond to App Store reviews daily
- Fix P0 bugs within 24 hours
- Ship patch releases every Friday

### Weekly: Challenge Rotation
- New daily challenge seed (automatic — date-based)
- Weekly dungeon resets every Monday 00:00 UTC
- Leaderboard snapshot every Sunday 23:59 UTC

### Monthly: Platform Expansions

**Month 1 — Azure Platform (12 lessons)**
- Azure Fundamentals, Compute, Networking, Security
- IDs 501-512 in `azure_data.py`

**Month 2 — GCP Platform (12 lessons)**
- GCP Fundamentals, Compute, Storage, Networking, IAM
- IDs 601-612 in `gcp_data.py`

**Month 3 — Security Specialisation (12 lessons)**
- Cloud security deep-dive across all platforms
- IAM, KMS, secrets management, compliance frameworks
- IDs 701-712 in `security_data.py`

**Month 4 — CI/CD Pipeline Track (12 lessons)**
- GitHub Actions, Jenkins, GitLab CI, ArgoCD
- IDs 801-812 in `cicd_data.py`

### Quarterly: Major Features

**Q3 2026 — Multiplayer Leagues**
- Weekly leaderboards with gem rewards
- Friend challenges (send a 5-question gauntlet to a friend)
- League tiers: Bronze, Silver, Gold, Diamond, Legend

**Q4 2026 — Content Workshop (Valve model)**
- Community-contributed lesson format
- Lesson review + merge pipeline
- Featured community lessons in daily/weekly rotation

**Q1 2027 — Learning Paths 2.0**
- Certification-aligned tracks (AWS SA, CKA, Terraform Associate)
- Progress tracking per certification objective
- Practice exam mode with timed runs

## Support Tiers

| Tier | Response | Channels |
|------|----------|----------|
| Free | Best effort | GitHub Issues |
| Community | < 48 hours | GitHub Discussions |

## Success Metrics (Monthly Review)

| Metric | Target | Review |
|--------|--------|--------|
| Lesson completion rate | >60% | Monthly |
| D1 retention | >40% | Monthly |
| D7 retention | >20% | Monthly |
| Avg session length | 8-12 min | Monthly |
| Crash-free sessions | >99.5% | Weekly |
| App Store rating | >=4.3 | Weekly |

## Release Cadence

- **Patch** (x.y.Z): Bug fixes, weekly or as needed
- **Minor** (x.Y.0): New platform or feature, monthly
- **Major** (Y.0.0): Architecture changes, quarterly
