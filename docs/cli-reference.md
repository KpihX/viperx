# CLI Reference

## Commands Overview

| Command                 | Description                                   |
| ----------------------- | --------------------------------------------- |
| `viperx init`           | Initialize a new project (alias for `config`) |
| `viperx config`         | Apply declarative configuration               |
| `viperx config get`     | Generate template `viperx.yaml`               |
| `viperx package add`    | Add package to workspace                      |
| `viperx package delete` | Remove package from workspace                 |
| `viperx package update` | Update package dependencies                   |

---

## `viperx init` / `viperx config`

Create or update a project.

```bash
viperx init [OPTIONS]
viperx config [OPTIONS]
```

### Options

| Flag                | Description                           | Default    |
| ------------------- | ------------------------------------- | ---------- |
| `-n, --name`        | Project name **(Required unless -c)** | -          |
| `-t, --type`        | `classic`, `ml`, `dl`                 | `classic`  |
| `-d, --description` | Project description                   | -          |
| `-a, --author`      | Author name                           | git user   |
| `-l, --license`     | `MIT`, `Apache-2.0`, `GPLv3`          | `MIT`      |
| `-b, --builder`     | `uv`, `hatch`                         | `uv`       |
| `-f, --framework`   | `pytorch`, `tensorflow` (DL only)     | `pytorch`  |
| `--env / --no-env`  | Generate `.env` file                  | `--no-env` |
| `-c, --config`      | Path to `viperx.yaml`                 | -          |

### Examples

```bash
# Classic library
viperx init -n my-lib

# ML project with .env
viperx init -n churn-model -t ml --env

# DL project with TensorFlow
viperx init -n vision-ai -t dl -f tensorflow

# From config file
viperx config -c viperx.yaml
```

---

## `viperx config get`

Generate a template `viperx.yaml` in current directory.

```bash
viperx config get
```

---

## `viperx package add`

Add a new package to your workspace.

```bash
viperx package add [OPTIONS]
```

### Options

| Flag                     | Description                 | Default    |
| ------------------------ | --------------------------- | ---------- |
| `-n, --name`             | Package name **(Required)** | -          |
| `-t, --type`             | `classic`, `ml`, `dl`       | `classic`  |
| `--readme / --no-readme` | Generate local README       | `--readme` |
| `--env / --no-env`       | Generate `.env`             | `--no-env` |

### Example

```bash
viperx package add -n worker-api -t classic --no-readme
```

---

## `viperx package delete`

Remove a package from workspace.

```bash
viperx package delete -n <package-name>
```

!!! warning
    This permanently deletes the package folder.

---

## `viperx package update`

Update package dependencies.

```bash
viperx package update -n <package-name>
```

Runs `uv lock --upgrade` for the specified package.

---

## Global Options

| Flag            | Description  |
| --------------- | ------------ |
| `-v, --version` | Show version |
| `--help`        | Show help    |
