# Why the src/ Layout?

## The Two Layouts

Python projects can be structured in two ways:

### Flat Layout (Looks Simple)
```
my-package/
├── mypackage/
│   ├── __init__.py
│   └── module.py
├── tests/
├── pyproject.toml
└── README.md
```

### src/ Layout (ViperX Default)
```
my-package/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── module.py
├── tests/
├── pyproject.toml
└── README.md
```

**One extra directory. Why does it matter?**

## The Problem: Accidental Imports

### Flat Layout Danger

With flat layout, you can accidentally import **uninstalled** code:

```bash
# Flat layout directory
my-package/
├── mypackage/  # Package directory
│   └── module.py
└── tests/
    └── test_module.py
```

```python
# In tests/test_module.py
import mypackage  # This works!
```

**But you never installed the package!**

Python finds `mypackage/` in the current directory and imports it directly.

**Why is this bad?**
1. ✅ Tests pass locally
2. ❌ Tests fail on CI (package not in current dir)
3. ❌ Tests fail for other developers
4. ❌ Package breaks when pip-installed

**The Bug:**
```python
# You added this in mypackage/__init__.py
from .config import load_settings

# But forgot to add config.py to MANIFEST.in
# Local tests pass (config.py is there in the filesystem)
# But after pip install, config.py is missing!
# Users get ImportError
```

### src/ Layout Safety

With src/ layout:

```bash
my-package/
├── src/
│   └── mypackage/
│       └── module.py
└── tests/
    └── test_module.py
```

```python
# In tests/test_module.py
import mypackage  # ModuleNotFoundError!
```

**You MUST install the package first:**
```bash
$ pip install -e .  # or uv sync
```

Now imports work correctly because the package is **installed**, not just found in the filesystem.

**Benefits:**
1. ✅ Can't accidentally import uninstalled code
2. ✅ Tests run against the INSTALLED package
3. ✅ Catches packaging bugs early
4. ✅ Identical behavior local vs CI vs production

## Real-World Scenario

### The Bug That Would Have Been Caught

**Developer writes code (flat layout):**
```python
# mypackage/utils.py
def helper():
    return "data"

# mypackage/main.py
from .utils import helper  # Works locally!
```

**Adds to pyproject.toml but forgets to commit utils.py:**
```toml
[project]
name = "mypackage"
# utils.py exists in local filesystem but not in git
```

**Tests pass locally:**
```bash
$ pytest  # ✅ Passes (imports from filesystem)
```

**CI fails:**
```bash
$ pip install .
$ pytest  # ❌ ImportError: cannot import name 'helper'
```

**With src/ layout, this would have failed immediately:**
```bash
$ pytest  # ❌ ModuleNotFoundError: No module named 'mypackage'
$ pip install -e .  # Developer realizes they need to install
$ pytest  # ❌ ImportError (catches the missing utils.py)
```

## Benefits in Detail

### 1. Import Safety

**Flat layout:**
- Python finds package in current directory
- No installation needed for local imports
- Easy to forget to actually install the package

**src/ layout:**
- Package not in Python's search path by default
- MUST install to import
- Forces you to develop like a user would use it

### 2. Testing Clarity

**Question:** Are you testing the SOURCE CODE or the INSTALLED PACKAGE?

**Flat layout:** Testing source code directly (not realistic)
**src/ layout:** Testing installed package (realistic)

### 3. Packaging Bugs Caught Early

Common packaging bugs that src/ layout catches:

❌ **Missing files in package:**
```python
# Forgot to include data_file.json
from . import data_file  # Works in flat, breaks in src/
```

❌ **Wrong import paths:**
```python
# Used absolute import instead of relative
import mypackage.utils  # Works in flat, might break in src/
```

❌ **Namespace collisions:**
```python
# Package name conflicts with stdlib
import email  # Python's email or your email/?
```

### 4. Editable Installs Work Correctly

```bash
$ pip install -e .
# or
$ uv sync
```

Editable installs create a link to the package source.

**Flat layout:** Might work accidentally without editable install
**src/ layout:** Forces proper editable install setup

## Workflow Comparison

### Flat Layout Workflow

```bash
# Clone repo
$ git clone repo.git
$ cd repo

# Run tests (accidentally works)
$ pytest  # Imports from local dir, not installed package

# Make changes
$ edit mypackage/module.py

# Tests still pass locally
$ pytest  # Still using local dir

# Ship to production
$ pip install .
$ python -m mypackage  # ❌ Might fail if packaging is broken!
```

### src/ Layout Workflow (ViperX)

```bash
# Clone repo
$ git clone repo.git
$ cd repo

# Try to run tests
$ pytest  # ❌ ModuleNotFoundError (good!)

# Install package (editable mode)
$ uv sync  # or pip install -e .

# Now tests work
$ pytest  # ✅ Using installed package

# Make changes
$ edit src/mypackage/module.py

# Tests run against changes (editable install)
$ pytest  # ✅ Still using installed package

# Ship to production
$ pip install .
$ python -m mypackage  # ✅ Works (packaging was tested!)
```

## When to Use Flat Layout?

Flat layout is acceptable for:

1. **Single-file scripts** (not packages)
2. **Learning/tutorial projects** (simplicity matters)
3. **Namespace packages** (advanced use case)

For everything else, use src/ layout.

## Migration from Flat to src/

Easy migration:

```bash
# Before
mypackage/
  __init__.py
  module.py

# After
mkdir src
mv mypackage src/
```

Update `pyproject.toml`:
```toml
[tool.setuptools.packages.find]
where = ["src"]  # If using setuptools
```

Reinstall:
```bash
$ pip install -e .
```

## Common Misconceptions

### "It's just one extra directory"

**True**, but that directory changes **how Python finds your package**.

### "Flat layout is simpler"

**Simpler to set up**, but more complex to maintain and debug.

### "My tests work locally, so it's fine"

**Locally** ≠ **on CI** ≠ **for users**. src/ layout makes all three identical.

## Official Recommendations

The Python Packaging Authority (PyPA) recommends src/ layout:

> "The src layout is generally recommended for new projects."
> — [PyPA Packaging Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)

**Used by:**
- pytest
- pip
- Most modern Python tools

## Learning More

### Official Resources
- [PyPA: src/ vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [Ionel's Article (Detailed)](https://blog.ionelmc.ro/2014/05/25/python-packaging/)
- [Hynek's Article](https://hynek.me/articles/testing-packaging/)

### Related Topics
- [Why pyproject.toml?](pyproject.md) - Modern Python packaging
- [Why config-in-package?](config-in-package.md) - Where to put config files

---

**Next Steps:**
1. Look at your generated project structure
2. Try `uv sync` to install the package
3. Try importing without installing (should fail!)
4. Compare `pytest` results before and after install

*"src/ layout: Safety through isolation."*
