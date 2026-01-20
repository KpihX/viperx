# Why pyproject.toml?

## The Problem: Python Packaging Chaos (Pre-2016)

Before `pyproject.toml`, Python packaging was a nightmare of multiple files:

```
my-project/
├── setup.py         # Executable Python (security risk!)
├── setup.cfg        # Some metadata
├── requirements.txt # Just dependencies
├── MANIFEST.in      # What files to include
├── pytest.ini       # pytest config
├── .coveragerc      # coverage config
└── tox.ini          # tox config
```

**Problems:**
1. **Security**: `setup.py` is executable code. Malicious packages could run arbitrary code during install!
2. **Inconsistency**: No standard format. Every tool invented its own config file.
3. **Fragmentation**: Metadata scattered across multiple files.
4. **Confusion**: "Which file do I edit to add a dependency?"

## The Solution: PEP 518 & pyproject.toml (2016)

[PEP 518](https://peps.python.org/pep-0518/) introduced `pyproject.toml` as the **single source of truth**.

### What is TOML?

TOML (Tom's Obvious Minimal Language) is a config file format designed to be:
- **Easy to read**: More human-friendly than JSON
- **Easy to write**: Less verbose than XML
- **Unambiguous**: One obvious way to represent each data type

```toml
# This is clear and readable
[project]
name = "my-package"
version = "1.0.0"
dependencies = ["requests>=2.28.0"]
```

### What Goes in pyproject.toml?

```toml
# =============================================================================
# EVERYTHING for your Python project
# =============================================================================

[project]  # PEP 621: Project metadata
name = "my-package"
version = "1.0.0"
description = "What my package does"
authors = [{name = "Your Name", email = "you@example.com"}]
dependencies = ["requests>=2.28.0"]

[build-system]  # PEP 517: How to build the package
requires = ["uv_build"]
build-backend = "uv_build"

[tool.pytest.ini_options]  # pytest configuration
testpaths = ["tests"]

[tool.ruff]  # ruff linter configuration
line-length = 100

# All in ONE file!
```

## Benefits

### 1. **Declarative (Not Executable)**

**Old way (setup.py):**
```python
# This is EXECUTABLE CODE - security risk!
import sys
if sys.platform == "win32":
    # Malicious code could go here
    os.system("rm -rf /")  # Danger!

setup(
    name="my-package",
    version="1.0.0"
)
```

**New way (pyproject.toml):**
```toml
# This is DATA, not code. Safe!
[project]
name = "my-package"
version = "1.0.0"
```

### 2. **Standard Format**

Before PEP 621, every tool had its own metadata format:
- setuptools: `setup()` function
- poetry: Custom `[tool.poetry]` section
- flit: Different conventions

Now everyone follows **PEP 621** for the `[project]` section.

### 3. **Single Source of Truth**

All configuration in one place:
- Project metadata → `[project]`
- Dependencies → `[project.dependencies]`
- Build system → `[build-system]`
- Tool configs → `[tool.*]`

### 4. **Extensible**

Tools can add their own sections:
```toml
[tool.pytest.ini_options]
# pytest-specific config

[tool.ruff]
# ruff-specific config

[tool.mypy]
# mypy-specific config
```

## Common Sections Explained

### `[project]` - PEP 621 Metadata

```toml
[project]
name = "my-package"           # PyPI name (lowercase, hyphens)
version = "1.0.0"              # Semantic versioning
description = "Short summary"  # One-line description
readme = "README.md"           # Long description file
requires-python = ">=3.9"      # Minimum Python version
dependencies = [               # Runtime dependencies
    "requests>=2.28.0",
]
```

### `[build-system]` - PEP 517 Build Config

```toml
[build-system]
requires = ["uv_build"]      # What's needed to build
build-backend = "uv_build"   # Which backend to use
```

**Build backends:**
- **uv** (ViperX default): Modern, fast, Rust-based
- **hatchling**: Good defaults, popular
- **setuptools**: Old standard, complex but feature-rich

### `[project.scripts]` - Entry Points

```toml
[project.scripts]
myapp = "mypackage.main:main"
```

After install, users can run:
```bash
$ myapp  # Instead of python -m mypackage.main
```

### `[dependency-groups]` - Dev Dependencies

```toml
[dependency-groups]
dev = [
    "pytest>=8.0",
    "ruff>=0.1.0",
]
```

Install with: `uv sync --dev`

## Version Pinning Strategies

### For Libraries (Use `>=`)
```toml
dependencies = [
    "requests>=2.28.0",  # Allow newer versions
]
```
**Why:** Let users choose their own versions. Avoid dependency conflicts.

### For Applications (Use `==` or lock files)
```toml
dependencies = [
    "requests==2.31.0",  # Exact version
]
```
**Why:** Reproducible builds. Same versions in dev and production.

**Better:** Use `uv.lock` files (like `package-lock.json`):
```toml
dependencies = [
    "requests>=2.28.0",  # Flexible in pyproject.toml
]
# But uv.lock records exact versions:
# requests==2.31.0
# urllib3==2.0.4
# ...
```

## Migration from Old Files

### From setup.py

**Old:**
```python
from setuptools import setup

setup(
    name="my-package",
    version="1.0.0",
    install_requires=["requests"],
)
```

**New:**
```toml
[project]
name = "my-package"
version = "1.0.0"
dependencies = ["requests"]

[build-system]
requires = ["setuptools"]
build-backend = "setuptools.build_meta"
```

### From requirements.txt

**Old:**
```
# requirements.txt
requests==2.31.0
pandas>=2.0.0
```

**New:**
```toml
[project]
dependencies = [
    "requests>=2.31.0",  # Use >= for libraries
    "pandas>=2.0.0",
]
```

## Common Pitfalls

### ❌ Don't use exact versions in libraries
```toml
# BAD for libraries
dependencies = ["requests==2.31.0"]
```
**Problem:** Forces users to use that exact version.

### ✅ Do use minimum versions
```toml
# GOOD for libraries
dependencies = ["requests>=2.31.0"]
```

### ❌ Don't duplicate metadata
```toml
# BAD
[project]
version = "1.0.0"

[tool.myapp]
version = "1.0.0"  # Duplicate!
```

### ✅ Do keep version in one place
```toml
# GOOD
[project]
version = "1.0.0"

# Reference it dynamically in code if needed
```

## Learning More

### Official Documentation
- [PEP 518 - pyproject.toml](https://peps.python.org/pep-0518/)
- [PEP 621 - Project Metadata](https://peps.python.org/pep-0621/)
- [PEP 517 - Build Systems](https://peps.python.org/pep-0517/)
- [PyPA Packaging Guide](https://packaging.python.org/)

### Tools That Use pyproject.toml
- [uv](https://docs.astral.sh/uv/) (ViperX default)
- [hatch](https://hatch.pypa.io/)
- [poetry](https://python-poetry.org/)
- [setuptools](https://setuptools.pypa.io/)

### Related Topics
- [Why uv?](uv.md) - Why ViperX uses uv as the default builder
- [Why src/ layout?](src-layout.md) - Project structure best practices

---

**Next Steps:**
1. Read the [PEP 621 specification](https://peps.python.org/pep-0621/)
2. Explore your generated `pyproject.toml` (it has educational comments!)
3. Try modifying it (add a dependency, change the version)

*"pyproject.toml: One file to rule them all."*
