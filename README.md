# AWS Orbit Learning Platform

AWS Orbit is a gamified learning platform designed to take you from AWS beginner to SysOps/CloudOps expert. Inspired by Duolingo, it features micro‑lessons drawn exclusively from official AWS documentation and whitepapers, interactive quizzes, and a friendly alien mascot named **Zap** who guides you on your journey.

## What You’ll Learn

The curriculum is aligned with the AWS Certified SysOps Administrator (Associate) exam and covers domains such as:

- **Monitoring, Logging & Remediation** – Learn to use CloudWatch, CloudTrail and EventBridge to monitor and automate remediation.
- **Reliability & Business Continuity** – Explore auto scaling, high availability and backup strategies:contentReference[oaicite:2]{index=2}.
- **Deployment, Provisioning & Automation** – Master infrastructure as code with CloudFormation:contentReference[oaicite:3]{index=3}.
- **Security & Compliance** – Implement least‑privilege IAM, encryption and auditing practices:contentReference[oaicite:4]{index=4}.
- **Networking & Content Delivery** – Configure VPCs, Route 53 and CloudFront:contentReference[oaicite:5]{index=5}.
- **Cost & Performance Optimization** – Use Cost Explorer and right‑sizing to optimise spend:contentReference[oaicite:6]{index=6}.

Each lesson summarises key concepts from AWS Well‑Architected Framework pillars and official AWS sources, and ends with a quiz to test your knowledge.

## Gamification Features

- **XP & Streaks** – Earn experience points (XP) and maintain daily streaks by completing lessons and quizzes.
- **Energy Shields** – You start with three shields. Wrong quiz answers cost one shield; correct answers restore shields. If you lose all shields, Zap prompts you to review before continuing.
- **Badges** – Unlock badges (e.g. *Monitoring Master*, *Security Sentinel*) when you complete each domain.
- **Adaptive Navigation** – Passing a quiz advances you to the next lesson; incorrect answers let you retry until you’re ready to move on.

## Getting Started

### Prerequisites

- Python 3.8 or later installed on your machine
- `pip` package installer

### Setup

1. **Clone or extract the project** into a directory, then create and activate a virtual environment (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

