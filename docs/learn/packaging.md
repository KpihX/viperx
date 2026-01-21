# Modern Python Packaging 📦

Python packaging has evolved. ViperX adheres strictly to **modern standards**, specifically **PEP 621**.

## The `pyproject.toml` Standard

Gone are the days of `setup.py`, `setup.cfg`, `requirements.txt`, and `MANIFEST.in`.
The **Single Source of Truth** for your project is now `pyproject.toml`.

### Anatomy of a ViperX `pyproject.toml`

```toml
[project]
name = "my-lib"
version = "0.1.0"
description = "My awesome library"
requires-python = ">=3.12"
dependencies = [
    "typer>=0.9.0",
    "rich>=13.0.0"
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = [
    "pytest>=8.0",
    "ruff>=0.1.0"
]
```

### Why no `requirements.txt`?

We use `uv.lock` instead.
- **requirements.txt** is often manually maintained or generated via `pip freeze`, which is error-prone.
- **uv.lock** is automatically generated, strictly deterministic, and handles cross-platform hashes.

!!! note "Deployment"
    If you need `requirements.txt` for a legacy deploy system, you can generate it easily:
    `uv export --format requirements-txt > requirements.txt`

## The Build Backend

ViperX defaults to **Hatchling** (`hatchling.build`). It is a modern, extensible build backend that supports the standard `src` layout out of the box and is significantly faster and cleaner than `setuptools`.
