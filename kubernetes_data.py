"""
Cloud Orbit — Kubernetes Platform Lessons
CKA / CKAD quality scenario-based questions.
Lesson IDs 101-120  |  4 sectors  |  20 lessons
"""


def get_lessons():
    """Return Kubernetes lesson list (IDs 101-120)."""
    return [

        # ─────────────────────── CORE CONCEPTS (101-105) ────────────────────────
        {
            "id": 101,
            "title": "Pods & Multi-Container Patterns",
            "description": "Master Pod design and the sidecar / ambassador / adapter patterns",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "A Pod is the smallest deployable unit in Kubernetes. Containers inside "
                "a Pod share the same network namespace and can communicate via localhost. "
                "Common multi-container patterns: Sidecar (logging/proxy alongside main), "
                "Ambassador (proxy external traffic), Adapter (transform output format)."
            ),
            "scenario": (
                "Your team deploys a web app Pod. The app writes logs to /var/log/app.log "
                "but your central logging system only accepts logs via HTTP. You need to "
                "forward those file-based logs without modifying the application container."
            ),
            "question": (
                "Which multi-container Pod pattern ships /var/log/app.log to an HTTP "
                "logging endpoint without changing the application image?"
            ),
            "options": [
                "Init container — runs the log-shipper once at startup before the app",
                "Sidecar container — runs log-shipper alongside the app, sharing the log volume",
                "Ambassador container — proxies external HTTP requests into the Pod",
                "Ephemeral container — attaches log-shipper dynamically at runtime",
            ],
            "answer": "Sidecar container — runs log-shipper alongside the app, sharing the log volume",
            "explanation": (
                "The Sidecar pattern places a helper container in the same Pod that shares a volume "
                "with the main container. The sidecar mounts /var/log, tails app.log, and ships it "
                "over HTTP. Init containers run once before the app starts — they cannot tail live "
                "logs. Ambassadors proxy inbound traffic, not outbound log shipping."
            ),
            "badge": "Pod Architect",
            "loot": {
                "type": "relic",
                "name": "Sidecar Lens",
                "description": "Reveals hidden log streams in any container cluster",
            },
        },
        {
            "id": 102,
            "title": "Deployments & Rolling Updates",
            "description": "Control rollouts, rollbacks, and update strategies",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "Deployments manage ReplicaSets and provide declarative update strategies. "
                "RollingUpdate (default) replaces Pods incrementally using maxUnavailable and "
                "maxSurge. Recreate terminates all Pods before creating new ones. "
                "`kubectl rollout undo` reverts to the previous revision instantly."
            ),
            "scenario": (
                "You push a new image to your Deployment. After 3 Pods update, monitoring "
                "shows a spike in 500 errors from the new version. The rollout is still "
                "in progress. You need to restore the previous working version immediately."
            ),
            "question": (
                "What is the FASTEST way to restore service to the previous working version "
                "while the rolling update is still in progress?"
            ),
            "options": [
                "Delete the Deployment and re-apply the old manifest from source control",
                "Scale the Deployment to 0, update the image tag, scale back up",
                "kubectl rollout undo deployment/<name> — reverts to the previous revision",
                "Edit the Deployment spec's imageTag in-place via kubectl patch",
            ],
            "answer": "kubectl rollout undo deployment/<name> — reverts to the previous revision",
            "explanation": (
                "kubectl rollout undo atomically swaps the current ReplicaSet with the previous one, "
                "triggering a reverse rolling update. It works even mid-rollout. Deleting the "
                "Deployment causes downtime. Scaling to 0 causes downtime. kubectl patch achieves "
                "the same outcome but is slower and requires knowing the old tag."
            ),
            "badge": "Rollback Master",
            "loot": {
                "type": "potion",
                "name": "Rollback Elixir",
                "description": "Instantly reverts any deployment to its last stable state",
            },
        },
        {
            "id": 103,
            "title": "Services — ClusterIP, NodePort, LoadBalancer",
            "description": "Expose Pods with stable network endpoints",
            "room_type": "elite",
            "difficulty": "medium",
            "reward_type": "relic",
            "content": (
                "Services provide stable IPs and DNS for Pod sets selected by labels. "
                "ClusterIP (default): only reachable inside the cluster. "
                "NodePort: opens a port (30000-32767) on every node. "
                "LoadBalancer: provisions a cloud load balancer. "
                "ExternalName: maps to an external DNS name."
            ),
            "scenario": (
                "You have a three-tier app on a managed cloud Kubernetes cluster. "
                "The React frontend must be reachable from the internet. The backend API "
                "must only be reachable from the frontend Pods. The database must only be "
                "reachable from the backend Pods."
            ),
            "question": (
                "Which combination of Service types correctly implements this three-tier "
                "isolation model?"
            ),
            "options": [
                "Frontend: NodePort / Backend: NodePort / Database: ClusterIP",
                "Frontend: LoadBalancer / Backend: ClusterIP / Database: ClusterIP",
                "Frontend: LoadBalancer / Backend: LoadBalancer / Database: NodePort",
                "Frontend: ExternalName / Backend: ClusterIP / Database: ClusterIP",
            ],
            "answer": "Frontend: LoadBalancer / Backend: ClusterIP / Database: ClusterIP",
            "explanation": (
                "LoadBalancer provisions an internet-facing IP for the frontend via the cloud "
                "provider. ClusterIP for backend and database means they are only reachable inside "
                "the cluster, enforcing isolation. NodePort on backend or database would expose "
                "those services on every node's public IP, violating the isolation requirement."
            ),
            "badge": "Network Architect",
            "loot": {
                "type": "relic",
                "name": "Service Mesh Crystal",
                "description": "Grants mastery over internal and external traffic routing",
            },
        },
        {
            "id": 104,
            "title": "ConfigMaps & Secrets — Live Reload",
            "description": "Decouple configuration and sensitive data from container images",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "ConfigMaps store non-sensitive key-value data. Secrets store sensitive data "
                "(base64-encoded; enable EncryptionConfiguration for encryption at rest). "
                "When mounted as volumes, both update automatically within ~60s (kubelet sync). "
                "When injected as environment variables, they are copied at Pod creation "
                "and DO NOT update while the Pod is running."
            ),
            "scenario": (
                "Your app reads a database password from an environment variable at startup. "
                "Security requires the password be rotated every 30 days. After rotation, "
                "running Pods must use the new value without a full redeployment."
            ),
            "question": (
                "Which approach allows a Kubernetes Secret to update in a running Pod "
                "WITHOUT a Pod restart or redeployment?"
            ),
            "options": [
                "Inject the Secret as an env var — env vars update automatically on Secret change",
                "Mount the Secret as a volume — the file updates within ~60s (kubelet sync period)",
                "Use a ConfigMap instead of a Secret — ConfigMaps support live reload, Secrets don't",
                "Annotate the Pod with a secret-checksum — Kubernetes triggers a rolling update",
            ],
            "answer": "Mount the Secret as a volume — the file updates within ~60s (kubelet sync period)",
            "explanation": (
                "Volume-mounted Secrets and ConfigMaps are kept in sync by the kubelet (default 60s). "
                "The app can watch the mounted file and reload credentials without restarting. "
                "Environment variables from Secrets are copied at Pod creation and NEVER update "
                "while the Pod is running — a restart is required. ConfigMaps and Secrets behave "
                "identically for this: both update via volumes, neither updates via env vars."
            ),
            "badge": "Secrets Guardian",
            "loot": {
                "type": "relic",
                "name": "Vault Keyring",
                "description": "Automatically distributes and rotates secrets across the cluster",
            },
        },
        {
            "id": 105,
            "title": "Namespaces & Resource Quotas",
            "description": "Partition clusters and enforce resource limits per team",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Namespaces partition cluster resources. ResourceQuota limits total CPU/memory/"
                "object counts per namespace. LimitRange sets default and maximum per-container "
                "limits. RBAC can be scoped to a namespace. kube-system, kube-public, and "
                "default namespaces exist by default."
            ),
            "scenario": (
                "You manage a shared cluster for 3 teams: frontend, backend, data. The data team "
                "runs ML batch jobs that have previously consumed all cluster CPU, starving others. "
                "Data team jobs must still run but must not exceed 50% of total cluster CPU. "
                "Containers without explicit requests currently crash the scheduler."
            ),
            "question": (
                "Which combination of Kubernetes objects BEST solves this multi-team "
                "resource isolation problem?"
            ),
            "options": [
                "One Namespace per team + ResourceQuota on the data namespace + LimitRange with defaults",
                "One Namespace for all teams + PodDisruptionBudget per team + PriorityClass for data",
                "Separate clusters per team — namespace quotas cannot prevent cross-team starvation",
                "Taint nodes for the data team + toleration on data Pods + no quotas needed",
            ],
            "answer": "One Namespace per team + ResourceQuota on the data namespace + LimitRange with defaults",
            "explanation": (
                "ResourceQuota on the data namespace sets a hard CPU ceiling preventing starvation. "
                "LimitRange provides default requests/limits so containers without explicit values "
                "are not rejected by the scheduler. Separate namespaces give each team isolated "
                "RBAC and quota scopes. Taints control scheduling placement but not CPU consumption. "
                "PodDisruptionBudgets protect availability, not resource consumption."
            ),
            "badge": "Namespace Commander",
            "loot": {
                "type": "legendary_relic",
                "name": "Quota Crown",
                "description": "Legendary: enforces perfect resource balance across any cluster",
            },
        },

        # ──────────────────────────── WORKLOADS (106-110) ────────────────────────
        {
            "id": 106,
            "title": "DaemonSets — Node-level Agents",
            "description": "Run exactly one Pod per node for cluster-wide agents",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "DaemonSets ensure one Pod runs on every (or selected) node. Common uses: "
                "log collectors (Fluentd), monitoring (Prometheus node-exporter), "
                "network plugins (CNI), storage drivers. When a new node joins the cluster, "
                "the DaemonSet Pod is automatically scheduled on it."
            ),
            "scenario": (
                "You need Prometheus node-exporter on every node, including nodes added by "
                "the cluster autoscaler. The exporter must also run on control-plane nodes "
                "that have the node-role.kubernetes.io/control-plane:NoSchedule taint."
            ),
            "question": (
                "Which DaemonSet configuration ensures node-exporter runs on ALL nodes "
                "including tainted control-plane nodes?"
            ),
            "options": [
                "Set nodeSelector: kubernetes.io/os: linux — matches all nodes including masters",
                "Add a toleration for node-role.kubernetes.io/control-plane:NoSchedule in the Pod spec",
                "Use a Deployment with requiredDuringSchedulingIgnoredDuringExecution affinity",
                "Set hostNetwork: true — this bypasses taints and schedules on all nodes",
            ],
            "answer": "Add a toleration for node-role.kubernetes.io/control-plane:NoSchedule in the Pod spec",
            "explanation": (
                "Taints prevent Pods from being scheduled unless the Pod has a matching toleration. "
                "Control-plane nodes have a NoSchedule taint by default. Adding a toleration for "
                "node-role.kubernetes.io/control-plane:NoSchedule allows the DaemonSet Pod to "
                "land on those nodes. nodeSelector doesn't bypass taints. hostNetwork controls "
                "network isolation, not scheduling. A Deployment doesn't guarantee one-per-node."
            ),
            "badge": "Node Agent Master",
            "loot": {
                "type": "relic",
                "name": "DaemonSet Beacon",
                "description": "Ensures monitoring coverage on every node in any cluster",
            },
        },
        {
            "id": 107,
            "title": "StatefulSets — Ordered, Persistent Workloads",
            "description": "Deploy stateful applications with stable identity and storage",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "StatefulSets provide stable, unique Pod names (app-0, app-1...), stable network "
                "identities via headless Services, and ordered deployment/scaling. Each Pod gets "
                "its own PersistentVolumeClaim via volumeClaimTemplates. Ideal for databases, "
                "message queues, and distributed systems requiring stable peer discovery."
            ),
            "scenario": (
                "You're deploying a 3-node Cassandra ring. Each node needs its own persistent "
                "storage that survives Pod rescheduling, a stable DNS hostname for peer discovery, "
                "and must start in order (0 → 1 → 2) to bootstrap the ring correctly."
            ),
            "question": (
                "Which Kubernetes objects are REQUIRED to deploy the Cassandra ring with "
                "stable identity, per-Pod storage, and ordered startup?"
            ),
            "options": [
                "Deployment + PersistentVolume (manually provisioned) + ClusterIP Service",
                "StatefulSet + volumeClaimTemplates + Headless Service (clusterIP: None)",
                "StatefulSet + ConfigMap for storage paths + NodePort Service",
                "DaemonSet + PersistentVolumeClaim + ClusterIP Service",
            ],
            "answer": "StatefulSet + volumeClaimTemplates + Headless Service (clusterIP: None)",
            "explanation": (
                "StatefulSet provides ordered startup (0→1→2) and stable Pod names. "
                "volumeClaimTemplates automatically provisions a unique PVC per Pod that persists "
                "across rescheduling. A Headless Service (clusterIP: None) creates individual DNS "
                "entries (cassandra-0.cassandra, cassandra-1.cassandra) for peer discovery. "
                "A Deployment doesn't guarantee ordering or stable names. DaemonSet places "
                "one Pod per node — not N replicas with individual storage."
            ),
            "badge": "StatefulSet Sage",
            "loot": {
                "type": "relic",
                "name": "Persistent Identity Gem",
                "description": "Grants stable network identity to any stateful workload",
            },
        },
        {
            "id": 108,
            "title": "Horizontal Pod Autoscaler & KEDA",
            "description": "Auto-scale Pods based on CPU, memory, or custom event metrics",
            "room_type": "battle",
            "difficulty": "hard",
            "reward_type": "knowledge_card",
            "content": (
                "HPA adjusts replica count based on observed metrics vs a target. "
                "Requires metrics-server for CPU/memory. Custom metrics (queue depth, RPS) "
                "require a custom metrics API adapter. KEDA extends HPA to event sources "
                "(SQS, Kafka, Redis, Prometheus). Scale-down has a cooldown to prevent flapping."
            ),
            "scenario": (
                "Your API Deployment processes messages from an SQS queue. CPU stays low even "
                "during backlogs because the bottleneck is queue depth, not CPU. You need "
                "Pods to scale with queue depth. The cluster runs on EKS."
            ),
            "question": (
                "What is required to make HPA scale your Deployment based on SQS queue depth?"
            ),
            "options": [
                "Set targetCPUUtilizationPercentage: 10 — simulates queue pressure via CPU proxy",
                "Install KEDA — provides an SQS ScaledObject that bridges queue depth into HPA",
                "Use a CronJob that runs kubectl scale when a CloudWatch alarm triggers",
                "Switch to VPA (Vertical Pod Autoscaler) — VPA supports external queue metrics",
            ],
            "answer": "Install KEDA — provides an SQS ScaledObject that bridges queue depth into HPA",
            "explanation": (
                "KEDA extends Kubernetes HPA with support for external event sources including SQS. "
                "A ScaledObject points at the SQS queue; KEDA bridges queue depth into the custom "
                "metrics API, and HPA scales Pods based on that value. Low CPU target is a hack "
                "that doesn't reflect true demand. CronJob scaling is manual and imprecise. VPA "
                "adjusts CPU/memory per Pod — it doesn't scale replica counts."
            ),
            "badge": "Autoscaling Architect",
            "loot": {
                "type": "relic",
                "name": "KEDA Compass",
                "description": "Scales any workload from any event source — queues, streams, databases",
            },
        },
        {
            "id": 109,
            "title": "Jobs, CronJobs & concurrencyPolicy",
            "description": "Run batch and scheduled workloads reliably to completion",
            "room_type": "elite",
            "difficulty": "medium",
            "reward_type": "relic",
            "content": (
                "Jobs run Pods until a specified number complete successfully. "
                "CronJobs create Jobs on a schedule. backoffLimit sets retry attempts. "
                "ttlSecondsAfterFinished auto-cleans completed Jobs. "
                "concurrencyPolicy: Allow (default) / Forbid (skip new run if prev running) "
                "/ Replace (cancel prev run, start new one)."
            ),
            "scenario": (
                "Your nightly database backup CronJob takes 40 minutes. The schedule fires "
                "every 30 minutes to catch up after failures. You've seen two backup jobs "
                "running simultaneously, causing data corruption and doubled storage costs."
            ),
            "question": (
                "Which CronJob setting prevents two backup jobs from running simultaneously?"
            ),
            "options": [
                "Set backoffLimit: 0 — failed jobs won't retry, preventing parallel runs",
                "Set concurrencyPolicy: Forbid — skips a new run if the previous is still running",
                "Set parallelism: 1 — limits each Job to one Pod at a time",
                "Set successfulJobsHistoryLimit: 1 — keeps only one completed job record",
            ],
            "answer": "Set concurrencyPolicy: Forbid — skips a new run if the previous is still running",
            "explanation": (
                "concurrencyPolicy: Forbid tells the CronJob controller to skip scheduling a new Job "
                "if the previous Job hasn't finished yet. This is the exact guard against overlapping "
                "backup runs. backoffLimit controls retries on failure, not concurrency between runs. "
                "parallelism controls Pod count within a single Job. successfulJobsHistoryLimit "
                "controls history retention — unrelated to preventing overlap."
            ),
            "badge": "Batch Processing Pro",
            "loot": {
                "type": "relic",
                "name": "Concurrency Lock",
                "description": "Prevents any two batch processes from conflicting during critical ops",
            },
        },
        {
            "id": 110,
            "title": "Resource Requests, Limits & QoS Classes",
            "description": "Guarantee and constrain compute resources for stable workloads",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "requests: what the scheduler reserves on the node. limits: hard cap on usage. "
                "QoS classes: Guaranteed (req==limit), Burstable (req<limit), BestEffort (none). "
                "OOMKiller evicts BestEffort first, then Burstable, then Guaranteed. "
                "CPU is compressible (throttled); memory is not (OOMKilled if limit exceeded). "
                "LimitRange sets defaults so every container has a request/limit."
            ),
            "scenario": (
                "A production payment service Pod keeps getting OOMKilled during peak traffic. "
                "The Pod's memory limit is 256Mi but profiling shows it occasionally needs 512Mi. "
                "You need to prevent OOMKills without over-provisioning permanently. "
                "The node has 4Gi free memory."
            ),
            "question": (
                "Which resource configuration prevents OOMKills while giving the Pod the highest "
                "eviction protection and the exact headroom it needs?"
            ),
            "options": [
                "Remove the memory limit — the Pod uses what it needs, no OOMKill possible",
                "Set memory request: 256Mi, limit: 512Mi — Burstable QoS allows burst to limit",
                "Set memory request: 512Mi, limit: 512Mi — Guaranteed QoS, 512Mi always reserved",
                "Set memory request: 128Mi, limit: 256Mi — tighter limit forces app optimisation",
            ],
            "answer": "Set memory request: 512Mi, limit: 512Mi — Guaranteed QoS, 512Mi always reserved",
            "explanation": (
                "Guaranteed QoS (request == limit) gives the Pod the highest eviction protection — "
                "it is the last to be evicted under memory pressure. Setting both to 512Mi ensures "
                "the node always reserves 512Mi for this Pod and the OOMKiller won't kill it up to "
                "that limit. Removing the limit risks unbounded memory consumption. Burstable QoS "
                "risks earlier eviction. A tighter limit makes OOMKills more frequent."
            ),
            "badge": "Resource Wizard",
            "loot": {
                "type": "legendary_relic",
                "name": "Guaranteed QoS Shield",
                "description": "Legendary: your Pods are last to be evicted under any memory pressure",
            },
        },

        # ──────────────────────────── NETWORKING (111-115) ───────────────────────
        {
            "id": 111,
            "title": "Ingress & TLS Termination",
            "description": "Route external HTTP/S traffic to Services with one load balancer",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Ingress manages external HTTP/S access to Services. An Ingress Controller "
                "(nginx, traefik, AWS ALB) implements the rules. Rules match by host or path. "
                "TLS termination uses a Secret with cert+key. cert-manager automates "
                "TLS cert issuance and renewal via Let's Encrypt."
            ),
            "scenario": (
                "Your cluster hosts app.example.com (frontend) and api.example.com (backend). "
                "Both need HTTPS with auto-renewing Let's Encrypt certs via a single cloud "
                "load balancer entry point."
            ),
            "question": (
                "Which combination correctly implements single-entry-point HTTPS for both "
                "subdomains with automated certificate management?"
            ),
            "options": [
                "Two LoadBalancer Services (one per subdomain) + manual cert rotation",
                "One Ingress with host-based rules + cert-manager ClusterIssuer + TLS Secret per host",
                "One NodePort Service + external nginx + manual cert renewal script",
                "Two Ingress objects (one per subdomain) + wildcard TLS Secret shared between them",
            ],
            "answer": "One Ingress with host-based rules + cert-manager ClusterIssuer + TLS Secret per host",
            "explanation": (
                "A single Ingress with host-based routing sends app.example.com to the frontend "
                "Service and api.example.com to the backend — one cloud LB IP. cert-manager watches "
                "Ingress TLS annotations, requests certs from Let's Encrypt, and stores them in "
                "Secrets the Ingress Controller uses for TLS termination. Two LoadBalancer Services "
                "waste IPs and cost extra. NodePort exposes every node's IP."
            ),
            "badge": "Ingress Master",
            "loot": {
                "type": "relic",
                "name": "TLS Crown",
                "description": "Auto-provisions and rotates TLS certs for any hostname",
            },
        },
        {
            "id": 112,
            "title": "NetworkPolicy — Zero-Trust Networking",
            "description": "Enforce allow-list traffic rules between Pods and namespaces",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "NetworkPolicy uses label selectors to define which Pods can communicate. "
                "By default all Pod traffic is allowed. Once ANY NetworkPolicy selects a Pod, "
                "only explicitly allowed traffic is permitted for that Pod. Rules apply to "
                "ingress and egress separately. Requires a CNI plugin (Calico, Cilium, Weave)."
            ),
            "scenario": (
                "Three Pods: frontend (app: frontend), backend (app: backend), db (app: db). "
                "Rules: frontend→backend allowed; backend→db allowed; frontend→db DENIED; "
                "nothing external can reach backend or db directly."
            ),
            "question": (
                "Which NetworkPolicy on the db Pod ensures ONLY the backend can reach it?"
            ),
            "options": [
                "Egress policy on backend Pod allowing traffic to app: db",
                "Ingress policy on db Pod with podSelector: app: backend as the only allowed source",
                "Ingress policy on db Pod with namespaceSelector matching the backend namespace",
                "Both egress on backend AND ingress on db — bidirectional policies are required",
            ],
            "answer": "Ingress policy on db Pod with podSelector: app: backend as the only allowed source",
            "explanation": (
                "NetworkPolicy is applied to the selected Pod (db) and controls who can initiate "
                "connections to it. An ingress rule with podSelector: {app: backend} allows ONLY "
                "backend Pods as sources. All other Pods, including frontend, are denied. An egress "
                "policy on backend is NOT required — the ingress on db is sufficient. "
                "namespaceSelector alone is too broad (allows any Pod in the namespace)."
            ),
            "badge": "Zero-Trust Guardian",
            "loot": {
                "type": "relic",
                "name": "Network Fortress",
                "description": "Enforces perfect traffic isolation between any set of Pods",
            },
        },
        {
            "id": 113,
            "title": "CoreDNS & Cross-Namespace Service Discovery",
            "description": "Resolve Service hostnames correctly across namespaces",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "CoreDNS handles all in-cluster DNS. Services get entries: "
                "<service>.<namespace>.svc.cluster.local. Pods in the same namespace can "
                "use just <service>. Cross-namespace requires at minimum <service>.<namespace>. "
                "Headless Services get per-Pod records: <pod>.<service>.<ns>.svc.cluster.local."
            ),
            "scenario": (
                "Your backend Pod (namespace: backend) tries to connect to a PostgreSQL "
                "Service named 'postgres' in namespace 'data' using host=postgres. "
                "The connection fails with 'host not found'. The Pod can reach 8.8.8.8 fine."
            ),
            "question": (
                "What is the correct hostname to reach the postgres Service from the "
                "backend namespace?"
            ),
            "options": [
                "postgres — short names automatically resolve across all namespaces",
                "postgres.data — the namespace suffix alone resolves cross-namespace services",
                "postgres.data.svc.cluster.local — fully qualified cross-namespace Service FQDN",
                "data.postgres.svc.cluster.local — namespace always comes first in cluster DNS",
            ],
            "answer": "postgres.data.svc.cluster.local — fully qualified cross-namespace Service FQDN",
            "explanation": (
                "DNS search domains for a Pod in namespace 'backend' include "
                "backend.svc.cluster.local and svc.cluster.local — NOT data.svc.cluster.local. "
                "So 'postgres' resolves to postgres.backend.svc.cluster.local (not found). "
                "The FQDN postgres.data.svc.cluster.local bypasses namespace scoping. "
                "postgres.data also works via the svc.cluster.local search suffix. "
                "The format is always <service>.<namespace>.svc.cluster.local."
            ),
            "badge": "DNS Detective",
            "loot": {
                "type": "potion",
                "name": "DNS Resolver Potion",
                "description": "Resolves any service hostname in any namespace instantly",
            },
        },
        {
            "id": 114,
            "title": "PersistentVolumes & StorageClasses",
            "description": "Provision and manage durable storage in Kubernetes",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "PersistentVolumes (PV): cluster-level storage resources. "
                "PersistentVolumeClaims (PVC): namespace-level storage requests. "
                "StorageClasses enable dynamic provisioning — PVCs trigger automatic PV creation. "
                "Access modes: ReadWriteOnce, ReadWriteMany, ReadOnlyMany. "
                "Reclaim policy: Retain (keep data), Delete (destroy on PVC deletion)."
            ),
            "scenario": (
                "A developer accidentally deletes a PVC that backed a 100Gi production database. "
                "The StorageClass used reclaimPolicy: Delete, so the PV and data were destroyed. "
                "You must prevent this from happening again without blocking dynamic provisioning."
            ),
            "question": (
                "Which StorageClass reclaimPolicy change prevents data loss on future PVC deletions?"
            ),
            "options": [
                "reclaimPolicy: Delete — data is deleted but the PV slot is freed for reuse",
                "reclaimPolicy: Retain — the PV and its data persist after PVC deletion",
                "reclaimPolicy: Recycle — the PV is wiped and made available for new PVCs",
                "reclaimPolicy: Archive — data moves to cold storage before PV deletion",
            ],
            "answer": "reclaimPolicy: Retain — the PV and its data persist after PVC deletion",
            "explanation": (
                "With Retain, deleting a PVC moves the PV to 'Released' status but does NOT delete "
                "the underlying storage. An admin can manually recover or rebind it. Delete (common "
                "cloud default) destroys the underlying volume immediately. Recycle is deprecated "
                "in modern Kubernetes. Archive is not a real Kubernetes reclaim policy."
            ),
            "badge": "Storage Guardian",
            "loot": {
                "type": "relic",
                "name": "Data Preservation Orb",
                "description": "Protects persistent data from any accidental deletion",
            },
        },
        {
            "id": 115,
            "title": "Canary Deployments with Ingress",
            "description": "Progressive traffic splitting for safe feature rollouts",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Advanced Ingress controllers support canary deployments via annotations: "
                "canary-weight (percentage to canary), canary-by-header (always route to canary "
                "if header present). Enables A/B testing, gradual rollouts, and header-pinned "
                "testing. Session affinity keeps a user on the same backend. "
                "Traffic weighting is managed by a secondary Ingress with canary: true."
            ),
            "scenario": (
                "You want 10% of api.example.com traffic to hit v2 and 90% to stay on v1. "
                "Internal QA testers who send header X-Canary: always must always hit v2. "
                "You use nginx-ingress."
            ),
            "question": (
                "Which nginx-ingress annotations on the v2 Ingress implement both weighted "
                "and header-based canary routing simultaneously?"
            ),
            "options": [
                "canary: true + canary-weight: 10 on the v2 Ingress only",
                "canary: true + canary-weight: 10 + canary-by-header: X-Canary on the v2 Ingress",
                "Two separate Ingress objects with different path rules: /v1 and /v2",
                "A Service with two EndpointSlices weighted 90/10 via endpointslice annotations",
            ],
            "answer": "canary: true + canary-weight: 10 + canary-by-header: X-Canary on the v2 Ingress",
            "explanation": (
                "nginx-ingress canary works by creating a second Ingress (for v2) with canary: true. "
                "canary-weight: 10 routes 10% of traffic to v2 randomly. canary-by-header: X-Canary "
                "routes ALL requests with that header to v2 regardless of weight. Both annotations "
                "coexist on the same canary Ingress. Path-based routing requires clients to change "
                "URLs. EndpointSlice weighting is not a standard Kubernetes mechanism."
            ),
            "badge": "Canary Deploy Expert",
            "loot": {
                "type": "legendary_relic",
                "name": "Canary Crown",
                "description": "Legendary: route traffic with surgical precision across any release",
            },
        },

        # ──────────────────────────── SECURITY (116-120) ─────────────────────────
        {
            "id": 116,
            "title": "RBAC — Role-Based Access Control",
            "description": "Grant least-privilege permissions to users and service accounts",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "RBAC controls who can do what on which resources. "
                "Role/ClusterRole: define permissions (verbs on resources). "
                "RoleBinding/ClusterRoleBinding: grant a Role to a subject. "
                "Role + RoleBinding: namespace-scoped. ClusterRole + ClusterRoleBinding: "
                "cluster-wide. ClusterRole + RoleBinding: cluster permissions scoped to one namespace."
            ),
            "scenario": (
                "A CI/CD pipeline must deploy Deployments and Services to the 'production' "
                "namespace only. It must NOT read Secrets or modify RBAC policies. "
                "The pipeline runs as a ServiceAccount in the 'ci' namespace."
            ),
            "question": (
                "Which RBAC configuration grants the CI pipeline exactly the permissions it needs?"
            ),
            "options": [
                "ClusterRole with get/list/create/update on deployments+services + ClusterRoleBinding to the SA",
                "Role in 'production' with get/list/create/update on deployments+services + RoleBinding to the SA",
                "ClusterRole with full access + RoleBinding scoped to the 'production' namespace",
                "Role in 'ci' namespace with get/list/create/update on deployments+services",
            ],
            "answer": "Role in 'production' with get/list/create/update on deployments+services + RoleBinding to the SA",
            "explanation": (
                "A Role defined IN the 'production' namespace scopes permissions to that namespace. "
                "A RoleBinding in 'production' can grant the Role to the SA from the 'ci' namespace "
                "(cross-namespace bindings are allowed). This is minimal privilege: specific verbs "
                "on specific resources, only in production. A ClusterRoleBinding grants cluster-wide "
                "access — violating least-privilege. A Role in 'ci' cannot grant access to 'production'."
            ),
            "badge": "RBAC Architect",
            "loot": {
                "type": "relic",
                "name": "Least Privilege Key",
                "description": "Grants exactly the right permissions — never more, never less",
            },
        },
        {
            "id": 117,
            "title": "IRSA & Pod Identity — Keyless Cloud Access",
            "description": "Authenticate workloads to cloud APIs without static credentials",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Static credentials (access keys) in Pods are a security anti-pattern. "
                "IRSA (EKS) / Workload Identity (GKE) / Pod Identity (AKS) bind a Kubernetes "
                "ServiceAccount to a cloud IAM role via OIDC federation. Only Pods using that "
                "SA receive temporary credentials. automountServiceAccountToken: false "
                "disables SA token mounting for Pods that don't need API access."
            ),
            "scenario": (
                "Your app Pods on EKS need to read S3. Currently all node Pods can access S3 "
                "because the EC2 node IAM role has S3 permissions. A security audit requires "
                "that ONLY the specific app Pods get S3 access."
            ),
            "question": (
                "Which approach gives per-Pod S3 access without node-level IAM permissions?"
            ),
            "options": [
                "Mount an AWS access key as a Kubernetes Secret into the specific Pods",
                "Use IRSA — annotate the ServiceAccount with the IAM role ARN, remove S3 from node role",
                "Add a NetworkPolicy allowing only the app Pods to reach the S3 VPC endpoint",
                "Set IMDSv2 hop limit to 1 on nodes — blocks all Pods from reading node IMDS",
            ],
            "answer": "Use IRSA — annotate the ServiceAccount with the IAM role ARN, remove S3 from node role",
            "explanation": (
                "IRSA creates an OIDC trust between a Kubernetes ServiceAccount and an AWS IAM role. "
                "Only Pods using that ServiceAccount receive temporary STS credentials for the role. "
                "Other Pods on the same node get nothing. Remove S3 from the node IAM role. Static "
                "access keys are a security anti-pattern (rotation burden, secret sprawl). "
                "NetworkPolicy controls network access, not IAM. IMDSv2 hop limit restricts "
                "Pod IMDS access but doesn't grant per-Pod IAM roles."
            ),
            "badge": "Pod Identity Expert",
            "loot": {
                "type": "relic",
                "name": "IRSA Keystone",
                "description": "Grants secure, temporary cloud credentials to exactly the right Pods",
            },
        },
        {
            "id": 118,
            "title": "PodSecurityContext & Linux Capabilities",
            "description": "Harden Pods by restricting privileges",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "securityContext controls privilege levels. runAsNonRoot: true prevents root "
                "containers. readOnlyRootFilesystem: true blocks filesystem writes. "
                "allowPrivilegeEscalation: false blocks setuid. "
                "capabilities.drop: [ALL] removes all Linux capabilities; add back only needed ones. "
                "PodSecurity admission enforces security profiles at namespace level."
            ),
            "scenario": (
                "A CIS Kubernetes Benchmark audit flags your API server Pods: running as root "
                "and retaining NET_RAW capability (enables crafting raw packets — often exploited "
                "in container escapes). The app only needs to bind port 8080."
            ),
            "question": (
                "Which securityContext settings remediate both findings without breaking the app?"
            ),
            "options": [
                "runAsUser: 0 + capabilities.drop: [NET_RAW] — root kept, removes the specific cap",
                "runAsNonRoot: true + runAsUser: 1000 + capabilities.drop: [ALL] + capabilities.add: [NET_BIND_SERVICE]",
                "runAsNonRoot: true + runAsUser: 1000 + capabilities.drop: [ALL]",
                "privileged: false + runAsNonRoot: true — privileged: false removes all capabilities",
            ],
            "answer": "runAsNonRoot: true + runAsUser: 1000 + capabilities.drop: [ALL]",
            "explanation": (
                "runAsNonRoot: true + runAsUser: 1000 runs as a non-root user — remediates finding 1. "
                "capabilities.drop: [ALL] removes NET_RAW and all other capabilities — remediates "
                "finding 2. The app binds port 8080 (>1024) so it does NOT need NET_BIND_SERVICE "
                "(only required for ports <1024). privileged: false only removes a subset of "
                "capabilities and still leaves NET_RAW. Adding NET_BIND_SERVICE is unnecessary."
            ),
            "badge": "Security Hardener",
            "loot": {
                "type": "relic",
                "name": "Capability Vault",
                "description": "Locks container capabilities to the absolute minimum required",
            },
        },
        {
            "id": 119,
            "title": "OPA Gatekeeper — Policy as Code",
            "description": "Enforce organisational policies on every Kubernetes API request",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Admission controllers intercept API server requests before persistence. "
                "OPA Gatekeeper uses ValidatingWebhookConfiguration + ConstraintTemplates "
                "(Rego policies as CRDs). Constraints enforce the templates. "
                "Kyverno is a K8s-native alternative. Policies can be version-controlled "
                "and deployed via GitOps like any other manifest."
            ),
            "scenario": (
                "Your platform team must enforce cluster-wide: every Deployment has a 'team' "
                "label; all container images come from registry.internal.co; no container "
                "runs as root. Rules must apply to all namespaces automatically on every apply."
            ),
            "question": (
                "Which approach enforces all three rules as version-controlled code that "
                "cannot be bypassed by kubectl apply?"
            ),
            "options": [
                "LimitRange + ResourceQuota per namespace + PodSecurityContext in every Deployment",
                "OPA Gatekeeper ConstraintTemplates: one per rule (label, registry, non-root)",
                "A custom ValidatingWebhookConfiguration calling a Python Flask validation service",
                "CI/CD pipeline linting that rejects non-compliant manifests pre-apply",
            ],
            "answer": "OPA Gatekeeper ConstraintTemplates: one per rule (label, registry, non-root)",
            "explanation": (
                "Gatekeeper ConstraintTemplates are Kubernetes CRDs expressing Rego policies. "
                "They are version-controlled, deployed via GitOps, and enforced by the API server's "
                "admission webhook on EVERY request — including kubectl apply run outside CI/CD. "
                "A custom Flask webhook works but requires maintaining extra infrastructure. "
                "CI/CD linting doesn't catch out-of-band applies. Manual template patterns "
                "are not automatically enforced."
            ),
            "badge": "Policy Enforcer",
            "loot": {
                "type": "relic",
                "name": "Gatekeeper Seal",
                "description": "Enforces any policy on every object entering the cluster",
            },
        },
        {
            "id": 120,
            "title": "Cluster Hardening & CIS Benchmarks",
            "description": "Secure the control plane, etcd, and API server",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "CIS Kubernetes Benchmark covers API server flags, etcd encryption, kubelet "
                "config, RBAC, audit logging, and network policies. kube-bench automates checks. "
                "etcd needs TLS + EncryptionConfiguration for encryption at rest. "
                "API server: disable anonymous auth, enable audit logs, restrict admission plugins. "
                "Nodes: disable read-only kubelet port, enable NodeRestriction admission plugin."
            ),
            "scenario": (
                "A penetration test finds that an attacker can query "
                "https://<api-server>:6443/api/v1/namespaces/default/pods with no credentials "
                "and retrieve all Pod names. You must fix anonymous access and ensure all "
                "future API calls are logged."
            ),
            "question": (
                "Which two kube-apiserver flags directly fix anonymous access and "
                "enable audit logging?"
            ),
            "options": [
                "--anonymous-auth=false + --audit-log-path=/var/log/audit.log",
                "--insecure-port=0 + --authorization-mode=Node,RBAC",
                "--disable-admission-plugins=AlwaysAllow + --enable-audit=true",
                "--token-auth-file='' + --audit-policy-file=/etc/audit-policy.yaml",
            ],
            "answer": "--anonymous-auth=false + --audit-log-path=/var/log/audit.log",
            "explanation": (
                "--anonymous-auth=false disables unauthenticated API requests — the direct fix. "
                "--audit-log-path enables structured audit logging of all API calls. "
                "--insecure-port=0 disables the HTTP port (also good) but does not fix anonymous "
                "auth on the HTTPS port. AlwaysAllow is an authorization mode, not an admission "
                "plugin. --token-auth-file='' removes static token auth but anonymous auth "
                "is a separate flag."
            ),
            "badge": "Cluster Security Champion",
            "loot": {
                "type": "legendary_relic",
                "name": "CIS Benchmark Shield",
                "description": "Legendary: your cluster scores 100% on every security benchmark",
            },
        },
    ]
