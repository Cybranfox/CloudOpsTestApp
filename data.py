# Sample lessons with quiz questions and badge names

def get_lessons():
    """
    Return a list of lesson dictionaries. Each dictionary contains:
      id: Numerical identifier
      title: Short name of the domain
      description: Brief overview
      content: Micro‑lesson summary derived from official AWS sources
      question: Quiz question to test understanding
      options: List of answer options
      answer: Correct answer
      badge: Name of the badge earned when completing this lesson

    These lessons align with the AWS SysOps Administrator exam domains. The
    content summarises best practices from AWS Well‑Architected Framework
    pillars and official documentation【706124378528268†L59-L67】.
    """
    return [
        {
            "id": 1,
            "title": "Monitoring, Logging & Remediation",
            "description": "Configure metrics and alarms with CloudWatch, collect logs with CloudTrail/CloudWatch Logs, and remediate issues using EventBridge and Systems Manager.",
            "content": (
                "Use Amazon CloudWatch to monitor metrics and logs, create alarms to detect anomalies, and automate remediation using EventBridge rules and Systems Manager runbooks. "
                "Enable AWS CloudTrail to capture API calls for auditing and support operational excellence【706124378528268†L59-L67】."
            ),
            "question": "Which AWS service can you use to create alarms based on metrics?",
            "options": ["AWS CloudTrail", "Amazon CloudWatch", "AWS Config", "Amazon Route 53"],
            "answer": "Amazon CloudWatch",
            "badge": "Monitoring Master"
        },
        {
            "id": 2,
            "title": "Reliability & Business Continuity",
            "description": "Discover auto scaling, caching, high availability, and backup strategies to keep your workloads resilient.",
            "content": (
                "Implement AWS Auto Scaling to match resource capacity with demand, use Elastic Load Balancing and multi‑AZ deployments for high availability, and configure automated backups and disaster recovery using snapshots and AWS Backup. "
                "These practices support the reliability pillar of the Well‑Architected Framework【32460178008817†L190-L197】."
            ),
            "question": "What AWS feature automatically adjusts capacity to maintain performance and control costs?",
            "options": ["AWS Auto Scaling", "AWS WAF", "Amazon CloudFront", "AWS Lambda"],
            "answer": "AWS Auto Scaling",
            "badge": "Reliability Champion"
        },
        {
            "id": 3,
            "title": "Deployment, Provisioning & Automation",
            "description": "Use CloudFormation and other automation tools to provision resources efficiently.",
            "content": (
                "Create and manage Amazon Machine Images (AMIs), write AWS CloudFormation templates to provision resources across multiple accounts and regions, and choose deployment strategies (blue/green, rolling, canary) to minimise downtime. "
                "Infrastructure as code and automation are core to operational excellence【149018103694586†L154-L179】."
            ),
            "question": "Which service lets you define your AWS infrastructure as code?",
            "options": ["AWS Auto Scaling", "AWS CloudFormation", "Amazon EC2", "Amazon RDS"],
            "answer": "AWS CloudFormation",
            "badge": "Automation Architect"
        },
        {
            "id": 4,
            "title": "Security & Compliance",
            "description": "Understand IAM, encryption and auditing to secure your workloads.",
            "content": (
                "Implement least‑privilege access with IAM roles and policies, enforce MFA, use AWS Key Management Service (KMS) for encryption at rest, secure secrets with Secrets Manager, and audit access using CloudTrail and IAM Access Analyzer. "
                "These measures align with the security pillar of the Well‑Architected Framework【149018103694586†L154-L179】."
            ),
            "question": "Which service manages encryption keys for your data on AWS?",
            "options": ["AWS Shield", "AWS KMS", "Amazon Inspector", "AWS Trusted Advisor"],
            "answer": "AWS KMS",
            "badge": "Security Sentinel"
        },
        {
            "id": 5,
            "title": "Networking & Content Delivery",
            "description": "Configure VPC networking, Route 53 DNS and content delivery through CloudFront.",
            "content": (
                "Set up Amazon VPC with subnets, route tables, security groups and NAT gateways. Configure Route 53 hosted zones, DNS records and routing policies, and use Amazon CloudFront for efficient content delivery and DDoS protection. "
                "Effective networking enhances performance and reliability【32460178008817†L190-L197】."
            ),
            "question": "What service provides a globally distributed network of edge locations to cache and deliver content?",
            "options": ["Amazon Route 53", "AWS Direct Connect", "Amazon CloudFront", "AWS VPN"],
            "answer": "Amazon CloudFront",
            "badge": "Networking Navigator"
        },
        {
            "id": 6,
            "title": "Cost & Performance Optimization",
            "description": "Manage costs and optimize performance of your AWS resources.",
            "content": (
                "Use Cost Explorer and cost allocation tags to monitor spending, implement auto‑scaling and right‑sizing, use Spot Instances where appropriate, and optimise S3, EBS and RDS performance by monitoring metrics and adjusting configurations. "
                "Cost optimisation is one of the Well‑Architected pillars【149018103694586†L154-L179】."
            ),
            "question": "Which service helps you analyse your AWS costs and usage patterns?",
            "options": ["AWS Auto Scaling", "AWS Cost Explorer", "Amazon S3", "AWS IAM"],
            "answer": "AWS Cost Explorer",
            "badge": "Cost Controller"
        }
    ]