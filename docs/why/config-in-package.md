# Why Config Files Inside src/package/?

## The Standard Approach

Most Python projects put configuration at the project root:

```
my-package/
├── config.yaml          # ❌ At root
├── settings.toml
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
│       ├── config.yaml  # ✅ Inside package
│       └── py.typed
└── pyproject.toml
```

**Why does this matter?**

## The Problem: Root Files Don't Get Packaged

### What Happens with Root Config Files

When you build a Python wheel:

```bash
$ python -m build
# or
$ uv build
```

**Only files inside your package directory are included by default.**

Root-level files like `config.yaml` are **not automatically packaged**.

### Real-World Bug

**Developer writes code:**
```python
# mypackage/__init__.py
import yaml
from pathlib import Path

def load_config():
    # Tries to load from project root
    config_path = Path(__file__).parent.parent.parent / "config.yaml"
    with open(config_path) as f:
        return yaml.safe_load(f)
```

**Works locally:**
```bash
$ python -c "import mypackage; mypackage.load_config()"
# ✅ Works! config.yaml is in the filesystem
```

**Install and use:**
```bash
$ pip install dist/mypackage-0.1.0-py3-none-any.whl
$ python -c "import mypackage; mypackage.load_config()"
# ❌ FileNotFoundError: config.yaml not found!
```

**Why?** The wheel doesn't contain `config.yaml` from the project root!

### The Manual Fix (Old Way)

You could manually include root files:

**MANIFEST.in:**
```
include config.yaml
include settings.toml
```

**pyproject.toml (setuptools):**
```toml
[tool.setuptools]
include-package-data = true

[tool.setuptools.package-data]
"*" = ["../config.yaml"]  # Hacky relative path
```

**Problems:**
1. Easy to forget MANIFEST.in
2. Different build tools have different syntax
3. Relative path hacks are fragile
4. Files still aren't in the importable package

## The Bigger Problem: Colab, Kaggle, Cloud Notebooks

### Notebooks Don't Have a "Project Root"

**Google Colab scenario:**
```python
# In a Colab notebook
!pip install mypackage

import mypackage
mypackage.load_config()  # ❌ Where is "project root"?
```

**There is no project root!** You only have:
- The installed package in site-packages
- The current notebook directory

**User workarounds (all bad):**
```python
# Bad workaround 1: Download config separately
!wget https://example.com/config.yaml
import mypackage
# But now config is in current dir, not where package expects it

# Bad workaround 2: Pass config path manually
config = mypackage.load_config("/content/my_config.yaml")
# Every user needs custom config management

# Bad workaround 3: Give up
# Just don't use the package in Colab ☹️
```

### The Same Problem Everywhere

**Anywhere you pip install without cloning the repo:**
- Jupyter notebooks
- Google Colab
- Kaggle notebooks
- AWS Lambda
- Azure Functions
- Docker containers (multi-stage builds)
- Production servers

**Pattern:** Install from PyPI/wheel → Config not available

## The Solution: importlib.resources

### Modern Python's Answer

Python 3.9+ provides `importlib.resources` for package data:

```python
from importlib.resources import files

def load_config():
    # Access file INSIDE the package
    config_text = files("mypackage").joinpath("config.yaml").read_text()
    return yaml.safe_load(config_text)
```

**This works everywhere:**
- ✅ Local development
- ✅ After pip install
- ✅ In wheels
- ✅ In Google Colab
- ✅ In Docker containers
- ✅ On production servers

**Why?** The config is part of the installed package, not external!

### How ViperX Implements This

**Generated package structure:**
```
src/mypackage/
├── __init__.py
├── config.yaml          # Config lives WITH the code
├── templates/           # Templates also in package
│   └── base.html
└── py.typed
```

**Generated code to load config:**
```python
# src/mypackage/config.py
from importlib.resources import files
import yaml
from pathlib import Path

def get_config_path() -> Path:
    """Get path to config.yaml inside the package."""
    # This works whether installed or in editable mode
    return files(__package__).joinpath("config.yaml")

def load_config() -> dict:
    """Load configuration from package data."""
    config_text = files(__package__).joinpath("config.yaml").read_text()
    return yaml.safe_load(config_text)

# Usage anywhere
config = load_config()
```

**The magic:**
- `files(__package__)` finds the package directory
- Works in wheels, zips, editable installs, everywhere
- Config is guaranteed to be available

## Benefits in Detail

### 1. Portability

**Traditional approach:**
```python
# Fragile: Assumes specific directory structure
config_path = Path(__file__).parent.parent.parent / "config.yaml"
```

**Config-in-package:**
```python
# Robust: Uses package resources
config_text = files("mypackage").joinpath("config.yaml").read_text()
```

**Works in:**
- Development (editable install)
- Production (wheel install)
- Notebooks (pip install)
- Zipapps
- Frozen applications (PyInstaller)

### 2. Zero Configuration for Users

**Traditional approach:**
```bash
# User must:
$ pip install mypackage
$ wget https://example.com/config.yaml  # Download separately
$ export CONFIG_PATH=/path/to/config.yaml  # Set environment
```

**Config-in-package:**
```bash
# User only needs:
$ pip install mypackage
# Everything works out of the box!
```

### 3. Versioned Configuration

Config is part of the package → Config is versioned with code!

**Example:**
```bash
# Different versions, different configs
$ pip install mypackage==1.0.0  # Has config v1.0
$ pip install mypackage==2.0.0  # Has config v2.0
```

**Traditional approach:**
- Config is separate from code
- Users might use old config with new code
- Version mismatches cause bugs

### 4. Type Safety

Config as package data enables type-safe access:

```python
from importlib.resources import files
from typing import Any
import yaml

def load_config() -> dict[str, Any]:
    """Type-safe config loading."""
    config_bytes = files("mypackage").joinpath("config.yaml").read_bytes()
    return yaml.safe_load(config_bytes)

# Your editor knows this returns a dict
config = load_config()
```

### 5. Distribution Simplicity

**Building a wheel:**
```bash
$ uv build
```

**Everything is included automatically:**
- ✅ Python modules
- ✅ Config files
- ✅ Templates
- ✅ Static assets
- ✅ Type stubs

**No MANIFEST.in needed!** (pyproject.toml handles it)

## Real-World Scenario

### The Kaggle Competition

**Problem:**
You build an ML package for a Kaggle competition.

**Requirements:**
1. Train locally on GPU workstation
2. Share with team via PyPI
3. Team uses Kaggle notebooks
4. Needs same config everywhere

**Traditional approach fails:**

```python
# Your local code
# mypackage/__init__.py (assumes project root exists)
import yaml
config_path = Path("config.yaml")  # ❌ Breaks on Kaggle

# Your config.yaml at project root
model:
  architecture: "resnet50"
  pretrained: true
```

**What happens:**
```bash
# Local: ✅ Works
$ python train.py

# Kaggle notebook: ❌ Breaks
!pip install mypackage
import mypackage  # FileNotFoundError: config.yaml
```

**ViperX approach succeeds:**

```
src/mypackage/
├── __init__.py
├── config.yaml          # ✅ Inside package
├── models.py
└── train.py
```

```python
# mypackage/config.py
from importlib.resources import files
import yaml

def load_config():
    config_text = files("mypackage").joinpath("config.yaml").read_text()
    return yaml.safe_load(config_text)

# mypackage/train.py
from . import config

def train():
    cfg = config.load_config()  # ✅ Works everywhere
    model = build_model(cfg["model"]["architecture"])
```

**Result:**
```python
# Kaggle notebook
!pip install mypackage
import mypackage
mypackage.train()  # ✅ Works! Config included in wheel
```

## Edge Cases & Solutions

### 1. User-Specific Overrides

**Problem:** Default config in package, but users need custom values.

**Solution:** Cascade loading
```python
from importlib.resources import files
import yaml
from pathlib import Path

def load_config():
    # 1. Load default from package
    default_config = yaml.safe_load(
        files("mypackage").joinpath("config.yaml").read_text()
    )
    
    # 2. Check for user override
    user_config_path = Path.home() / ".mypackage" / "config.yaml"
    if user_config_path.exists():
        user_config = yaml.safe_load(user_config_path.read_text())
        # Merge (user overrides default)
        default_config.update(user_config)
    
    return default_config
```

### 2. Environment-Specific Config

**Problem:** Different config for dev/staging/prod.

**Solution:** Multiple config files
```
src/mypackage/
├── config.yaml          # Default
├── config.dev.yaml
├── config.staging.yaml
└── config.prod.yaml
```

```python
import os

def load_config():
    env = os.getenv("APP_ENV", "default")
    config_name = f"config.{env}.yaml" if env != "default" else "config.yaml"
    
    config_text = files("mypackage").joinpath(config_name).read_text()
    return yaml.safe_load(config_text)
```

### 3. Large Config Files

**Problem:** Config is 100MB (ML models, embeddings).

**Solution:** Separate data package
```python
# Don't bundle huge files in code package
# Instead: Load on-demand from S3, Hugging Face Hub, etc.

def load_large_config():
    """Load config; download large parts if needed."""
    base_config = yaml.safe_load(
        files("mypackage").joinpath("config.yaml").read_text()
    )
    
    # Download large model weights separately
    if not Path("~/.mypackage/model.bin").exists():
        download_from_s3(base_config["model_url"])
    
    return base_config
```

## Backward Compatibility

### Supporting Both Patterns

If you need to support legacy root configs:

```python
from importlib.resources import files
from pathlib import Path
import yaml

def load_config():
    # Try new way first (package data)
    try:
        config_text = files("mypackage").joinpath("config.yaml").read_text()
        return yaml.safe_load(config_text)
    except (FileNotFoundError, ModuleNotFoundError):
        pass
    
    # Fall back to old way (project root)
    root_config = Path(__file__).parent.parent.parent / "config.yaml"
    if root_config.exists():
        return yaml.safe_load(root_config.read_text())
    
    raise FileNotFoundError("No config.yaml found")
```

### Migrating Existing Projects

**Step 1: Move config**
```bash
$ mv config.yaml src/mypackage/
```

**Step 2: Update code**
```python
# Old
config_path = Path(__file__).parent.parent / "config.yaml"

# New
from importlib.resources import files
config_text = files("mypackage").joinpath("config.yaml").read_text()
```

**Step 3: Update pyproject.toml**
```toml
[tool.setuptools.package-data]
mypackage = ["*.yaml", "*.json", "*.toml"]
```

**Step 4: Test**
```bash
$ uv build
$ pip install dist/*.whl --force-reinstall
$ python -c "import mypackage; mypackage.load_config()"
```

## Comparison with Other Approaches

### Approach 1: Environment Variables

**Pros:**
- 12-factor app compliant
- No files needed

**Cons:**
- Complex config is hard (nested structures)
- Not beginner-friendly
- Requires documentation for every variable

**When to use:** Secrets, deployment-specific values

### Approach 2: Setup-time Configuration

**Example:** Django's `manage.py startproject` generates settings.py

**Pros:**
- User customizes during setup

**Cons:**
- Can't update defaults (not in package)
- Users must regenerate on updates

**When to use:** Framework initialization

### Approach 3: Config-in-Package (ViperX)

**Pros:**
- Works everywhere
- Versioned with code
- Easy to use (just import)
- Can still override

**Cons:**
- Config file can't be edited after install (but can override)

**When to use:** Libraries, packages for distribution

## Python Version Compatibility

### Python 3.9+

```python
from importlib.resources import files  # ✅ Recommended

config = files("mypackage").joinpath("config.yaml").read_text()
```

### Python 3.7-3.8 (Legacy)

```python
from importlib.resources import read_text  # Older API

config = read_text("mypackage", "config.yaml")
```

### Python 2.7 / 3.6 (Ancient)

```python
import pkg_resources  # setuptools

config = pkg_resources.resource_string("mypackage", "config.yaml")
```

**ViperX uses Python 3.9+ API** (modern standard).

## Learning More

### Official Resources
- [importlib.resources](https://docs.python.org/3/library/importlib.resources.html) - Official Python docs
- [PyPA: Package Data](https://packaging.python.org/en/latest/guides/using-manifest-in/) - Including non-code files
- [PEP 420](https://www.python.org/dev/peps/pep-0420/) - Namespace packages

### Related Topics
- [Why src/ layout?](src-layout.md) - Package structure rationale
- [Why .env in package?](env-isolation.md) - Environment variable isolation
- [ViperX Configuration](../configuration.md) - How to use ViperX config

### Tools that Use Config-in-Package
- Django (staticfiles, templates)
- Flask (static, templates)
- pytest (config plugins)
- Sphinx (themes, extensions)

---

**Next Steps:**
1. Look at your generated package: `src/mypackage/config.yaml`
2. Try accessing it: `from importlib.resources import files`
3. Build a wheel: `uv build`
4. Install and verify: `pip install dist/*.whl && python -c "import mypackage"`
5. Try in a notebook environment (Colab/Kaggle)

*"Config-in-package: Your settings travel with your code."*
