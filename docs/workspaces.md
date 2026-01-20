# Workspaces

ViperX supports monorepo-style workspaces with multiple packages.

## What is a Workspace?

A workspace is a single project containing multiple sub-packages, each with its own:
- Source code in `src/<package>/`
- Entry point (CLI command)
- Optional `.env`, `config.py`, `tests/`

## Creating a Workspace

### Option 1: Declarative (viperx.yaml)

```yaml
project:
  name: "my-platform"

workspace:
  packages:
    - name: "api"
      type: "classic"
    - name: "ml-core"
      type: "ml"
      use_env: true
    - name: "worker"
      type: "classic"
```

```bash
viperx config -c viperx.yaml
```

### Option 2: Imperative (Step by Step)

```bash
# Create root project
viperx init -n my-platform

# Add packages
cd my_platform
viperx package add -n api -t classic
viperx package add -n ml-core -t ml --env
viperx package add -n worker -t classic
```

## Resulting Structure

```
my_platform/
├── pyproject.toml          # Root with all scripts
├── viperx.yaml
├── notebooks/              # If any package is ML/DL
└── src/
    ├── my_platform/        # Root package
    │   ├── main.py
    │   └── ...
    ├── api/
    │   ├── main.py
    │   └── ...
    ├── ml_core/
    │   ├── main.py
    │   ├── .env            # Only here (use_env: true)
    │   └── ...
    └── worker/
        ├── main.py
        └── ...
```

## Running Packages

Each package gets its own CLI command:

```bash
uv sync
uv run my-platform    # Root
uv run api            # API package
uv run ml-core        # ML package
uv run worker         # Worker package
```

## Package Isolation

### Strict `.env` Isolation

`.env` files are always in `src/<package>/`, never at root.

```
src/
├── api/              # No .env (use_env: false)
└── ml_core/
    └── .env          # Only here (use_env: true)
```

### Config Inheritance

Packages inherit from root `settings` unless overridden:

```yaml
settings:
  use_config: true    # Default for all
  use_tests: true

workspace:
  packages:
    - name: "api"
      use_tests: false  # Override: no tests
```

## Managing Packages

### Add

```bash
viperx package add -n new-service -t classic
```

### Delete

```bash
viperx package delete -n old-service
```

### Update Dependencies

```bash
viperx package update -n api
```
