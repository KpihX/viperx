"""
Educational explanations for ViperX actions.

This module contains detailed explanations that are shown when --explain mode is active.
Each explanation teaches the user WHY something is done, not just what is done.
"""

EXPLANATIONS = {
    "uv_init": """
🎓 WHAT'S HAPPENING: Running `uv init`

WHY: `uv init` creates a minimal Python project structure:
- pyproject.toml (project metadata)
- src/<package>/ (your code goes here)
- .python-version (pins Python version)

This is faster than manually creating files and ensures
a standard structure that works with modern Python tooling.

BENEFITS:
- Consistent project layout
- Automatic virtual environment setup
- Compatible with modern Python tools (pytest, ruff, mypy)

📚 Learn more about uv: https://docs.astral.sh/uv/
""",

    "src_layout": """
🎓 WHY THE src/ LAYOUT?

ViperX uses the "src layout" where your package lives in src/<name>/.

PROBLEM (Without src/):
You run `import mypackage` and Python finds the local directory,
even though you haven't installed it. Tests pass locally but fail
on other machines!

SOLUTION (With src/):
You MUST install the package first (uv sync). No accidental imports.

BENEFITS:
1. IMPORT SAFETY: Can't accidentally import uninstalled code
2. TESTING CLARITY: Tests always run against the INSTALLED package
3. PACKAGING SAFETY: Catches packaging bugs before release
4. INDUSTRY STANDARD: Used by pytest, pip, and most modern projects

📚 Learn more: https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/
""",

    "config_in_package": """
🎓 WHY CONFIG INSIDE THE PACKAGE?

Traditional approach: config.yaml at project root
PROBLEM: When installed via pip, root files aren't included!

ViperX approach: config.yaml inside src/<package>/
BENEFITS:
- ✅ Works when pip-installed (config is packaged)
- ✅ Works on Colab/Kaggle (no path issues)
- ✅ Each package has its OWN config (monorepo-friendly)

The config.py loader uses `importlib.resources` which works
whether your code is:
- In a directory
- In a .whl file
- In a .egg file
- On a weird cloud path (Colab/Kaggle)

REAL WORLD SCENARIO:
You upload your package to PyPI. A user pip-installs it.
Your config.yaml is there, inside the package, working perfectly!

📚 Learn more: https://docs.python.org/3/library/importlib.resources.html
""",

    "env_isolation": """
🎓 WHY .env IS ISOLATED IN THE PACKAGE?

Traditional: .env at project root
PROBLEM in monorepos: Which .env gets loaded?

ViperX: .env inside src/<package>/
Each package has its OWN secrets, no confusion.

SECURITY BENEFITS:
- Secrets are isolated per package
- No accidental cross-contamination
- Easier to audit what secrets exist where

⚠️ SECURITY REMINDER:
- NEVER commit .env to git (.env is in .gitignore)
- Use .env.example as a template (committed, no real values)
- In production, use real environment variables

EXAMPLE:
Monorepo with 3 packages? Each has its own .env:
- src/auth/.env (has AUTH_SECRET)
- src/api/.env (has API_KEY)
- src/worker/.env (has QUEUE_URL)
No confusion, no leaks!

📚 Learn more about .env: https://12factor.net/config
""",

    "pyproject_toml": """
🎓 WHY pyproject.toml?

Before 2016, Python packaging was chaos:
- setup.py (executable, security risk)
- setup.cfg (declarative, limited)
- requirements.txt (just deps, no metadata)
- MANIFEST.in (for including files)

PEP 518 introduced pyproject.toml as the SINGLE source of truth.

BENEFITS:
- ✅ Declarative (not executable - no code injection)
- ✅ Standard format (TOML - easy to read and parse)
- ✅ Extensible (tools add their own sections)
- ✅ Build-system agnostic (works with uv, hatch, setuptools)
- ✅ All-in-one (metadata + deps + build + tool configs)

WHAT IT CONTAINS:
[project] - Name, version, authors, dependencies
[build-system] - How to build your package
[tool.*] - Configs for pytest, ruff, mypy, etc.

📚 Learn more:
- PEP 518: https://peps.python.org/pep-0518/
- PEP 621: https://peps.python.org/pep-0621/
""",

    "tests_isolation": """
🎓 WHY TESTS INSIDE THE PACKAGE?

ViperX puts tests in src/<package>/tests/ instead of a top-level tests/.

BENEFITS:
- Tests are packaged with the code
- Clear ownership (which tests belong to which package)
- Works in monorepos without confusion

ALTERNATIVE APPROACH:
Some projects use top-level tests/. That's fine too!
ViperX chooses in-package tests for clarity in workspaces.

RUNNING TESTS:
pytest automatically discovers tests in src/<package>/tests/
No configuration needed!

📚 Learn more: https://docs.pytest.org/en/stable/goodpractices.html
""",

    "uv_benefits": """
🎓 WHY uv?

uv is a modern Python package manager written in Rust.

SPEED:
- 10-100x faster than pip
- Parallel downloads
- Efficient dependency resolution

FEATURES:
- Built-in virtual environment management
- Lock file support (reproducible builds)
- Compatible with pip/PyPI
- No need for separate tools (poetry, pipenv)

DEVELOPER EXPERIENCE:
- One tool for everything: uv sync, uv run, uv add, uv build
- Clear error messages
- Modern CLI design

WHY NOT pip?
pip is great, but uv is the future:
- Faster
- Better UX
- More features
- Still compatible with pip/PyPI

📚 Learn more:
- Official docs: https://docs.astral.sh/uv/
- GitHub: https://github.com/astral-sh/uv
""",

    "gitignore_patterns": """
🎓 WHY .gitignore?

Git tracks EVERYTHING by default. Without .gitignore, you'd commit:
- 500MB of downloaded datasets
- Your secret API keys (SECURITY RISK!)
- Thousands of cache files (__pycache__)
- OS-specific junk (.DS_Store, Thumbs.db)

RULE OF THUMB:
If it can be REGENERATED or is PERSONAL, ignore it.

WHAT TO IGNORE:
✅ Virtual environments (.venv/, venv/)
✅ Compiled Python (__pycache__/, *.pyc)
✅ Build artifacts (dist/, build/, *.egg-info/)
✅ Secrets (.env, *.pem, *.key)
✅ Data files (data/, *.csv - if large)
✅ IDE settings (.vscode/, .idea/)
✅ OS files (.DS_Store, Thumbs.db)

WHAT NOT TO IGNORE:
❌ Source code (obviously!)
❌ .env.example (template, no real secrets)
❌ README, LICENSE, docs
❌ pyproject.toml, uv.lock

📚 Learn more:
- Git docs: https://git-scm.com/docs/gitignore
- Templates: https://github.com/github/gitignore
""",

    "license_choice": """
🎓 WHY LICENSES MATTER?

Without a license, your code is "all rights reserved" by default.
Others CAN'T legally use, modify, or distribute it!

COMMON LICENSES:

MIT (Most Permissive):
- "Do whatever you want, just credit me"
- Used by: React, Node.js, Rails
- Best for: Most projects

Apache-2.0 (Patent Protection):
- Like MIT but with explicit patent rights
- Used by: Kubernetes, Android, TensorFlow
- Best for: Enterprise projects

GPLv3 (Copyleft):
- "Keep it open source forever"
- Used by: Linux, Git, WordPress
- Best for: Projects that must stay open

CHOOSING:
- Want max adoption? MIT
- Want patent protection? Apache-2.0
- Want to keep derivatives open? GPLv3

📚 Learn more: https://choosealicense.com/
""",

    "dependency_pinning": """
🎓 WHY VERSION PINNING MATTERS?

Three strategies:

1. "package>=1.0" (Minimum Version)
   - Flexible, lets users choose
   - BEST FOR: Libraries

2. "package==1.0.0" (Exact Version)
   - Reproducible, predictable
   - BEST FOR: Applications

3. "package~=1.0" (Compatible Release)
   - >=1.0, <2.0 (allows patches/minors)
   - BEST FOR: Balance of both

RULE OF THUMB:
- Libraries: Use >= (let users choose)
- Applications: Use == or lock files (reproducibility)

WHY LOCK FILES (uv.lock)?
Lock files record EXACT versions of ALL dependencies
(including transitive ones). Result: Perfect reproducibility!

📚 Learn more: https://peps.python.org/pep-0440/
""",

    "entry_points": """
🎓 WHY ENTRY POINTS / SCRIPTS?

Entry points create CLI commands when your package is installed!

EXAMPLE:
[project.scripts]
myapp = "mypackage.main:main"

After `pip install mypackage`, users can run:
$ myapp

Instead of:
$ python -m mypackage.main

BENEFITS:
- Cleaner UX
- Works system-wide (if installed globally)
- Standard Python packaging feature

FORMAT:
"command-name" = "module.path:function"

The function must:
- Exist in the specified module
- Take no required arguments (or use argparse/typer)

📚 Learn more: https://packaging.python.org/en/latest/specifications/entry-points/
""",

    "workspace_members": """
🎓 WHY WORKSPACES / MONOREPOS?

A workspace is multiple packages in one repository.

BENEFITS:
- Share dependencies (one lock file)
- Atomic commits across packages
- Easier refactoring
- Single CI/CD pipeline

STRUCTURE:
my-project/
├── src/
│   ├── core/      (package 1)
│   ├── api/       (package 2)
│   └── cli/       (package 3)
├── pyproject.toml (workspace root)
└── uv.lock        (shared lock file)

uv AUTOMATICALLY DETECTS workspaces!
No manual configuration needed.

WHEN TO USE:
- Multiple related packages
- Shared development
- Monorepo architecture

WHEN NOT TO USE:
- Single package projects
- Unrelated code

📚 Learn more: https://docs.astral.sh/uv/concepts/workspaces/
""",
}


def explain(key: str) -> None:
    """
    Print an educational explanation if explain mode is on.
    
    Args:
        key: The explanation key to display
    """
    from viperx.main import state, console
    from rich.panel import Panel
    
    if state.get("explain"):
        if key in EXPLANATIONS:
            console.print()
            console.print(Panel(
                EXPLANATIONS[key].strip(),
                title="🎓 Educational Note",
                border_style="blue",
                padding=(1, 2)
            ))
            console.print()
