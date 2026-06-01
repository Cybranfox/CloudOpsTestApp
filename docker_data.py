"""
Cloud Orbit — Docker Platform Lessons
Scenario-based questions for container engineers.
Lesson IDs 201-210  |  3 sectors  |  10 lessons
"""


def get_lessons():
    """Return Docker lesson list (IDs 201-210)."""
    return [
        # ───────────────────────────── BASICS (201-203) ──────────────────────────
        {
            "id": 201,
            "title": "Dockerfile Best Practices & Layer Caching",
            "description": "Write efficient Dockerfiles that build fast and produce small images",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "Docker builds images in layers. Each instruction (RUN, COPY, ADD) creates a layer. "
                "Layers are cached: if nothing above a layer changes, Docker reuses the cache. "
                "COPY package.json before COPY . (source code) so dependency install is cached "
                "independently of code changes. Combine RUN commands to reduce layers."
            ),
            "scenario": (
                "Your Node.js app Dockerfile runs `npm install` every time you rebuild, even "
                "when only a single .js file changed. Builds take 3 minutes due to re-downloading "
                "packages. You need to reduce rebuild time to under 10 seconds on code-only changes."
            ),
            "question": (
                "Which Dockerfile ordering correctly caches npm install independently "
                "from application code changes?"
            ),
            "options": [
                "COPY . . \\nRUN npm install — copy everything first, then install",
                "COPY package*.json . \\nRUN npm install \\nCOPY . . — install before copying code",
                "RUN npm install \\nCOPY . . — run install first with no context, then copy code",
                "COPY . . \\nRUN npm ci --only=production — production flag speeds up install",
            ],
            "answer": "COPY package*.json . \\nRUN npm install \\nCOPY . . — install before copying code",
            "explanation": (
                "Docker invalidates cache at the first changed layer. By copying only package.json "
                "and package-lock.json first, the `npm install` layer is cached as long as "
                "dependencies don't change. Copying the full source (COPY . .) comes after — "
                "it invalidates only the layers below it, not the npm install cache. "
                "The other options copy source before installing, breaking cache on every code edit."
            ),
            "badge": "Dockerfile Expert",
            "loot": {
                "type": "relic",
                "name": "Layer Cache Gem",
                "description": "Builds any Docker image 10x faster through perfect cache ordering",
            },
        },
        {
            "id": 202,
            "title": "Multi-Stage Builds",
            "description": "Produce minimal production images using builder and runtime stages",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Multi-stage builds use multiple FROM statements. Early stages (builder) compile "
                "or test; later stages (runtime) copy only the final artifact. The final image "
                "contains NO build tools, compilers, or test dependencies — dramatically reducing "
                "attack surface and image size. COPY --from=<stage> copies between stages."
            ),
            "scenario": (
                "Your Go API image is 1.2GB because the Golang SDK is included. The compiled "
                "binary is only 12MB. Security scanners flag CVEs in the build toolchain that "
                "don't affect the running binary. You need an image under 20MB with no CVEs "
                "from build tools."
            ),
            "question": (
                "Which Dockerfile pattern produces the smallest, most secure production image "
                "for a compiled Go binary?"
            ),
            "options": [
                "FROM golang:1.22 + RUN go build + RUN apt-get remove gcc — remove toolchain after build",
                "FROM golang:1.22 AS builder, RUN go build, FROM scratch, COPY --from=builder /app/binary /",
                "FROM golang:1.22-alpine — alpine variant is small enough for production",
                "FROM golang:1.22 + RUN strip /app/binary — strip debug symbols to reduce size",
            ],
            "answer": "FROM golang:1.22 AS builder, RUN go build, FROM scratch, COPY --from=builder /app/binary /",
            "explanation": (
                "A multi-stage build compiles the binary in the full golang image, then copies ONLY "
                "the compiled binary into a FROM scratch image (literally empty — zero OS, zero CVEs). "
                "The final image is just the binary (~12MB). Removing apt packages in the same stage "
                "still leaves layers with the installed packages. Alpine is smaller but still ~5MB "
                "with a shell and libc. strip reduces size slightly but doesn't remove toolchain CVEs."
            ),
            "badge": "Multi-Stage Architect",
            "loot": {
                "type": "relic",
                "name": "Scratch Stage Orb",
                "description": "Strips any image to its absolute minimum — zero attack surface",
            },
        },
        {
            "id": 203,
            "title": "Container Security — Non-Root & Read-Only Filesystem",
            "description": "Harden containers against escape and privilege escalation",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Running containers as root is dangerous: a container escape gives root on the host. "
                "USER <uid> in Dockerfile sets the runtime user. --read-only mounts the root "
                "filesystem read-only; use --tmpfs for /tmp. --no-new-privileges blocks setuid. "
                "Scan images for CVEs with Trivy, Grype, or Docker Scout before pushing."
            ),
            "scenario": (
                "A Docker security audit finds your API container runs as root (uid 0) and "
                "can write to /etc/passwd. If an attacker exploits your API, they get root "
                "in the container. You need to remediate without changing the application code — "
                "the app only writes to /tmp and /var/log/app."
            ),
            "question": (
                "Which combination of Dockerfile and docker run flags hardens the container "
                "without requiring code changes?"
            ),
            "options": [
                "Add USER nobody to Dockerfile + docker run --privileged=false",
                "Add USER 10001 to Dockerfile + docker run --read-only --tmpfs /tmp --tmpfs /var/log/app",
                "Add USER nobody to Dockerfile + VOLUME /tmp /var/log/app for writable directories",
                "docker run --security-opt no-new-privileges + --cap-drop ALL — no Dockerfile change needed",
            ],
            "answer": "Add USER 10001 to Dockerfile + docker run --read-only --tmpfs /tmp --tmpfs /var/log/app",
            "explanation": (
                "USER 10001 bakes a non-root UID into the image — no root at runtime. --read-only "
                "mounts the root filesystem read-only, preventing writes to /etc/passwd. --tmpfs "
                "for /tmp and /var/log/app gives the app its required writable paths as in-memory "
                "filesystems. USER nobody maps to uid 65534 on most systems — a valid choice but "
                "uid 10001 is more explicit. VOLUME doesn't make directories writable in the same "
                "way and persists data unexpectedly. --privileged=false is the default, not a fix."
            ),
            "badge": "Container Hardener",
            "loot": {
                "type": "relic",
                "name": "Container Fortress",
                "description": "Makes any container escape attempt extraordinarily difficult",
            },
        },
        # ──────────────────────────── COMPOSE (204-207) ──────────────────────────
        {
            "id": 204,
            "title": "Docker Compose — Service Dependencies & Health Checks",
            "description": "Ensure services start in the right order and stay healthy",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "depends_on controls startup order but NOT health readiness by default. "
                "depends_on with condition: service_healthy waits until the dependency's "
                "healthcheck passes before starting the dependent service. "
                "healthcheck: test/interval/timeout/retries defines when a service is 'healthy'. "
                "This prevents app containers from connecting to databases before they're ready."
            ),
            "scenario": (
                "Your Compose app (web + postgres) crashes on startup because the web container "
                "tries to connect to postgres before the database is ready to accept connections. "
                "The web container exits with 'connection refused' and never retries."
            ),
            "question": (
                "Which Compose configuration ensures web waits for postgres to be ready "
                "to accept connections before starting?"
            ),
            "options": [
                "depends_on: [postgres] — Compose waits for the postgres container to start",
                "links: [postgres] — links ensure postgres is reachable before web starts",
                "healthcheck on postgres + depends_on: postgres: condition: service_healthy on web",
                "restart: always on web — it will keep retrying until postgres is ready",
            ],
            "answer": "healthcheck on postgres + depends_on: postgres: condition: service_healthy on web",
            "explanation": (
                "depends_on alone only waits for the container to START, not for the database "
                "process to be READY. Adding a healthcheck (e.g. pg_isready) marks postgres as "
                "'healthy' only when it accepts connections. depends_on with condition: "
                "service_healthy then blocks web from starting until that health check passes. "
                "links is deprecated in modern Compose. restart: always just loops on failure "
                "rather than preventing the initial failure."
            ),
            "badge": "Compose Orchestrator",
            "loot": {
                "type": "potion",
                "name": "Health Check Potion",
                "description": "Guarantees all services are ready before any dependent starts",
            },
        },
        {
            "id": 205,
            "title": "Volumes & Bind Mounts — Data Persistence",
            "description": "Persist data beyond container lifecycle with the right storage type",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Named volumes: managed by Docker, persist after container removal, best for "
                "databases and app state. Bind mounts: map a host path into the container, "
                "ideal for development (live code reload) but not for production data. "
                "tmpfs mounts: in-memory, lost on container stop, ideal for secrets and temp files. "
                "Volume drivers allow volumes on NFS, cloud block storage, etc."
            ),
            "scenario": (
                "In development, you want code changes in ./src to instantly appear in the "
                "running container without rebuilding. In production, your database data must "
                "survive container restarts and host reboots — but must NOT be accessible "
                "via the host filesystem."
            ),
            "question": (
                "Which storage types match the dev (live reload) and prod (database) requirements?"
            ),
            "options": [
                "Dev: named volume on ./src | Prod: bind mount to /var/lib/mysql",
                "Dev: bind mount ./src:/app/src | Prod: named volume for /var/lib/mysql",
                "Dev: tmpfs on /app/src | Prod: named volume for /var/lib/mysql",
                "Dev: bind mount ./src:/app/src | Prod: bind mount /data/mysql:/var/lib/mysql",
            ],
            "answer": "Dev: bind mount ./src:/app/src | Prod: named volume for /var/lib/mysql",
            "explanation": (
                "Bind mount (./src:/app/src) maps host source files directly into the container — "
                "edits on the host instantly appear inside. Named volumes for the database are "
                "managed by Docker, survive reboots, and are NOT directly accessible via the host "
                "filesystem (stored in Docker's data root). Bind mounting database data exposes "
                "it to host processes and causes permission issues. tmpfs is in-memory and lost "
                "on stop — useless for a database."
            ),
            "badge": "Volume Strategist",
            "loot": {
                "type": "relic",
                "name": "Persistence Engine",
                "description": "Ensures data survives any container lifecycle event",
            },
        },
        {
            "id": 206,
            "title": "Compose Networking & Service Discovery",
            "description": "Isolate services and control inter-service communication",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Compose creates a default network for all services. Services discover each other "
                "by service name (DNS). Multiple networks can isolate services: a frontend network "
                "for public-facing services and a backend network for internal services. "
                "A service on both networks is the only bridge. External port mapping (ports:) "
                "exposes services to the host; internal-only services omit ports:."
            ),
            "scenario": (
                "Your Compose app has: nginx (public), api (internal), postgres (internal). "
                "nginx must reach api. api must reach postgres. nginx must NOT reach postgres "
                "directly. Only nginx should be reachable from outside the host (port 80)."
            ),
            "question": (
                "Which Compose network configuration correctly implements this isolation?"
            ),
            "options": [
                "One default network for all services + firewall rules to block nginx→postgres",
                "frontend network (nginx+api) + backend network (api+postgres) + ports: only on nginx",
                "frontend network (nginx only) + backend network (api+postgres) + ports: only on nginx",
                "All services on the default network + expose: on api+postgres (not ports:)",
            ],
            "answer": "frontend network (nginx+api) + backend network (api+postgres) + ports: only on nginx",
            "explanation": (
                "nginx and api share the frontend network — they can communicate. api and postgres "
                "share the backend network — they can communicate. nginx is NOT on the backend "
                "network, so it cannot reach postgres at all. Only nginx has ports: 80:80 — it's "
                "the only service reachable from outside the host. A single flat network with "
                "firewall rules is fragile and bypassed inside Docker. expose: makes a port "
                "available to linked services only, not between arbitrary services."
            ),
            "badge": "Network Isolator",
            "loot": {
                "type": "relic",
                "name": "Network Segmentation Key",
                "description": "Creates perfect isolation between any set of services",
            },
        },
        {
            "id": 207,
            "title": "Environment Variables & .env Files",
            "description": "Manage configuration and secrets in Compose without hardcoding",
            "room_type": "battle",
            "difficulty": "easy",
            "reward_type": "knowledge_card",
            "content": (
                "environment: in Compose sets vars directly in the service. "
                "env_file: loads vars from a file. "
                ".env in the project root is automatically loaded for variable substitution "
                "in docker-compose.yml (${VAR_NAME}). "
                "Never commit .env files with secrets — add to .gitignore. "
                "Docker secrets (swarm) or Kubernetes Secrets are the production alternative."
            ),
            "scenario": (
                "Your docker-compose.yml hardcodes POSTGRES_PASSWORD=mysecret. The repo is "
                "public. A GitGuardian scan flags this as a secret leak. You need to remove "
                "the hardcoded password and let each developer supply their own local value "
                "without breaking CI/CD."
            ),
            "question": (
                "Which approach removes the secret from docker-compose.yml while keeping "
                "it functional for local dev and CI?"
            ),
            "options": [
                "Move POSTGRES_PASSWORD to a .env file + add .env to .gitignore + use ${POSTGRES_PASSWORD} in Compose",
                "Encrypt the password in docker-compose.yml using base64 encoding",
                "Use environment: POSTGRES_PASSWORD: '' and let each developer override it at runtime",
                "Replace docker-compose.yml with a Makefile that exports the password before docker compose up",
            ],
            "answer": "Move POSTGRES_PASSWORD to a .env file + add .env to .gitignore + use ${POSTGRES_PASSWORD} in Compose",
            "explanation": (
                "Compose automatically loads .env from the project root for variable substitution. "
                "The Compose file references ${POSTGRES_PASSWORD} — no secret in source control. "
                "Adding .env to .gitignore prevents accidental commits. CI/CD sets the variable "
                "via environment variables or a secrets manager. base64 encoding is not encryption "
                "— GitGuardian will still detect it. An empty value breaks the database. "
                "A Makefile wrapper is fragile and non-standard."
            ),
            "badge": "Config Hygiene Expert",
            "loot": {
                "type": "potion",
                "name": "Secret Sanitizer",
                "description": "Instantly removes all hardcoded secrets from any Compose project",
            },
        },
        # ─────────────────────── REGISTRY & SECURITY (208-210) ───────────────────
        {
            "id": 208,
            "title": "Image Scanning & CVE Remediation",
            "description": "Identify and fix vulnerabilities in container images before deployment",
            "room_type": "battle",
            "difficulty": "medium",
            "reward_type": "knowledge_card",
            "content": (
                "Container image scanners (Trivy, Grype, Docker Scout, Snyk) analyse image layers "
                "for known CVEs in OS packages and application dependencies. "
                "Remediation strategies: update base image, update vulnerable packages, "
                "use distroless/scratch images, or use multi-stage builds to exclude dev deps. "
                "Scan in CI to gate builds before push to registry."
            ),
            "scenario": (
                "Trivy reports 47 HIGH CVEs in your nginx:1.18 base image, all in Ubuntu packages "
                "that your application never uses. Rebuilding with the same base image daily "
                "reduces the count but never to zero. You need to reach zero HIGH CVEs."
            ),
            "question": (
                "Which approach eliminates CVEs from unused OS packages in the nginx base image?"
            ),
            "options": [
                "Pin the base image to a specific SHA digest — prevents new CVEs from appearing",
                "Switch to nginx:alpine — Alpine Linux has far fewer packages and a smaller CVE surface",
                "RUN apt-get upgrade in the Dockerfile — updates all packages to patch CVEs",
                "Add a .trivyignore file to suppress the CVE findings in scan results",
            ],
            "answer": "Switch to nginx:alpine — Alpine Linux has far fewer packages and a smaller CVE surface",
            "explanation": (
                "Alpine-based images ship with ~14MB of OS packages vs Ubuntu's ~130MB. Fewer "
                "packages means drastically fewer CVEs — many teams reach zero HIGH CVEs by "
                "switching. Pinning a SHA prevents updates, locking in existing CVEs. "
                "apt-get upgrade patches CVEs but adds a mutable layer that drifts over time. "
                ".trivyignore suppresses findings without fixing them — violates security policy."
            ),
            "badge": "CVE Eliminator",
            "loot": {
                "type": "relic",
                "name": "Alpine Shield",
                "description": "Reduces the attack surface of any image to near-zero",
            },
        },
        {
            "id": 209,
            "title": "Private Registry — Authentication & Image Promotion",
            "description": "Manage image lifecycle from build through production release",
            "room_type": "elite",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "A typical image lifecycle: build → push to dev registry → scan → test → "
                "promote to staging registry → sign → promote to prod registry. "
                "Never build new images for production from source — promote pre-tested images "
                "by re-tagging with immutable digests. "
                "Docker Content Trust (DCT) / cosign + Sigstore enable image signing. "
                "Registry mirrors cache public images to prevent rate limiting and supply-chain attacks."
            ),
            "scenario": (
                "Your team builds app:latest in CI and deploys that tag to production. Two "
                "incidents occurred: (1) a broken build deployed before tests ran; (2) an "
                "attacker pushed a compromised image to Docker Hub with the same tag. "
                "You need to prevent both classes of incident."
            ),
            "question": (
                "Which image lifecycle practice addresses BOTH the broken-build and "
                "supply-chain compromise risks?"
            ),
            "options": [
                "Always pull the latest tag — fresh pulls get the newest, most patched version",
                "Use immutable tags (SHA digest) + promote only scan-passed and signed images to prod",
                "Use a private registry mirror — public images can't be compromised on a private registry",
                "Add a post-deploy smoke test — catch broken images after deployment, then rollback",
            ],
            "answer": "Use immutable tags (SHA digest) + promote only scan-passed and signed images to prod",
            "explanation": (
                "Immutable SHA digests (sha256:abc...) ensure the exact image that was tested is "
                "the one deployed — mutable tags like :latest can be overwritten. Promotion pipelines "
                "only move images that passed scanning and signing to the production registry, "
                "preventing broken builds and supply-chain attacks. A private mirror prevents "
                "rate limiting but if an attacker controls your CI/CD, they can still push malicious "
                "images. Post-deploy tests catch failures after the damage is done."
            ),
            "badge": "Registry Architect",
            "loot": {
                "type": "relic",
                "name": "Image Signing Seal",
                "description": "Guarantees only verified, tested images ever reach production",
            },
        },
        {
            "id": 210,
            "title": "Docker Security — Runtime Defences",
            "description": "Deploy containers with defence-in-depth at the runtime layer",
            "room_type": "boss",
            "difficulty": "hard",
            "reward_type": "relic",
            "content": (
                "Runtime defences complement image hardening. Key controls: "
                "--cap-drop ALL --cap-add <specific> (drop all Linux capabilities, re-add minimum), "
                "--security-opt seccomp=<profile> (restrict syscalls), "
                "--security-opt apparmor=<profile> (MAC policy), "
                "--no-new-privileges (block setuid/setgid), "
                "--pid host (dangerous — shares host PID namespace). "
                "Rootless Docker: the daemon itself runs as non-root, limiting host exposure."
            ),
            "scenario": (
                "A security review of your production containers shows: they run with all Linux "
                "capabilities (no --cap-drop), they can make any syscall (no seccomp profile), "
                "and the daemon runs as root. An auditor recommends defence-in-depth. "
                "The app is a stateless API — it makes no privileged system calls."
            ),
            "question": (
                "Which combination of docker run flags implements the deepest defence-in-depth "
                "for a stateless API container?"
            ),
            "options": [
                "--user 10001 only — non-root user is sufficient for most attack scenarios",
                "--cap-drop ALL --no-new-privileges --security-opt seccomp=default.json --user 10001",
                "--privileged=false --user 10001 — privileged: false is equivalent to dropping all caps",
                "--cap-drop NET_RAW --cap-drop SYS_ADMIN --user 10001 — drop the most dangerous caps",
            ],
            "answer": "--cap-drop ALL --no-new-privileges --security-opt seccomp=default.json --user 10001",
            "explanation": (
                "Defence-in-depth uses multiple layers: --cap-drop ALL removes all Linux capabilities "
                "(the app needs none). --no-new-privileges blocks privilege escalation via setuid. "
                "--security-opt seccomp=default.json restricts the syscall surface (Docker's default "
                "profile blocks ~44 dangerous syscalls). --user 10001 ensures no root UID. "
                "--privileged=false is the default and does NOT drop capabilities. Dropping only "
                "specific caps leaves others (like NET_BIND_SERVICE, CHOWN) that may be exploitable. "
                "--user alone doesn't prevent capability abuse."
            ),
            "badge": "Runtime Security Master",
            "loot": {
                "type": "legendary_relic",
                "name": "Defence-in-Depth Crown",
                "description": "Legendary: every layer of container security active simultaneously",
            },
        },
    ]
