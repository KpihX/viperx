# 🐍 ViperX

> **Don't just build. Understand.**  
> **A tool that teaches you to fly solo.**

## The Problem: "Magic Black Boxes"

Most tools hide complexity. They say *"Trust us"*. 
This creates dependency: when things break, you don't know why.

## The ViperX Way: Conscious Mastery

ViperX is built on a different principle: **Education First**.
When you run `viperx config -t dl`, we don't just dump files. We generate **ultra-commented templates** that explain:

- Why `src/` layout prevents import errors.
- Why `importlib.resources` is safer than `open()`.
- Why your `.env` is isolated.

We handle the heavy lifting (dependencies, boilerplate) so you can focus on **learning the architecture**.

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
