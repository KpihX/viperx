# 🧠 The Philosophy of ViperX

> "ViperX is not a tool for developers who want to go fast.  
> ViperX is a tool for developers who want to **understand**."

## 🎯 The Mission

**ViperX's success is measured by how many users no longer need it.**

ViperX is an **educational scaffolding tool** for Python projects. Unlike other project generators that optimize for speed and abstraction, ViperX optimizes for **learning** and **understanding**.

Our goal: After using ViperX 3-5 times, you should be able to create professional Python projects **without** it.

---

## 🌟 Core Principles

### 1. **Transparency Over Abstraction**

**Bad Tool**: Generates 50 files with cryptic configs. You have no idea what they do.  
**ViperX**: Generates 5-10 files, each with **extensive comments** explaining WHY it exists.

- Every template file is "ultra-commented"
- No hidden magic or black boxes
- Every decision is visible in `viperx.yaml`

### 2. **Education Over Automation**

**Bad Tool**: "Just run this command, don't worry about the details."  
**ViperX**: "Here's what this does, here's WHY, here's where to learn more."

- `--explain` mode shows detailed educational notes
- Generated files teach through comments
- Documentation focuses on "Why?" not just "How?"

### 3. **Empowerment Over Dependency**

**Bad Tool**: Lock-in. If you stop using the tool, your project breaks.  
**ViperX**: No lock-in. `viperx eject` removes all ViperX-specific files, leaving a standard Python project.

- No runtime dependencies on ViperX
- All outputs are standard Python/uv files
- You can graduate from ViperX any time

### 4. **Simplicity Over Completeness**

**Bad Tool**: Supports 47 frameworks, 12 build systems, infinite configurations.  
**ViperX**: Supports what matters: `uv`, modern Python, ML/DL essentials.

- Fewer choices = easier learning
- Opinionated but not rigid
- Focus on best practices, not every practice

### 5. **Respect Over Convenience**

**Bad Tool**: Overwrites your files. Deletes things without asking.  
**ViperX**: Safe Mode. Never destroys your work without explicit permission.

- Never overwrites existing files
- Reports conflicts for manual review
- `--force` flags require explicit confirmation

---

## 👤 Target User: The Learner

ViperX is built for:

- **Beginners** who want to learn project structure (not just copy it)
- **Intermediates** transitioning from scripts to packages
- **Instructors** teaching Python best practices
- **Professionals** who want a "teaching template" for their team

ViperX is **NOT** for:

- Developers who need to scaffold 10 projects per day (use Cookiecutter)
- Teams with established custom templates (use your own generator)
- Production systems that need automated, unattended setup

---

## 🧭 The Learning Journey

### Phase 1: **User** (Projects 1-2)
*"I can create projects, but I don't know why they work."*

- Use ViperX with basic flags
- Run `uv sync`, see it work
- Understand the **what** (files exist)

### Phase 2: **Observer** (Projects 3-5)
*"I understand WHY each file exists."*

- Use `--explain` mode
- Read the ultra-comments in generated files
- Understand the **why** (design decisions)

### Phase 3: **Apprentice** (Projects 6-10)
*"I can modify projects confidently."*

- Add dependencies manually
- Create new modules
- Customize templates

### Phase 4: **Independent** (Projects 11+)
*"I don't need ViperX anymore."*

- Create `pyproject.toml` from scratch
- Set up projects without tools
- **ViperX succeeded.** 🎉

---

## 🏗️ Design Metaphor: The Parent-Child Relationship

Good parents don't do everything for their children—they **teach** them to be independent.

- **Bad Parent (Bad Tool)**: Does homework for the child. Fast results, zero learning.
- **Good Parent (ViperX)**: Shows how to solve problems, explains WHY, then lets the child try.

ViperX is a **mentor**, not a servant.

---

## 📜 Key Design Decisions

### Why `src/` Layout?
**Teaching Moment**: Import safety. You can't accidentally import uninstalled code.  
**Link**: [Python Packaging Guide](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)

### Why Config-in-Package?
**Teaching Moment**: Works on Colab/Kaggle. Solves the "where's my config?" problem.  
**Link**: [importlib.resources](https://docs.python.org/3/library/importlib.resources.html)

### Why `uv`?
**Teaching Moment**: Modern, fast, Rust-based. The future of Python packaging.  
**Link**: [uv Documentation](https://docs.astral.sh/uv/)

### Why Isolated `.env`?
**Teaching Moment**: Each package has its own secrets. Prevents leaks in monorepos.  
**Link**: [12-Factor App - Config](https://12factor.net/config)

### Why `pyproject.toml`?
**Teaching Moment**: Single source of truth. End of setup.py chaos.  
**Link**: [PEP 518](https://peps.python.org/pep-0518/), [PEP 621](https://peps.python.org/pep-0621/)

---

## 🎓 Educational Features

### 1. Ultra-Commented Templates
Every generated file has extensive comments explaining:
- **WHAT** it is
- **WHY** it exists
- **HOW** to use it
- **WHERE** to learn more (links to PEPs, docs)

### 2. `--explain` Mode
Interactive educational mode that shows:
- What ViperX is doing at each step
- Why that step is necessary
- Links to learn more

### 3. "Why?" Documentation
Dedicated docs section answering:
- Why pyproject.toml?
- Why src/ layout?
- Why uv?
- Why config-in-package?
- Why isolated .env?

### 4. Learning Path
Progressive guide from beginner to independent:
- Level 1: Use ViperX
- Level 2: Understand ViperX
- Level 3: Customize ViperX outputs
- Level 4: Don't need ViperX

---

## 🚫 What ViperX Is NOT

### Not a Production Framework
ViperX generates **starting points**, not production systems. Once generated, you own the code.

### Not a Build Tool
ViperX uses `uv` for builds. It's a scaffolder, not a replacement for `uv`, `pip`, or `poetry`.

### Not a Lock-In System
You can `viperx eject` at any time. No runtime dependency on ViperX.

### Not Feature-Complete
ViperX doesn't support every possible configuration. It supports **what you need to learn**.

---

## 🌱 The Graduation Moment

**The best outcome**: You read this file, use ViperX a few times, and then...

```bash
$ viperx eject
✅ Ejected successfully. You are now free! 🦅
```

You close your terminal, smile, and create your next project **from scratch**.

**That's the moment ViperX was built for.**

---

## 💡 Contributing to the Philosophy

ViperX's philosophy is living, not static. If you have ideas to make ViperX more educational:

1. Open an issue tagged `philosophy`
2. Propose changes that align with the mission
3. Remember: We optimize for **learning**, not features

---

## 📚 Further Reading

- [PEP 518 - pyproject.toml](https://peps.python.org/pep-0518/)
- [PEP 621 - Project Metadata](https://peps.python.org/pep-0621/)
- [Python Packaging Guide](https://packaging.python.org/)
- [12-Factor App](https://12factor.net/)
- [uv Documentation](https://docs.astral.sh/uv/)

---

*"The success of ViperX is measured by how many users no longer need it."*

— The ViperX Philosophy
