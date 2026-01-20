# Configuration

ViperX supports declarative configuration via `viperx.yaml`.

## Generating a Template

```bash
viperx config get
```

Creates a `viperx.yaml` template in the current directory.

## Full Specification

```yaml
# viperx.yaml

project:
  name: "my-project"           # Required
  description: "A cool project"
  author: "Your Name"
  license: "MIT"               # MIT | Apache-2.0 | GPLv3
  builder: "uv"                # uv | hatch

settings:
  type: "classic"              # classic | ml | dl
  framework: "pytorch"         # pytorch | tensorflow (DL only)
  use_env: false               # Generate .env
  use_config: true             # Generate config.py
  use_tests: true              # Generate tests/
  use_readme: true             # Generate README.md

workspace:
  packages:
    - name: "api"
      type: "classic"
      use_env: false
    - name: "ml-core"
      type: "ml"
      use_env: true
```

## Section Details

### `project`

| Key           | Type   | Required | Default  |
| ------------- | ------ | -------- | -------- |
| `name`        | string | ✅        | -        |
| `description` | string | ❌        | `""`     |
| `author`      | string | ❌        | git user |
| `license`     | string | ❌        | `"MIT"`  |
| `builder`     | string | ❌        | `"uv"`   |

### `settings`

| Key          | Type   | Default     | Description          |
| ------------ | ------ | ----------- | -------------------- |
| `type`       | string | `"classic"` | Project type         |
| `framework`  | string | `"pytorch"` | DL framework         |
| `use_env`    | bool   | `false`     | Generate `.env`      |
| `use_config` | bool   | `true`      | Generate `config.py` |
| `use_tests`  | bool   | `true`      | Generate `tests/`    |
| `use_readme` | bool   | `true`      | Generate `README.md` |

### `workspace.packages`

Each package inherits from root `settings` unless overridden.

```yaml
workspace:
  packages:
    - name: "worker"
      type: "classic"     # Override root type
      use_env: true       # Override root use_env
```

## Applying Configuration

```bash
viperx config -c viperx.yaml
```

This is **idempotent**:

- Creates project if it doesn't exist
- **Hydrates** missing features (e.g., adds `.env` if `use_env: true`)
- **Reports** conflicts without overwriting

## Safe Mode

ViperX follows a non-destructive philosophy:

| Action        | Behavior                     |
| ------------- | ---------------------------- |
| **Add**       | ✅ Creates new files/packages |
| **Update**    | ⚠️ Reports changes for review |
| **Delete**    | ❌ Never deletes—warns user   |
| **Overwrite** | ❌ Never overwrites           |
