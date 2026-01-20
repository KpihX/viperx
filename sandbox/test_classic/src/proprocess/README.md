# proprocess

proprocess utilities

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



- **Environment**: `src/proprocess/.env` (Isolated variables)


The project uses a **Config-in-Package** architecture:


3. `.env` is isolated within the package source.



---

## 🚀 Getting Started

### Prerequisites

You only need **[uv](https://docs.astral.sh/uv/)**.
No need to install Python or create venvs manually.

### Installation

```bash
# Ensure you are in the project directory
cd proprocess

# Sync dependencies (creates .venv and installs python if needed)
uv sync
```

## 🧑‍💻 Usage

### For Developers (Code)

To run the package entry point or scripts:

```bash
# Run the main package
uv run proprocess

# Or run a specific script
uv run python src/proprocess/main.py
```



## 🔧 Internal Structure

```text
proprocess/
├── pyproject.toml      # The Single Source of Truth (Dependencies, Metadata)
├── uv.lock             # Exact versions lockfile
├── .python-version     # Pinned Python version
├── src/


│   └── proprocess/
│       ├── __init__.py




```


