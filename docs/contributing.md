# Contributing

Thank you for your interest in contributing to ViperX!

## Development Setup

```bash
# Clone
git clone https://github.com/KpihX/viperx.git
cd viperx

# Install dependencies
uv sync

# Verify
uv run viperx --version
```

## Running Tests

```bash
# All tests
uv run pytest src/viperx/tests -v

# With coverage
uv run pytest src/viperx/tests --cov=src/viperx
```

### Test Structure

```
tests/
├── unit/           # Validation tests
├── functional/     # Feature tests
├── scenarios/      # Usage scenarios
└── integration/    # E2E lifecycle
```

## Code Style

We use **ruff** for linting and formatting:

```bash
uv run ruff check src/
uv run ruff format src/
```

## Documentation

### Building Locally

```bash
uv run mkdocs serve
```

Open http://localhost:8000

### Deploying

```bash
uv run mkdocs gh-deploy
```

## Project Structure

```
viperx/
├── src/viperx/
│   ├── main.py           # CLI (Typer)
│   ├── core.py           # Project generation
│   ├── config_engine.py  # Declarative config
│   ├── constants.py      # Defaults
│   ├── templates/        # Jinja2 templates
│   └── tests/            # Test suite
├── docs/                 # MkDocs documentation
├── mkdocs.yml            # MkDocs config
└── pyproject.toml        # Project config
```

## Submitting Changes

1. Fork the repository
2. Create a feature branch: `git checkout -b feat/my-feature`
3. Make your changes
4. Run tests: `uv run pytest`
5. Commit: `git commit -m "feat: description"`
6. Push: `git push origin feat/my-feature`
7. Open a Pull Request

## Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `refactor:` Code restructure
- `test:` Adding tests
- `chore:` Maintenance

## Questions?

Open an issue on [GitHub](https://github.com/KpihX/viperx/issues).
