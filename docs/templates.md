# Templates

This page documents the Jinja2 templates used by ViperX.

!!! tip "For Contributors"
    This is essential reading if you want to modify or add templates.

## Template Location

All templates are in `src/viperx/templates/`.

## Available Variables

### Project Metadata

| Variable      | Type | Description                  |
| ------------- | ---- | ---------------------------- |
| `name`        | str  | Raw project name             |
| `clean_name`  | str  | Sanitized name (underscores) |
| `description` | str  | Project description          |
| `author`      | str  | Author name                  |
| `email`       | str  | Author email                 |
| `version`     | str  | Initial version              |
| `license`     | str  | License type                 |

### Feature Flags

| Variable     | Type | Default |
| ------------ | ---- | ------- |
| `use_env`    | bool | `False` |
| `use_config` | bool | `True`  |
| `use_tests`  | bool | `True`  |
| `use_readme` | bool | `True`  |

### Project Type

| Variable    | Type | Description               |
| ----------- | ---- | ------------------------- |
| `type`      | str  | `classic`, `ml`, `dl`     |
| `is_ml`     | bool | True if ML or DL          |
| `is_dl`     | bool | True if DL                |
| `framework` | str  | `pytorch` or `tensorflow` |

### Build System

| Variable         | Type | Description        |
| ---------------- | ---- | ------------------ |
| `builder`        | str  | `uv` or `hatch`    |
| `build_backend`  | str  | Full backend path  |
| `build_requires` | list | Build dependencies |

## Template Files

### Core

| File                | Purpose             |
| ------------------- | ------------------- |
| `pyproject.toml.j2` | Main project config |
| `README.md.j2`      | Documentation       |
| `__init__.py.j2`    | Package init        |
| `main.py.j2`        | CLI entry point     |
| `config.py.j2`      | Config loader       |

### ML/DL

| File                    | Purpose            |
| ----------------------- | ------------------ |
| `data_loader.py.j2`     | Smart data caching |
| `Base_General.ipynb.j2` | General notebook   |
| `Base_Kaggle.ipynb.j2`  | Kaggle notebook    |

## Examples

### Conditional Dependencies

```jinja2
{% if is_ml %}
"numpy>=1.26.0",
"pandas>=2.2.0",
{% endif %}

{% if is_dl and framework == "pytorch" %}
"torch>=2.5.0",
{% elif is_dl and framework == "tensorflow" %}
"tensorflow>=2.19.0",
{% endif %}
```

### Feature Toggle

```jinja2
{% if use_config %}
from .config import SETTINGS, get_config
{% endif %}
```

## Adding a New Template

1. Create `src/viperx/templates/myfile.j2`
2. Add rendering in `core.py`:
   ```python
   self._render_template("myfile.j2", target / "myfile.ext", context)
   ```
3. Run tests to verify
