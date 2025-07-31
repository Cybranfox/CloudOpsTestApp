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
        },
        {
            "id": 7,
            "title": "Configuration Management",
            "description": "Track and evaluate changes to your AWS resources.",
            "content": (
                "AWS Config provides resource inventory, configuration history and change notifications to help with security and governance. "
                "It records configuration changes and evaluates your resources against compliance rules."
            ),
            "question": "Which AWS service automatically records configuration changes and evaluates compliance?",
            "options": ["AWS Config", "AWS CloudTrail", "Amazon S3", "AWS Shield"],
            "answer": "AWS Config",
            "badge": "Config Pro"
        },
        {
            "id": 8,
            "title": "Systems Manager",
            "description": "Operate your hybrid and AWS environments from a single place.",
            "content": (
                "AWS Systems Manager lets you manage EC2 and on‑premises servers with an agent and IAM role. "
                "State Manager documents define the desired state and help keep instances in a predefined configuration."
            ),
            "question": "Which Systems Manager document defines actions to keep managed instances in a desired state?",
            "options": ["State Manager Command Document", "AWS Config Rule", "CloudFormation Template", "Inspector Assessment Template"],
            "answer": "State Manager Command Document",
            "badge": "SSM Specialist"
        },
        {
            "id": 9,
            "title": "Amazon Inspector",
            "description": "Automated security assessments for EC2 workloads.",
            "content": (
                "Amazon Inspector automatically assesses applications for vulnerabilities. "
                "Amazon Linux AMIs with Inspector include the Inspector agent by default for seamless installation."
            ),
            "question": "Which Amazon Machine Image includes the Amazon Inspector agent by default?",
            "options": ["Amazon Linux AMI with Amazon Inspector", "Amazon Linux 2", "Ubuntu with Inspector", "Red Hat Enterprise Linux"],
            "answer": "Amazon Linux AMI with Amazon Inspector",
            "badge": "Inspector Agent"
        },
        {
            "id": 10,
            "title": "CloudFormation Helpers",
            "description": "Handle deployment success and clean‑up in CloudFormation.",
            "content": (
                "CloudFormation helper scripts signal the status of instance configuration. "
                "Use the cfn-signal helper script to notify CloudFormation when software installation or configuration completes successfully."
            ),
            "question": "Which CloudFormation helper script signals that software configuration is complete?",
            "options": ["cfn-init", "cfn-signal", "cfn-get-metadata", "cfn-hup"],
            "answer": "cfn-signal",
            "badge": "CloudFormation Guru"
        },
        {
            "id": 11,
            "title": "CloudWatch Monitoring",
            "description": "Advanced monitoring and dashboards in CloudWatch.",
            "content": (
                "To view metrics at one‑minute granularity and build dashboards across regions, enable Detailed Monitoring. "
                "Metric math lets you combine multiple metrics into custom expressions."
            ),
            "question": "To view metrics at one‑minute intervals and build cross‑region dashboards, what must you enable?",
            "options": ["Detailed Monitoring", "Basic Monitoring", "X-Ray Tracing", "Config Aggregator"],
            "answer": "Detailed Monitoring",
            "badge": "Monitoring Maven"
        },
        {
            "id": 12,
            "title": "Service Catalog",
            "description": "Centrally manage and distribute approved IT services.",
            "content": (
                "AWS Service Catalog enables administrators to create catalogues of approved products. "
                "It proactively ensures resources are tagged correctly during creation, whereas AWS Config is reactive and checks resources after creation."
            ),
            "question": "Why use AWS Service Catalog instead of AWS Config for tag enforcement during resource creation?",
            "options": [
                "Service Catalog ensures resources are tagged at creation while AWS Config is reactive",
                "Service Catalog provides resource inventory and history",
                "Service Catalog enforces encryption keys for data at rest",
                "Service Catalog monitors metrics across regions"
            ],
            "answer": "Service Catalog ensures resources are tagged at creation while AWS Config is reactive",
            "badge": "Service Catalog Champion"
        },
        {
            "id": 13,
            "title": "Capacity Reservations",
            "description": "Understand On‑Demand Capacity Reservations and billing.",
            "content": (
                "On‑Demand Capacity Reservations let you reserve EC2 capacity in a specific Availability Zone for any duration. "
                "These reservations do not provide billing discounts by themselves; you can combine them with Savings Plans or Reserved Instances to get discounts."
            ),
            "question": "Which statements are true about On‑Demand Capacity Reservations? (Select two)",
            "options": [
                "Capacity Reservations do not offer billing discounts",
                "Capacity Reservations are transferable between AWS accounts",
                "On‑Demand Capacity Reservations require a one‑year or three‑year commitment",
                "On‑Demand Capacity Reservations enable you to reserve capacity for any duration"
            ],
            "answers": ["Capacity Reservations do not offer billing discounts", "On‑Demand Capacity Reservations enable you to reserve capacity for any duration"],
            "multi_select": true,
            "badge": "Capacity Analyst"
        }
    ]