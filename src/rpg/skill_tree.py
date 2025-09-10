"""
Defines the skill tree for AWS Orbit RPG edition. Each node represents an AWS domain and
may unlock subsequent abilities. This structure can be expanded to include cost, prerequisites
and reward descriptions.
"""

def get_skill_tree():
    return {
        "cloud_foundations": {
            "label": "Cloud Foundations",
            "unlocked": True,
            "children": ["compute", "storage"],
        },
        "compute": {
            "label": "Compute",
            "unlocked": False,
            "children": ["ec2_mastery"],
        },
        "storage": {
            "label": "Storage",
            "unlocked": False,
            "children": ["s3_expertise"],
        },
        "ec2_mastery": {
            "label": "EC2 Mastery",
            "unlocked": False,
            "children": ["auto_scaling"],
        },
        "s3_expertise": {
            "label": "S3 Expertise",
            "unlocked": False,
            "children": ["lifecycle_policies"],
        },
        "auto_scaling": {
            "label": "Auto Scaling",
            "unlocked": False,
            "children": [],
        },
        "lifecycle_policies": {
            "label": "Lifecycle Policies",
            "unlocked": False,
            "children": [],
        },
    }
