"""
Curated learning resources for Python project development.

This module provides links to high-quality documentation and learning
materials for each concept used in ViperX.
"""

from typing import Dict, List, Tuple
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# Resource type: Dict[category_key, {title, links: [(name, url), ...]}]
RESOURCES: Dict[str, Dict[str, any]] = {
    "packaging": {
        "title": "📦 Python Packaging",
        "description": "Learn how to package and distribute Python code",
        "links": [
            ("Python Packaging Guide", "https://packaging.python.org/"),
            ("PEP 518 - pyproject.toml", "https://peps.python.org/pep-0518/"),
            ("PEP 621 - Project Metadata", "https://peps.python.org/pep-0621/"),
            ("PEP 440 - Version Specifiers", "https://peps.python.org/pep-0440/"),
            ("Packaging Tutorial", "https://packaging.python.org/en/latest/tutorials/packaging-projects/"),
        ]
    },
    "uv": {
        "title": "⚡ uv - Fast Python Package Manager",
        "description": "The modern Rust-based package manager",
        "links": [
            ("Official Documentation", "https://docs.astral.sh/uv/"),
            ("GitHub Repository", "https://github.com/astral-sh/uv"),
            ("Concepts: Workspaces", "https://docs.astral.sh/uv/concepts/workspaces/"),
            ("Concepts: Projects", "https://docs.astral.sh/uv/concepts/projects/"),
        ]
    },
    "testing": {
        "title": "🧪 Python Testing",
        "description": "Write better tests with pytest",
        "links": [
            ("pytest Documentation", "https://docs.pytest.org/"),
            ("pytest Good Practices", "https://docs.pytest.org/en/stable/goodpractices.html"),
            ("Testing Best Practices", "https://docs.python-guide.org/writing/tests/"),
            ("Coverage.py", "https://coverage.readthedocs.io/"),
        ]
    },
    "config": {
        "title": "⚙️ Configuration Management",
        "description": "Manage application configuration properly",
        "links": [
            ("12-Factor App - Config", "https://12factor.net/config"),
            ("python-dotenv", "https://pypi.org/project/python-dotenv/"),
            ("importlib.resources", "https://docs.python.org/3/library/importlib.resources.html"),
            ("YAML in Python", "https://pyyaml.org/wiki/PyYAMLDocumentation"),
        ]
    },
    "git": {
        "title": "🔧 Git & Version Control",
        "description": "Master version control with Git",
        "links": [
            ("Pro Git Book (Free)", "https://git-scm.com/book/"),
            ("gitignore Documentation", "https://git-scm.com/docs/gitignore"),
            ("GitHub gitignore Templates", "https://github.com/github/gitignore"),
            ("Git Cheat Sheet", "https://education.github.com/git-cheat-sheet-education.pdf"),
        ]
    },
    "licenses": {
        "title": "📜 Open Source Licenses",
        "description": "Choose the right license for your project",
        "links": [
            ("Choose a License", "https://choosealicense.com/"),
            ("SPDX License List", "https://spdx.org/licenses/"),
            ("OSI Approved Licenses", "https://opensource.org/licenses/"),
            ("License Comparison", "https://choosealicense.com/licenses/"),
        ]
    },
    "project-structure": {
        "title": "🏗️ Project Structure",
        "description": "Organize your Python projects",
        "links": [
            ("src Layout vs Flat Layout", "https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/"),
            ("Structuring Your Project", "https://docs.python-guide.org/writing/structure/"),
            ("Python Application Layouts", "https://realpython.com/python-application-layouts/"),
        ]
    },
    "best-practices": {
        "title": "✨ Python Best Practices",
        "description": "Write better Python code",
        "links": [
            ("The Hitchhiker's Guide to Python", "https://docs.python-guide.org/"),
            ("PEP 8 - Style Guide", "https://peps.python.org/pep-0008/"),
            ("Real Python Tutorials", "https://realpython.com/"),
            ("Python Design Patterns", "https://refactoring.guru/design-patterns/python"),
        ]
    },
    "ml-dl": {
        "title": "🤖 Machine Learning & Deep Learning",
        "description": "ML/DL specific resources",
        "links": [
            ("PyTorch Documentation", "https://pytorch.org/docs/"),
            ("TensorFlow Documentation", "https://www.tensorflow.org/api_docs"),
            ("scikit-learn User Guide", "https://scikit-learn.org/stable/user_guide.html"),
            ("Kaggle Learn", "https://www.kaggle.com/learn"),
        ]
    },
}


def display_resources(topic: str = None, console: Console = None) -> None:
    """
    Display learning resources in a formatted table.
    
    Args:
        topic: Optional specific topic to show. If None, shows all topics.
        console: Rich console instance. If None, creates one.
    """
    if console is None:
        console = Console()
    
    # Show specific topic
    if topic:
        if topic not in RESOURCES:
            console.print(f"[red]Unknown topic: {topic}[/red]")
            console.print(f"\nAvailable topics: {', '.join(RESOURCES.keys())}")
            return
        
        resource = RESOURCES[topic]
        table = Table(title=resource["title"], show_header=True, header_style="bold cyan")
        table.add_column("Resource", style="green")
        table.add_column("URL", style="blue")
        
        for name, url in resource["links"]:
            table.add_row(name, url)
        
        console.print()
        console.print(Panel(resource["description"], border_style="cyan"))
        console.print(table)
        console.print()
        return
    
    # Show all topics
    console.print()
    console.print(Panel(
        "📚 [bold]ViperX Learning Resources[/bold]\n\n"
        "Curated links to help you master Python project development.\n"
        "Use [cyan]viperx learn <topic>[/cyan] to see specific resources.",
        title="🎓 Educational Resources",
        border_style="green"
    ))
    console.print()
    
    for key, resource in RESOURCES.items():
        console.print(f"[bold cyan]• {resource['title']}[/bold cyan]")
        console.print(f"  [dim]{resource['description']}[/dim]")
        console.print(f"  Topic: [green]{key}[/green]")
        console.print()


def get_all_topics() -> List[str]:
    """Return a list of all available topic keys."""
    return list(RESOURCES.keys())


def get_topic_description(topic: str) -> str:
    """Get the description for a specific topic."""
    if topic in RESOURCES:
        return RESOURCES[topic]["description"]
    return ""
