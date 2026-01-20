# 🐍 ViperX

> **Professional Python Project Initializer**  
> *The modern, snake-fast way to bootstrap Python projects.*

**ViperX** is a CLI tool designed to generate production-ready Python projects instantly. It leverages **[uv](https://github.com/astral-sh/uv)** for blazing fast dependency management and offers specialized templates for **Machine Learning** (`ml`) and **Deep Learning** (`dl`).

## ✨ Features

- **Blazing Fast**: Built on top of `uv`
- **Pre-configured**: `pyproject.toml`, proper `src` layout, `ruff` ready
- **ML/DL First**: Templates with `torch`, `tensorflow`, `kagglehub`
- **Smart Caching**: Auto-downloads and caches datasets
- **Strict Isolation**: `.env` files isolated in `src/<pkg>/`
- **Config-in-Package**: Works on Local, Colab, and Kaggle
- **Safe Mode**: Never overwrites or deletes files automatically

## Quick Example

```bash
# Classic Package
viperx init -n my-lib

# Machine Learning Project
viperx init -n churn-prediction -t ml --env

# Deep Learning (PyTorch)
viperx init -n deep-vision -t dl -f pytorch
```

## Installation

```bash
# Recommended
pipx install viperx

# Alternative
uv tool install viperx
```

## Next Steps

- [Installation](installation.md) - Detailed installation guide
- [Quick Start](quickstart.md) - 5-minute tutorial
- [CLI Reference](cli-reference.md) - All commands and options
