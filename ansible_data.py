"""
Cloud Orbit — Ansible Platform Lessons
RHCE / Ansible Automation quality scenario-based questions.
Lesson IDs 301-312  |  4 sectors  |  12 lessons
"""


def get_lessons():
    """Return Ansible lesson list (IDs 301-312)."""
    return [
        # ─────────────────────── PLAYBOOKS (301-303) ─────────────────────────
        {
            "id": 301,
            "title": "Playbook Structure & YAML Best Practices",
            "description": "Master Ansible playbook anatomy and YAML conventions",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "Ansible playbooks are YAML files defining the desired state of your infrastructure. "
                "A playbook contains one or more plays, each targeting a host group and executing tasks "
                "sequentially. Key sections: hosts (target inventory group), become (privilege escalation), "
                "vars (play-level variables), tasks (ordered list of modules to execute), and handlers "
                "(triggered tasks that run once at the end). YAML indentation must be consistent — "
                "Ansible is strict about 2-space indentation."
            ),
            "scenario": (
                "Your team needs to automate Nginx deployment across 50 web servers in the "
                "'webservers' inventory group. The playbook must install nginx, configure a custom "
                "index.html from a template, ensure the service is running, and restart it only if "
                "the config changes. You have sudo access via the 'ansible' user."
            ),
            "question": (
                "Which playbook structure correctly deploys Nginx with a handler for config-triggered restart?"
            ),
            "options": [
                "Single play with tasks: install nginx, template config, service started; "
                "handler: restart nginx — notified by the template task",
                "Two plays: first installs nginx, second runs a handler task directly after template",
                "Single play with tasks: install nginx, template config, service restarted — "
                "no handler needed since it runs sequentially",
                "Tasks use 'notify: restart nginx' on the install step, with the handler "
                "defined in a separate playbook imported via import_playbook",
            ],
            "answer": (
                "Single play with tasks: install nginx, template config, service started; "
                "handler: restart nginx — notified by the template task"
            ),
            "explanation": (
                "Handlers are special tasks that only run when notified. The template task notifies "
                "the handler, which executes once at the end of the play — even if notified multiple times. "
                "This prevents unnecessary restarts when the config hasn't changed. The service task uses "
                "state: started (idempotent) — it won't restart unless the handler fires."
            ),
            "badge": "Playbook Scribe",
            "loot": {
                "type": "relic",
                "name": "YAML Lint Lens",
                "description": "Highlights syntax issues before playbook execution",
            },
        },
        {
            "id": 302,
            "title": "Variables, Facts & Jinja2 Templating",
            "description": "Harness Ansible variables, gathered facts, and Jinja2 expressions",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Ansible variables can be defined in many places with a strict precedence hierarchy: "
                "extra vars (-e) > task vars > block vars > role vars > play vars > inventory vars > "
                "role defaults. Facts are discovered system properties (gathered at play start) — "
                "use ansible_facts['os_family'] or the shorthand ansible_os_family. Jinja2 templating "
                "powers dynamic expressions: conditionals with 'when', loops with 'loop', and "
                "filters like '| default()', '| map()', '| selectattr()'."
            ),
            "scenario": (
                "You're writing a playbook that configures different firewall rules for Debian "
                "vs RHEL servers. On Debian, use UFW; on RHEL, use firewalld. The playbook must "
                "also skip any host with less than 2GB RAM, and use a default SSH port of 22 "
                "unless overridden by an inventory variable 'custom_ssh_port'."
            ),
            "question": (
                "How do you conditionally configure the correct firewall per OS and skip low-memory hosts?"
            ),
            "options": [
                "when: ansible_os_family == 'Debian' on the UFW task, "
                "'RedHat' on the firewalld task; when: ansible_memtotal_mb < 2048 with meta: end_host",
                "Use a shell script called via command module that detects the OS internally; "
                "skip hosts with ansible_memtotal_mb < 2048 in the play's hosts directive",
                "when: inventory_hostname is search('deb') for UFW; "
                "delegate_to: localhost for memory checks",
                "Use vars_files to load OS-specific task lists; "
                "set gather_facts: no and use custom fact scripts for memory",
            ],
            "answer": (
                "when: ansible_os_family == 'Debian' on the UFW task, "
                "'RedHat' on the firewalld task; when: ansible_memtotal_mb < 2048 with meta: end_host"
            ),
            "explanation": (
                "ansible_os_family is a gathered fact. Use 'when' conditionals on each task — "
                "the UFW task only runs on Debian-family hosts, firewalld only on RedHat-family. "
                "For low-memory hosts, 'when: ansible_memtotal_mb < 2048' combined with "
                "'meta: end_host' gracefully exits the play for that host without failing. "
                "The SSH port uses '{{ custom_ssh_port | default(22) }}' in the template."
            ),
            "badge": "Fact Finder",
            "loot": {
                "type": "relic",
                "name": "Jinja2 Filter Book",
                "description": "Unlocks advanced variable manipulation in all playbooks",
            },
        },
        {
            "id": 303,
            "title": "Conditionals, Loops & Error Handling",
            "description": "Control playbook flow with conditionals, iteration, and blocks",
            "room_type": "elite",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Ansible offers rich flow control. Conditionals use 'when' with Jinja2 expressions — "
                "no curly braces needed. Loops iterate with 'loop' over lists, 'with_dict' over "
                "dictionaries, and 'until' for retry patterns. Blocks group tasks with shared "
                "attributes and error handling: 'block' contains tasks, 'rescue' runs on failure, "
                "'always' runs regardless. The 'any_errors_fatal' and 'max_fail_percentage' settings "
                "control when to abort a play. 'ignore_errors: yes' continues past a task failure."
            ),
            "scenario": (
                "You need to deploy an app that requires: 1) Create 5 users from a list with "
                "specific UIDs, 2) Install packages from a list — retry up to 3 times if the "
                "package manager is locked, 3) Start the app service — if it fails, restore "
                "the previous deployment from a backup and alert the on-call channel. The play "
                "should stop entirely if more than 30% of hosts fail."
            ),
            "question": (
                "Which block/rescue pattern handles the app deployment with rollback and retry logic?"
            ),
            "options": [
                "block: start app service; rescue: restore backup + debug msg; "
                "always: send notification. Package install uses until: 3 retries with 10s delay. "
                "max_fail_percentage: 30 at play level",
                "Two sequential plays: first deploys, second (conditional) runs rollback. "
                "Package install loop has retries: 3. Serial: 1 for canary deployment",
                "ignore_errors: yes on all tasks; use assert module after each to check state; "
                "delegate rollback to a dedicated recovery host",
                "Use async tasks with poll for deployment; "
                "failed_when: custom condition triggers rollback handler; "
                "run_once: true for notifications",
            ],
            "answer": (
                "block: start app service; rescue: restore backup + debug msg; "
                "always: send notification. Package install uses until: 3 retries with 10s delay. "
                "max_fail_percentage: 30 at play level"
            ),
            "explanation": (
                "The block/rescue/always pattern is Ansible's try/catch/finally. 'block' attempts "
                "the deployment. 'rescue' only executes on failure — here it restores from backup. "
                "'always' runs regardless — perfect for notifications. Package install uses 'until: "
                "package_check.rc == 0' with 'retries: 3' and 'delay: 10' for transient lockfile "
                "issues. 'max_fail_percentage: 30' at the play level aborts if >30% of hosts fail. "
                "Users are created with 'loop' over the user list with per-item UIDs."
            ),
            "badge": "Flow Controller",
            "loot": {
                "type": "potion",
                "name": "Retry Elixir",
                "description": "One free retry on a failed lesson challenge",
            },
        },
        # ─────────────────────── ROLES (304-306) ─────────────────────────────
        {
            "id": 304,
            "title": "Role Structure & ansible-galaxy",
            "description": "Build reusable automation with the Ansible role framework",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Roles are Ansible's primary mechanism for bundling automation into reusable, "
                "shareable units. The standard role directory layout: tasks/ (main.yml — entry point), "
                "handlers/, templates/, files/, vars/, defaults/, meta/ (dependencies + galaxy info). "
                "ansible-galaxy init creates the scaffold; ansible-galaxy install installs from "
                "Galaxy, GitHub, or a requirements.yml file. Role variables should use defaults/main.yml "
                "for overridable values and vars/main.yml for internal constants."
            ),
            "scenario": (
                "You're building a reusable 'nginx_role' for your org. It should: install nginx, "
                "deploy a custom config template, support multiple vhosts via a list variable, "
                "allow the nginx version to be pinned (default: latest from repo), and optionally "
                "configure TLS if certificate files are provided. Other teams will consume this "
                "via ansible-galaxy from your internal Git server."
            ),
            "question": (
                "Where should the nginx version (overridable), vhost list (required), and TLS cert "
                "path (optional) be defined in the role?"
            ),
            "options": [
                "nginx_version in defaults/main.yml (overridable); vhosts in vars/main.yml or "
                "required check in tasks; TLS cert path defaults to '' in defaults/main.yml "
                "with conditional TLS tasks",
                "All variables in vars/main.yml with explicit values; consumers must edit the "
                "role directly to customise",
                "nginx_version in tasks/main.yml as a set_fact; vhosts and TLS in a vars "
                "file included at play level",
                "Everything in defaults/main.yml — Ansible role consumers should never need "
                "to look at vars/main.yml",
            ],
            "answer": (
                "nginx_version in defaults/main.yml (overridable); vhosts in vars/main.yml or "
                "required check in tasks; TLS cert path defaults to '' in defaults/main.yml "
                "with conditional TLS tasks"
            ),
            "explanation": (
                "defaults/main.yml contains variables with the LOWEST precedence — perfect for "
                "overridable values like version pins. vars/main.yml has higher precedence for "
                "internal role constants. Required variables (vhosts) should be validated in "
                "tasks/main.yml with a fail or assert task if not defined. Optional variables "
                "(TLS cert path) default to empty/false in defaults/ and trigger conditional "
                "tasks via 'when: tls_cert_path | length > 0'. Consumers set variables in their "
                "playbook or inventory to override the defaults."
            ),
            "badge": "Role Crafter",
            "loot": {
                "type": "relic",
                "name": "Galaxy Compass",
                "description": "Points to the best community roles for any task",
            },
        },
        {
            "id": 305,
            "title": "Role Dependencies & Meta Configuration",
            "description": "Chain roles together and manage the dependency graph",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Role dependencies are declared in meta/main.yml via the 'dependencies' list. "
                "Each entry can specify: role name, version, source URL, and variables to pass. "
                "Dependencies execute BEFORE the role that declares them — creating an ordered chain. "
                "Ansible Galaxy supports semantic versioning for roles. For complex apps, use "
                "requirements.yml to declare all roles with their versions and sources. "
                "Role duplication is prevented: if two roles depend on a common role, it's "
                "only executed once."
            ),
            "scenario": (
                "Your 'my_app' role needs: 1) 'geerlingguy.docker' (v7+) from Galaxy, "
                "2) 'internal_org.ssl_certs' from your GitLab with tag v2.1.0, "
                "3) A 'monitoring_agent' role that should only install if the "
                "'enable_monitoring' variable is true. Order matters — Docker must be "
                "installed first, then SSL certs, then the app, then optionally monitoring."
            ),
            "question": (
                "How should these role dependencies be structured in meta/main.yml?"
            ),
            "options": [
                "dependencies list in meta/main.yml: geerlingguy.docker (v7+), then "
                "internal_org.ssl_certs (src: gitlab, version: v2.1.0), then monitoring_agent "
                "with when: enable_monitoring | default(false) | bool",
                "import_role tasks in tasks/main.yml with sequential ordering; use "
                "requirements.yml only for ansible-galaxy install",
                "include_role in the consuming playbook for each dependency; meta/main.yml "
                "only lists informational metadata",
                "Use ansible-galaxy collection instead of roles — dependencies are handled "
                "via galaxy.yml in collections",
            ],
            "answer": (
                "dependencies list in meta/main.yml: geerlingguy.docker (v7+), then "
                "internal_org.ssl_certs (src: gitlab, version: v2.1.0), then monitoring_agent "
                "with when: enable_monitoring | default(false) | bool"
            ),
            "explanation": (
                "Dependencies declared in meta/main.yml execute in order BEFORE the role's tasks. "
                "Each dependency can have a 'when' conditional — monitoring_agent only installs if "
                "enable_monitoring is true. Galaxy roles (geerlingguy.docker) are resolved from "
                "Ansible Galaxy; the custom role uses a Git source with a version tag. "
                "requirements.yml documents all external roles for reproducible installs via "
                "'ansible-galaxy install -r requirements.yml'. Dependencies execute exactly once "
                "even if multiple roles declare them."
            ),
            "badge": "Dependency Master",
            "loot": {
                "type": "relic",
                "name": "Meta Compass",
                "description": "Auto-resolves role dependency conflicts",
            },
        },
        {
            "id": 306,
            "title": "ansible-lint, Molecule & Role Testing",
            "description": "Test and validate Ansible roles with industry-standard tooling",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Production Ansible requires testing. ansible-lint enforces best practices "
                "(naming conventions, risky module flags, idempotency patterns). Molecule "
                "provides a complete test framework: create ephemeral instances (Docker/Vagrant), "
                "apply the role with converge, verify with idempotence check (no changes on "
                "second run), run testinfra/inspec verify steps, then destroy. CI integration "
                "via molecule test in GitHub Actions ensures every PR is validated against "
                "multiple platforms."
            ),
            "scenario": (
                "Your PR for the 'redis_role' fails CI because: 1) ansible-lint flags "
                "'command: apt-get update' as risky, 2) Molecule's idempotence check fails — "
                "a task reports 'changed' on the second converge, 3) The verify step can't "
                "connect to Redis on port 6379 inside the test container. You have 30 minutes "
                "to fix all three before the release window closes."
            ),
            "question": ("What fixes address all three CI failures correctly?"),
            "options": [
                "Replace 'command: apt-get update' with the apt module's update_cache: yes; "
                "add 'changed_when: false' to a shell task reading existing state; "
                "expose port 6379 in molecule's create.yml platform config",
                "Add 'noqa: risky-shell' comment to suppress the lint warning; "
                "add 'always_run: yes' to make the task idempotent; "
                "use connection: local in molecule config to bypass container networking",
                "Wrap the command in a block with 'ignore_errors: yes'; "
                "add 'check_mode: no' to skip idempotence check for that task; "
                "install redis-tools in the verify playbook for connectivity",
                "Use shell module instead of command (shell allows pipes); "
                "add 'register: result' and 'changed_when: result.rc != 0'; "
                "set network_mode: host in molecule driver config",
            ],
            "answer": (
                "Replace 'command: apt-get update' with the apt module's update_cache: yes; "
                "add 'changed_when: false' to a shell task reading existing state; "
                "expose port 6379 in molecule's create.yml platform config"
            ),
            "explanation": (
                "1) ansible-lint flags raw 'command' usage because Ansible has idempotent modules. "
                "The apt module with 'update_cache: yes' is the correct replacement — it's declarative "
                "and idempotent. 2) Idempotence failures mean a task changes something on every run. "
                "A shell/command task that reads state (e.g. 'redis-cli ping') should use "
                "'changed_when: false' since reading never changes state. 3) Molecule test containers "
                "need exposed ports defined in molecule/default/create.yml under the platform's "
                "'published_ports' or 'exposed_ports' configuration."
            ),
            "badge": "Quality Gatekeeper",
            "loot": {
                "type": "potion",
                "name": "CI Unblocker",
                "description": "Auto-fixes one failed Molecule test per sprint",
            },
        },
        # ─────────────────────── INVENTORY (307-309) ─────────────────────────
        {
            "id": 307,
            "title": "Static vs Dynamic Inventory",
            "description": "Manage host inventories from simple INI files to cloud-native plugins",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Ansible inventory defines the hosts and groups your playbooks target. Static "
                "inventory uses INI or YAML files — simple but requires manual updates. Dynamic "
                "inventory scripts or plugins query cloud providers (AWS EC2, Azure RM, GCP), "
                "CMDBs, or any API that returns JSON. The inventory plugin system (Ansible 2.4+) "
                "uses YAML config files pointing to plugin types. Key patterns: use '_meta' for "
                "hostvars, group children for hierarchies, and 'compose' to create derived variables."
            ),
            "scenario": (
                "Your infrastructure spans AWS EC2 (3 AZs) and an on-premise vCenter cluster. "
                "You need a unified inventory that: auto-discovers EC2 instances tagged 'env:prod', "
                "groups them by the 'service' tag, adds the on-prem hosts from a static file, "
                "creates a parent 'production' group containing both, and sets 'ansible_user' "
                "to 'ec2-user' for AWS and 'ansible' for on-prem."
            ),
            "question": (
                "How do you configure a unified, tag-driven inventory for this hybrid setup?"
            ),
            "options": [
                "aws_ec2 inventory plugin YAML with keyed_groups on tag:service + filters on "
                "tag:env=prod; static INI file for vCenter hosts; constructed plugin to create "
                "'production' parent group; group_vars for per-environment ansible_user",
                "Single INI file with all hosts manually listed; a cron job that runs "
                "'aws ec2 describe-instances' and appends to the file hourly",
                "Use ansible-inventory CLI to merge AWS and vCenter outputs; write a shell "
                "wrapper that generates the combined JSON each run",
                "Terraform outputs JSON inventory after provisioning; Ansible reads it via "
                "the script inventory plugin",
            ],
            "answer": (
                "aws_ec2 inventory plugin YAML with keyed_groups on tag:service + filters on "
                "tag:env=prod; static INI file for vCenter hosts; constructed plugin to create "
                "'production' parent group; group_vars for per-environment ansible_user"
            ),
            "explanation": (
                "The aws_ec2 inventory plugin auto-discovers EC2 instances via AWS API. "
                "'filters: tag:env: prod' limits to production. 'keyed_groups' with "
                "'key: tags.service' auto-creates groups per service tag value. The "
                "constructed plugin merges AWS and static groups into a 'production' parent. "
                "group_vars/production.yml sets shared vars; host_vars/ or group_vars per "
                "sub-group overrides ansible_user. This is declarative, zero-code, and "
                "always up-to-date with EC2."
            ),
            "badge": "Inventory Architect",
            "loot": {
                "type": "relic",
                "name": "Cloud Compass",
                "description": "Auto-discovers all resources across cloud providers",
            },
        },
        {
            "id": 308,
            "title": "group_vars, host_vars & Variable Precedence",
            "description": "Master Ansible's hierarchical variable resolution system",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Ansible resolves variables through a strict precedence chain (lowest to highest): "
                "role defaults < inventory file < group_vars/all < group_vars/parent_group < "
                "group_vars/child_group < host_vars/hostname < play vars < role vars < block vars < "
                "task vars < set_fact < include_vars < registered vars < role params < extra vars (-e). "
                "The 'hash_behaviour' setting (merge vs replace) affects how dictionaries from "
                "different levels combine. Use 'ansible-inventory --graph' to visualise the "
                "hierarchy and '--host HOST' to see resolved variables."
            ),
            "scenario": (
                "Your inventory structure: 'all' > 'datacenter' > 'webservers' > 'frontend'. "
                "The frontend group has host 'fe01' which should use port 8443 instead of the "
                "default 443. All webservers use SSL; all datacenter hosts share an NTP server; "
                "but one developer overrides the port to 8080 via '-e' for testing. What port "
                "does fe01 get in normal vs dev-test runs?"
            ),
            "question": (
                "With group_vars/webservers setting https_port: 443 and host_vars/fe01 setting "
                "https_port: 8443, what port does fe01 use, and why?"
            ),
            "options": [
                "8443 — host_vars has higher precedence than group_vars. With extra vars (-e), "
                "port becomes 8080 because extra vars are absolute highest",
                "443 — group_vars takes precedence over host_vars because groups contain hosts; "
                "extra vars only override if hash_behaviour is set to merge",
                "8443 normally, but 443 with extra vars because extra vars explicitly override "
                "only role defaults, not host_vars",
                "The play fails — Ansible detects conflicting variables at different hierarchy "
                "levels and requires explicit resolution",
            ],
            "answer": (
                "8443 — host_vars has higher precedence than group_vars. With extra vars (-e), "
                "port becomes 8080 because extra vars are absolute highest"
            ),
            "explanation": (
                "Variable precedence: host_vars > group_vars > inventory. So host_vars/fe01 (8443) "
                "overrides group_vars/webservers (443). However, extra vars (-e https_port=8080) "
                "sit at the ABSOLUTE TOP of the precedence chain — they override everything including "
                "host_vars, set_fact, and registered vars. This makes -e perfect for one-off "
                "overrides like developer testing, but dangerous for production if misused. "
                "The inventory hierarchy is: all < datacenter < webservers < frontend, so "
                "group_vars/frontend would override group_vars/webservers for hosts in the "
                "frontend group."
            ),
            "badge": "Variable Sage",
            "loot": {
                "type": "relic",
                "name": "Precedence Prism",
                "description": "Shows the resolved value source for any variable in real-time",
            },
        },
        {
            "id": 309,
            "title": "Inventory Plugins: AWX, Terraform & ServiceNow",
            "description": "Connect Ansible to external sources of truth for inventory",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Modern infrastructure uses external sources of truth: AWX/AAP Controller "
                "maintains inventories with smart filters; Terraform state tracks provisioned "
                "resources; ServiceNow CMDB holds IT asset records. Ansible's inventory plugin "
                "system connects to all of them. The 'tfmigrate' or terraform_state plugin "
                "parses tfstate files. The 'servicenow.itsm' collection provides a ServiceNow "
                "inventory plugin. AWX/AAP uses its own inventory API with 'smart inventories' "
                "that filter hosts programmatically across multiple sources."
            ),
            "scenario": (
                "Your org has: 1) Terraform managing AWS EKS clusters — cluster endpoint IPs "
                "are in tfstate, 2) ServiceNow CMDB tracking which apps run on which clusters, "
                "3) An on-prem DC with hosts managed in AWX. You need a playbook that targets "
                "'all production Kubernetes control planes, regardless of cloud or on-prem' — "
                "using the authoritative source for each."
            ),
            "question": (
                "How should you construct the unified inventory for a cross-source production "
                "control plane target?"
            ),
            "options": [
                "Multiple inventory sources in ansible.cfg or AWX: terraform_state plugin for "
                "EKS endpoints (filter: outputs matching 'control_plane'), servicenow.itsm "
                "plugin for CMDB apps tagged 'prod+k8s-cp', AWX inventory for on-prem clusters. "
                "Use a 'constructed' plugin to union them into a 'k8s_control_planes' group",
                "Export all inventory sources to CSV, import into a single static INI file; "
                "update via a weekly CI job that pulls from each source",
                "Use add_host in a pre-task playbook that queries Terraform output, ServiceNow "
                "REST API, and AWX API — dynamically building inventory at runtime",
                "Deploy Ansible Automation Platform with a single Execution Environment; "
                "AAP auto-discovers all sources via its universal inventory connector",
            ],
            "answer": (
                "Multiple inventory sources in ansible.cfg or AWX: terraform_state plugin for "
                "EKS endpoints (filter: outputs matching 'control_plane'), servicenow.itsm "
                "plugin for CMDB apps tagged 'prod+k8s-cp', AWX inventory for on-prem clusters. "
                "Use a 'constructed' plugin to union them into a 'k8s_control_planes' group"
            ),
            "explanation": (
                "Each inventory plugin handles one source of truth. terraform_state reads .tfstate "
                "files (or remote state backends) to extract resource attributes. The servicenow.itsm "
                "plugin queries CMDB via API with query filters (e.g., 'cmdb_ci_appl tagged prod'). "
                "AWX/AAP natively manages its own inventory. The 'constructed' plugin unifies them "
                "— it creates new groups from existing ones using Jinja2 expressions. All three "
                "sources stay authoritative; there's no sync lag or manual CSV export. AWX 'smart "
                "inventories' can also do this by filtering across multiple regular inventories."
            ),
            "badge": "Source of Truth",
            "loot": {
                "type": "relic",
                "name": "Unified Lens",
                "description": "Queries all inventory sources from a single playbook",
            },
        },
        # ─────────────────────── VAULT (310-312) ─────────────────────────────
        {
            "id": 310,
            "title": "Ansible Vault — Encrypt, Decrypt & Rekey",
            "description": "Protect secrets at rest with Ansible's built-in encryption",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Ansible Vault encrypts files at rest using AES-256-CBC. Commands: "
                "'ansible-vault create', 'encrypt' (existing file), 'view', 'edit', 'decrypt', "
                "'rekey' (change password). The vault password can come from: --ask-vault-pass "
                "(interactive), --vault-password-file (script or file), or the ANSIBLE_VAULT_PASSWORD_FILE "
                "environment variable. Best practice: encrypt only sensitive vars files "
                "(group_vars/all/vault.yml, host_vars/HOST/vault.yml), not entire playbooks. "
                "Use 'ansible-vault encrypt_string' to encrypt individual values for inline use."
            ),
            "scenario": (
                "Your team accidentally committed an unencrypted 'secrets.yml' containing "
                "database passwords and API keys to the Git repository. You need to: "
                "1) Rotate all compromised credentials, 2) Encrypt the new values, 3) Ensure "
                "this never happens again with a pre-commit hook, 4) The CI pipeline must "
                "be able to decrypt the vault for testing — but the vault password can't be "
                "in the repo."
            ),
            "question": (
                "What is the correct workflow to recover from the leak and prevent recurrence?"
            ),
            "options": [
                "Rotate all credentials; encrypt new secrets.yml with ansible-vault encrypt; "
                "add a pre-commit hook checking for unencrypted secrets; CI pipeline gets the "
                "vault password from a CI secret variable and writes it to a file referenced "
                "by --vault-password-file",
                "Delete the Git history with git filter-branch; move secrets to environment "
                "variables only; use lookup('env', 'SECRET') everywhere instead of Vault",
                "Encrypt the entire repo with ansible-vault; share the password via Slack to "
                "the team; CI uses --ask-vault-pass with expect script",
                "Convert to HashiCorp Vault (the external secret store); remove ansible-vault "
                "entirely; use lookup('hashi_vault') for all secrets",
            ],
            "answer": (
                "Rotate all credentials; encrypt new secrets.yml with ansible-vault encrypt; "
                "add a pre-commit hook checking for unencrypted secrets; CI pipeline gets the "
                "vault password from a CI secret variable and writes it to a file referenced "
                "by --vault-password-file"
            ),
            "explanation": (
                "1) Rotate first — the old credentials are compromised regardless. 2) Encrypt "
                "the file with 'ansible-vault encrypt secrets.yml' (AES-256). 3) A pre-commit "
                "hook can grep for patterns like 'password:', 'api_key:', 'secret:' and reject "
                "unencrypted files. 4) CI stores the vault password as a protected variable "
                "(e.g., GitHub Secrets, GitLab CI Variables), writes it to a temp file, and "
                "passes '--vault-password-file /tmp/vault_pass' to ansible-playbook. HashiCorp "
                "Vault is a valid alternative but ansible-vault is simpler for small teams. "
                "Never commit .vault_pass files or share passwords in chat."
            ),
            "badge": "Vault Guardian",
            "loot": {
                "type": "relic",
                "name": "Vault Seal",
                "description": "Auto-encrypts newly created variable files",
            },
        },
        {
            "id": 311,
            "title": "Multi-Vault & vault-id Workflows",
            "description": "Manage multiple vault passwords for different environments",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Large organisations need multiple vault passwords: dev/staging/prod can't share "
                "the same encryption key. Ansible supports 'vault-id' labels: 'ansible-vault encrypt "
                "--vault-id prod@prompt secrets.yml'. A single file can even have values encrypted "
                "with different vault-ids. The 'encrypt_string' command with --vault-id creates "
                "inline encrypted variables tagged with the vault-id. During playbook execution, "
                "pass multiple --vault-id options, each with its own password source. AWX/AAP "
                "supports vault-id natively in credential management."
            ),
            "scenario": (
                "Your org has three environments with separate vault passwords. The 'db_password' "
                "variable in group_vars/all/vault.yml must be encrypted such that: the dev team "
                "can decrypt with the 'dev' vault-id, the staging pipeline uses 'staging' vault-id, "
                "and production uses 'prod' vault-id — all from the SAME vault file. You also "
                "need to rekey the prod password quarterly per compliance."
            ),
            "question": (
                "How do you set up multi-vault-id encryption for a shared vault file across "
                "three environments?"
            ),
            "options": [
                "Group variables by vault-id in separate vault files: group_vars/all/vault-dev.yml "
                "(encrypted with dev vault-id), vault-staging.yml, vault-prod.yml. Each environment "
                "uses --vault-id ENV@password_file to decrypt only its file. Rekey prod with "
                "'ansible-vault rekey --vault-id prod@prompt vault-prod.yml'",
                "Encrypt the entire vault.yml three separate times with each password; Ansible "
                "auto-detects which to use based on the target environment variable",
                "Use a single vault password; control access to the password file via filesystem "
                "permissions in each environment's CI",
                "Inline encrypt each variable with 'ansible-vault encrypt_string --vault-id "
                "dev@prompt', 'staging@prompt', 'prod@prompt' — all in one file. The vault-id "
                "label in the !vault tag determines which password decrypts each",
            ],
            "answer": (
                "Inline encrypt each variable with 'ansible-vault encrypt_string --vault-id "
                "dev@prompt', 'staging@prompt', 'prod@prompt' — all in one file. The vault-id "
                "label in the !vault tag determines which password decrypts each"
            ),
            "explanation": (
                "ansible-vault encrypt_string --vault-id dev@prompt creates an inline encrypted "
                "value wrapped in '!vault |' with a vault-id label. Multiple vault-ids can coexist "
                "in one file — each value's header identifies which vault-id encrypted it. During "
                "execution, 'ansible-playbook --vault-id dev@password_file --vault-id staging@..."
                "--vault-id prod@...' provides all three passwords. Ansible decrypts each variable "
                "with the matching vault-id. For rekeying prod: 'ansible-vault rekey --vault-id "
                "prod@prompt vault.yml' rewrites only the prod-encrypted values with a new password. "
                "Separate files per environment (option 1) is simpler but duplicates the variable "
                "definitions."
            ),
            "badge": "Multi-Vault Master",
            "loot": {
                "type": "relic",
                "name": "Key Ring",
                "description": "Manages all vault passwords for every environment",
            },
        },
        {
            "id": 312,
            "title": "Secrets Management: Vault + AWX + External Secret Stores",
            "description": "Integrate Ansible Vault with enterprise secret management",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "Enterprise secret management goes beyond file encryption. Ansible Automation "
                "Platform (AWX/AAP) integrates with: HashiCorp Vault, Azure Key Vault, AWS "
                "Secrets Manager, CyberArk Conjur, and Thycotic. Credential Types in AWX map "
                "external secrets to Ansible variables. The 'community.hashi_vault' lookup "
                "plugin fetches secrets at runtime instead of storing them in vault files. "
                "Best practice: use ansible-vault for simple cases (<5 environments, small "
                "team), external stores when you need audit trails, dynamic rotation, or "
                "compliance (PCI-DSS, SOC2). Both can coexist — vault for non-sensitive "
                "config, external stores for credentials."
            ),
            "scenario": (
                "Your CISO mandates: 1) All database credentials must rotate every 90 days "
                "automatically, 2) Access to production secrets requires an audit trail, "
                "3) Developers must not see production credentials — they use their own "
                "dev environment values, 4) The pipeline must fetch secrets at deploy time, "
                "not store them in the repo (encrypted or not). Your org already has "
                "HashiCorp Vault deployed."
            ),
            "question": (
                "Which architecture satisfies the CISO's four requirements using your existing "
                "HashiCorp Vault?"
            ),
            "options": [
                "Store secrets in HashiCorp Vault with auto-rotation policies; use "
                "community.hashi_vault.hashi_vault lookup in playbooks to fetch at runtime; "
                "Vault audit backend logs all production access; devs use separate KV v2 "
                "paths with their own credentials; pipeline authenticates via AppRole",
                "Encrypt secrets with ansible-vault, store in repo; use AWX credentials to "
                "inject at runtime; CISO requirement satisfied by quarterly git audit of "
                "who accessed the vault file",
                "Move all secrets to environment variables set by the CI pipeline; HashiCorp "
                "Vault syncs to CI variables via a custom plugin; audit is via CI logs",
                "Each developer has their own vault password; production vault password is "
                "split into three shares (Shamir's Secret Sharing); CISO approves each "
                "production deployment manually",
            ],
            "answer": (
                "Store secrets in HashiCorp Vault with auto-rotation policies; use "
                "community.hashi_vault.hashi_vault lookup in playbooks to fetch at runtime; "
                "Vault audit backend logs all production access; devs use separate KV v2 "
                "paths with their own credentials; pipeline authenticates via AppRole"
            ),
            "explanation": (
                "1) HashiCorp Vault's database secret engine auto-rotates credentials every 90 "
                "days via its backend integration — no manual intervention. 2) Vault's audit "
                "backend (file, syslog, or socket) logs every access, read, and modification "
                "to production secrets — satisfying the audit trail requirement. 3) Devs access "
                "a separate KV v2 mount or namespace with dev-only secrets. 4) The Ansible "
                "lookup plugin fetches secrets at runtime via 'lookup('community.hashi_vault."
                "hashi_vault', 'secret/data/prod/db')' — secrets never touch the repo, encrypted "
                "or not. The CI pipeline authenticates to Vault via AppRole (machine identity) "
                "with a wrapped secret_id. This architecture meets PCI-DSS and SOC2 requirements."
            ),
            "badge": "Secrets Sovereign",
            "loot": {
                "type": "relic",
                "name": "Zero-Knowledge Key",
                "description": "One free secret rotation per sprint — no downtime",
            },
        },
    ]
