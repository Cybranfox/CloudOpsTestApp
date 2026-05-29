"""
Cloud Orbit — Multi-platform content registry.
Each platform has sectors; each sector maps to lesson IDs in its own data module.
"""

PLATFORMS = [
    {
        "id": "aws",
        "name": "Amazon Web Services",
        "short_name": "AWS",
        "icon": "☁️",
        "color": "#FF9900",
        "color_rgb": "255, 153, 0",
        "description": "Master cloud infrastructure and services on AWS",
        "tagline": "The Cloud Galaxy",
        "status": "active",
        "total_lessons": 24,
        "sectors": [
            {"id": "compute",  "name": "Compute",  "icon": "⚡", "lesson_ids": [1, 2, 3, 4]},
            {"id": "storage",  "name": "Storage",  "icon": "💾", "lesson_ids": [5, 6, 7, 8]},
            {"id": "security", "name": "Security", "icon": "🛡️", "lesson_ids": [9, 10, 11, 12]},
            {"id": "network",  "name": "Network",  "icon": "🌐", "lesson_ids": [13, 14, 15, 16]},
            {"id": "database", "name": "Database", "icon": "🗄️", "lesson_ids": [17, 18, 19, 20]},
            {"id": "devops",   "name": "DevOps",   "icon": "🚀", "lesson_ids": [21, 22, 23, 24]},
        ],
    },
    {
        "id": "kubernetes",
        "name": "Kubernetes",
        "short_name": "K8s",
        "icon": "⚙️",
        "color": "#326CE5",
        "color_rgb": "50, 108, 229",
        "description": "Container orchestration at scale",
        "tagline": "The Orchestration Realm",
        "status": "coming_soon",
        "total_lessons": 0,
        "sectors": [
            {"id": "core",       "name": "Core Concepts", "icon": "🧩", "lesson_ids": []},
            {"id": "workloads",  "name": "Workloads",     "icon": "📦", "lesson_ids": []},
            {"id": "networking", "name": "Networking",    "icon": "🕸️", "lesson_ids": []},
            {"id": "security",   "name": "Security",      "icon": "🔐", "lesson_ids": []},
            {"id": "helm",       "name": "Helm & GitOps", "icon": "⛵", "lesson_ids": []},
        ],
    },
    {
        "id": "docker",
        "name": "Docker",
        "short_name": "Docker",
        "icon": "🐳",
        "color": "#2496ED",
        "color_rgb": "36, 150, 237",
        "description": "Containerize everything — build, ship, run",
        "tagline": "The Container Seas",
        "status": "coming_soon",
        "total_lessons": 0,
        "sectors": [
            {"id": "basics",     "name": "Basics",         "icon": "📦", "lesson_ids": []},
            {"id": "images",     "name": "Images & Builds","icon": "🏗️", "lesson_ids": []},
            {"id": "compose",    "name": "Compose",        "icon": "🔗", "lesson_ids": []},
            {"id": "networking", "name": "Networking",     "icon": "🌐", "lesson_ids": []},
        ],
    },
    {
        "id": "ansible",
        "name": "Ansible",
        "short_name": "Ansible",
        "icon": "🔧",
        "color": "#EE0000",
        "color_rgb": "238, 0, 0",
        "description": "Automate infrastructure — agentless and powerful",
        "tagline": "The Automation Forge",
        "status": "coming_soon",
        "total_lessons": 0,
        "sectors": [
            {"id": "playbooks",  "name": "Playbooks",  "icon": "📋", "lesson_ids": []},
            {"id": "roles",      "name": "Roles",      "icon": "🎭", "lesson_ids": []},
            {"id": "inventory",  "name": "Inventory",  "icon": "📇", "lesson_ids": []},
            {"id": "vault",      "name": "Vault",      "icon": "🔒", "lesson_ids": []},
        ],
    },
    {
        "id": "terraform",
        "name": "Terraform",
        "short_name": "Terraform",
        "icon": "🏔️",
        "color": "#7B42BC",
        "color_rgb": "123, 66, 188",
        "description": "Infrastructure as Code — provision anything",
        "tagline": "The IaC Mountains",
        "status": "coming_soon",
        "total_lessons": 0,
        "sectors": [
            {"id": "basics",    "name": "HCL Basics",     "icon": "📝", "lesson_ids": []},
            {"id": "providers", "name": "Providers",      "icon": "🔌", "lesson_ids": []},
            {"id": "state",     "name": "State & Backend","icon": "💾", "lesson_ids": []},
            {"id": "modules",   "name": "Modules",        "icon": "🧩", "lesson_ids": []},
        ],
    },
]


def get_platforms():
    return PLATFORMS


def get_platform(platform_id):
    return next((p for p in PLATFORMS if p["id"] == platform_id), None)


def get_platform_progress(progress, platform_id):
    """Return completed lesson count and total for a platform."""
    platform = get_platform(platform_id)
    if not platform:
        return 0, 0
    all_ids = [lid for s in platform["sectors"] for lid in s["lesson_ids"]]
    completed = len([lid for lid in all_ids if lid in progress.get("completed_lessons", [])])
    return completed, len(all_ids)
