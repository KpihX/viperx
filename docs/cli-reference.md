# CLI Reference

> **For those who prefer the command line.**

!!! tip "We recommend `viperx.yaml`"
    While CLI flags work great for quick projects, `viperx.yaml` is better for:
    
    - Reproducibility
    - Team sharing
    - Complex projects

---

## Main Command: `viperx config`

This is the primary command. It can:
- Create new projects
- Update existing projects
- Apply config files

```bash
# Declarative (recommended)
viperx config -c viperx.yaml

# Imperative (quick & dirty)
viperx config -n my-project -t ml --env
```

### All Options

| Flag            | Short | What it does           |
| --------------- | ----- | ---------------------- |
| `--name`        | `-n`  | Project name           |
| `--type`        | `-t`  | classic, ml, dl        |
| `--description` | `-d`  | Project description    |
| `--author`      | `-a`  | Author name            |
| `--license`     | `-l`  | MIT, Apache-2.0, GPLv3 |
| `--builder`     | `-b`  | uv, hatch              |
| `--framework`   | `-f`  | pytorch, tensorflow    |
| `--env`         |       | Generate `.env`        |
| `--no-env`      |       | No `.env` (default)    |
| `--config`      | `-c`  | Path to `viperx.yaml`  |

---

## Alias: `viperx init`

Same as `viperx config`. Use whichever feels natural:

```bash
viperx init -n my-project
# Same as
viperx config -n my-project
```

---

## `viperx config get`

Generates a template `viperx.yaml` in current directory.

```bash
viperx config get
# Creates viperx.yaml with all options commented
```

---

## Package Management

For workspaces with multiple packages.

### Add a Package

```bash
viperx package add -n worker -t classic
viperx package add -n ml-core -t ml --env
```

### Remove a Package

```bash
viperx package delete -n old-service
```

!!! warning
    This actually deletes the folder. Use with care.

### Update Dependencies

```bash
viperx package update -n worker
# Runs: uv lock --upgrade
```

---

## Migration

Upgrade existing projects to newer ViperX versions.

```bash
# Preview changes
viperx migrate --dry-run

# Apply migration
viperx migrate
```

---

## Examples by Use Case

### "I need a quick experiment"

```bash
viperx init -n experiment-42 -t ml --env
cd experiment_42
uv sync
jupyter lab
```

### "I'm starting a serious project"

```bash
viperx config get
# Edit viperx.yaml carefully
viperx config -c viperx.yaml
```

### "I'm adding a service to my platform"

```bash
cd my_platform
viperx package add -n new-api -t classic
```
