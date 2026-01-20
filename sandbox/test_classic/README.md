# test-classic

Classic project

---

## 🧐 Philosophy & Architecture

Values transparency and standard tooling over "black box" magic.
This project was generated with [ViperX](https://github.com/kpihx/viperx), using **[uv](https://docs.astral.sh/uv/)**, the extremely fast Python package and project manager written in Rust.

### Why `uv`?
Unlike traditional workflows (pip, poetry, venv mixing), `uv` manages the **entire lifecycle**:
- **Python Version**: It installs and manages the correct Python version for this project automatically.
- **Dependencies**: Locking is instant.
- **Environment**: Virtual environments are managed internally, you just run `uv run`.
### ⚙️ Configuration
- **Config**: `src/test_classic/config.yaml` (Loaded automatically)

The project uses a **Config-in-Package** architecture:
1. `config.yaml` is inside the package.
2. `config.py` loads it safely (even in production wheels).

---
## 🚀 Getting Started

### Prerequisites

You only need **[uv](https://docs.astral.sh/uv/)**.
No need to install Python or create venvs manually.

### Installation

```bash
# Ensure you are in the project directory
cd test-classic

# Sync dependencies (creates .venv and installs python if needed)
uv sync
```

## 🧑‍💻 Usage

### For Developers (Code)

To run the package entry point or scripts:

```bash
# Run the main package
uv run test-classic

# Or run a specific script
uv run python src/test_classic/main.py
```

## 🔧 Internal Structure

```text
test-classic/
├── pyproject.toml      # The Single Source of Truth (Dependencies, Metadata)
├── uv.lock             # Exact versions lockfile
├── .python-version     # Pinned Python version
├── src/
│   └── test_classic/
│       ├── __init__.py
│       ├── config.yaml # EDIT THIS for project settings
│       ├── config.py   # Code that loads the yaml above
│       └── tests/      # Unit tests
│   └── preprocess/
│       ├── __init__.py
│       ├── config.yaml # EDIT THIS for project settings
│       ├── config.py   # Code that loads the yaml above
│       └── tests/      # Unit tests
│   └── proprocess/
│       ├── __init__.py
│       ├── .env        # Secrets (Ignored by git)
│       ├── .env.example # Template for secrets
```