# Quick Start

> **Goal**: Go from zero to running project in 5 minutes.

---

## Scenario 1: "I just want a simple library"

**The problem**: You need a clean Python package, properly structured, with tests.

**The solution**:

```bash
viperx config get
```

This creates a `viperx.yaml` template. Edit it:

```yaml
project:
  name: "my-utils"
  description: "My utility library"
```

Apply:

```bash
viperx config -c viperx.yaml
cd my_utils
uv sync
uv run my-utils
# Output: Hi from my-utils!
```

**What you get**:
- ✅ Proper `src/` layout
- ✅ `pyproject.toml` ready for PyPI
- ✅ Tests folder
- ✅ CLI entry point

---

## Scenario 2: "I'm building a Kaggle model"

**The problem**: You need:
- Notebooks that can access your config
- A data folder for datasets
- Secrets for API keys

**The solution**:

```yaml
# viperx.yaml
project:
  name: "titanic-survival"
  description: "Kaggle Titanic competition"

settings:
  type: "ml"
  use_env: true
```

```bash
viperx config -c viperx.yaml
```

**What you get**:

```
titanic_survival/
├── notebooks/
│   ├── Base_Kaggle.ipynb    # Kaggle-ready!
│   └── Base_General.ipynb   # Local development
├── data/                    # Dataset caching
└── src/titanic_survival/
    ├── config.py            # Works on Colab/Kaggle!
    ├── .env                  # Your KAGGLE_KEY here
    └── data_loader.py        # Smart caching
```

**Why this works on Kaggle/Colab**:

```python
# In your notebook:
from titanic_survival import SETTINGS, get_config

# This works because config is INSIDE the package
print(SETTINGS['project_name'])
```

---

## Scenario 3: "I need PyTorch for deep learning"

**The problem**: You want all the ML stuff plus:
- PyTorch dependencies
- GPU setup hints
- Model structure

**The solution**:

```yaml
project:
  name: "vision-transformer"
  description: "ViT from scratch"

settings:
  type: "dl"
  framework: "pytorch"
  use_env: true
```

```bash
viperx config -c viperx.yaml
```

**What you get**:
- `torch>=2.5.0` in dependencies
- `torchvision>=0.21.0` included
- Same notebook + data structure

---

## Scenario 4: "I have multiple related packages"

**The problem**: You're building a platform with:
- An API service
- A ML model
- A worker

**The solution**:

```yaml
project:
  name: "my-platform"
  description: "Full stack ML platform"

workspace:
  packages:
    - name: "api"
      type: "classic"
    - name: "model"
      type: "ml"
      use_env: true
    - name: "worker"
      type: "classic"
```

```bash
viperx config -c viperx.yaml
```

**What you get**:

```
my_platform/
├── pyproject.toml       # All scripts registered
└── src/
    ├── my_platform/     # Root package
    ├── api/             # API service
    ├── model/           # ML with .env
    └── worker/          # Background jobs
```

Run any package:

```bash
uv run api
uv run model
uv run worker
```

---

## The Alternative: CLI Flags

Don't like config files? Use flags:

```bash
# Quick classic project
viperx init -n my-lib

# ML project with .env
viperx init -n my-model -t ml --env

# DL with TensorFlow
viperx init -n tf-project -t dl -f tensorflow
```

But **we recommend `viperx.yaml`** because:
- You can version it
- You can share it with teammates
- You won't forget what options you used
