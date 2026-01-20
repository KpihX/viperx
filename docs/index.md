# 🐍 ViperX

> **Stop wasting time on project setup.**  
> **Start coding in 30 seconds.**

## The Problem

Every time you start a new Python project, you face the same tedious questions:

- *"How do I structure this properly?"*
- *"What goes in `pyproject.toml`?"*
- *"Where should I put my config files so Colab can find them?"*
- *"Do I need `.env` at root or in the package?"*

**ViperX solves this.** One command, one config file, done.

---

## The Solution: `viperx.yaml`

Instead of memorizing CLI flags, just describe what you want:

```yaml
# viperx.yaml
project:
  name: "churn-predictor"
  description: "Customer churn prediction model"

settings:
  type: "ml"          # ML project with notebooks
  use_env: true       # I need secrets
```

Then run:

```bash
viperx config get     # Generate template (optional)
viperx config -c viperx.yaml
```

**That's it.** You get:

```
churn_predictor/
├── pyproject.toml    # Ready to go
├── notebooks/        # Jupyter ready
├── data/             # For datasets
└── src/churn_predictor/
    ├── main.py       # Entry point
    ├── config.py     # Works on Colab!
    └── .env          # Isolated, safe
```

---

## Why ViperX?

| Problem                       | ViperX Solution                                  |
| ----------------------------- | ------------------------------------------------ |
| "My config breaks on Colab"   | Config lives **inside** your package             |
| ".env leaks between projects" | `.env` is **isolated** in `src/pkg/`             |
| "I forgot what flags I used"  | `viperx.yaml` is your **single source of truth** |
| "Updating breaks my project"  | **Safe Mode**: ViperX never deletes files        |

---

## Quick Links

- [Installation](installation.md) - Get started in 2 minutes
- [Quick Start](quickstart.md) - Real-world examples
- [CLI Reference](cli-reference.md) - All commands
- [Configuration](configuration.md) - `viperx.yaml` deep dive
