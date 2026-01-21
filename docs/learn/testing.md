# Testing Strategy 🧪

Reliable software requires reliable tests. ViperX structures projects to make testing the path of least resistance.

## The `tests/` Directory

We place the `tests/` directory at the project root (outside `src/`).

```text
my-project/
├── src/
└── tests/
    ├── unit/
    ├── integration/
    └── conftest.py
```

### Exclusion by Default
This structure ensures that tests are **never** accidentally packaged into your distribution wheel. They are development artifacts, not production artifacts.

## Pytest Configuration

ViperX configures `pytest` in `pyproject.toml` to:
- Add the current directory to pythonpath (so it can find `src` if installed locally).
- Use strict markers.
- Filter warnings.

## Unit vs. Integration

ViperX encourages splitting tests:

- **`tests/unit/`**: Fast tests that check individual functions. Should mock out DBs and APIs.
- **`tests/integration/`**: Slower tests that verify the system works together (e.g., actually talking to a test DB).

## `conftest.py`

A global `conftest.py` is generated to hold **Fixtures**. Fixtures are reusable setup/teardown code (like creating a database connection) that can be injected into any test function.
