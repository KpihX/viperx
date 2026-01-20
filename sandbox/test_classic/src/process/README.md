# process

processing utilities

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
- **Config**: `src/process/config.yaml` (Loaded automatically)
- **Environment**: `src/process/.env` (Isolated variables)
- **Template**: `src/process/.env.example` (Copy this to `.env`)

The project uses a **Config-in-Package** architecture:
1. `config.yaml` is inside the package.
1. `config.py` loads it safely (even in production wheels).
1. `.env` is isolated within the package source.
1. `.env.example` serves as a template for new developers.

---

## 🧑‍💻 Usage

### For Developers (Code)

To run the package entry point or scripts:

```bash
# Run the main package
uv run process

# Or run a specific script
uv run python src/process/main.py
```

## 🔧 Internal Structure

```text
process/
├── __init__.py
├── config.yaml # EDIT THIS for project settings
├── config.py   # Code that loads the yaml above
├── .env        # Secrets (Ignored by git)
├── .env.example # Template for secrets
└── tests/      # Unit tests
```