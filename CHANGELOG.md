# Changelog

All notable changes to this project will be documented in this file.

## [1.3.2] - 2026-01-20 📚
### Added
- **Test for Inline Conflict Annotation**: Verifies `# NOT_APPLIED` comments are added

### Changed
- **README Updated**: Test stats (47 tests, 76% coverage), added `viperx config update` docs
- **Total Tests**: 47 (up from 46)

## [1.3.1] - 2026-01-20 🔍
### Added
- **Inline Conflict Commenting**: viperx.yaml now annotated with `# NOT_APPLIED` comments on conflicts
  - Type change blocked → `type: ml  # NOT_APPLIED: type change blocked`
  - use_env/config/tests disabled but file exists → `use_env: false  # NOT_APPLIED: file exists in codebase`
- Total transparency philosophy: No hidden conflicts, all visible in config file

## [1.3.0] - 2026-01-20 🚀
### Added
- **`viperx config update` Command**: Rebuild/sync viperx.yaml from existing codebase
  - Scans src/ for packages
  - Detects use_config, use_env, use_tests from actual files
  - Adds annotations for mismatches (never deletes config lines)
- **ConfigScanner Class**: New `config_scanner.py` for codebase analysis
- **5 New Tests**: Type blocking, README detection, ConfigScanner scenarios

### Changed
- **README Actual Files**: `use_readme` toggle now detects actual config/env/tests files in package
- **Type Change Blocking**: Changing project type (classic→ml, etc.) now blocked with explanation

### Fixed
- README no longer ignores actual config.py when use_config flag is false

## [1.2.2] - 2026-01-20 🐛
### Fixed
- **testpaths Duplication (Root Cause)**: Fixed template `pyproject.toml.j2` to use list-based deduplication
- **testpaths Cleanup**: `_update_testpaths` now always removes duplicates when writing

### Changed
- Added test assertion to verify no duplicate testpaths in initial generation or updates

## [1.2.1] - 2026-01-20 🧹
### Fixed
- **testpaths Deduplication**: No more duplicate entries in `testpaths`
- **Conflict Log Deduplication**: Same conflict not shown multiple times
- **Test Placeholder Consistency**: Toggle uses `test_dummy()` (same as init)
- **use_readme Template**: Toggle now uses Jinja2 `README.md.j2` template (like init)

### Changed
- **License Documentation**: `viperx_config.yaml.j2` now explains MIT vs Apache vs GPLv3

## [1.2.0] - 2026-01-20 🔧
### Fixed
- **No Blank Lines in pyproject.toml**: Consecutive blank lines are now cleaned when adding scripts
- **testpaths Sync**: Adding packages with `use_tests=true` now updates `[tool.pytest.ini_options].testpaths`
- **LICENSE Auto-Update**: Changing license between known types (MIT, Apache-2.0, GPLv3) now updates LICENSE file content

### Added
- **use_readme Toggle**: Enabling `use_readme` in config now creates README.md for packages
- **Feature Toggle Creation**: Enabling `use_env`, `use_config`, `use_tests` on existing packages now creates the corresponding files
- **7 New Tests**: Comprehensive tests for all update features

### Changed
- **Test Coverage**: 78% (up from 77%)
- **Total Tests**: 41 (up from 34)

## [1.1.0] - 2026-01-20 🚀
### Added
- **MkDocs Documentation Site**: Full documentation at https://kpihx.github.io/viperx/
  - Installation, Quick Start, CLI Reference, Configuration, Workspaces, Templates, Contributing
- **Migration System**: `viperx migrate` command for upgrading projects between versions
  - Supports `--dry-run` for preview
  - Tracks `viperx_version` in `viperx.yaml`
- **Homebrew Formula**: Template for macOS/Linux installation via `brew`
- **AUR Package**: Template for Arch Linux installation via `yay`

### Developer
- Added `packaging/homebrew/` and `packaging/aur/` directories

## [1.0.2] - 2026-01-20
### Added
- **`viperx init` Alias**: `viperx init` now works as an alias for `viperx config` (better UX).
- **Template Documentation**: Added `TEMPLATES.md` for contributors explaining all Jinja2 variables.

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
