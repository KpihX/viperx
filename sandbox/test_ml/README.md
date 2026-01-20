# test-ml

ML project

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
- **Config**: `src/test_ml/config.yaml` (Loaded automatically)
- **Environment**: `src/test_ml/.env` (Isolated variables)
- **Template**: `src/test_ml/.env.example` (Copy this to `.env`)

The project uses a **Config-in-Package** architecture:
1. `config.yaml` is inside the package.
1. `config.py` loads it safely (even in production wheels).
1. `.env` is isolated within the package source.
1. `.env.example` serves as a template for new developers.

---
## 🚀 Getting Started

### Prerequisites

You only need **[uv](https://docs.astral.sh/uv/)**.
No need to install Python or create venvs manually.

### Installation

```bash
# Ensure you are in the project directory
cd test-ml

# Sync dependencies (creates .venv and installs python if needed)
uv sync
```

## 🧑‍💻 Usage

### For Developers (Code)

To run the package entry point or scripts:

```bash
# Run the main package
uv run test-ml

# Or run a specific script
uv run python src/test_ml/main.py
```
### For Data Scientists (Notebooks)

We use `uv` to launch Jupyter, ensuring it sees the local package and config.

```bash
uv run jupyter notebook
```

- Open `notebooks/Base.ipynb`.
- Note how it imports `config` from the package.

### ☁️ Cloud (Colab / Kaggle)

You can use the code and config from this repository directly in cloud environments without cloning.

**Step 1: Install directly from Git**
```python
!pip install url_to_repo.git
```

**Step 2: Use the unified config**
```python
from test_ml import get_dataset_path, SETTINGS
import kagglehub as kh

# Transparency: You can inspect what was loaded
print(f"Loaded config for: {SETTINGS.get('project_name', 'Unknown')}")
# Download datasets defined in config.yaml
# The key 'titanic' maps to 'heptapod/titanic' in the yaml
if 'datasets' in SETTINGS and 'titanic' in SETTINGS['datasets']:
    path = kh.dataset_download(SETTINGS['datasets']['titanic'])
```

## 🔧 Internal Structure

```text
test-ml/
├── pyproject.toml      # The Single Source of Truth (Dependencies, Metadata)
├── uv.lock             # Exact versions lockfile
├── .python-version     # Pinned Python version
├── src/
│   └── test_ml/
│       ├── __init__.py
│       ├── config.yaml # EDIT THIS for project settings
│       ├── config.py   # Code that loads the yaml above
│       ├── .env        # Secrets (Ignored by git)
│       ├── .env.example # Template for secrets
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
└── notebooks/          # Experimentation (Jupyter)
```