# 🗺️ PyPro Roadmap

This document tracks the evolution of `pypro`.
**Workflow:** Check items in "To Do". When completed, move them to the "Done" history below.

## 🚀 To Do

### Phase 2: The "Ecosystem" Era (V1.5+) 🏗️
- [ ] **CI/CD Integration**
    - [ ] `viperx init --ci github`: Generate `.github/workflows/test.yml` (Optimized `uv cache`).
- [ ] **Docker Support** 🐳
    - [ ] Generate optimized `Dockerfile` (Distroless/Alpine).
    - [ ] Auto-detect DL type -> Use `nvidia/cuda` base image.

### Phase 3: The "Hard Mode" (V2.0) 🧠
- [ ] **Bidirectional Sync (Diff)**
    - [ ] `viperx sync`: Show diff between Code and Config before merging.
- [ ] **Plugins / Custom Templates**
    - [ ] `viperx template add <git-url>` for external organization templates.

## ✅ Done

- [x] **V1.4.0: Robustness & DX**
    - [x] **Safe Parsing**: Migrated regex -> `tomlkit` for `pyproject.toml` editing.
    - [x] **Ejection**: `viperx eject` to remove vendor lock-in.
    - [x] **Wizard**: Interactive mode for `viperx config` (no args).

- [x] **V9: Declarative Config (Infrastucture as Code)**
    - [x] `viperx.yaml` schema definition.
    - [x] `ConfigEngine` for parsing and idempotent execution.
    - [x] `viperx config init` and `viperx init --config`.
    - [x] Advanced robustness (Hydration, Git integration).

- [x] **V4-V8: Ecosystem & Polish**
    - [x] **Rebranding**: PyPro -> ViperX (v0.8.0).
    - [x] **Data Loading**: `data_loader.py` and `data/` caching (v0.7.0).
    - [x] **Isolation**: Strict `.env` encapsulation (v0.6.0).
    - [x] **DL Choice**: `--framework pytorch/tensorflow` (v0.5.0).
    - [x] **Refactor**: CLI Hygiene and `package` subcommand group.

- [x] **V3.1: Multi-Package & Polish**
    - [x] Global `-v`/`--verbose` flag for transparent logging.
    - [x] Command `add-package` to manage Workspaces.
    - [x] Automatic Workspace upgrade logic.
    - [x] `LICENSE` generation (MIT, Apache 2.0, GPLv3).
    - [x] "Glass Box" `README.md` templates.

- [x] **V2: Core Refinement**
    - [x] Native `uv init --package` integration.
    - [x] Dynamic system Python version detection.
    - [x] Config-in-Package architecture verification.
    - [x] ML/DL Templates with `kagglehub` integration.
