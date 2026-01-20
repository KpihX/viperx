import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock 
from viperx.templates import TemplateManager
from viperx.core import ProjectGenerator
from viperx.constants import USER_TEMPLATES_DIR, TEMPLATES_DIR

@pytest.fixture
def manager():
    return TemplateManager()

def test_template_manager_init(manager):
    assert manager.user_dir == USER_TEMPLATES_DIR
    assert manager.internal_dir == TEMPLATES_DIR

@patch("viperx.templates.shutil.copy2")
def test_eject_templates(mock_copy, manager, tmp_path):
    # Mock user_dir to a temp path
    manager.user_dir = tmp_path / "user_templates"
    
    # Mock internal glob
    with patch.object(Path, "glob", return_value=[Path("fake.j2")]):
        manager.eject_templates()
        
    assert manager.user_dir.exists()
    mock_copy.assert_called()

def test_list_templates(manager, capsys):
    # Just ensure it doesn't crash and prints something
    manager.list_templates()
    captured = capsys.readouterr()
    assert "ViperX Templates" in captured.out

# --- Integration / Core Logic Test ---

def test_project_generator_override_simple(tmp_path):
    fake_user_dir = tmp_path / "templates"
    fake_user_dir.mkdir()
    (fake_user_dir / "README.md.j2").write_text("# CUSTOM OVERRIDE")
    
    with patch("viperx.constants.USER_TEMPLATES_DIR", fake_user_dir):
        # Initialize generator
        gen = ProjectGenerator("test-override", "", "classic", "Me", verbose=True)
        # Check env loader
        # It takes time to render, let's just inspect loader paths or render something internal
        # Render 'README.md.j2'
        # Currently we don't expose render directly easily without file write.
        # But we can access gen.env
        tmpl = gen.env.get_template("README.md.j2")
        rendered = tmpl.render(project_name="X", description="D")
        assert "# CUSTOM OVERRIDE" in rendered
    
def test_choice_loader_precedence(tmp_path):
    """Test standard Jinja2 ChoiceLoader behavior with our logic."""
    from jinja2 import Environment, FileSystemLoader, ChoiceLoader, PackageLoader, select_autoescape
    
    # 1. User Dir with Custom Template
    user_dir = tmp_path / "user"
    user_dir.mkdir()
    (user_dir / "test.j2").write_text("User")
    
    # 2. System Dir (Simulated)
    system_dir = tmp_path / "system"
    system_dir.mkdir()
    (system_dir / "test.j2").write_text("System")
    
    # Loader
    loader = ChoiceLoader([
        FileSystemLoader(user_dir),
        FileSystemLoader(system_dir) # Simulate PackageLoader
    ])
    env = Environment(loader=loader)
    
    tmpl = env.get_template("test.j2")
    assert tmpl.render() == "User"
    
    # If user removed, should fall back
    (user_dir / "test.j2").unlink()
    # Need to clear cache or reload env? Jinja checks.
    # Actually FileSystemLoader caches?
    # Let's re-init env to be sure
    env = Environment(loader=loader)
    tmpl = env.get_template("test.j2")
    assert tmpl.render() == "System"

def test_partial_override(tmp_path):
    """Verify that we can override one template while keeping others default."""
    fake_user_dir = tmp_path / "templates"
    fake_user_dir.mkdir()
    (fake_user_dir / "README.md.j2").write_text("# CUSTOM OVERRIDE")
    
    with patch("viperx.constants.USER_TEMPLATES_DIR", fake_user_dir):
        # Initialize generator
        gen = ProjectGenerator("test-partial", "", "classic", "Me", verbose=True)
        
        # 1. Check Override
        readme_tmpl = gen.env.get_template("README.md.j2")
        assert "# CUSTOM OVERRIDE" in readme_tmpl.render(project_name="X", description="D")
        
        # 2. Check Fallback (Internal)
        # We assume 'pyproject.toml.j2' exists internally
        pyproject_tmpl = gen.env.get_template("pyproject.toml.j2")
        rendered = pyproject_tmpl.render(
            project_name="test-partial", 
            version="0.1.0", 
            description="", 
            readme_filename="README.md",
            requires_python=">=3.8",
            license="MIT",
            authors=[],
            dependencies=[],
            dev_dependencies=[],
            scripts={}
        )
        # Just check it looks like a toml file
        assert "[project]" in rendered
