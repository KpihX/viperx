# The `src` Layout 🏗️

ViperX strictly enforces the **`src/` layout** for all projects. This is a topic of much debate in the Python community, but modern best practices overwhelmingly favor `src/`.

## What is it?

In the `src` layout, your code lives inside a `src/` subdirectory, rather than at the root.

**✅ ViperX (Src Layout)**
```text
my-project/
├── pyproject.toml
├── src/
│   └── my_pkg/
│       ├── __init__.py
│       └── main.py
└── tests/
```

**❌ Flat Layout (Not Recommended)**
```text
my-project/
├── pyproject.toml
├── my_pkg/
│   ├── __init__.py
│   └── main.py
└── tests/
```

## Why `src/`?

### 1. The "Import Parity" Problem
In a Flat Layout, running `pytest` adds the current directory (`.`) to `sys.path`. This means `import my_pkg` imports the **local folder**, not the **installed package**.

This leads to:
- **"It works on my machine"**: You might be testing files that aren't actually included in your package build.
- **Testing against uninstalled code**: Your tests might pass, but the built wheel might fail because of missing files or build issues.

### 2. Forces Installation
With the `src/` layout, the root folder does **not** contain your package. To run tests, you **MUST** install your package (in editable mode).

```bash
uv sync  # Installs the package in editable mode
```

This guarantees that you are testing exactly what your users will experience when they install your package.

### 3. Cleaner Root
Your project root remains clean, containing only configuration files (`pyproject.toml`, `README.md`, `LICENSE`, etc.), rather than being cluttered with source code folders.
