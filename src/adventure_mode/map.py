"""
Defines the map for the Slay the Spire‑style adventure. Each node includes a type
(battle, event, rest, merchant, boss) and may define a question for battle nodes.
"""

def get_act1_map():
    return [
        {"id": "start", "label": "Start: Cloud Foundations", "type": "start", "children": ["compute", "storage"]},
        {"id": "compute", "label": "Compute Path", "type": "event", "children": ["ec2_battle"]},
        {"id": "storage", "label": "Storage Path", "type": "event", "children": ["s3_challenge"]},
        {"id": "ec2_battle", "label": "EC2 Battle", "type": "battle", "children": ["auto_scaling_boss"],
         "question": {
             "prompt": "Which EC2 purchase option provides a significant discount for a one‑year or three‑year commitment?",
             "options": ["On‑Demand", "Reserved Instances", "Spot Instances", "Savings Plans"],
             "answer": "Reserved Instances"
         },
         "explanation": "Reserved Instances provide up to 75% discount compared to On‑Demand pricing when you commit for a fixed term."},
        {"id": "s3_challenge", "label": "S3 Challenge", "type": "battle", "children": ["lifecycle_boss"],
         "question": {
             "prompt": "What S3 feature can automatically transition objects to cheaper storage classes?",
             "options": ["Versioning", "Replication", "Lifecycle Policies", "Server‑Side Encryption"],
             "answer": "Lifecycle Policies"
         },
         "explanation": "S3 lifecycle policies can automatically transition objects to different storage classes or delete them after a specified time."},
        {"id": "auto_scaling_boss", "label": "Auto Scaling Boss", "type": "boss", "children": ["final_exam"],
         "question": {
             "prompt": "Which scaling policy adjusts the number of EC2 instances based on a target metric such as CPU utilisation?",
             "options": ["Manual Scaling", "Scheduled Scaling", "Step Scaling", "Target Tracking"],
             "answer": "Target Tracking"
         },
         "explanation": "Target Tracking scaling policies adjust capacity to maintain a specified metric (e.g., keep CPU utilisation at 50%)."},
        {"id": "lifecycle_boss", "label": "Lifecycle Policy Boss", "type": "boss", "children": ["final_exam"],
         "question": {
             "prompt": "Which service helps manage S3 object transitions, versioning, and expiration?",
             "options": ["Object Lock", "Lifecycle Policies", "Replication", "Transfer Acceleration"],
             "answer": "Lifecycle Policies"
         },
         "explanation": "Lifecycle policies allow you to manage S3 object transitions and expiration rules at scale."},
        {"id": "final_exam", "label": "Final Exam: SysOps Certification", "type": "final", "children": []}
    ]
