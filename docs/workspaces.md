# Workspaces

> **The Problem**: You have multiple related packages (API, ML model, worker).  
> **The Solution**: One project, multiple packages, shared config.

---

## When Do You Need a Workspace?

| Situation                 | Workspace? |
| ------------------------- | ---------- |
| Single library or app     | ❌ No       |
| ML model + API together   | ✅ Yes      |
| Monorepo with shared code | ✅ Yes      |
| Microservices in one repo | ✅ Yes      |

---

## Creating a Workspace

### Step 1: Define Your Structure

```yaml
# viperx.yaml
project:
  name: "ml-platform"
  description: "ML Platform with API"

workspace:
  packages:
    - name: "api"
      type: "classic"
      description: "REST API"
      
    - name: "model"
      type: "ml"
      use_env: true
      description: "ML prediction model"
      
    - name: "worker"
      type: "classic"
      description: "Background jobs"
```

### Step 2: Apply

```bash
viperx config -c viperx.yaml
```

### Step 3: What You Get

```
ml_platform/
├── pyproject.toml        # All packages registered
├── viperx.yaml           # Your config
├── notebooks/            # From ML package
├── data/                 # Shared data folder
└── src/
    ├── ml_platform/      # Root package
    │   └── main.py
    ├── api/
    │   └── main.py
    ├── model/
    │   ├── main.py
    │   └── .env          # Only here (isolated!)
    └── worker/
        └── main.py
```

---

## Running Your Packages

Each package gets its own CLI command:

```bash
uv sync

# Run any package
uv run ml-platform    # Root
uv run api            # API service
uv run model          # ML model
uv run worker         # Worker
```

---

## Why `.env` is Isolated

**The Problem**: In a multi-package setup, you might have:
- `model/` needs OPENAI_KEY
- `api/` needs DB_PASSWORD
- `worker/` needs REDIS_URL

**If `.env` was at root**: All packages see all secrets (security risk).

**With ViperX**: Each `.env` lives in its own package:

```
src/
├── api/.env         # DB_PASSWORD only
├── model/.env       # OPENAI_KEY only
└── worker/.env      # REDIS_URL only
```

---

## Package Inheritance

Packages inherit settings from root unless overridden:

```yaml
settings:
  use_tests: true      # Default for all

workspace:
  packages:
    - name: "api"
      # Inherits use_tests: true
      
    - name: "scripts"
      use_tests: false  # Override: no tests
```

---

## Adding Packages Later

Project evolves? Add packages anytime:

```bash
viperx package add -n analytics -t ml --env
```

Or update `viperx.yaml` and re-apply:

```yaml
workspace:
  packages:
    - name: "api"
    - name: "model"
    - name: "analytics"    # New!
```

```bash
viperx config -c viperx.yaml
# Only creates analytics/, doesn't touch others
```

---

## Removing Packages

**ViperX won't delete your code.** If you remove a package from yaml:

```bash
viperx config -c viperx.yaml
# Warning: src/old-package/ exists but is not in config
# You need to delete it manually if you want
```

This is **Safe Mode** in action.
