# Configuration Deep Dive

> **The `viperx.yaml` file is your project's DNA.**

---

## Why Declarative Config?

### The Problem with CLI Flags

```bash
# Week 1: You run this
viperx init -n my-proj -t ml --env -l Apache-2.0 -b hatch

# Week 4: You need another project
# "What flags did I use again?"
```

### The Solution

```yaml
# viperx.yaml - Always here, always clear
project:
  name: "my-proj"
  license: "Apache-2.0"
  builder: "hatch"

settings:
  type: "ml"
  use_env: true
```

---

## Full Specification

### `project` Section

| Key           | What it does           | Default      |
| ------------- | ---------------------- | ------------ |
| `name`        | Your project name      | **Required** |
| `description` | Shows in PyPI          | `""`         |
| `author`      | Package author         | git user     |
| `license`     | MIT, Apache-2.0, GPLv3 | `MIT`        |
| `builder`     | uv or hatch            | `uv`         |

### `settings` Section

| Key          | What it does                  | Default   |
| ------------ | ----------------------------- | --------- |
| `type`       | classic, ml, dl               | `classic` |
| `framework`  | pytorch, tensorflow (DL only) | `pytorch` |
| `use_env`    | Generate `.env` file          | `false`   |
| `use_config` | Generate `config.py`          | `true`    |
| `use_tests`  | Generate `tests/` folder      | `true`    |

---

## Real Examples

### Minimal (Just the basics)

```yaml
project:
  name: "my-lib"
```

### Full ML Project

```yaml
project:
  name: "churn-model"
  description: "Customer churn prediction"
  author: "Data Science Team"
  license: "Apache-2.0"

settings:
  type: "ml"
  use_env: true
```

### Multi-package Platform

```yaml
project:
  name: "my-platform"

settings:
  use_tests: true

workspace:
  packages:
    - name: "api"
      type: "classic"
    - name: "model"
      type: "ml"
      use_env: true      # Only model needs secrets
    - name: "worker"
      type: "classic"
      use_tests: false   # No tests for worker
```

---

## Applying Your Config

```bash
# First time: Creates everything
viperx config -c viperx.yaml

# Later: Updates safely (adds missing, never deletes)
viperx config -c viperx.yaml
```

---

## Safe Mode: What Happens on Update?

| You change...            | ViperX does...                                    |
| ------------------------ | ------------------------------------------------- |
| `use_env: false → true`  | ✅ Creates `.env`                                  |
| `use_env: true → false`  | ⚠️ Warns you `.env` exists (doesn't delete)        |
| Add new package          | ✅ Creates it                                      |
| Remove package from yaml | ⚠️ Warns you folder exists (doesn't delete)        |
| Change license           | ⚠️ Warns you `LICENSE` differs (doesn't overwrite) |

**Philosophy**: ViperX will never destroy your work.

---

## Generating a Template

```bash
viperx config get
```

Creates a commented `viperx.yaml` with all options explained.
