# test-classic

test-classic

---

## 🧐 Philosophy & Architecture

Values transparency and standard tooling over "black box" magic.
This project was generated with [ViperX](https://github.com/kpihx/viperx).sh/uv/)**, the extremely fast Python package and project manager written in Rust.

### Why `uv`?
Unlike traditional workflows (pip, poetry, venv mixing), `uv` manages the **entire lifecycle**:
- **Python Version**: It installs and manages the correct Python version for this project automatically.
- **Dependencies**: Locking is instant.

- **Environment**: Virtual environments are managed internally, you just run `uv run`.

### ⚙️ Configuration

- **Config**: `src/test_classic/config.yaml` (Loaded automatically)

- **Environment**: `src/test_classic/.env` (Isolated variables)


Edit `config.yaml` to change parameters. The project uses a **Config-in-Package** architecture:
1. `config.yaml` is inside the package.
2. `config.py` loads it safely (even in production wheels).
3. `.env` is isolated within the package source.

---

## 🚀 Getting Started

### Prerequisites

You only need **[uv](https://docs.astral.sh/uv/)**.
No need to install Python or create venvs manually.

### Installation

```bash
# Clone the repo
git clone https://github.com/ivannkamdem/test-classic.git
cd test-classic

# Sync dependencies (creates .venv and installs python if needed)
uv sync
```

## 🧑‍💻 Usage

The entry point depends on your project type.

### For Developers (Code)

To run the package entry point or scripts:

```bash
# Run the main package
uv run test_classic

# Or run a specific script
uv run python src/test_classic/main.py
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

**Step 1: Install directly from GitHub**
```python
!pip install git+https://github.com/ivannkamdem/test-classic.git
```

**Step 2: Use the unified config**
```python
from test_classic import get_dataset_path, SETTINGS
import kagglehub as kh

# Transparency: You can inspect what was loaded
print(f"Loaded config for: {SETTINGS['project_name']}")

# Download datasets defined in config.yaml
# The key 'titanic' maps to 'heptapod/titanic' in the yaml
path = kh.dataset_download(SETTINGS['datasets']['titanic'])
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

└── notebooks/          # Experimentation (Jupyter)

```

