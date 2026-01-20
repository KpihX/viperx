# Quick Start

This guide will get you up and running with ViperX in 5 minutes.

## 1. Create Your First Project

```bash
viperx init -n my-awesome-lib -d "My first ViperX project"
```

This creates:

```
my_awesome_lib/
├── pyproject.toml
├── README.md
├── .gitignore
├── viperx.yaml
└── src/
    └── my_awesome_lib/
        ├── __init__.py
        ├── main.py
        ├── config.py
        └── tests/
```

## 2. Navigate and Sync

```bash
cd my_awesome_lib
uv sync
```

## 3. Run Your Project

```bash
uv run my-awesome-lib
# Output: Hi from my-awesome-lib!
```

## 4. Create a Machine Learning Project

```bash
viperx init -n churn-model -t ml --env
cd churn_model
```

This adds:
- `notebooks/` with starter notebooks
- `data/` for cached datasets
- `.env` in `src/churn_model/`
- ML dependencies (pandas, numpy, scikit-learn)

## 5. Use Declarative Config

Create a `viperx.yaml`:

```yaml
project:
  name: "my-project"
  description: "A cool project"
  license: "MIT"

settings:
  type: "ml"
  use_env: true

workspace:
  packages:
    - name: "api"
      type: "classic"
    - name: "ml-core"
      type: "ml"
```

Apply it:

```bash
viperx config -c viperx.yaml
```

## Next Steps

- [CLI Reference](cli-reference.md) - All commands
- [Configuration](configuration.md) - `viperx.yaml` spec
- [Workspaces](workspaces.md) - Multi-package projects
