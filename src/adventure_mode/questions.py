"""
Question bank for Adventure Mode battles.  Each function returns a random
question dictionary with a prompt, list of options and the correct answer.

These questions are derived from official AWS documentation, whitepapers
and exam guides.  They cover key concepts for the SysOps Administrator
certification and other AWS domains.

Note: multi‑select questions are currently not used in Adventure Mode but
could be added by returning a list of correct answers and setting a flag.
"""

import random

# EC2 battle questions
_EC2_QUESTIONS = [
    {
        "prompt": "Which EC2 purchase option provides a significant discount when you commit to a one‑year or three‑year term?",
        "options": ["On‑Demand", "Reserved Instances", "Spot Instances", "Savings Plans"],
        "answer": "Reserved Instances",
        "explanation": "Reserved Instances offer up to a 75% discount versus On‑Demand pricing when you commit to a fixed term."
    },
    {
        "prompt": "What is the smallest billing unit of EC2 when using On‑Demand Instances?",
        "options": ["Per second", "Per minute", "Per hour", "Per day"],
        "answer": "Per second",
        "explanation": "On‑Demand Instances are billed per second, with a minimum of 60 seconds."
    },
    {
        "prompt": "Which feature allows you to automatically recover an EC2 instance when a system impairment is detected?",
        "options": ["Auto Scaling", "Instance Status Checks", "Elastic Load Balancing", "CloudWatch Alarms"],
        "answer": "Instance Status Checks",
        "explanation": "CloudWatch Instance Status Checks can be configured to automatically recover an impaired instance."
    }
]

# S3 battle questions
_S3_QUESTIONS = [
    {
        "prompt": "Which S3 feature can automatically transition objects to a different storage class based on rules you define?",
        "options": ["Versioning", "Replication", "Lifecycle Policies", "Event Notifications"],
        "answer": "Lifecycle Policies",
        "explanation": "Lifecycle policies automatically transition objects to different storage classes or expire them according to your rules."
    },
    {
        "prompt": "What is the default number of S3 buckets you can create per AWS account per Region?",
        "options": ["10", "100", "1000", "Unlimited"],
        "answer": "100",  # According to AWS S3 service quotas
        "explanation": "By default you can create up to 100 buckets per AWS account per Region."
    },
    {
        "prompt": "Which S3 storage class is designed for data that is accessed less than once per quarter and has minimum storage duration charges?",
        "options": ["S3 Standard", "S3 One Zone‑IA", "S3 Intelligent‑Tiering", "S3 Glacier Deep Archive"],
        "answer": "S3 Glacier Deep Archive",
        "explanation": "S3 Glacier Deep Archive is the lowest cost storage class designed for long‑term retention and digital preservation of data accessed less than once per year."
    }
]

# Auto Scaling battle questions
_AUTOSCALING_QUESTIONS = [
    {
        "prompt": "Which scaling policy type adjusts the number of EC2 instances to maintain a specific metric such as average CPU utilisation?",
        "options": ["Step Scaling", "Scheduled Scaling", "Target Tracking", "Predictive Scaling"],
        "answer": "Target Tracking",
        "explanation": "Target tracking scaling policies automatically adjust capacity to maintain a target metric (e.g. 50% CPU utilisation)."
    },
    {
        "prompt": "What happens when your Auto Scaling group is set to a desired capacity of 4 instances with a minimum of 2 and a maximum of 6?",
        "options": ["Only 2 instances will run", "Only 6 instances will run", "Exactly 4 instances will run", "Auto Scaling is disabled"],
        "answer": "Exactly 4 instances will run",
        "explanation": "The desired capacity is the number of instances the Auto Scaling group attempts to maintain."
    },
    {
        "prompt": "Which Auto Scaling strategy can help reduce costs by automatically scaling down during low traffic periods?",
        "options": ["Scheduled Scaling", "Predictive Scaling", "Manual Scaling", "Reserve Scaling"],
        "answer": "Scheduled Scaling",
        "explanation": "Scheduled scaling allows you to scale your Auto Scaling group at specified times in anticipation of changes in demand."
    }
]

# Lifecycle boss questions
_LIFECYCLE_QUESTIONS = [
    {
        "prompt": "Which service helps manage the transition of S3 objects between storage classes and supports object expiration?",
        "options": ["Object Lock", "Lifecycle Policies", "Replication", "S3 Select"],
        "answer": "Lifecycle Policies",
        "explanation": "Lifecycle policies manage transitions, versioning and expiration of S3 objects."
    },
    {
        "prompt": "To reduce storage costs, what is the best practice for data that is no longer needed?",
        "options": ["Move to S3 Standard", "Store on EBS", "Delete or archive using lifecycle rules", "Enable cross‑region replication"],
        "answer": "Delete or archive using lifecycle rules",
        "explanation": "Deleting objects or moving them to lower‑cost storage classes through lifecycle rules helps optimise costs."
    }
]

def get_random_ec2_question():
    """Return a random EC2 question."""
    return random.choice(_EC2_QUESTIONS)


def get_random_s3_question():
    """Return a random S3 question."""
    return random.choice(_S3_QUESTIONS)


def get_random_autoscaling_question():
    """Return a random Auto Scaling question."""
    return random.choice(_AUTOSCALING_QUESTIONS)


def get_random_lifecycle_question():
    """Return a random lifecycle boss question."""
    return random.choice(_LIFECYCLE_QUESTIONS)