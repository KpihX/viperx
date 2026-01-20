# Installation

> **Time to install**: 30 seconds

---

## The Problem

You want ViperX available globally, without polluting your project's dependencies.

---

## The Solution

### Option 1: pipx (Recommended)

```bash
pipx install viperx
```

**Why pipx?**
- Isolated environment (no conflicts)
- Available everywhere
- Easy to upgrade

### Option 2: uv tool

```bash
uv tool install viperx
```

**Why uv?**
- If you're already using uv (you should!)
- Same isolation benefits

---

## Verify It Works

```bash
viperx --version
# ViperX CLI Version: 1.1.0
```

---

## Generate Your First Config

```bash
viperx config get
# Creates viperx.yaml template
```

---

## Updating

```bash
# pipx
pipx upgrade viperx

# uv
uv tool upgrade viperx
```

---

## For Contributors

```bash
git clone https://github.com/KpihX/viperx.git
cd viperx
uv sync
uv run viperx --help
```

---

## Next Steps

→ [Quick Start](quickstart.md) - Real-world examples
