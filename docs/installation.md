# Installation

## Requirements

- Python 3.11+
- [uv](https://github.com/astral-sh/uv) (recommended) or pip

## Recommended: pipx (Isolated Global Tool)

```bash
pipx install viperx
```

This installs ViperX in an isolated environment, available globally.

## Alternative: uv tool

```bash
uv tool install viperx
```

## Development Installation

```bash
git clone https://github.com/KpihX/viperx.git
cd viperx
uv sync
uv run viperx --help
```

## Verify Installation

```bash
viperx --version
# ViperX CLI Version: 1.0.2
```

## Updating

```bash
# pipx
pipx upgrade viperx

# uv
uv tool upgrade viperx
```
