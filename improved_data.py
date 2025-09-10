# Enhanced AWS Orbit lessons with comprehensive exam questions based on official AWS documentation


def get_lessons():
    """
    Return enhanced lesson dictionaries for AWS SysOps and Developer Associate preparation.
    All questions are based on official AWS documentation and exam patterns.
    """
    return [
        {
            "id": 1,
            "title": "CloudWatch Monitoring & Alarms",
            "description": "Master CloudWatch metrics, alarms, and automated remediation",
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
                "Inspector + GuardDuty + Security Hub + Lambda",
            ],
            "answer": "CloudWatch Metrics + CloudWatch Alarms + EventBridge + Systems Manager",
            "explanation": "CloudWatch Metrics track CPU usage, CloudWatch Alarms trigger when thresholds are breached, EventBridge routes the alarm to Systems Manager, which can execute runbooks to restart instances automatically.",
            "badge": "Monitoring Master",
            "loot": {
                "type": "relic",
                "name": "CloudWatch Lens",
                "description": "Provides deeper insight into system performance patterns",
            },
        },
        {
            "id": 2,
            "title": "Multi-AZ Deployments & Auto Scaling",
            "description": "Design fault-tolerant architectures with high availability",
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
                "Single AZ with larger instance types and enhanced networking",
                "Multi-AZ deployment with Application Load Balancer and Auto Scaling",
                "Single AZ with manual failover procedures and standby instances",
                "Multi-region deployment with Route 53 failover routing only",
            ],
            "answer": "Multi-AZ deployment with Application Load Balancer and Auto Scaling",
            "explanation": "Multi-AZ deployments with ALB automatically route traffic away from failed AZs, while Auto Scaling ensures new instances are launched in healthy AZs to maintain capacity and availability.",
            "badge": "Reliability Champion",
            "loot": {
                "type": "potion",
                "name": "High Availability Elixir",
                "description": "Temporarily boosts understanding of fault-tolerant patterns",
            },
        },
        {
            "id": 3,
            "title": "CodePipeline & Blue/Green Deployments",
            "description": "Master CI/CD pipelines and zero-downtime deployment strategies",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Use CloudFormation templates to define infrastructure as code, implement blue/green "
                "deployments with CodeDeploy, create CI/CD pipelines with CodePipeline, and manage "
                "application deployments with Elastic Beanstalk for automatic scaling and monitoring."
            ),
            "scenario": "Deploy a microservices application with zero-downtime updates across multiple environments using automated pipelines.",
            "question": "A development team needs to deploy updates to a production web application with zero downtime. The deployment should automatically rollback if health checks fail. Which deployment strategy is MOST appropriate?",
            "options": [
                "Rolling deployment with health checks and gradual traffic shifting",
                "Blue/green deployment with health checks and automatic rollback",
                "In-place deployment with manual verification steps",
                "Canary deployment with 10% traffic split for 24 hours",
            ],
            "answer": "Blue/green deployment with health checks and automatic rollback",
            "explanation": "Blue/green deployments create a complete duplicate environment, allowing instant traffic switching and immediate automatic rollback if health checks fail, ensuring zero downtime and maximum safety.",
            "badge": "Automation Architect",
            "loot": {
                "type": "relic",
                "name": "Deployment Automation Gem",
                "description": "Grants mastery over continuous deployment patterns",
            },
        },
        {
            "id": 4,
            "title": "IAM Policies & KMS Encryption",
            "description": "Implement defense-in-depth security using IAM, KMS, and security services",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Design least-privilege IAM policies using conditions and resource-based permissions, "
                "encrypt data at rest with KMS customer-managed keys, secure secrets with Secrets Manager, "
                "implement WAF for application protection, and use GuardDuty for threat detection."
            ),
            "scenario": "Secure a multi-tier application handling sensitive customer data with proper encryption and access controls.",
            "question": "A company stores sensitive customer data in S3 and needs to ensure only specific applications can decrypt the data. The encryption keys must be rotated automatically and provide detailed audit trails. Which approach provides the BEST security?",
            "options": [
                "S3 server-side encryption with S3-managed keys (SSE-S3)",
                "S3 server-side encryption with KMS customer-managed keys (SSE-KMS) and IAM policies",
                "Client-side encryption with application-managed keys stored in Systems Manager",
                "S3 server-side encryption with customer-provided keys (SSE-C) rotated monthly",
            ],
            "answer": "S3 server-side encryption with KMS customer-managed keys (SSE-KMS) and IAM policies",
            "explanation": "SSE-KMS with customer-managed keys provides fine-grained access control through IAM policies, automatic key rotation, detailed audit trails through CloudTrail, and centralized key management.",
            "badge": "Security Sentinel",
            "loot": {
                "type": "relic",
                "name": "Guardian's Shield",
                "description": "Provides enhanced protection against security vulnerabilities",
            },
        },
        {
            "id": 5,
            "title": "VPC Security & Network Design",
            "description": "Design secure VPC architectures with proper network segmentation",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Configure VPCs with public/private subnets across multiple AZs, implement security groups "
                "and NACLs for layered security, set up VPC peering and Transit Gateway for connectivity, "
                "configure Route 53 for DNS resolution, and optimize content delivery with CloudFront."
            ),
            "scenario": "Design a secure network architecture for a web application with database tier isolation and global content delivery.",
            "question": "A web application with a database backend needs to be accessible from the internet while keeping the database completely isolated. Which VPC design is MOST secure?",
            "options": [
                "Single public subnet for both web and database tiers with security group rules",
                "Public subnet for web tier, private subnet for database tier with NAT Gateway",
                "Private subnets for both tiers with Application Load Balancer in public subnet",
                "Public subnets in multiple AZs with restrictive Network ACLs only",
            ],
            "answer": "Public subnet for web tier, private subnet for database tier with NAT Gateway",
            "explanation": "This design keeps databases completely isolated in private subnets with no direct internet access, while allowing web servers in public subnets to receive traffic and access the internet through NAT Gateway for updates.",
            "badge": "Networking Navigator",
            "loot": {
                "type": "potion",
                "name": "Network Clarity Potion",
                "description": "Enhances understanding of complex network topologies",
            },
        },
        {
            "id": 6,
            "title": "Cost Optimization & Reserved Instances",
            "description": "Optimize AWS costs using Reserved Instances, Spot Instances, and Cost Explorer",
            "room_type": "shop",
            "difficulty": "medium",
            "reward_type": "gold",
            "content": (
                "Use Cost Explorer for detailed spending analysis, implement Reserved Instances and Savings Plans "
                "for predictable workloads, leverage Spot Instances for fault-tolerant applications, configure "
                "Auto Scaling for cost efficiency, and optimize S3 storage classes with lifecycle policies."
            ),
            "scenario": "Reduce infrastructure costs by 40% while maintaining performance for a variable-workload application.",
            "question": "A company's monthly AWS bill shows high costs for EC2 instances that run 24/7 with predictable workloads, plus batch processing jobs that can tolerate interruptions. Which combination provides MAXIMUM savings?",
            "options": [
                "Reserved Instances for 24/7 workloads + Spot Instances for batch processing",
                "Spot Instances for all workloads with automatic failover mechanisms",
                "Savings Plans for all EC2 usage with flexible instance family selection",
                "On-Demand instances with aggressive Auto Scaling policies",
            ],
            "answer": "Reserved Instances for 24/7 workloads + Spot Instances for batch processing",
            "explanation": "Reserved Instances provide up to 75% savings for predictable 24/7 workloads, while Spot Instances offer up to 90% savings for fault-tolerant batch processing, maximizing cost optimization.",
            "badge": "Cost Controller",
            "loot": {
                "type": "gold",
                "name": "Savings Multiplier",
                "description": "Doubles the value of cost optimization insights",
            },
        },
        {
            "id": 7,
            "title": "Lambda Functions & API Gateway",
            "description": "Build scalable serverless applications with proper error handling",
            "room_type": "battle",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Develop Lambda functions with proper error handling and dead letter queues, design REST APIs "
                "with API Gateway including throttling and caching, implement authentication with Cognito, "
                "process events with EventBridge, and manage complex workflows with Step Functions."
            ),
            "scenario": "Build a serverless e-commerce API that handles user authentication, order processing, and payment integration with automatic scaling.",
            "question": "A serverless API built with Lambda and API Gateway occasionally times out during peak traffic. The Lambda function processes data from DynamoDB and makes external API calls. What is the MOST comprehensive solution?",
            "options": [
                "Increase Lambda memory allocation and timeout settings only",
                "Enable API Gateway caching and implement Lambda reserved concurrency",
                "Enable DynamoDB auto-scaling and implement exponential backoff with jitter",
                "Implement all: API Gateway caching, Lambda reserved concurrency, DynamoDB on-demand billing, and external API retry logic",
            ],
            "answer": "Implement all: API Gateway caching, Lambda reserved concurrency, DynamoDB on-demand billing, and external API retry logic",
            "explanation": "Serverless timeout issues require a comprehensive approach: API Gateway caching reduces backend calls, reserved concurrency prevents throttling, DynamoDB on-demand handles traffic spikes, and retry logic handles external API failures.",
            "badge": "Serverless Architect",
            "loot": {
                "type": "potion",
                "name": "Serverless Scaling Serum",
                "description": "Enhances understanding of auto-scaling serverless patterns",
            },
        },
        {
            "id": 8,
            "title": "RDS & DynamoDB Optimization",
            "description": "Design and optimize database solutions for different use cases",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Choose appropriate database services (RDS Multi-AZ, DynamoDB, ElastiCache), implement "
                "read replicas for read scaling, configure automated backups and point-in-time recovery, "
                "design efficient DynamoDB partition keys and GSIs, and optimize query performance with caching."
            ),
            "scenario": "Design a database architecture for a gaming application with millions of users requiring sub-millisecond latency for leaderboards.",
            "question": "A gaming application needs to store user profiles (key-value lookups) and real-time leaderboards (complex queries) with millions of concurrent users. The access patterns are predictable but require different optimization strategies. Which database architecture is MOST appropriate?",
            "options": [
                "Single Aurora Serverless cluster with auto-scaling read replicas",
                "RDS MySQL Multi-AZ with ElastiCache for Redis caching layer",
                "DynamoDB with DAX for user profiles + DynamoDB with GSI for leaderboards",
                "DynamoDB Global Tables with multiple regions for user profiles only",
            ],
            "answer": "DynamoDB with DAX for user profiles + DynamoDB with GSI for leaderboards",
            "explanation": "DynamoDB with DAX provides microsecond latency for user profile lookups, while DynamoDB with Global Secondary Indexes efficiently handles leaderboard queries. Both scale automatically for millions of users.",
            "badge": "Database Architect",
            "loot": {
                "type": "relic",
                "name": "Data Optimization Orb",
                "description": "Provides mastery over database performance tuning",
            },
        },
        {
            "id": 9,
            "title": "ECS Fargate & Container Orchestration",
            "description": "Deploy and manage containerized applications with ECS and EKS",
            "room_type": "boss",
            "difficulty": "boss",
            "reward_type": "legendary_relic",
            "content": (
                "Deploy containers with ECS and Fargate for serverless container management, manage Kubernetes "
                "clusters with EKS, implement service discovery with AWS Cloud Map, configure Application Load "
                "Balancers for container traffic, handle auto-scaling with target tracking, and monitor performance."
            ),
            "scenario": "Migrate a monolithic application to microservices architecture using containers with proper service mesh and zero-downtime deployments.",
            "question": "A company is migrating from EC2-based deployments to containers. They need automatic scaling, service discovery, zero infrastructure management, and want to minimize operational overhead. The development team is familiar with Docker but new to Kubernetes. Which approach is MOST suitable?",
            "options": [
                "EKS with Fargate for serverless Kubernetes with AWS Load Balancer Controller",
                "ECS with Fargate, Application Load Balancer, and AWS Cloud Map service discovery",
                "Self-managed Kubernetes on EC2 instances with manual load balancing",
                "Docker Swarm on EC2 with manual service discovery and nginx load balancer",
            ],
            "answer": "ECS with Fargate, Application Load Balancer, and AWS Cloud Map service discovery",
            "explanation": "ECS with Fargate provides container orchestration without Kubernetes complexity, includes built-in auto-scaling, integrates seamlessly with ALB, and AWS Cloud Map handles service discovery automatically.",
            "badge": "Container Master",
            "loot": {
                "type": "legendary_relic",
                "name": "Orchestration Crown",
                "description": "Ultimate mastery over container deployment patterns and microservices architecture",
            },
        },
        {
            "id": 10,
            "title": "CloudFormation & Infrastructure as Code",
            "description": "Master advanced CloudFormation templates and AWS CDK",
            "room_type": "battle",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Create complex CloudFormation templates with nested stacks, use parameters and conditions "
                "for flexible deployments, implement custom resources with Lambda, manage stack updates safely "
                "with change sets, and use AWS CDK for programmatic infrastructure definition."
            ),
            "scenario": "Deploy a complex multi-tier application across multiple environments using Infrastructure as Code with proper dependency management.",
            "question": "A CloudFormation stack deployment fails during an update, leaving resources in an inconsistent state. The team needs to implement a strategy to prevent this and enable safe rollbacks. Which combination of features should they use?",
            "options": [
                "Stack policies and termination protection only",
                "Change sets for preview, stack policies for protection, and rollback triggers",
                "Nested stacks with cross-stack references and manual rollback procedures",
                "AWS Config rules for compliance checking and SNS notifications",
            ],
            "answer": "Change sets for preview, stack policies for protection, and rollback triggers",
            "explanation": "Change sets allow previewing changes before execution, stack policies prevent accidental updates to critical resources, and rollback triggers automatically revert changes when CloudWatch alarms are triggered.",
            "badge": "Infrastructure Architect",
            "loot": {
                "type": "relic",
                "name": "CloudFormation Template Engine",
                "description": "Grants mastery over Infrastructure as Code patterns",
            },
        },
        {
            "id": 11,
            "title": "S3 Storage Classes & Lifecycle Management",
            "description": "Optimize S3 storage costs and implement data lifecycle policies",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Design S3 lifecycle policies to automatically transition objects between storage classes, "
                "implement S3 Intelligent-Tiering for automatic optimization, use S3 Transfer Acceleration "
                "for global uploads, and configure Cross-Region Replication for disaster recovery."
            ),
            "scenario": "Optimize storage costs for a data lake containing 100TB of files with varying access patterns and compliance requirements.",
            "question": "A company has 100TB of data in S3 Standard with the following access patterns: 20% accessed weekly, 30% accessed monthly, 30% accessed yearly, and 20% never accessed after 90 days. They need 99.999999999% durability and want to minimize costs. Which lifecycle policy is MOST cost-effective?",
            "options": [
                "Move all data to S3 One Zone-IA after 30 days, then Glacier after 90 days",
                "Move frequently accessed to S3 Standard-IA after 30 days, others to S3 Intelligent-Tiering",
                "Implement S3 Intelligent-Tiering for automatic optimization across all access patterns",
                "Transition to S3 Standard-IA after 30 days, Glacier Flexible Retrieval after 90 days, Glacier Deep Archive after 365 days",
            ],
            "answer": "Transition to S3 Standard-IA after 30 days, Glacier Flexible Retrieval after 90 days, Glacier Deep Archive after 365 days",
            "explanation": "This lifecycle policy optimizes costs by moving data through appropriate storage classes based on access patterns while maintaining 99.999999999% durability across all tiers.",
            "badge": "Storage Optimizer",
            "loot": {
                "type": "potion",
                "name": "Cost Reduction Elixir",
                "description": "Enhances understanding of storage optimization strategies",
            },
        },
        {
            "id": 12,
            "title": "Route 53 & DNS Failover",
            "description": "Implement advanced DNS routing and health checks",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Configure Route 53 health checks and failover routing, implement geolocation and latency-based "
                "routing for global applications, use weighted routing for gradual deployments, and set up "
                "private hosted zones for internal DNS resolution."
            ),
            "scenario": "Design a global DNS strategy for a multi-region application with automatic failover and geographic optimization.",
            "question": "A global application runs in US-East-1 (primary) and EU-West-1 (secondary) regions. Users should be routed to the closest healthy region, with automatic failover if the primary region fails. Which Route 53 routing configuration is MOST appropriate?",
            "options": [
                "Weighted routing with 80% to US-East-1 and 20% to EU-West-1 with health checks",
                "Geolocation routing with specific countries mapped to regions and health checks",
                "Latency-based routing with health checks and failover to secondary region",
                "Simple routing with multiple IP addresses and client-side failover logic",
            ],
            "answer": "Latency-based routing with health checks and failover to secondary region",
            "explanation": "Latency-based routing automatically directs users to the region with the lowest latency, while health checks ensure automatic failover to the healthy region if the primary fails.",
            "badge": "DNS Master",
            "loot": {
                "type": "potion",
                "name": "Global Routing Potion",
                "description": "Enhances understanding of global DNS strategies",
            },
        },
        {
            "id": 13,
            "title": "ElastiCache & Session Management",
            "description": "Implement caching strategies for high-performance applications",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Deploy ElastiCache for Redis and Memcached clusters, implement session management "
                "for stateless applications, configure Redis AUTH and encryption in transit, use Redis "
                "Sentinel for high availability, and implement cache-aside patterns for optimal performance."
            ),
            "scenario": "Improve application performance by implementing distributed caching and session management for a stateless web application.",
            "question": "A web application experiences slow database queries and needs to implement caching. The application also requires session persistence across multiple server instances. Users' sessions must persist even if a cache node fails. Which caching strategy is BEST?",
            "options": [
                "ElastiCache for Memcached cluster with session replication across nodes",
                "ElastiCache for Redis cluster with Redis AUTH and Multi-AZ deployment",
                "In-memory caching on each EC2 instance with sticky sessions on the load balancer",
                "Amazon DynamoDB for session storage with ElastiCache Memcached for query caching",
            ],
            "answer": "ElastiCache for Redis cluster with Redis AUTH and Multi-AZ deployment",
            "explanation": "Redis provides persistence and replication features that ensure session data survives node failures, while Multi-AZ deployment provides automatic failover and high availability.",
            "badge": "Caching Expert",
            "loot": {
                "type": "potion",
                "name": "Performance Boost Serum",
                "description": "Enhances understanding of caching strategies",
            },
        },
        {
            "id": 14,
            "title": "EventBridge & Event-Driven Architecture",
            "description": "Build loosely coupled applications using event-driven patterns",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Design event-driven architectures using EventBridge custom event buses, create event rules "
                "with pattern matching, implement cross-account event routing, use SQS and SNS for message "
                "queuing and fan-out patterns, and handle failures with dead letter queues."
            ),
            "scenario": "Build a microservices architecture where services communicate through events without direct coupling.",
            "question": "An e-commerce application needs to process orders through multiple microservices (inventory, payment, shipping, notifications). Each service should process events independently, handle failures gracefully, and scale automatically. Which architecture pattern is MOST suitable?",
            "options": [
                "Direct API calls between services with retry logic and circuit breakers",
                "EventBridge with custom event bus, SQS queues for each service, and Lambda processors",
                "SNS fan-out to multiple SQS queues with Lambda functions and Step Functions orchestration",
                "Kinesis Data Streams with multiple consumers and checkpoint management",
            ],
            "answer": "EventBridge with custom event bus, SQS queues for each service, and Lambda processors",
            "explanation": "EventBridge provides event routing with pattern matching, SQS queues ensure reliable message delivery with built-in retry and DLQ, and Lambda processors enable automatic scaling and cost optimization.",
            "badge": "Event Architect",
            "loot": {
                "type": "relic",
                "name": "Event Orchestration Crystal",
                "description": "Grants mastery over event-driven architecture patterns",
            },
        },
        {
            "id": 15,
            "title": "Systems Manager & Patch Management",
            "description": "Automate operations tasks and maintain system compliance",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Use Systems Manager Session Manager for secure shell access, implement automated patching "
                "with Patch Manager, manage configuration with Parameter Store and Systems Manager documents, "
                "track compliance across your fleet, and automate remediation tasks."
            ),
            "scenario": "Implement automated patch management and compliance monitoring for 200+ EC2 instances across multiple environments.",
            "question": "A company needs to patch 200+ EC2 instances monthly while minimizing downtime and ensuring rollback capability. The instances run different operating systems and applications with varying maintenance windows. Which approach is MOST efficient?",
            "options": [
                "Manual patching during scheduled maintenance windows with instance snapshots",
                "Systems Manager Patch Manager with maintenance windows, patch groups, and approval rules",
                "Auto Scaling group replacement with pre-patched AMIs during low-traffic periods",
                "Lambda functions triggered by CloudWatch Events to patch instances individually",
            ],
            "answer": "Systems Manager Patch Manager with maintenance windows, patch groups, and approval rules",
            "explanation": "Patch Manager provides automated patching with configurable maintenance windows, patch groups for different instance types, approval workflows for controlled deployments, and built-in rollback capabilities.",
            "badge": "Operations Master",
            "loot": {
                "type": "potion",
                "name": "Automation Enhancement Potion",
                "description": "Enhances understanding of operational automation",
            },
        },
        {
            "id": 16,
            "title": "WAF & Security Best Practices",
            "description": "Implement web application security with AWS WAF and Shield",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Configure AWS WAF with custom rules and managed rule sets, implement rate limiting "
                "and IP blocking, use AWS Shield Advanced for DDoS protection, integrate with CloudFront "
                "for global edge security, and monitor attacks with AWS Security Hub."
            ),
            "scenario": "Protect a web application from common attacks including SQL injection, XSS, and DDoS while maintaining good user experience.",
            "question": "A web application behind CloudFront is experiencing various attacks including SQL injection, XSS, and bot traffic. The application serves global users and needs protection without impacting legitimate traffic. Which security configuration is MOST comprehensive?",
            "options": [
                "AWS WAF with Core Rule Set and rate limiting rules on CloudFront distributions",
                "AWS WAF with managed rules, custom rules, IP reputation lists, and Shield Advanced",
                "Security groups with restricted ports and NACLs with IP blacklists only",
                "CloudFront with geographic restrictions and custom Lambda@Edge functions",
            ],
            "answer": "AWS WAF with managed rules, custom rules, IP reputation lists, and Shield Advanced",
            "explanation": "This combination provides comprehensive protection: managed rules cover common attacks, custom rules address specific threats, IP reputation lists block known bad actors, and Shield Advanced provides DDoS protection.",
            "badge": "Security Guardian",
            "loot": {
                "type": "relic",
                "name": "Web Security Fortress",
                "description": "Provides advanced protection against web application attacks",
            },
        },
        {
            "id": 17,
            "title": "Step Functions & Workflow Orchestration",
            "description": "Coordinate distributed applications using visual workflows",
            "room_type": "battle",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Design state machines with Step Functions for complex workflows, implement error handling "
                "and retry logic, use parallel execution for performance optimization, integrate with Lambda, "
                "ECS, and other AWS services, and monitor execution with CloudWatch integration."
            ),
            "scenario": "Orchestrate a complex order processing workflow with multiple steps, error handling, and parallel processing capabilities.",
            "question": "An order processing workflow involves payment processing, inventory check, shipping calculation, and notification sending. Some steps can run in parallel, and the workflow must handle failures with specific retry policies. Which Step Functions pattern is MOST appropriate?",
            "options": [
                "Sequential state machine with try-catch blocks for each step",
                "Parallel state machine with Map states for batch processing only",
                "Express workflow with high-volume, short-duration execution model",
                "Standard workflow with parallel branches, error handling, and custom retry policies",
            ],
            "answer": "Standard workflow with parallel branches, error handling, and custom retry policies",
            "explanation": "Standard workflows support parallel execution for independent tasks, comprehensive error handling with catch and retry configurations, and provide full execution history for debugging and auditing.",
            "badge": "Workflow Orchestrator",
            "loot": {
                "type": "potion",
                "name": "Process Coordination Elixir",
                "description": "Enhances understanding of distributed system orchestration",
            },
        },
        {
            "id": 18,
            "title": "Kinesis & Real-time Data Processing",
            "description": "Process streaming data with Kinesis and real-time analytics",
            "room_type": "battle",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Design real-time data pipelines with Kinesis Data Streams, process streaming data with "
                "Kinesis Analytics and Lambda, use Kinesis Data Firehose for data lake ingestion, implement "
                "producer and consumer applications with proper scaling strategies."
            ),
            "scenario": "Process millions of real-time events from IoT devices for analytics and immediate alerting on anomalies.",
            "question": "An IoT application generates millions of events per hour that need real-time processing for anomaly detection and batch processing for analytics. The system must scale automatically and handle data durability. Which architecture is MOST suitable?",
            "options": [
                "Kinesis Data Streams → Lambda for real-time processing → Kinesis Data Firehose → S3 for batch analytics",
                "SQS queues → Lambda processors → DynamoDB for real-time storage → scheduled batch jobs",
                "API Gateway → Lambda → DynamoDB Streams → additional Lambda for downstream processing",
                "EventBridge → multiple SQS queues → EC2 Auto Scaling groups for processing",
            ],
            "answer": "Kinesis Data Streams → Lambda for real-time processing → Kinesis Data Firehose → S3 for batch analytics",
            "explanation": "Kinesis Data Streams handles high-throughput ingestion with automatic scaling, Lambda provides serverless real-time processing, and Kinesis Data Firehose efficiently delivers data to S3 for batch analytics.",
            "badge": "Streaming Data Expert",
            "loot": {
                "type": "potion",
                "name": "Real-time Processing Accelerator",
                "description": "Enhances understanding of streaming data architectures",
            },
        },
        {
            "id": 19,
            "title": "Secrets Manager & Parameter Store",
            "description": "Manage application secrets and configuration securely",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Store and retrieve secrets using AWS Secrets Manager with automatic rotation, manage "
                "application configuration with Systems Manager Parameter Store, implement least-privilege "
                "access policies, use parameter hierarchies for organized configuration management."
            ),
            "scenario": "Securely manage database credentials, API keys, and application configuration for a microservices architecture.",
            "question": "A microservices application needs to manage database passwords, API keys, and configuration settings. Database passwords must rotate automatically, API keys are static but encrypted, and configuration should support hierarchical organization. Which combination is MOST appropriate?",
            "options": [
                "Secrets Manager for all sensitive data with automatic rotation enabled for everything",
                "Parameter Store SecureString for everything with manual rotation procedures",
                "Secrets Manager for database credentials with rotation, Parameter Store SecureString for API keys and configuration",
                "Environment variables encrypted with KMS for all secrets and configuration",
            ],
            "answer": "Secrets Manager for database credentials with rotation, Parameter Store SecureString for API keys and configuration",
            "explanation": "Secrets Manager provides automatic rotation for database credentials, while Parameter Store SecureString offers cost-effective encrypted storage for API keys and supports hierarchical configuration organization.",
            "badge": "Secrets Guardian",
            "loot": {
                "type": "potion",
                "name": "Security Configuration Elixir",
                "description": "Enhances understanding of secure configuration management",
            },
        },
        {
            "id": 20,
            "title": "Global Infrastructure & Disaster Recovery",
            "description": "Design multi-region architectures for disaster recovery and global scale",
            "room_type": "boss",
            "difficulty": "boss",
            "reward_type": "legendary_relic",
            "content": (
                "Design multi-region architectures with Route 53 health checks and failover routing, "
                "implement cross-region replication for databases and storage, use CloudFormation "
                "StackSets for multi-region deployments, and plan recovery strategies with defined RPO/RTO."
            ),
            "scenario": "Design a globally distributed application with 99.99% availability requirements and disaster recovery capabilities across multiple regions.",
            "question": "A mission-critical application must achieve 99.99% availability with RPO of 15 minutes and RTO of 1 hour. The application serves global users and must handle complete regional failures. Which multi-region architecture is MOST appropriate?",
            "options": [
                "Active-passive with manual failover and daily backups to secondary region",
                "Active-active with Route 53 health checks, RDS cross-region read replicas, and S3 cross-region replication",
                "Single region with multiple AZs and automated backup to another region",
                "Active-passive with automatic failover using Lambda functions and CloudWatch alarms",
            ],
            "answer": "Active-active with Route 53 health checks, RDS cross-region read replicas, and S3 cross-region replication",
            "explanation": "Active-active architecture provides the highest availability with automatic traffic distribution, Route 53 health checks ensure rapid failover, cross-region replication meets RPO requirements, and the setup minimizes RTO.",
            "badge": "Global Architect",
            "loot": {
                "type": "legendary_relic",
                "name": "Global Resilience Crown",
                "description": "Ultimate mastery over multi-region architecture and disaster recovery patterns",
            },
        },
    ]
