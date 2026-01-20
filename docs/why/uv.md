# Why uv?

## What is uv?

`uv` is a modern Python package manager and resolver written in Rust. Think of it as:
- **pip** (install packages)
- **venv** (virtual environments)
- **poetry** (dependency management)
- **pyproject.toml** support

All in one blazing-fast tool.

## The Speed Difference

Real benchmarks from the uv team:

```
Installing 10 packages:

pip:     45 seconds
poetry:  30 seconds
uv:      0.5 seconds  🚀

Resolving dependencies:

pip:     15 seconds
poetry:  10 seconds
uv:      0.3 seconds  🚀
```

**10-100x faster** in real-world use.

## Why ViperX Uses uv

### 1. **Speed**

Waiting for `pip install` slows you down.

**Before (pip):**
```bash
$ pip install torch pandas numpy scikit-learn
# ☕ Time to get coffee... (2-3 minutes)
```

**With uv:**
```bash
$ uv sync
# ✅ Done in 5 seconds
```

### 2. **Better Dependency Resolution**

pip uses a simple resolver that can fail on complex dependencies.

**pip problem:**
```bash
$ pip install package-a package-b
ERROR: package-a requires foo>=1.0, package-b requires foo<1.0
# You have to manually figure it out
```

**uv solution:**
```bash
$ uv add package-a package-b
# Resolves automatically or tells you it's impossible
```

### 3. **Lock Files Built-In**

**Problem with pip:**
```
requirements.txt:
  numpy>=1.20

# Which version actually gets installed?
# Different on different days!
# numpy==1.24.0 today
# numpy==1.25.0 tomorrow (new release)
```

**uv's solution:**
```
pyproject.toml:
  dependencies = ["numpy>=1.20"]

uv.lock:
  [[package]]
  name = "numpy"
  version = "1.24.3"
  # Exact versions locked
```

**Benefits:**
- Same versions on every machine
- Same versions in 6 months
- Reproducible builds

### 4. **Single Tool, Multiple Tasks**

**Old workflow (multiple tools):**
```bash
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ pip install -e .
$ pip freeze > requirements.txt
```

**uv workflow:**
```bash
$ uv sync  # Creates venv, installs deps, installs package
```

One command. Done.

### 5. **Modern Python Support**

uv understands:
- `pyproject.toml` (PEP 621)
- Dependency groups (dev, test, docs)
- Editable installs
- Workspaces (monorepos)

### 6. **Cross-Platform**

Works identically on:
- macOS
- Linux
- Windows
- CI/CD systems

No "works on my machine" problems.

## uv vs pip vs poetry

| Feature | pip | poetry | uv |
|---------|-----|--------|-----|
| Speed | Slow | Medium | **Fast** |
| Lock files | ❌ (manual) | ✅ | ✅ |
| Dependency resolution | Basic | Good | **Excellent** |
| pyproject.toml | ✅ | ✅ | ✅ |
| Workspaces | ❌ | ✅ | ✅ |
| Written in | Python | Python | **Rust** |
| Learning curve | Easy | Medium | Easy |

## Common uv Commands

### Project Setup
```bash
# Initialize new project
$ uv init my-project

# Install dependencies
$ uv sync

# Install with dev dependencies
$ uv sync --dev
```

### Dependency Management
```bash
# Add a dependency
$ uv add requests

# Add a dev dependency
$ uv add --dev pytest

# Remove a dependency
$ uv remove requests

# Update all dependencies
$ uv lock --upgrade
```

### Running Code
```bash
# Run a script
$ uv run python script.py

# Run a command in the venv
$ uv run pytest

# Run your CLI entry point
$ uv run myapp
```

### Virtual Environments
```bash
# Create venv (automatic with uv sync)
$ uv venv

# Activate venv
$ source .venv/bin/activate  # Unix
$ .venv\Scripts\activate     # Windows

# Or just use uv run (no activation needed!)
$ uv run python script.py
```

## How uv is Fast

### Parallel Downloads
```
pip:     Download 1 → Download 2 → Download 3
uv:      Download 1, 2, 3 simultaneously
```

### Smart Caching
```bash
# First install of numpy
$ uv add numpy
# Downloads from PyPI (1 second)

# Later, in another project
$ uv add numpy
# Uses cache (0.1 seconds)
```

### Rust Performance
- Written in Rust (compiled, not interpreted)
- Zero-copy operations
- Efficient memory usage

## Compatibility with pip

uv is compatible with the entire PyPI ecosystem:

```bash
# All these work:
$ uv add package-from-pypi
$ uv add git+https://github.com/user/repo
$ uv add ./local-package
$ uv add package[extra]
```

## Lock File Example

`uv.lock` (generated automatically):
```
version = 1

[[package]]
name = "numpy"
version = "1.24.3"
source = { registry = "https://pypi.org/simple" }
dependencies = []

[[package]]
name = "pandas"
version = "2.0.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "numpy", version = "1.24.3" },
]
```

**What it does:**
- Records exact versions
- Records all transitive dependencies
- Records source (PyPI, git, local)
- Ensures reproducibility

## Workspaces (Monorepos)

uv automatically detects workspaces:

```
my-workspace/
├── src/
│   ├── core/      # Package 1
│   ├── api/       # Package 2
│   └── cli/       # Package 3
├── pyproject.toml # Workspace root
└── uv.lock        # Single lock file
```

**Benefits:**
- Shared dependencies
- Single lock file
- Develop all packages together

## When NOT to Use uv

uv is excellent, but stick with pip if:

1. **Legacy systems**: Python 2.7 or very old Python 3
2. **Corporate restrictions**: Can't install Rust binaries
3. **pip-only CI**: System only has pip

For everything else, uv is superior.

## Migration from pip

### Step 1: Install uv
```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
# or
$ pip install uv
```

### Step 2: Convert requirements.txt
```bash
# Before
requirements.txt:
  numpy>=1.20
  pandas>=2.0

# After (pyproject.toml)
[project]
dependencies = [
    "numpy>=1.20",
    "pandas>=2.0",
]
```

### Step 3: Generate lock file
```bash
$ uv lock
# Creates uv.lock
```

### Step 4: Install
```bash
$ uv sync
# Replaces: pip install -r requirements.txt
```

## Migration from poetry

```bash
# poetry.lock exists
$ uv lock  # Converts to uv.lock

# pyproject.toml with [tool.poetry]
# uv reads [project] section instead
```

## Common Issues & Solutions

### "uv: command not found"

**Install uv:**
```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Add to PATH (in shell config):
```bash
export PATH="$HOME/.cargo/bin:$PATH"
```

### "Python version mismatch"

```bash
# Specify Python version
$ uv venv --python 3.11
```

### "Package not found"

```bash
# Check package name on PyPI
$ uv add package-name  # Correct name
```

## Advanced Features

### Dependency Groups

```toml
[dependency-groups]
dev = ["pytest", "ruff"]
docs = ["mkdocs", "mkdocs-material"]
```

```bash
$ uv sync --dev        # Install dev dependencies
$ uv sync --group docs # Install docs dependencies
```

### Custom Indexes

```bash
$ uv add package --index https://custom.pypi.org
```

### Environment Variables

```bash
$ UV_INDEX_URL=https://pypi.org/simple uv sync
```

## The Future of Python Packaging

uv represents the future:
- **Rust-based** tools (ruff for linting, uv for packaging)
- **Fast** by default
- **Modern** standards (pyproject.toml)
- **Simple** UX

The Python ecosystem is moving to Rust-based tools for performance.

## Learning More

### Official Resources
- [uv Documentation](https://docs.astral.sh/uv/)
- [GitHub: astral-sh/uv](https://github.com/astral-sh/uv)
- [uv Concepts](https://docs.astral.sh/uv/concepts/)

### Comparisons
- [uv vs pip](https://docs.astral.sh/uv/pip/)
- [uv vs poetry](https://docs.astral.sh/uv/concepts/projects/)

### Related Topics
- [Why pyproject.toml?](pyproject.md) - The config file uv uses
- [Why workspaces?](safe-mode.md) - Monorepo support

---

**Next Steps:**
1. Install uv: `curl -LsSf https://astral.sh/uv/install.sh | sh`
2. Try it: `uv sync` in your ViperX project
3. Compare speed: Time `uv add numpy` vs `pip install numpy`

*"uv: Python packaging at the speed of Rust."*
