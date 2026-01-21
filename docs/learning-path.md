# 🎓 Learning Path: From Beginner to Autonomous

> **The Goal:** After following this path, you won't need ViperX anymore. And that's exactly what we want.

ViperX is designed to **teach** you Python project development, not just automate it. This learning path takes you from complete beginner to independent developer in 4 progressive levels.

---

## 📊 The Four Levels

```
Level 1: USER       → "I can create projects with ViperX"
Level 2: OBSERVER   → "I understand WHY ViperX does this"
Level 3: APPRENTICE → "I can modify what ViperX creates"
Level 4: INDEPENDENT → "I don't need ViperX anymore" 🎉
```

Each level builds on the previous one. Don't skip ahead!

---

## Level 1: 👤 User (Projects 1-2)

**Goal:** Create working projects using ViperX

**Duration:** 1-2 hours

### What You'll Learn
- How to use ViperX CLI
- Basic project structure
- Running your first project

### Checklist

- [ ] Install ViperX
  ```bash
  pipx install viperx
  ```

- [ ] Create a classic project
  ```bash
  viperx config -n my-lib
  ```

- [ ] Understand the generated structure
  ```
  my-lib/
  ├── src/
  │   └── my_lib/
  │       ├── __init__.py
  │       ├── main.py
  │       └── config.py
  ├── pyproject.toml
  ├── README.md
  └── .gitignore
  ```

- [ ] Install and run
  ```bash
  cd my_lib
  uv sync
  uv run my-lib
  ```

- [ ] Create an ML project
  ```bash
  viperx config -n ml-experiment -t ml
  ```

- [ ] Explore the notebooks
  ```bash
  jupyter notebook notebooks/Base_General.ipynb
  ```

### Success Criteria

✅ You can create projects
✅ You can run the generated code
✅ You understand WHAT files exist

### What You DON'T Know Yet

❓ WHY each file exists
❓ WHY this structure is used
❓ HOW to modify the structure

**Time to move to Level 2!**

---

## Level 2: 👁️ Observer (Projects 3-5)

**Goal:** Understand WHY each file exists and HOW they work together

**Duration:** 2-4 hours

### What You'll Learn
- Why src/ layout
- Why pyproject.toml
- Why config-in-package
- How imports work
- How entry points work

### Checklist

- [ ] Use `--explain` mode
  ```bash
  viperx config -n my-project --explain
  ```
  **Read every explanation that appears!**

- [ ] Read the ultra-comments
  Open these generated files and READ the comments:
  - [ ] `pyproject.toml` (every section explained)
  - [ ] `src/my_project/config.py` (config pattern explained)
  - [ ] `src/my_project/main.py` (entry points explained)
  - [ ] `.gitignore` (every pattern explained)

- [ ] Read the "Why?" documentation
  - [ ] [Why pyproject.toml?](why/pyproject.md)
  - [ ] [Why src/ layout?](why/src-layout.md)
  - [ ] [Why uv?](why/uv.md)
  - [ ] [Why config-in-package?](why/config-in-package.md)
  - [ ] [Why isolated .env?](why/env-isolation.md)
  - [ ] [Why Safe Mode?](why/safe-mode.md)

- [ ] Use the `learn` command
  ```bash
  viperx learn          # See all topics
  viperx learn packaging
  viperx learn uv
  viperx learn testing
  ```

- [ ] Experiment with imports
  ```python
  # Try importing WITHOUT installing
  import my_project  # Should fail!

  # Install first
  # uv sync

  # Now import works
  import my_project  # Success!
  ```

- [ ] Understand the entry point
  ```bash
  # Look in pyproject.toml
  [project.scripts]
  my-project = "my_project.main:main"

  # This is why `my-project` runs your code!
  ```

### Success Criteria

✅ You understand WHY src/ layout is used
✅ You understand WHY config is in the package
✅ You can explain the project structure to someone else
✅ You know what pyproject.toml does

### Exercises

1. **The Import Test**
   - Delete `.venv/`
   - Try to run `python -c "import my_project"`
   - Understand why it fails
   - Run `uv sync`
   - Try again, understand why it works

2. **The Config Test**
   - Modify `src/my_project/config.yaml`
   - Run your project
   - See the changes take effect
   - Understand why config-in-package works

3. **The Entry Point Test**
   - Look at `[project.scripts]` in pyproject.toml
   - Try running `my-project` command
   - Understand how it finds the `main()` function

**Ready for Level 3!**

---

## Level 3: 🔧 Apprentice (Projects 6-10)

**Goal:** Modify projects confidently and understand advanced features

**Duration:** 1-2 weeks (real projects)

### What You'll Learn
- How to add dependencies
- How to create new modules
- How to write tests
- How to use workspaces
- How to customize templates

### Checklist

- [ ] Add a dependency manually
  ```bash
  uv add requests
  # Or edit pyproject.toml:
  dependencies = [
      "requests>=2.31.0",
  ]
  uv sync
  ```

- [ ] Create a new module
  ```bash
  touch src/my_project/utils.py
  ```
  ```python
  # src/my_project/utils.py
  def helper():
      return "Hello!"

  # src/my_project/main.py
  from .utils import helper
  ```

- [ ] Write and run tests
  ```python
  # src/my_project/tests/test_utils.py
  from my_project.utils import helper

  def test_helper():
      assert helper() == "Hello!"
  ```
  ```bash
  pytest
  ```

- [ ] Create a workspace (monorepo)
  ```bash
  viperx config -n my-workspace
  cd my_workspace
  viperx package add -n core
  viperx package add -n api
  viperx package add -n cli
  ```

- [ ] Customize templates
  ```bash
  viperx template eject
  # Edit ~/.config/viperx/templates/main.py.j2
  viperx config -n custom-project
  ```

- [ ] Use advanced features
  ```toml
  [dependency-groups]
  dev = ["pytest", "ruff"]
  docs = ["mkdocs"]
  ```
  ```bash
  uv sync --dev
  ```

- [ ] Configure tools
  ```toml
  [tool.pytest.ini_options]
  testpaths = ["src/my_project/tests"]

  [tool.ruff]
  line-length = 100
  ```

### Success Criteria

✅ You can add dependencies without ViperX
✅ You can create new modules
✅ You can write and run tests
✅ You can use workspaces
✅ You understand how to customize

### Projects to Build

At this level, build real projects:

1. **CLI Tool** (requests, typer)
   - Fetch data from an API
   - Process and display results
   - Add tests

2. **Data Analysis** (pandas, matplotlib)
   - Load a dataset
   - Analyze and visualize
   - Create a notebook

3. **Web API** (fastapi)
   - Create REST endpoints
   - Add database
   - Add tests

4. **Workspace Project** (monorepo)
   - Core library
   - CLI interface
   - Web API
   - Shared tests

**Almost there! Level 4 awaits.**

---

## Level 4: 🦅 Independent (Projects 11+)

**Goal:** Create projects WITHOUT ViperX

**Duration:** Ongoing

### What You'll Learn
- How to create pyproject.toml from scratch
- How to set up src/ layout manually
- How to configure build systems
- How to publish to PyPI

### Checklist

- [ ] Create a project from scratch (no ViperX)
  ```bash
  mkdir my-project
  cd my-project
  ```

- [ ] Write pyproject.toml manually
  ```toml
  [project]
  name = "my-project"
  version = "0.1.0"
  description = "My awesome project"
  dependencies = []

  [build-system]
  requires = ["uv_build"]
  build-backend = "uv_build"
  ```

- [ ] Create src/ layout
  ```bash
  mkdir -p src/my_project
  touch src/my_project/__init__.py
  touch src/my_project/main.py
  ```

- [ ] Add entry points
  ```toml
  [project.scripts]
  my-project = "my_project.main:main"
  ```

- [ ] Configure pytest
  ```toml
  [dependency-groups]
  dev = ["pytest>=8.0"]

  [tool.pytest.ini_options]
  testpaths = ["src/my_project/tests"]
  ```

- [ ] Build and publish
  ```bash
  uv build
  # Creates dist/my_project-0.1.0.tar.gz

  uv publish
  # Publishes to PyPI
  ```

- [ ] Optional: Eject from ViperX
  ```bash
  viperx eject
  # Removes viperx.yaml
  # You're free!
  ```

### Success Criteria

✅ You created a project without ViperX
✅ You understand every line in pyproject.toml
✅ You can explain the structure to beginners
✅ **You no longer need ViperX!** 🎉

### Advanced Topics

Once independent, explore:

- **CI/CD**: GitHub Actions, GitLab CI
- **Documentation**: MkDocs, Sphinx
- **Linting**: Ruff, mypy
- **Type hints**: Full type coverage
- **Publishing**: PyPI, conda-forge
- **Docker**: Containerize your apps
- **Packaging**: Wheels, source dists

---

## 📊 Quick Reference Cards

### Level 1: User Commands
```bash
viperx config -n NAME          # Create project
cd NAME && uv sync             # Install
uv run NAME                    # Run
```

### Level 2: Learning Commands
```bash
viperx config -n NAME --explain  # Educational mode
viperx learn TOPIC               # Show resources
cat src/NAME/config.py           # Read comments
```

### Level 3: Development Commands
```bash
uv add PACKAGE                 # Add dependency
uv sync --dev                  # Install dev deps
pytest                         # Run tests
viperx template eject          # Customize templates
```

### Level 4: Independent Commands
```bash
# No ViperX needed!
mkdir -p src/NAME
vim pyproject.toml
uv sync
uv build
```

---

## 🎯 Milestones

Track your progress:

- [ ] **Milestone 1:** Created first project with ViperX
- [ ] **Milestone 2:** Understand src/ layout
- [ ] **Milestone 3:** Can explain pyproject.toml to a friend
- [ ] **Milestone 4:** Added custom dependency
- [ ] **Milestone 5:** Created workspace
- [ ] **Milestone 6:** Customized templates
- [ ] **Milestone 7:** Created project from scratch (no ViperX)
- [ ] **Milestone 8:** Published to PyPI
- [ ] **Milestone 9:** Helped someone else learn
- [ ] **Milestone 10:** Taught Python packaging to others

---

## 🆘 When You Get Stuck

### Level 1-2: Getting Started
- Read the [Quick Start](quickstart.md)
- Use `--explain` mode
- Read the generated comments

### Level 3: Development
- Read the [Why? docs](why/index.md)
- Use `viperx learn <topic>`
- Check official docs (uv, pytest, etc.)

### Level 4: Advanced
- Official packaging guide: https://packaging.python.org/
- PEP 621: https://peps.python.org/pep-0621/
- uv docs: https://docs.astral.sh/uv/

---

## 📚 Recommended Reading Order

1. **Start Here:**
   - [Quick Start](quickstart.md)
   - [Why pyproject.toml?](why/pyproject.md)
   - [Why src/ layout?](why/src-layout.md)

2. **Deep Dive:**
   - [Why uv?](why/uv.md)
   - [Why config-in-package?](why/config-in-package.md)
   - [Why isolated .env?](why/env-isolation.md)

3. **Philosophy:**
   - [PHILOSOPHY.md](../PHILOSOPHY.md)
   - [Why Safe Mode?](why/safe-mode.md)

4. **Advanced:**
   - [Workspaces](workspaces.md)
   - [Templates](templates.md)
   - [Publishing](publishing.md)

---

## 🎓 The Graduation Moment

You'll know you've "graduated" when:

1. You create a new project and think: "I don't need ViperX for this"
2. You can explain to a colleague why src/ layout is better
3. You help someone else learn Python packaging
4. You run `viperx eject` and feel confident

**That's the moment ViperX was built for.** 🎉

---

## 💬 Final Thoughts

The journey from beginner to independent takes time. Don't rush it.

- **Level 1:** A few hours
- **Level 2:** A few days
- **Level 3:** A few weeks
- **Level 4:** A few months

But once you reach Level 4, you have a **lifetime skill**.

**Good luck on your journey!** 🚀

---

*"The best tool is the one you no longer need."*  
— The ViperX Philosophy
