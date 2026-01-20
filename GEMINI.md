
# 🤖 GEMINI PROTOCOL

## 🌟 Core Philosophy
- **Transparency**: No hidden state. Every choice is visible in `viperx.yaml`.
- **Efficiency**: Save time. "Start coding in 30s".
- **Education**: Generated files are "ultra-commented". We don't just dump config; we teach usage.
- **Verbosity**: Verbose by default. The user shouldn't have to guess what's happening.

**CRITICAL INSTRUCTIONS FOR AI AGENT**

You must follow these rules at the end of **EVERY** substantial task.
Do not consider a task "Done" until you have performed this check.

## 🔄 The "Update Loop"

After completing any code modification or feature addition, you MUST check if updates are needed for:

4.  **`pyproject.toml`**:
    - Did you add a dependency? (e.g., `typer`, `rich`).
    - Did you change build scripts?

5. **`docs/` & Meta-Files**:
   - **CRITICAL**: Before any release, verify `docs/changelog.md` and other documentation files match the new version.
   - Users rely on the site; it must not lag behind the code.

2.  **`CHANGELOG.md`**:
    - Add a new entry under `[Unreleased]` or bump the version.
    - Document everything you just did (Added, Changed, Fixed).

3.  **`ROADMAP.md`**:
    - Move completed items from "To Do" to "Done".
    - Add new future tasks if identified during execution.

4.  **`pyproject.toml`**:
    - Did you add a dependency? (e.g., `typer`, `rich`).
    - Did you change build scripts?

## 🧪 Test & Verification Protocol

**Before finalizing any changes (Git Sync/Release), you MUST:**
1.  **Run the full test suite**:
    ```bash
    uv run pytest src/viperx/tests
    ```
2.  **Verify no regressions**: If tests fail, FIX THEM. Do not proceed.

## 🚀 Deployment Protocol

**After verifying the code and updating documentation (The "Update Loop"), you MUST execute the following Release Cycle:**

1.  **Meta-Sync Check**:
    - Confirm `docs/` site files match `CHANGELOG.md` and current features.

2.  **Git Sync**:
    ```bash
    git add .
    git commit -m "feat: <Summary of changes>"
    git remote | xargs -n1 git push
    ```

2.  **PyPI Release**:
    ```bash
    rm -rf dist/*
    uv build
    uv publish
    ```

3.  **Local Verification**:
    ```bash
    # Update local tool to match the new release
    pipx install --force viperx
    ```

4.  **Retention Policy**:
    - Keep only the **last 2 versions** on PyPI and Local `dist/`.
    - Delete older versions to keep context and storage clean.

Only when this cycle is complete is the task considered "Done".

## 🚫 Stop Condition

> "I will not stop until I have checked if these files need updates."

If you forget this, the documentation will drift from the code, which is strictly forbidden.
