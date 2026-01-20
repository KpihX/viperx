class Viperx < Formula
  include Language::Python::Virtualenv

  desc "Professional Python Project Initializer with uv, ml/dl support"
  homepage "https://github.com/KpihX/viperx"
  url "https://files.pythonhosted.org/packages/source/v/viperx/viperx-1.0.2.tar.gz"
  sha256 "REPLACE_WITH_ACTUAL_SHA256"
  license "MIT"
  head "https://github.com/KpihX/viperx.git", branch: "master"

  depends_on "python@3.11"

  resource "typer" do
    url "https://files.pythonhosted.org/packages/source/t/typer/typer-0.21.1.tar.gz"
    sha256 "REPLACE_WITH_TYPER_SHA256"
  end

  resource "rich" do
    url "https://files.pythonhosted.org/packages/source/r/rich/rich-14.2.0.tar.gz"
    sha256 "REPLACE_WITH_RICH_SHA256"
  end

  resource "pyyaml" do
    url "https://files.pythonhosted.org/packages/source/p/pyyaml/pyyaml-6.0.1.tar.gz"
    sha256 "REPLACE_WITH_PYYAML_SHA256"
  end

  resource "jinja2" do
    url "https://files.pythonhosted.org/packages/source/j/jinja2/jinja2-3.1.6.tar.gz"
    sha256 "REPLACE_WITH_JINJA2_SHA256"
  end

  resource "gitpython" do
    url "https://files.pythonhosted.org/packages/source/g/gitpython/gitpython-3.1.46.tar.gz"
    sha256 "REPLACE_WITH_GITPYTHON_SHA256"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match "ViperX CLI Version", shell_output("#{bin}/viperx --version")
  end
end
