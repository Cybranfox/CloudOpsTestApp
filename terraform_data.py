"""
Cloud Orbit — Terraform Platform Lessons
HashiCorp Terraform Associate quality scenario-based questions.
Lesson IDs 401-412  |  4 sectors  |  12 lessons
"""


def get_lessons():
    """Return Terraform lesson list (IDs 401-412)."""
    lessons = [
        # ─────────────────────── HCL BASICS (401-403) ────────────────────────
        {
            "id": 401,
            "title": "HCL Syntax, Blocks & Resource Lifecycle",
            "description": "Master Terraform's HashiCorp Configuration Language fundamentals",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "HCL (HashiCorp Configuration Language) is Terraform's declarative language. "
                "Key block types: terraform (backend, required_providers), provider (credentials, "
                "region), resource (the infrastructure you're creating), data (read-only lookups), "
                "variable (input parameters), output (exported values), locals (computed constants). "
                'Resources use the syntax \'resource "TYPE" "NAME" { arguments }\'. The lifecycle '
                "meta-argument controls create_before_destroy, prevent_destroy, and ignore_changes."
            ),
            "scenario": (
                "Your team is migrating an AWS S3 bucket from manual creation to Terraform. The "
                "bucket stores critical customer data — it must NEVER be accidentally destroyed, "
                "even if someone runs 'terraform destroy'. However, you still need to be able to "
                "rename the bucket in the future by replacing the resource. The bucket also has "
                "tags that change frequently via the AWS console, and Terraform shouldn't overwrite "
                "those manual tag changes."
            ),
            "question": (
                "Which lifecycle configuration protects the S3 bucket from accidental deletion "
                "while still allowing controlled replacement and respecting manual tag changes?"
            ),
            "options": [
                "lifecycle { prevent_destroy = true; ignore_changes = [tags] }",
                "lifecycle { create_before_destroy = true; prevent_destroy = false }",
                "lifecycle { prevent_destroy = true } — rename requires manual state mv",
                "Use a data source to reference the bucket instead of a resource block",
            ],
            "answer": (
                "lifecycle { prevent_destroy = true } — rename requires manual state mv"
            ),
            "explanation": (
                "prevent_destroy = true blocks 'terraform destroy' and any plan that would delete "
                "this resource — exactly what you need for critical data. However, it also blocks "
                "in-place replacement (e.g., renaming). To rename, you'd use 'terraform state mv' "
                "to move the resource in state to a new address, then import the renamed bucket. "
                "ignore_changes = [tags] prevents Terraform from reverting AWS console tag edits, "
                "but that wasn't the core question. create_before_destroy helps avoid downtime but "
                "doesn't prevent destruction."
            ),
            "badge": "HCL Apprentice",
            "loot": {
                "type": "relic",
                "name": "Syntax Highlighter",
                "description": "Flags HCL syntax errors before terraform validate runs",
            },
        },
        {
            "id": 402,
            "title": "Variables, Outputs & Locals",
            "description": "Parameterise your Terraform configurations with typed inputs",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "Terraform variables accept input via: CLI (-var, -var-file), environment "
                "(TF_VAR_name), terraform.tfvars files, or variable defaults. Variable types: "
                "string, number, bool, list(), set(), map(), object({...}), tuple([]), and 'any'. "
                "Outputs export resource attributes for use by other configurations or modules. "
                "Locals compute derived values within a configuration — they can reference "
                "variables, resources, data sources, and other locals. Use 'sensitive = true' "
                "on outputs to suppress values in the console."
            ),
            "scenario": (
                "You're building a reusable VPC module. It needs: a CIDR block that defaults to "
                "'10.0.0.0/16', a list of AZ names that's required (no default), subnet counts "
                "derived automatically from the AZ list, and the VPC ID exported so other teams "
                "can reference it. You also need to suppress the database password output from "
                "showing in CI logs."
            ),
            "question": (
                "How do you declare the CIDR (with default), AZ list (required), derived subnet "
                "count, VPC ID output, and sensitive DB password output?"
            ),
            "options": [
                "variable 'cidr' { default = '10.0.0.0/16' }; variable 'azs' { type = list(string) }; "
                "locals { subnet_count = length(var.azs) * 2 }; output 'vpc_id' { value = ... }; "
                "output 'db_password' { value = ..., sensitive = true }",
                "locals { cidr = '10.0.0.0/16', azs = [], subnet_count = 4 }; "
                "output 'vpc_id', 'db_password' with no special handling",
                "Use terraform.tfvars for everything; declare outputs without sensitivity; "
                "hardcode subnet_count as a number",
                "Data sources for all values; no variables needed since data sources are "
                "always up-to-date with the provider",
            ],
            "answer": (
                "variable 'cidr' { default = '10.0.0.0/16' }; "
                "variable 'azs' { type = list(string) }; "
                "locals { subnet_count = length(var.azs) * 2 }; "
                "output 'vpc_id' { value = ... }; "
                "output 'db_password' { value = ..., sensitive = true }"
            ),
            "explanation": (
                "Variables without a 'default' are required — Terraform prompts for them or "
                "errors if not provided. 'locals' compute values without accepting external input, "
                "perfect for derived calculations like subnet_count. Outputs export values after "
                "apply — other configs access them via 'module.NAME.output_name' or "
                "'terraform_remote_state'. 'sensitive = true' on outputs suppresses the value "
                "in the console and plan output — crucial for secrets in CI logs."
            ),
            "badge": "Parameter Wizard",
            "loot": {
                "type": "relic",
                "name": "Variable Lens",
                "description": "Shows all variable values resolved at plan time",
            },
        },
        {
            "id": 403,
            "title": "Expressions, Functions & Dynamic Blocks",
            "description": "Unlock Terraform's expression language for sophisticated configurations",
            "room_type": "elite",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Terraform expressions power conditionals (condition ? true_val : false_val), "
                "for expressions ([for s in list : upper(s)]), splat expressions (aws_instance.web[*].id), "
                'and dynamic blocks (dynamic "block_name" { for_each = ... content { ... } }). '
                "Built-in functions: length(), lookup(), merge(), element(), try(), can(), "
                "flatten(), concat(), join(), split(), jsonencode(), yamlencode(). The 'try()' "
                "function evaluates arguments in order and returns the first non-error result — "
                "ideal for optional values. 'can()' returns true/false if an expression succeeds."
            ),
            "scenario": (
                "Your security group module needs: 1) An ingress rule for each port in a "
                "var.allowed_ports list, 2) An optional self-referencing rule that only exists "
                "if var.self_reference is true, 3) A description that combines the port number "
                "and the var.environment name using a for expression, 4) Graceful handling of "
                "a var.timeout that may or may not be set by the caller."
            ),
            "question": (
                "How do you build the security group with dynamic blocks, conditional rules, "
                "descriptive names, and optional timeout handling?"
            ),
            "options": [
                "dynamic 'ingress' { for_each = var.allowed_ports; content { from_port = "
                "ingress.value; to_port = ingress.value; description = '${ingress.value}-${"
                "var.environment}'; }}; dynamic 'ingress' { for_each = var.self_reference ? [1] "
                ": []; content { self = true; }}; timeout = try(var.timeout, '60s')",
                "Use count with length(var.allowed_ports) for multiple security group resources; "
                "manually create self-reference rules; use can(var.timeout) to check existence",
                "for_each = var.allowed_ports on the aws_security_group resource itself; "
                "use lookup() for timeout; hardcode self-reference as a separate resource",
                "Generate the entire security group config via a Python script that creates "
                "a JSON template; Terraform reads the template via templatefile()",
            ],
            "answer": (
                "dynamic 'ingress' { for_each = var.allowed_ports; content { "
                "from_port = ingress.value; to_port = ingress.value; "
                "description = '${ingress.value}-${var.environment}'; }}; "
                "dynamic 'ingress' { for_each = var.self_reference ? [1] : []; "
                "content { self = true; }}; "
                "timeout = try(var.timeout, '60s')"
            ),
            "explanation": (
                "1) dynamic blocks iterate over a collection and generate a nested block for each "
                "element — perfect for port lists. 2) A conditional for_each (ternary returning "
                "[1] or []) creates a dynamic block only when the condition is true — cleaner than "
                "a separate resource. 3) for expressions in the description interpolate values. "
                "4) try() is ideal for optional variables: it evaluates var.timeout (may error "
                "if undefined) and falls back to '60s'. Unlike can() which returns bool, try() "
                "returns the actual value or fallback."
            ),
            "badge": "Expression Crafter",
            "loot": {
                "type": "potion",
                "name": "Expression Elixir",
                "description": "One free try() — auto-resolves the next undefined variable",
            },
        },
        # ─────────────────────── PROVIDERS (404-406) ─────────────────────────
        {
            "id": 404,
            "title": "Provider Configuration & Authentication",
            "description": "Configure Terraform providers with secure authentication patterns",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Providers are plugins that translate Terraform configurations into API calls "
                "for a specific service (AWS, Azure, GCP, Kubernetes, etc.). Provider configuration "
                "includes: region, credentials (via static keys, environment variables, shared "
                "credentials file, IAM roles, or OIDC), endpoints (for local/test environments), "
                "and aliases (for managing resources in multiple regions or accounts). The "
                "'required_providers' block in the terraform block specifies provider source "
                "(registry.terraform.io/hashicorp/aws) and version constraints (>= 5.0, ~> 4.0)."
            ),
            "scenario": (
                "Your org's security policy requires: 1) AWS provider credentials must NEVER "
                "appear in source code, 2) The CI pipeline must authenticate to AWS using "
                "GitHub Actions OIDC (no long-lived keys), 3) You need to manage resources "
                "in both us-east-1 AND eu-west-2 from the same configuration, 4) A DynamoDB "
                "local instance running on localhost:8000 must be used when testing locally, "
                "not the real DynamoDB endpoint."
            ),
            "question": (
                "How do you configure the AWS provider for OIDC, multi-region, and local "
                "testing without hardcoding credentials?"
            ),
            "options": [
                "provider 'aws' { region = 'us-east-1' }; provider 'aws' { alias = 'london'; "
                "region = 'eu-west-2' }; provider 'aws' { alias = 'local'; region = 'us-east-1'; "
                "endpoints { dynamodb = 'http://localhost:8000' }}; CI uses "
                "configure-aws-credentials action with OIDC — no keys in code",
                "Set AWS_ACCESS_KEY_ID + AWS_SECRET_ACCESS_KEY in CI secrets; define one "
                "provider block per region using alias; use terraform workspace for local testing",
                "Store credentials in terraform.tfvars (gitignored); use for_each over regions "
                "map to create per-region provider; localstack for local testing",
                "Use AWS SSO profiles in ~/.aws/config; terraform assumes the role; "
                "separate root modules for each region rather than provider aliases",
            ],
            "answer": (
                "provider 'aws' { region = 'us-east-1' }; provider 'aws' { "
                "alias = 'london'; region = 'eu-west-2' }; provider 'aws' { "
                "alias = 'local'; region = 'us-east-1'; "
                "endpoints { dynamodb = 'http://localhost:8000' }}; "
                "CI uses configure-aws-credentials action with OIDC — no keys in code"
            ),
            "explanation": (
                "1) Provider aliases allow multiple configurations of the same provider. The "
                "default provider (no alias) handles us-east-1. The 'london' alias manages "
                "eu-west-2 — reference it in resources with 'provider = aws.london'. 2) GitHub "
                "Actions OIDC (configure-aws-credentials + OIDC trust) exchanges a GitHub JWT for "
                "temporary AWS credentials — no long-lived keys needed. 3) The 'endpoints' argument "
                "overrides API endpoints, redirecting DynamoDB calls to a local container. This is "
                "cleaner than running localstack for the single service you need."
            ),
            "badge": "Provider Master",
            "loot": {
                "type": "relic",
                "name": "Cross-Region Lens",
                "description": "Shows resources across all regions in a single plan view",
            },
        },
        {
            "id": 405,
            "title": "Multiple Providers & Provider Aliasing",
            "description": "Orchestrate resources across cloud providers and accounts",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Real infrastructure spans multiple providers: AWS for compute, Cloudflare for "
                "DNS, Datadog for monitoring, Kubernetes for workloads. Provider aliasing extends "
                "this to multiple accounts/regions of the same provider. The 'providers' "
                "meta-argument in a module block passes specific provider configurations to "
                "child modules. Provider configurations are NOT inherited by modules — you must "
                "explicitly pass them or rely on the module picking up the default provider."
            ),
            "scenario": (
                "You're building a multi-cloud architecture: 1) AWS EC2 for compute (us-east-1), "
                "2) Cloudflare for DNS pointing to the EC2 public IP, 3) A separate AWS account "
                "('audit') for CloudTrail logging, 4) A reusable 'monitoring' module that deploys "
                "Datadog monitors — it needs the Datadog provider passed explicitly. All in one "
                "'terraform apply'."
            ),
            "question": (
                "How do you configure a single root module to manage AWS, Cloudflare, a "
                "cross-account AWS provider, and pass the Datadog provider to a child module?"
            ),
            "options": [
                "provider 'aws' {}; provider 'aws' { alias = 'audit'; assume_role {...} }; "
                "provider 'cloudflare' {}; provider 'datadog' {}; module 'monitoring' "
                "{ providers = { datadog = datadog }; source = './modules/monitoring' }",
                "Each provider gets its own root module; use terragrunt to orchestrate them "
                "with dependency ordering and remote state sharing",
                "Use the 'hashicorp/multi-cloud' meta-provider that wraps all others; "
                "configure each sub-provider in its own directory with separate state files",
                "Put all providers in a single provider block; use provider aliases only "
                "for cross-region (cross-account requires separate Terraform runs)",
            ],
            "answer": (
                "provider 'aws' {}; provider 'aws' { alias = 'audit'; assume_role {...} }; "
                "provider 'cloudflare' {}; provider 'datadog' {}; "
                "module 'monitoring' { providers = { datadog = datadog }; "
                "source = './modules/monitoring' }"
            ),
            "explanation": (
                "Each cloud gets its own provider block. Cross-account AWS uses an alias with "
                "'assume_role' — Terraform assumes the audit account role via STS, getting "
                "temporary credentials scoped to that account. Cloudflare and Datadog are separate "
                "providers with their own API keys (from env vars or CI secrets). The monitoring "
                "module needs the Datadog provider explicitly passed via the 'providers' "
                "meta-argument — without it, the module can't access Datadog resources. One "
                "'terraform apply' orchestrates everything: EC2, DNS record pointing to EC2 IP, "
                "CloudTrail in audit account, and Datadog monitors."
            ),
            "badge": "Multi-Cloud Architect",
            "loot": {
                "type": "relic",
                "name": "Unified Plan Lens",
                "description": "Shows the full multi-cloud plan graph in a single view",
            },
        },
        {
            "id": 406,
            "title": "Terraform Registry & Provider Versioning",
            "description": "Manage provider sources, versions, and dependency locking",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "The Terraform Registry (registry.terraform.io) hosts thousands of providers. "
                "The 'required_providers' block specifies source and version constraints. The "
                "dependency lock file (.terraform.lock.hcl) records exact provider versions and "
                "hashes — commit this to git for reproducible runs. Version constraints: '>= 1.0' "
                "(minimum), '~> 1.2' (>= 1.2, < 2.0), '>= 1.0, < 2.0' (range). Use "
                "'terraform init -upgrade' to update to latest allowed versions, then commit "
                "the updated lock file."
            ),
            "scenario": (
                "Your team's Terraform config pinned AWS provider to '~> 4.0' last year. AWS "
                "provider 5.0 is now out with breaking S3 changes. You need to: 1) Audit which "
                "resources will be affected by the upgrade, 2) Pin the exact 4.x version for "
                "production while testing 5.x in a dev workspace, 3) Ensure CI and all team "
                "members get identical provider versions — no 'works on my machine' drift."
            ),
            "question": (
                "How do you safely manage the AWS provider 4.x → 5.x migration across "
                "environments while ensuring reproducible builds?"
            ),
            "options": [
                "Production pins '~> 4.67' (last 4.x); dev workspace uses '~> 5.0'; both "
                "commit .terraform.lock.hcl. Run 'terraform plan' in dev to preview S3 changes "
                "before applying the version bump to production",
                "Switch all environments to '>= 4.0' and use terraform apply -refresh-only "
                "to update state without changing resources; migrate by recreating resources",
                "Use 'terraform version' constraint on the Terraform binary itself; run 4.x "
                "on production and 5.x on dev machines; ignore the lock file",
                "Fork the AWS provider 4.x and maintain an internal version; never upgrade "
                "to avoid breaking changes",
            ],
            "answer": (
                "Production pins '~> 4.67' (last 4.x); dev workspace uses '~> 5.0'; "
                "both commit .terraform.lock.hcl. Run 'terraform plan' in dev to preview "
                "S3 changes before applying the version bump to production"
            ),
            "explanation": (
                "The lock file (.terraform.lock.hcl) is your guarantee of reproducibility — "
                "every 'terraform init' installs the exact same provider binary with matched "
                "hashes. Production stays on 4.x with '~> 4.67' (the tilde prevents 5.0). "
                "Dev/test switches to '~> 5.0' — 'terraform plan' shows exactly which resources "
                "will change (e.g., S3 bucket ACL deprecation, new default settings). Once you've "
                "updated your HCL to handle 5.x changes, you bump production's constraint. Never "
                "skip the lock file — it's the Terraform equivalent of package-lock.json."
            ),
            "badge": "Version Guardian",
            "loot": {
                "type": "relic",
                "name": "Lock Key",
                "description": "Automatically validates provider versions match lock file before apply",
            },
        },
        # ─────────────────────── STATE & BACKEND (407-409) ──────────────────
        {
            "id": 407,
            "title": "State Management & Drift Detection",
            "description": "Master Terraform state — the source of truth for your infrastructure",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Terraform state (terraform.tfstate) maps real-world resource IDs to your "
                "configuration. State enables: dependency resolution (knowing which resources "
                "already exist), performance (caching resource attributes), and metadata tracking. "
                "'terraform refresh' updates state to match real infrastructure — detecting drift. "
                "'terraform plan -refresh-only' shows drift without applying changes. "
                "'terraform import' brings existing resources under Terraform management. "
                "State commands: 'terraform state list', 'mv' (rename/move resource), 'rm' "
                "(stop managing), 'show' (inspect a resource)."
            ),
            "scenario": (
                "Your team discovers that someone manually added a security group rule to the "
                "production AWS security group via the console. Terraform's state still shows "
                "the old configuration. You need to: 1) Detect ALL drift between state and "
                "reality, 2) Decide whether to import the manual change or revert it, "
                "3) Also rename the 'aws_instance.web' resource to 'aws_instance.frontend' "
                "without destroying and recreating the EC2 instance."
            ),
            "question": (
                "How do you detect drift, handle the manual SG rule, and rename the EC2 "
                "resource non-destructively?"
            ),
            "options": [
                "terraform plan -refresh-only to detect all drift; for the SG rule: either "
                "add it to config + import into state, or remove it manually + refresh; "
                "rename EC2: terraform state mv aws_instance.web aws_instance.frontend",
                "terraform destroy && terraform apply to rebuild from clean state; manually "
                "document the SG rule; rename by editing the resource block",
                "Use AWS Config to detect drift (not Terraform); delete and recreate the "
                "EC2 instance with the new name; the SG rule is auto-detected by refresh",
                "terraform refresh to sync state to reality (accepting all drift); then "
                "terraform plan shows nothing because state now matches reality",
            ],
            "answer": (
                "terraform plan -refresh-only to detect all drift; for the SG rule: either "
                "add it to config + import into state, or remove it manually + refresh; "
                "rename EC2: terraform state mv aws_instance.web aws_instance.frontend"
            ),
            "explanation": (
                "1) 'terraform plan -refresh-only' shows what's different between state and "
                "reality without proposing changes — pure drift detection. 2) For the manual "
                "SG rule: if you want to keep it, add the rule to your Terraform config and "
                "run 'terraform import aws_security_group_rule.manual sg-XXXX_ingress_tcp_..."
                "to bring it into state. If you don't want it, delete it in the console and "
                "'terraform refresh' updates state. 3) 'terraform state mv' renames a resource "
                "in state without touching the real resource — the next plan shows no changes "
                "because state now matches the renamed resource block."
            ),
            "badge": "State Keeper",
            "loot": {
                "type": "relic",
                "name": "Drift Detector",
                "description": "Alerts when any resource drifts from its Terraform-managed state",
            },
        },
        {
            "id": 408,
            "title": "Remote State, Backends & State Locking",
            "description": "Secure team collaboration with remote state and DynamoDB locking",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Never store terraform.tfstate in git — it contains secrets (database passwords, "
                "API keys in plaintext). Remote backends solve this: S3 + DynamoDB (AWS), "
                "Azure Storage (Azure), GCS (GCP), Terraform Cloud/Enterprise, or HTTP backends. "
                "State locking prevents concurrent 'terraform apply' from corrupting state — "
                "DynamoDB provides this for S3 backends. The 'backend' block in the terraform "
                "block configures this. Migration from local to remote uses 'terraform init "
                "-migrate-state'. Partial configuration allows backend config to be passed "
                "at init time via -backend-config — useful for CI where backend details vary."
            ),
            "scenario": (
                "Your team of 5 engineers keeps corrupting state because two people run "
                "'terraform apply' simultaneously against the same S3 backend. You also need "
                "the CI pipeline to use a different state key for PR preview environments "
                "('pr-123/terraform.tfstate') vs production ('prod/terraform.tfstate'). "
                "The S3 bucket name is different in dev and prod AWS accounts."
            ),
            "question": (
                "How do you configure the S3 backend with DynamoDB locking and CI-variable "
                "state keys across accounts?"
            ),
            "options": [
                "terraform { backend 's3' { bucket = var.backend_bucket; key = "
                "var.state_key; region = 'us-east-1'; dynamodb_table = 'terraform-locks' }}; "
                "CI passes -backend-config='key=pr-${PR_NUMBER}/terraform.tfstate' -backend-"
                "config='bucket=dev-tfstate' at init time. DynamoDB ensures exclusive lock",
                "Store state in Git LFS; use GitHub branch protection rules to prevent "
                "concurrent applies; separate directories per environment for state isolation",
                "Use Terraform Cloud workspaces (free tier) — auto-locking, auto-secrets, "
                "remote execution; no backend config needed in code",
                "Terragrunt with a hierarchical config; each environment is a terragrunt.hcl "
                "that inherits from a root config and overrides account/region",
            ],
            "answer": (
                "terraform { backend 's3' { bucket = var.backend_bucket; "
                "key = var.state_key; region = 'us-east-1'; "
                "dynamodb_table = 'terraform-locks' }}; "
                "CI passes -backend-config='key=pr-${PR_NUMBER}/terraform.tfstate' "
                "-backend-config='bucket=dev-tfstate' at init time. DynamoDB ensures exclusive lock"
            ),
            "explanation": (
                "1) DynamoDB provides state locking — when 'terraform apply' starts, it acquires "
                "a lock in the DynamoDB table. If another process tries to apply, it waits "
                "(or fails with a lock timeout). This eliminates the corruption from concurrent "
                "applies. 2) Backend partial configuration: you can't use variables in the backend "
                "block (Terraform limitation), but '-backend-config' flags at init time fill in "
                "the blanks. CI passes the PR number for isolated state files and the correct "
                "bucket per account. 3) Separate state keys per PR mean each preview environment "
                "has its own isolated state — 'terraform destroy' on PR close only affects that "
                "PR's resources."
            ),
            "badge": "State Lord",
            "loot": {
                "type": "relic",
                "name": "Lock Breaker",
                "description": "Force-unlocks a stuck state lock once per sprint",
            },
        },
        {
            "id": 409,
            "title": "Workspaces & State Isolation Strategies",
            "description": "Manage multiple environments with Terraform workspaces and file layouts",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Terraform offers two environment isolation strategies: 1) Workspaces "
                "('terraform workspace new/select/list') — one config, multiple state files. "
                "Best for identical environments (dev/staging/prod) where differences are "
                "small. Use '${terraform.workspace}' to vary config per workspace. 2) File "
                "layout (directory-per-environment) — separate root modules per environment. "
                "Best for environments that differ significantly or need different backends. "
                "Workspaces are NOT suitable for strong isolation (same backend, same "
                "credentials). For true isolation, use separate directories + separate "
                "AWS accounts + separate state buckets."
            ),
            "scenario": (
                "Your org has: 1) Dev and staging are near-identical (just different instance "
                "sizes), 2) Production is in a completely separate AWS account with different "
                "networking, 3) You need to prevent a 'terraform destroy' in dev from ever "
                "touching production state, 4) Staging should be able to replicate production "
                "data for load testing without affecting production infrastructure."
            ),
            "question": (
                "Which isolation strategy correctly separates dev/staging from production "
                "while keeping dev/staging easily maintainable?"
            ),
            "options": [
                "Workspaces for dev + staging (terraform.workspace drives instance sizes); "
                "separate root module directory for production with its own backend (different "
                "S3 bucket in the prod account). Destroy in dev workspace only affects dev state",
                "Three Terraform Cloud workspaces; use remote execution with Sentinel policies "
                "to prevent production destruction; all share the same variable set",
                "Single workspace with three .tfvars files; select environment by passing "
                "-var-file=prod.tfvars; use count to conditionally create resources",
                "Terragrunt with a hierarchical config; each environment is a terragrunt.hcl "
                "that inherits from a root config and overrides account/region",
            ],
            "answer": (
                "Workspaces for dev + staging (terraform.workspace drives instance sizes); "
                "separate root module directory for production with its own backend (different "
                "S3 bucket in the prod account). Destroy in dev workspace only affects dev state"
            ),
            "explanation": (
                "Workspaces are perfect for dev/staging: one config, terraform.workspace "
                "drives the differences (e.g., 't3.small' for dev, 't3.medium' for staging). "
                "Production, however, is a different AWS account with different networking — "
                "a separate root module directory is the right call. It uses a different S3 "
                "backend (prod account's bucket) with its own DynamoDB lock table. A "
                "'terraform destroy' in the dev workspace literally cannot touch production "
                "— different state file, different account, different credentials. This "
                "provides the blast-radius isolation that compliance often requires."
            ),
            "badge": "Workspace Sage",
            "loot": {
                "type": "relic",
                "name": "Isolation Ward",
                "description": "Prevents cross-environment state corruption automatically",
            },
        },
        # ─────────────────────── MODULES (410-412) ──────────────────────────
        {
            "id": 410,
            "title": "Module Structure & Best Practices",
            "description": "Build composable, reusable Terraform modules",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "A Terraform module is a directory containing .tf files. The standard structure: "
                "main.tf (resources), variables.tf (input declarations), outputs.tf (exported "
                "values), versions.tf (required providers + version constraints), and optionally "
                "README.md. Module sources: local paths (./modules/vpc), Terraform Registry "
                "(terraform-aws-modules/vpc/aws), GitHub (github.com/org/repo), S3, HTTP URLs, "
                "or generic git repos. Module versioning uses git tags or registry versions. "
                "Best practice: modules should do ONE thing well — a VPC module creates "
                "networking, not networking + compute + database."
            ),
            "scenario": (
                "Your org needs a standardised 's3-bucket' module that: 1) Creates an S3 bucket "
                "with configurable name, versioning, and encryption, 2) Optionally creates a "
                "bucket policy for CloudFront access, 3) Outputs the bucket ARN, ID, and "
                "regional domain name, 4) Is versioned with git tags so teams can pin to "
                "specific versions (v1.0.0, v1.1.0). The module should be usable by any "
                "team in the org from the internal GitHub repo."
            ),
            "question": (
                "What is the correct module structure and how should consumers reference "
                "a specific version?"
            ),
            "options": [
                "Module directory: main.tf (bucket resource + optional policy), variables.tf "
                "(name, versioning, encryption, cloudfront_arn), outputs.tf (arn, id, domain); "
                "consumers: source = 'git::https://github.com/org/s3-module.git?ref=v1.0.0'",
                "Single main.tf with everything inline; consumers copy-paste the file; "
                "versioning by commenting // v1.0 at the top of the file",
                "Publish to Terraform Registry as 'org/s3-bucket/aws'; consumers use "
                "source = 'org/s3-bucket/aws'; version = '~> 1.0' in the module block",
                "Module as a monorepo folder /modules/s3; all teams import it via relative "
                "path ../../modules/s3; versions are branches in the monorepo",
            ],
            "answer": (
                "Module directory: main.tf (bucket resource + optional policy), "
                "variables.tf (name, versioning, encryption, cloudfront_arn), "
                "outputs.tf (arn, id, domain); consumers: "
                "source = 'git::https://github.com/org/s3-module.git?ref=v1.0.0'"
            ),
            "explanation": (
                "A well-structured module separates concerns: main.tf for resources, "
                "variables.tf for inputs (with types, defaults, and validation blocks), "
                "outputs.tf for exported values. Git tags (v1.0.0) enable semantic versioning "
                "— teams pin to specific versions for stability. The 'git::' prefix with "
                "'?ref=v1.0.0' tells Terraform to clone the repo at that tag. For private "
                "GitHub repos, Terraform uses the runner's git credentials (or SSH). "
                "Option 3 (Registry) is also valid for public modules but requires publishing; "
                "the Git approach works immediately for internal org use."
            ),
            "badge": "Module Crafter",
            "loot": {
                "type": "relic",
                "name": "Blueprint Scroll",
                "description": "Pre-validates module inputs before terraform plan runs",
            },
        },
        {
            "id": 411,
            "title": "Module Composition & Data Passing",
            "description": "Chain modules together and pass data between them",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Modules compose by passing outputs from one as inputs to another. The root "
                "module orchestrates: module A produces VPC ID → module B consumes it for "
                "subnets → module C consumes subnet IDs for EC2. This creates an implicit "
                "dependency graph — Terraform orders operations correctly. The 'depends_on' "
                "meta-argument forces explicit ordering when Terraform can't infer it. "
                "'for_each' on modules (Terraform 0.13+) creates multiple instances of a "
                "module — powerful for per-environment or per-customer deployments. "
                "Module outputs can include entire resource objects with all attributes."
            ),
            "scenario": (
                "You're building a three-tier architecture: 1) A VPC module that outputs "
                "vpc_id, public_subnet_ids, private_subnet_ids, 2) An RDS module that "
                "creates a database in the private subnets (needs subnet_ids + vpc_id), "
                "3) An EC2 module that creates app servers in the public subnets (needs "
                "subnet_ids + db_endpoint from RDS). The RDS module must be created before "
                "EC2. Each module should create one instance per environment (dev, staging, "
                "prod) using for_each."
            ),
            "question": (
                "How do you compose VPC → RDS → EC2 with data passing and per-environment "
                "module instances?"
            ),
            "options": [
                "module 'vpc' { ... }; module 'rds' { for_each = var.environments; "
                "subnet_ids = module.vpc.private_subnet_ids; vpc_id = module.vpc.vpc_id; ... }; "
                "module 'ec2' { for_each = var.environments; subnet_ids = module.vpc.public_"
                "subnet_ids; db_endpoint = module.rds[each.key].endpoint; ... }",
                "Chain via terraform_remote_state data sources; each module writes outputs "
                "that the next reads; use count for multiple instances",
                "Flatten everything into a single root module — modules add unnecessary "
                "indirection; use locals to pass data between resource blocks",
                "Each module outputs to a central data store (SSM Parameter Store); the next "
                "module reads from SSM rather than module outputs directly",
            ],
            "answer": (
                "module 'vpc' { ... }; module 'rds' { for_each = var.environments; "
                "subnet_ids = module.vpc.private_subnet_ids; vpc_id = module.vpc.vpc_id; ... }; "
                "module 'ec2' { for_each = var.environments; "
                "subnet_ids = module.vpc.public_subnet_ids; "
                "db_endpoint = module.rds[each.key].endpoint; ... }"
            ),
            "explanation": (
                "Module composition via output-passing creates clean dependency graphs. "
                "module.vpc runs first (no dependencies). module.rds depends on VPC outputs "
                "— Terraform automatically orders it second. module.ec2 depends on both VPC "
                "and RDS outputs, so it runs last. The for_each on RDS and EC2 creates "
                "per-environment instances: each environment gets its own database and app "
                "server. module.rds['dev'] and module.rds['prod'] are separate instances "
                "with different configurations. This pattern is the foundation of reusable, "
                "scalable Terraform architectures."
            ),
            "badge": "Composer Elite",
            "loot": {
                "type": "relic",
                "name": "Dependency Graph Lens",
                "description": "Visualises the full module dependency tree before apply",
            },
        },
        {
            "id": 412,
            "title": "Testing Terraform: plan, validate & Terratest",
            "description": "Validate infrastructure changes with automated testing pipelines",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Terraform testing spans multiple levels: 1) 'terraform fmt -check' (style), "
                "2) 'terraform validate' (syntax + provider schema checks), 3) 'terraform plan' "
                "in CI (dry run — catches logical errors before apply), 4) 'check' blocks "
                "(Terraform 1.5+) — assert conditions on resources (e.g., S3 bucket must have "
                "encryption enabled), 5) Terratest (Go) or pytest-terraform (Python) — deploy "
                "real resources, run assertions, destroy. The CI pipeline: fmt → validate → "
                "plan (post as PR comment) → tflint (best practices) → apply (on merge) → "
                "Terratest (post-deploy verification)."
            ),
            "scenario": (
                "Your PR pipeline must: 1) Reject code that's not formatted with terraform fmt, "
                "2) Fail if terraform validate finds errors, 3) Post the plan output as a PR "
                "comment so reviewers can see what will change, 4) Run tflint to catch common "
                "mistakes (e.g., security group with 0.0.0.0/0 without a description), "
                "5) The S3 bucket module must always have encryption enabled — add an "
                "automated check that runs before plan."
            ),
            "question": (
                "What is the complete CI pipeline that gates PRs on formatting, validation, "
                "linting, plan preview, and policy checks?"
            ),
            "options": [
                "CI steps: terraform fmt -diff -check -recursive → terraform validate → "
                "tflint → check block { assert { condition = aws_s3_bucket.main."
                "server_side_encryption_configuration[0].apply_server_side_encryption_by_"
                "default[0].sse_algorithm == 'aws:kms'; error_message = 'S3 must use KMS' }} "
                "→ terraform plan (output posted as PR comment)",
                "Just terraform validate — if it passes syntax check, the logic is correct; "
                "rely on Terraform Cloud's speculative plans for plan preview",
                "terratest with Go test suite that does deploy → assert → destroy; validate "
                "and fmt are optional since the Go compiler catches syntax errors",
                "Git pre-commit hooks run fmt + validate locally; CI only handles the apply; "
                "policy checks are manual code review by the security team",
            ],
            "answer": (
                "CI steps: terraform fmt -diff -check -recursive → terraform validate → "
                "tflint → check block { assert { condition = aws_s3_bucket.main."
                "server_side_encryption_configuration[0].apply_server_side_encryption_by_"
                "default[0].sse_algorithm == 'aws:kms'; error_message = 'S3 must use KMS' }} "
                "→ terraform plan (output posted as PR comment)"
            ),
            "explanation": (
                "This pipeline catches issues at each stage: 1) terraform fmt -check -recursive "
                "fails if any .tf file isn't canonical format — style issues caught immediately. "
                "2) terraform validate checks syntax + provider schema references — catches "
                "typos and missing attributes. 3) tflint checks best practices (e.g., AWS "
                "provider rules like 'security groups with 0.0.0.0/0 must have descriptions'). "
                "4) check blocks in Terraform 1.5+ allow inline policy assertions: the "
                "condition runs at plan time and blocks apply if it fails. 5) The plan is "
                "posted as a PR comment via github-comment or similar — reviewers see exactly "
                "what will be created/modified/destroyed before approving. Terratest is the "
                "final gate, running after apply to verify the deployed resources work correctly."
            ),
            "badge": "Pipeline Guardian",
            "loot": {
                "type": "relic",
                "name": "Gatekeeper's Seal",
                "description": "One free PR pipeline bypass — auto-fixes one failing check",
            },
        },
    ]

    # Post-process: ensure answer strings match option strings exactly
    # Black formatting may split long strings differently between answer and options
    for lesson in lessons:
        answer = lesson.get("answer", "")
        options = lesson.get("options", [])
        if answer and answer not in options:
            # Find the matching option by stripping and comparing
            answer_stripped = " ".join(answer.split())
            for opt in options:
                if " ".join(opt.split()) == answer_stripped:
                    lesson["answer"] = opt
                    break

    return lessons
