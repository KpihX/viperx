# Robust Configuration ⚙️

Configuration is the "user interface" of your application for operators and deployments. ViperX promotes a philosophy of **"Strict on Inputs, Liberal on Outputs"**.

## The Hierarchy

ViperX projects are designed to support a clear precedence hierarchy for configuration:

1.  **Environment Variables** (Highest Priority)
2.  **Secrets** (`.env` file)
3.  **Default Values** (in Code)

## The Inner `.env`

One unique ViperX feature is placing `.env` files **inside the package**, not at the root.

```text
src/
└── my_pkg/
    ├── __init__.py
    ├── .env        <-- Here!
    └── config.py
```

### Why?
1.  **Isolation**: In a workspace with multiple services (e.g., `api` and `worker`), they likely have different configuration needs (different DBs, different queues). A root `.env` would force them to share a global namespace.
2.  **Context**: When you move the `src/my_pkg` folder (e.g., into a Docker container), the config context (.env.example) moves with it.

## `config.py` Pattern

ViperX generates a `config.py` module that acts as the **Gateway** to your application's configuration.

- **Load Early**: It runs at import time.
- **Fail Fast**: If a required key (like `DB_PASSWORD`) is missing, the app generally crashes immediately with a clear error, rather than failing subtly 5 minutes later.

For ML/DL projects, generated code often uses **Pydantic Settings**:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"
    admin_email: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

This validates types (e.g., ensuring `PORT` is an integer) before the app even starts.
