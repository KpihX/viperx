# Changelog

All notable changes to this project will be documented in this file.

## [1.0.1] - 2026-01-20
### Changed
- **Test Structure Reorganization**: Cleaner 4-directory layout:
  - `unit/` - Validation (5 tests)
  - `functional/` - CLI, licenses, project types, builders, content (16 tests)
  - `scenarios/` - Classic, workspace, updates, edge cases (11 tests)
  - `integration/` - E2E lifecycle (2 tests)
- Merged redundant test files for maintainability.

## [1.0.0] - 2026-01-20 🎉
### Added
- **34 Comprehensive Tests**: Full coverage of all usage scenarios.
  - Imperative mode tests (`viperx config -n name -t type`)
  - License change detection (safe mode, no overwrite)
  - Deletion warning for removed packages
  - Feature disable warning for tests/config/env
- **77% Code Coverage**: Up from 74%.

### Philosophy
- ViperX **only adds** new things safely.
- Deletions and updates are **reported** for manual user action.
- Safe Mode: Files are never overwritten or deleted automatically.

## [0.9.99] - 2026-01-20
### Added
- **Comprehensive Test Suite Expansion**: 28 tests covering all usage scenarios.
  - TensorFlow DL framework (`test_dl_tensorflow.py`)
  - All license variations: MIT, Apache-2.0, GPLv3 (`test_licenses.py`)
  - Hatch builder verification (`test_builders.py`)
  - Edge cases: hyphenated names, empty workspaces, unicode (`test_edge_cases.py`)
  - Deep file content verification: `.gitignore`, `README.md`, `main.py` (`test_file_content.py`)

## [0.9.98] - 2026-01-20
### Added
- **Deep Verification Test Suite**: Expanded test coverage to 18 comprehensive tests including functional, CLI, and integration scenarios.
- **Strict Isolation Protocol**: `.env` files are now strictly enforced to reside in `src/<package>/` for all project types, ensuring true non-monolithic architecture.
- **Output Consistency**: Terminal logs now rigorously verified to avoid confusing "Updated" messages during fresh creation.
- **Meticulous Architecture Verification**: Added automated checks for file placement correctness in ML/DL and Workspace modes.

### Changed
- Refactored `config_engine.py` hydration logic to check package-level paths instead of root paths for feature toggles.
- Standardized `ProjectGenerator` to always verify strict isolation rules during scaffolding.

### Fixed
- Fixed a bug where `check_feature` would incorrectly look for `.env` at the workspace root during updates.
- Corrected misleading "Hydrating" logs appearing during initial project setup.

## [0.9.95] - 2026-01-20
### Added
- **Smart Update v2**: Logic to detect and hydrate missing features (tests, config, env) when enabled in `viperx.yaml`.
- **Script Injection**: Automatically adds new package scripts to `[project.scripts]` in `pyproject.toml` without breaking formatting.

## [0.9.80] - 2026-01-20
### Changed
- Switched from `toml` library to regex-based text manipulation for `pyproject.toml` to preserve user comments and formatting.
