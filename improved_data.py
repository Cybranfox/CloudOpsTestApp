# Enhanced AWS Orbit lessons with Slay the Spire room mechanics and improved exam alignment

def get_lessons():
    """
    Return enhanced lesson dictionaries for AWS SysOps and Developer Associate preparation.
    Each lesson now includes:
    - room_type: Type of Slay the Spire room (battle, elite, event, shop, rest)
    - reward_type: Type of reward/loot gained (knowledge_card, relic, potion, gold)
    - explanation: Detailed explanation for mascot feedback
    - scenario: Real-world scenario context
    - difficulty: Room difficulty (easy, medium, hard, elite, boss)
    """
    return [
        {
            "id": 1,
            "title": "Monitoring, Logging & Remediation",
            "description": "Configure CloudWatch alarms and automate remediation for production systems",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "CloudWatch is your primary monitoring service for AWS resources. Create custom metrics, "
                "set up alarms based on thresholds, and use EventBridge to trigger automated remediation "
                "through Systems Manager runbooks. CloudTrail captures all API calls for security auditing."
            ),
            "scenario": "Your production EC2 instances are experiencing high CPU usage during peak hours. You need to set up automated monitoring and alerting.",
            "question": "A company needs to automatically restart EC2 instances when CPU usage exceeds 90% for 5 consecutive minutes. Which services should be configured together to achieve this?",
            "options": [
                "CloudWatch Metrics + CloudWatch Alarms + EventBridge + Systems Manager",
                "CloudTrail + Config + Lambda + EC2",
                "X-Ray + CloudWatch Logs + SNS + Auto Scaling",
                "Inspector + GuardDuty + Security Hub + Lambda"
            ],
            "answer": "CloudWatch Metrics + CloudWatch Alarms + EventBridge + Systems Manager",
            "explanation": "CloudWatch Metrics track CPU usage, CloudWatch Alarms trigger when thresholds are breached, EventBridge routes the alarm to Systems Manager, which can execute runbooks to restart instances automatically.",
            "badge": "Monitoring Master",
            "loot": {
                "type": "relic",
                "name": "CloudWatch Lens",
                "description": "Provides deeper insight into system performance patterns"
            }
        },
        {
            "id": 2,
            "title": "Reliability & Business Continuity",
            "description": "Design fault-tolerant architectures with multi-AZ deployments and backup strategies",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Build resilient systems using Auto Scaling Groups across multiple AZs, configure "
                "Elastic Load Balancers for health checks, implement automated backups with AWS Backup, "
                "and design disaster recovery strategies using cross-region replication."
            ),
            "scenario": "Your web application must maintain 99.9% uptime even during AZ failures. Design a resilient architecture.",
            "question": "An application running on EC2 instances must remain available even if an entire Availability Zone fails. Which architectural pattern provides the HIGHEST availability?",
            "options": [
                "Single AZ with larger instance types",
                "Multi-AZ deployment with Application Load Balancer and Auto Scaling",
                "Single AZ with manual failover procedures",
                "Multi-region deployment with Route 53 failover only"
            ],
            "answer": "Multi-AZ deployment with Application Load Balancer and Auto Scaling",
            "explanation": "Multi-AZ deployments with ALB automatically route traffic away from failed AZs, while Auto Scaling ensures new instances are launched in healthy AZs to maintain capacity.",
            "badge": "Reliability Champion",
            "loot": {
                "type": "potion",
                "name": "High Availability Elixir",
                "description": "Temporarily boosts understanding of fault-tolerant patterns"
            }
        },
        {
            "id": 3,
            "title": "Deployment, Provisioning & Automation",
            "description": "Master Infrastructure as Code with CloudFormation and deployment strategies",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Use CloudFormation templates to define infrastructure as code, implement blue/green "
                "deployments with CodeDeploy, create CI/CD pipelines with CodePipeline, and manage "
                "application deployments with Elastic Beanstalk."
            ),
            "scenario": "Deploy a microservices application with zero-downtime updates across multiple environments using automated pipelines.",
            "question": "A development team needs to deploy updates to a production web application with zero downtime. The deployment should automatically rollback if health checks fail. Which deployment strategy is MOST appropriate?",
            "options": [
                "Rolling deployment with health checks",
                "Blue/green deployment with health checks and automatic rollback",
                "In-place deployment with manual verification",
                "Canary deployment with 50% traffic split"
            ],
            "answer": "Blue/green deployment with health checks and automatic rollback",
            "explanation": "Blue/green deployments create a complete duplicate environment, allowing instant traffic switching and automatic rollback if health checks fail, ensuring zero downtime.",
            "badge": "Automation Architect",
            "loot": {
                "type": "relic",
                "name": "Deployment Automation Gem",
                "description": "Grants mastery over continuous deployment patterns"
            }
        },
        {
            "id": 4,
            "title": "Security & Compliance",
            "description": "Implement defense-in-depth security using IAM, KMS, and security services",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Design least-privilege IAM policies, encrypt data at rest with KMS, secure secrets "
                "with Secrets Manager, implement WAF for application protection, and use GuardDuty "
                "for threat detection."
            ),
            "scenario": "Secure a multi-tier application handling sensitive customer data with proper encryption and access controls.",
            "question": "A company stores sensitive customer data in S3 and needs to ensure only specific applications can decrypt the data. The encryption keys must be rotated automatically. Which approach provides the BEST security?",
            "options": [
                "S3 server-side encryption with S3-managed keys (SSE-S3)",
                "S3 server-side encryption with KMS keys (SSE-KMS) and IAM policies",
                "Client-side encryption with application-managed keys",
                "S3 server-side encryption with customer-provided keys (SSE-C)"
            ],
            "answer": "S3 server-side encryption with KMS keys (SSE-KMS) and IAM policies",
            "explanation": "SSE-KMS provides fine-grained access control through IAM policies, automatic key rotation, and detailed audit trails through CloudTrail, making it ideal for sensitive data.",
            "badge": "Security Sentinel",
            "loot": {
                "type": "relic",
                "name": "Guardian's Shield",
                "description": "Provides enhanced protection against security vulnerabilities"
            }
        },
        {
            "id": 5,
            "title": "Networking & Content Delivery",
            "description": "Design secure VPC architectures and optimize content delivery",
            "room_type": "battle",
            "difficulty": "medium", 
            "reward_type": "knowledge_card",
            "content": (
                "Configure VPCs with public/private subnets, implement security groups and NACLs, "
                "set up VPC peering and Transit Gateway, configure Route 53 for DNS resolution, "
                "and optimize content delivery with CloudFront."
            ),
            "scenario": "Design a secure network architecture for a web application with database tier isolation and global content delivery.",
            "question": "A web application with a database backend needs to be accessible from the internet while keeping the database completely isolated. Which VPC design is MOST secure?",
            "options": [
                "Single public subnet for both web and database tiers",
                "Public subnet for web tier, private subnet for database tier with NAT Gateway",
                "Private subnets for both tiers with Application Load Balancer in public subnet",
                "Public subnets in multiple AZs with security group restrictions"
            ],
            "answer": "Public subnet for web tier, private subnet for database tier with NAT Gateway",
            "explanation": "This design keeps databases completely isolated in private subnets with no direct internet access, while allowing web servers in public subnets to receive traffic and access the internet through NAT Gateway for updates.",
            "badge": "Networking Navigator",
            "loot": {
                "type": "potion",
                "name": "Network Clarity Potion",
                "description": "Enhances understanding of complex network topologies"
            }
        },
        {
            "id": 6,
            "title": "Cost & Performance Optimization",
            "description": "Optimize AWS costs and improve application performance",
            "room_type": "shop",
            "difficulty": "medium",
            "reward_type": "gold",
            "content": (
                "Use Cost Explorer for spending analysis, implement Reserved Instances and Savings Plans, "
                "configure Auto Scaling for cost efficiency, optimize S3 storage classes, and tune "
                "RDS instances for performance."
            ),
            "scenario": "Reduce infrastructure costs by 30% while maintaining performance for a variable-workload application.",
            "question": "A company's monthly AWS bill shows high costs for EC2 instances that run 24/7 with predictable workloads. Which cost optimization strategy provides the MAXIMUM savings?",
            "options": [
                "Switch to Spot Instances for all workloads",
                "Purchase Reserved Instances for predictable workloads",
                "Implement Auto Scaling to reduce instance count",
                "Move all workloads to Lambda functions"
            ],
            "answer": "Purchase Reserved Instances for predictable workloads",
            "explanation": "Reserved Instances provide up to 75% cost savings for predictable, steady-state workloads compared to On-Demand pricing, making them ideal for 24/7 applications.",
            "badge": "Cost Controller",
            "loot": {
                "type": "gold",
                "name": "Savings Multiplier",
                "description": "Doubles the value of cost optimization insights"
            }
        },
        {
            "id": 7,
            "title": "Developer Tools & CI/CD",
            "description": "Build automated deployment pipelines and manage application lifecycle",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card", 
            "content": (
                "Create CI/CD pipelines with CodePipeline, build applications with CodeBuild, "
                "deploy with CodeDeploy, manage infrastructure with CDK, and monitor deployments "
                "with X-Ray tracing."
            ),
            "scenario": "Implement a fully automated CI/CD pipeline that builds, tests, and deploys a microservices application.",
            "question": "A development team wants to automatically build, test, and deploy their application whenever code is pushed to the main branch. Which AWS services combination provides a complete CI/CD solution?",
            "options": [
                "CodeCommit + CodeBuild + CodeDeploy + CodePipeline",
                "GitHub + Lambda + S3 + CloudFormation", 
                "GitLab + EC2 + Elastic Beanstalk + CloudWatch",
                "Bitbucket + CodeStar + ECS + Route 53"
            ],
            "answer": "CodeCommit + CodeBuild + CodeDeploy + CodePipeline",
            "explanation": "CodePipeline orchestrates the entire workflow, CodeCommit stores source code, CodeBuild compiles and tests, and CodeDeploy handles deployment automation across environments.",
            "badge": "DevOps Master",
            "loot": {
                "type": "relic",
                "name": "Pipeline Automation Crystal",
                "description": "Grants mastery over continuous integration patterns"
            }
        },
        {
            "id": 8,
            "title": "Serverless Development",
            "description": "Build scalable serverless applications with Lambda and API Gateway",
            "room_type": "battle",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Develop Lambda functions with proper error handling, design REST APIs with API Gateway, "
                "implement authentication with Cognito, process events with EventBridge, and manage "
                "state with Step Functions."
            ),
            "scenario": "Build a serverless e-commerce API that handles user authentication, order processing, and payment integration.",
            "question": "A serverless API built with Lambda and API Gateway occasionally times out during peak traffic. The Lambda function processes data from DynamoDB and makes external API calls. What is the MOST likely cause and solution?",
            "options": [
                "Lambda concurrent execution limit - Request limit increase",
                "API Gateway timeout limit - Enable caching to reduce backend calls",
                "DynamoDB throttling - Enable auto-scaling or use on-demand billing",
                "All of the above could be potential causes requiring investigation"
            ],
            "answer": "All of the above could be potential causes requiring investigation",
            "explanation": "Serverless timeouts can result from multiple bottlenecks: Lambda concurrency limits, API Gateway 29-second timeout, or DynamoDB throttling. Proper monitoring with CloudWatch and X-Ray helps identify the root cause.",
            "badge": "Serverless Architect", 
            "loot": {
                "type": "potion",
                "name": "Serverless Scaling Serum",
                "description": "Enhances understanding of auto-scaling serverless patterns"
            }
        },
        {
            "id": 9,
            "title": "Database Management",
            "description": "Design and optimize database solutions for different use cases",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Choose appropriate database services (RDS, DynamoDB, ElastiCache), implement "
                "read replicas for scaling, configure automated backups, design partition keys "
                "for DynamoDB, and optimize query performance."
            ),
            "scenario": "Design a database architecture for a gaming application with millions of users requiring low-latency reads and writes.",
            "question": "A gaming application needs to store user profiles with fast read/write access and leaderboards that are frequently queried. The data access patterns are predictable but vary significantly between game features. Which database strategy is MOST appropriate?",
            "options": [
                "Single RDS instance with read replicas",
                "DynamoDB with GSI for leaderboards + ElastiCache for user profiles",
                "Aurora Serverless with auto-scaling enabled",
                "Multiple DynamoDB tables with optimized partition keys for each access pattern"
            ],
            "answer": "Multiple DynamoDB tables with optimized partition keys for each access pattern",
            "explanation": "DynamoDB excels at gaming workloads with predictable access patterns. Using separate tables optimized for user profiles and leaderboards allows for better partition key design and independent scaling.",
            "badge": "Database Architect",
            "loot": {
                "type": "relic", 
                "name": "Data Optimization Orb",
                "description": "Provides mastery over database performance tuning"
            }
        },
        {
            "id": 10,
            "title": "Container Orchestration",
            "description": "Deploy and manage containerized applications with ECS and EKS",
            "room_type": "boss",
            "difficulty": "boss",
            "reward_type": "legendary_relic",
            "content": (
                "Deploy containers with ECS and Fargate, manage Kubernetes clusters with EKS, "
                "implement service discovery, configure load balancing, handle auto-scaling, "
                "and monitor container performance."
            ),
            "scenario": "Migrate a monolithic application to microservices architecture using containers with proper service mesh and monitoring.",
            "question": "A company is migrating from EC2-based deployments to containers. They need automatic scaling, service discovery, and want to minimize infrastructure management. The development team is familiar with Docker but new to Kubernetes. Which approach is MOST suitable?",
            "options": [
                "EKS with Fargate for serverless Kubernetes",
                "ECS with Fargate and Application Load Balancer",
                "Self-managed Kubernetes on EC2 instances", 
                "Docker Swarm on EC2 with manual load balancing"
            ],
            "answer": "ECS with Fargate and Application Load Balancer",
            "explanation": "ECS with Fargate provides container orchestration without Kubernetes complexity, includes built-in service discovery, integrates with ALB for load balancing, and handles auto-scaling automatically - ideal for teams new to container orchestration.",
            "badge": "Container Master",
            "loot": {
                "type": "legendary_relic",
                "name": "Orchestration Crown",
                "description": "Ultimate mastery over container deployment patterns and microservices architecture"
            }
        }
    ]