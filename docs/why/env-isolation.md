# Why .env Inside src/package/?

## The Traditional Approach

Most tutorials put `.env` at the project root:

```
my-package/
├── .env                 # ❌ At root
├── src/
│   └── mypackage/
│       └── __init__.py
└── pyproject.toml
```

**ViperX does it differently:**

```
my-package/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── .env         # ✅ Inside package
└── pyproject.toml
```

**Why does this matter?**

## The Problem: Monorepo Chaos

### Single Root .env Breaks Down

**Traditional approach in a monorepo:**

```
company-monorepo/
├── .env                 # ❌ Single .env for everything
├── api/
│   └── src/api/
├── frontend/
│   └── src/
├── ml-service/
│   └── src/ml/
└── admin-dashboard/
    └── src/admin/
```

**What's in that single .env?**

```bash
# Which service needs what? Nobody knows!
DATABASE_URL=postgres://...
API_KEY=abc123
ML_MODEL_PATH=/models/
FRONTEND_API_URL=http://api:8000
ADMIN_SECRET=xyz789
REDIS_URL=redis://...
SMTP_HOST=smtp.gmail.com
AWS_ACCESS_KEY=...
STRIPE_KEY=...
# ... 100 more variables
```

**Problems:**

1. **Security leak:** Frontend doesn't need `DATABASE_URL`, but it's there
2. **Unclear ownership:** Who manages which variable?
3. **Naming conflicts:** Two services need `API_KEY` for different APIs
4. **Blast radius:** One mistake exposes everything
5. **Onboarding nightmare:** New devs see 100 variables, need 5

### Real-World Security Bug

**Scenario:** Frontend developer accidentally logs environment

```javascript
// frontend/src/debug.js
console.log("Environment:", process.env);  // ❌ Oops
```

**With root .env:**
```
Logged to browser console:
- DATABASE_URL: postgres://admin:password@db:5432/prod
- ADMIN_SECRET: super_secret_key
- AWS_ACCESS_KEY: AKIA...
- STRIPE_SECRET_KEY: sk_live_...
```

**Entire production exposed!**

**With isolated .env:**
```
Logged to browser console:
- FRONTEND_API_URL: http://api:8000
- PUBLIC_KEY: pk_...
```

**Only frontend variables exposed.** DB credentials in different `.env` file entirely.

## The Solution: Package-Level .env Files

### Isolation by Design

**ViperX structure (monorepo):**

```
company-monorepo/
├── api/
│   └── src/api/
│       ├── __init__.py
│       └── .env         # API secrets only
├── ml-service/
│   └── src/ml/
│       ├── __init__.py
│       └── .env         # ML secrets only
└── admin-dashboard/
    └── src/admin/
        ├── __init__.py
        └── .env         # Admin secrets only
```

**Each package knows only what it needs:**

```bash
# api/src/api/.env
DATABASE_URL=postgres://...
API_SECRET_KEY=abc123

# ml-service/src/ml/.env
ML_MODEL_PATH=/models/
AWS_S3_BUCKET=ml-models

# admin-dashboard/src/admin/.env
ADMIN_SECRET=xyz789
DATABASE_URL=postgres://admin:...@db/admin
```

**Benefits:**
1. ✅ Clear ownership
2. ✅ Minimal blast radius
3. ✅ No naming conflicts
4. ✅ Easy to understand
5. ✅ Security by isolation

### How ViperX Loads Package .env

**Generated code pattern:**

```python
# src/mypackage/__init__.py
from pathlib import Path
from dotenv import load_dotenv

# Load .env from THIS package's directory
package_dir = Path(__file__).parent
env_path = package_dir / ".env"

if env_path.exists():
    load_dotenv(env_path)
    
# Now environment variables are available
import os
DATABASE_URL = os.getenv("DATABASE_URL")
```

**Key insight:** Each package loads its OWN `.env`, not a global one.

## Benefits in Detail

### 1. Security Isolation

**Principle of Least Privilege:** Each service gets only what it needs.

**Example: Microservices**

```
services/
├── public-api/          # Public-facing
│   └── src/api/
│       └── .env         # Read-only DB access
├── admin-service/       # Internal only
│   └── src/admin/
│       └── .env         # Full DB access
└── metrics/             # Monitoring
    └── src/metrics/
        └── .env         # Metrics API key only
```

**public-api/.env:**
```bash
DATABASE_URL=postgres://readonly:...@db/public
PUBLIC_API_KEY=pk_live_...
```

**admin-service/.env:**
```bash
DATABASE_URL=postgres://admin:...@db/admin
ADMIN_SECRET=...
STRIPE_SECRET_KEY=sk_live_...
```

**If public-api is compromised:**
- ❌ Attacker gets read-only DB access
- ✅ Admin DB not exposed
- ✅ Stripe keys not exposed
- ✅ Admin secrets not exposed

**Blast radius minimized!**

### 2. Monorepo Support

**Problem:** Multiple services, one repo.

**Traditional approach:**
```bash
# Root .env has everything
API_PORT=8000
ML_PORT=8001
ADMIN_PORT=8002
# ... namespace pollution
```

**ViperX approach:**
```bash
# Each service has its own
api/src/api/.env:
  PORT=8000

ml/src/ml/.env:
  PORT=8001

admin/src/admin/.env:
  PORT=8002
```

**No conflicts, clear ownership.**

### 3. Development Workflow

**Scenario:** You work on API, not ML service.

**Traditional .env:**
```bash
# Must have ALL variables set, even for services you don't use
DATABASE_URL=...          # API needs this
API_KEY=...              # API needs this
ML_MODEL_PATH=...        # ML needs this ← You don't care
ML_S3_BUCKET=...         # ML needs this ← You don't care
METRICS_ENDPOINT=...     # Metrics needs this ← You don't care
```

**You need to set up ML and metrics just to run API!**

**Package-level .env:**
```bash
# api/src/api/.env - Only API variables
DATABASE_URL=...
API_KEY=...

# Done! Start coding on API immediately
```

**ML service down? Doesn't matter. You're working on API.**

### 4. Testing Isolation

**Problem:** Tests interfere with each other's environment.

**Traditional approach:**
```python
# tests/test_api.py
def test_api():
    os.environ["DATABASE_URL"] = "sqlite:///test.db"  # Set for test
    # ... test API

# tests/test_ml.py
def test_ml():
    # DATABASE_URL still set from previous test! ❌
    # Might cause unexpected behavior
```

**ViperX approach:**
```python
# api/tests/test_api.py
def test_api():
    # Load API's .env
    load_dotenv("api/src/api/.env")
    # API tests run with API environment

# ml/tests/test_ml.py
def test_ml():
    # Load ML's .env
    load_dotenv("ml/src/ml/.env")
    # ML tests run with ML environment
```

**Each test suite has isolated environment.**

### 5. Deployment Flexibility

**Different deployment strategies for different services:**

**Example:**
- API: Kubernetes (uses ConfigMaps)
- ML: AWS Lambda (uses environment variables)
- Admin: Docker Compose (uses .env file)

**Package-level .env maps cleanly:**

```yaml
# API: Kubernetes ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: api-config
data:
  # From api/src/api/.env
  DATABASE_URL: "postgres://..."
  API_KEY: "..."

---
# ML: Lambda environment
# From ml/src/ml/.env
Environment:
  Variables:
    ML_MODEL_PATH: "/models/"
    AWS_S3_BUCKET: "ml-models"

---
# Admin: Docker Compose
# From admin/src/admin/.env
services:
  admin:
    env_file:
      - admin/src/admin/.env
```

**Each service's environment configuration lives with its code.**

## Real-World Scenario

### The Startup That Learned the Hard Way

**Initial setup (root .env):**

```
startup/
├── .env                 # Everyone's secrets
├── api/
├── web/
└── worker/
```

**.env file:**
```bash
DATABASE_URL=postgres://admin:prod_password@db/main
STRIPE_SECRET_KEY=sk_live_xxxxxxxxx
SENDGRID_API_KEY=SG.xxxxxxxxx
JWT_SECRET=super_secret_key
AWS_ACCESS_KEY_ID=AKIA...
AWS_SECRET_ACCESS_KEY=...
```

**What happened:**

**Month 1:** Frontend dev adds debugging
```javascript
// Accidentally committed
console.log(process.env);  // ❌ Oops
```

**Result:** All production secrets in browser console. Security audit required.

**Month 3:** ML team joins
```bash
# ML needs different DB
DATABASE_URL=postgres://...  # Conflicts with API!
```

**Result:** Naming conflicts. Created `ML_DATABASE_URL`, `API_DATABASE_URL`, etc.

**Month 6:** 50 environment variables
```bash
# Which service needs what? Nobody knows!
DATABASE_URL=...
ML_DATABASE_URL=...
ADMIN_DATABASE_URL=...
WORKER_DATABASE_URL=...
# ... getting messy
```

**Result:** New hires spend days understanding environment setup.

**Month 12:** Refactor to ViperX pattern

```
startup/
├── api/src/api/.env
│   DATABASE_URL=postgres://...
│   JWT_SECRET=...
│
├── web/src/web/.env
│   PUBLIC_API_KEY=pk_...
│   ANALYTICS_KEY=...
│
├── worker/src/worker/.env
│   QUEUE_URL=redis://...
│   EMAIL_API_KEY=...
│
└── ml/src/ml/.env
    ML_DATABASE_URL=postgres://...
    S3_BUCKET=...
```

**Result:**
- ✅ Security: Frontend can't access API secrets
- ✅ Clarity: Each service's .env is small (5-10 vars)
- ✅ Onboarding: New devs set up only what they need
- ✅ Deployment: Each service independently configured

## Following 12-Factor App Principles

### What is 12-Factor?

[12-Factor App](https://12factor.net/) methodology says:

> **III. Config**
> Store config in the environment

**Traditional interpretation:** One global environment.

**Better interpretation:** Environment per service/package.

### ViperX Alignment

**Factor III: Config**
✅ Config in environment (not code)
✅ Separate from code
✅ Varies between deployments

**Factor IV: Backing Services**
✅ Each package declares its own backing service connections
```bash
# api/.env
DATABASE_URL=...

# ml/.env
S3_BUCKET=...
```

**Factor VI: Processes**
✅ Stateless processes
✅ Environment loaded at startup
✅ No shared global state

### Environment Per Deployment

**12-factor says:** Different config for staging/prod.

**ViperX approach:** Different .env per environment AND per package.

```
api/
└── src/api/
    ├── .env              # Local dev
    ├── .env.staging      # Staging
    └── .env.production   # Production (not in git!)
```

**Load the right one:**
```python
import os
from pathlib import Path
from dotenv import load_dotenv

env = os.getenv("APP_ENV", "development")
env_file = Path(__file__).parent / f".env.{env}"

if env_file.exists():
    load_dotenv(env_file)
else:
    load_dotenv(Path(__file__).parent / ".env")
```

**Deployment:**
```bash
# Staging
$ APP_ENV=staging python -m api

# Production
$ APP_ENV=production python -m api
```

## Edge Cases & Solutions

### 1. Shared Secrets

**Problem:** Multiple packages need the same secret (e.g., shared Redis).

**Bad solution:** Duplicate in every .env (maintenance nightmare)

**Good solution:** Hierarchical loading

```python
from pathlib import Path
from dotenv import load_dotenv

# 1. Load shared .env (if exists)
repo_root = Path(__file__).parent.parent.parent.parent
shared_env = repo_root / ".env.shared"
if shared_env.exists():
    load_dotenv(shared_env)

# 2. Load package .env (overrides shared)
package_env = Path(__file__).parent / ".env"
if package_env.exists():
    load_dotenv(package_env)
```

**Structure:**
```
repo/
├── .env.shared          # Shared secrets (Redis, etc.)
├── api/src/api/.env     # API-specific
└── ml/src/ml/.env       # ML-specific
```

### 2. CI/CD Environment

**Problem:** CI needs to set environment variables.

**Solution:** CI sets them globally, package .env is fallback.

```python
import os
from dotenv import load_dotenv

# Load .env only if not in CI (CI sets env vars directly)
if not os.getenv("CI"):
    load_dotenv(Path(__file__).parent / ".env")

# Now use env vars (works in dev and CI)
DATABASE_URL = os.getenv("DATABASE_URL")
```

**GitHub Actions:**
```yaml
jobs:
  test:
    env:
      DATABASE_URL: postgres://test
      API_KEY: test_key
    steps:
      - run: pytest  # Uses CI env vars, not .env
```

### 3. Docker Compose

**Problem:** Docker Compose wants root `env_file`.

**Solution:** Point to package .env

```yaml
services:
  api:
    build: ./api
    env_file:
      - ./api/src/api/.env  # Package .env
  
  ml:
    build: ./ml
    env_file:
      - ./ml/src/ml/.env    # Different package .env
```

**Best of both worlds:** Package isolation + Docker Compose compatibility.

## Migration Guide

### From Root .env to Package .env

**Step 1: Identify dependencies**

```bash
# Which variables does each package need?
$ grep -r "os.getenv\|os.environ" api/src/
# List: DATABASE_URL, API_KEY

$ grep -r "os.getenv\|os.environ" ml/src/
# List: S3_BUCKET, MODEL_PATH
```

**Step 2: Split .env**

```bash
# Create package .env files
$ mkdir -p api/src/api ml/src/ml

# api/src/api/.env
$ cat > api/src/api/.env << EOF
DATABASE_URL=postgres://...
API_KEY=abc123
EOF

# ml/src/ml/.env
$ cat > ml/src/ml/.env << EOF
S3_BUCKET=my-bucket
MODEL_PATH=/models/
EOF
```

**Step 3: Update code**

```python
# api/src/api/__init__.py
from pathlib import Path
from dotenv import load_dotenv

# OLD: load_dotenv()  # Loads from current dir (unreliable)
# NEW:
load_dotenv(Path(__file__).parent / ".env")
```

**Step 4: Update .gitignore**

```bash
# .gitignore
# OLD: /.env
# NEW:
**/src/*/.env
!**/src/*/.env.example
```

**Step 5: Create .env.example**

```bash
# api/src/api/.env.example
DATABASE_URL=postgres://localhost/dev
API_KEY=your_api_key_here

# Commit examples, not real secrets
$ git add api/src/api/.env.example
```

## Comparison with Other Approaches

### Approach 1: Root .env (Traditional)

**Pros:**
- Simple (one file)
- Familiar to most developers

**Cons:**
- No isolation
- Security risk
- Monorepo nightmare
- Naming conflicts

### Approach 2: Separate .env.api, .env.ml (Root variants)

```
project/
├── .env.api
├── .env.ml
├── .env.worker
└── api/
```

**Pros:**
- Some isolation
- Still in root

**Cons:**
- Manual loading logic
- Not colocated with code
- Harder to deploy separately

### Approach 3: Package .env (ViperX)

```
project/
├── api/src/api/.env
├── ml/src/ml/.env
└── worker/src/worker/.env
```

**Pros:**
- Full isolation
- Colocated with code
- Clear ownership
- Easy to deploy

**Cons:**
- Slightly more complex (multiple files)

### Approach 4: No .env (Pure environment variables)

**Pros:**
- True 12-factor
- Platform-agnostic

**Cons:**
- Hard for local development
- No fallback defaults
- Difficult to manage many variables

**ViperX hybrid:** .env for dev, env vars for prod.

## Security Best Practices

### 1. Never Commit Secrets

**.gitignore:**
```bash
# Ignore all .env files
**/.env
**/src/*/.env

# Except examples
!**/.env.example
!**/src/*/.env.example
```

### 2. Use .env.example

**Provide templates:**
```bash
# api/src/api/.env.example
DATABASE_URL=postgres://user:pass@localhost/dbname
API_KEY=your_key_here
SECRET_KEY=generate_with_openssl_rand_hex_32
```

**Onboarding:**
```bash
$ cp api/src/api/.env.example api/src/api/.env
$ vim api/src/api/.env  # Fill in real values
```

### 3. Validate Required Variables

```python
import os
import sys

REQUIRED = ["DATABASE_URL", "API_KEY"]

missing = [var for var in REQUIRED if not os.getenv(var)]
if missing:
    print(f"Missing required environment variables: {missing}")
    print("Copy .env.example to .env and fill in values")
    sys.exit(1)
```

### 4. Use Secret Management in Production

**Development:** .env files
**Production:** Secret managers

```python
import os

if os.getenv("ENVIRONMENT") == "production":
    # Load from AWS Secrets Manager, Vault, etc.
    from cloud_secrets import load_secrets
    load_secrets()
else:
    # Load from .env
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent / ".env")
```

## Learning More

### Official Resources
- [12-Factor App: Config](https://12factor.net/config) - Config principles
- [python-dotenv](https://github.com/theskumar/python-dotenv) - .env loading library
- [Environment Variables](https://en.wikipedia.org/wiki/Environment_variable) - OS-level config

### Related Topics
- [Why config-in-package?](config-in-package.md) - Config file placement
- [Why safe mode?](safe-mode.md) - ViperX safety philosophy
- [Monorepo Patterns](https://monorepo.tools/) - Managing multiple packages

### Tools for Secret Management
- AWS Secrets Manager
- HashiCorp Vault
- Azure Key Vault
- Google Secret Manager
- Doppler
- Infisical

---

**Next Steps:**
1. Check your generated package: `src/mypackage/.env`
2. Review what variables your package needs
3. Create `.env.example` for your team
4. Set up hierarchical loading if needed
5. Configure production secret management

*"Env isolation: Each package knows only what it needs."*
