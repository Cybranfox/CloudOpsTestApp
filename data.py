# Sample lessons based on AWS SysOps exam domains
def get_lessons():
    return [
        {
            "id": 1,
            "title": "Monitoring, Logging & Remediation",
            "description": "Learn how to configure metrics and alarms with CloudWatch, collect logs with CloudTrail/CloudWatch Logs, and remediate issues using EventBridge and Systems Manager.",
            "content": "AWS recommends using Amazon CloudWatch to monitor metrics and logs, create alarms to detect anomalies, and automate remediation using EventBridge rules and Systems Manager runbooks. You should also enable AWS CloudTrail to capture API calls for auditing.",
        },
        {
            "id": 2,
            "title": "Reliability & Business Continuity",
            "description": "Discover auto scaling, caching, high availability, and backup strategies to keep your workloads resilient.",
            "content": "Implement AWS Auto Scaling to match resource capacity with demand, use Elastic Load Balancing and multi‑AZ deployments for high availability, and configure automated backups and disaster recovery using snapshots, AWS Backup, and S3 Cross‑Region Replication.",
        },
        {
            "id": 3,
            "title": "Deployment, Provisioning & Automation",
            "description": "Use CloudFormation and other automation tools to provision resources efficiently.",
            "content": "Create and manage Amazon Machine Images (AMIs), write AWS CloudFormation templates to provision resources across multiple accounts and regions, and choose deployment strategies (blue/green, rolling, canary) to minimize downtime.",
        },
        {
            "id": 4,
            "title": "Security & Compliance",
            "description": "Understand IAM, encryption and auditing to secure your workloads.",
            "content": "Implement least-privilege access with IAM roles and policies, enforce MFA, use AWS Key Management Service (KMS) for encryption at rest, secure secrets with Secrets Manager, and audit access using CloudTrail and IAM Access Analyzer.",
        },
        {
            "id": 5,
            "title": "Networking & Content Delivery",
            "description": "Configure VPC networking, Route 53 DNS and content delivery through CloudFront.",
            "content": "Set up Amazon VPC with subnets, route tables, security groups and NAT gateways. Configure Route 53 hosted zones, DNS records and routing policies, and use Amazon CloudFront for efficient content delivery and DDoS protection.",
        },
        {
            "id": 6,
            "title": "Cost & Performance Optimization",
            "description": "Manage costs and optimize performance of your AWS resources.",
            "content": "Use Cost Explorer and cost allocation tags to monitor spending, implement auto-scaling and right-sizing, use Spot Instances where appropriate, and optimize S3, EBS and RDS performance by monitoring metrics and adjusting configurations.",
        },
    ]
