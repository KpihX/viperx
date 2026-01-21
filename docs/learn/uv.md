# Why uv? 🦀

ViperX is built on top of **[uv](https://github.com/astral-sh/uv)**, an extremely fast Python package installer and resolver written in Rust.

!!! tip "ViperX Philosophy"
    We believe developers shouldn't spend time waiting for dependency resolution. `uv` makes project setup and updates instantaneous.

## Key Benefits

### 1. Speed ⚡
`uv` is designed to be a drop-in replacement for `pip` and `pip-tools`, but significantly faster. It manages its own global cache and uses parallel downloads.

- **10-100x faster** than pip/poetry.
- **Warm cache** installs are essentially instant.

### 2. Determinism 🔒
ViperX uses `uv` to generate a `uv.lock` file. This lockfile ensures that every developer on your team and your CI/CD pipeline installs **exactly** the same versions of dependencies.

### 3. Workspace Support 📦
`uv` has native support for **Workspaces** (monorepos). It allows you to have multiple packages in a single repository that depend on each other, handling the complex resolution graph automatically.

### 4. No Python Dependency 🐍
You don't need to install Python to install `uv` (it's a binary). And crucially, `uv` can **manage Python versions** for you. ViperX leverages this to ensure you're using the correct Python version defined in your `.python-version` file.

## Common Commands

While ViperX abstracts most of this, it's useful to know the underlying `uv` commands:

```bash
uv sync         # Install dependencies from uv.lock
uv add <pkg>    # Add a dependency
uv run <cmd>    # Run a command in the virtual environment
```
