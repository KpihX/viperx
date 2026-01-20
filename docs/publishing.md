# 📦 Publishing Guide: Beyond PyPI

Releasing to PyPI (`pip install`) is the basics. To be a professional tool, you need to be where your users are: **Homebrew** (macOS) and **Conda** (Data Science).

## 🍺 Homebrew Tap (The "Hacker" Standard)

Users expect `brew install your-tool`. To do this without waiting for months for Homebrew Core acceptance, create a **Personal Tap**.

### Step 1: Create the Repo
Create a public GitHub repository named EXACTLY `homebrew-viperx`.
(Or `homebrew-commands`, but `homebrew-viperx` allows `brew tap kpihx/viperx`).

### Step 2: The Formula
Create a file `viperx.rb` in that repo:

```ruby
class Viperx < Formula
  include Language::Python::Virtualenv

  desc "Professional Python Project Initializer with uv & config-as-code"
  homepage "https://github.com/KpihX/viperx"
  url "https://files.pythonhosted.org/packages/.../viperx-1.4.0.tar.gz" # Get this from PyPI
  sha256 "..." # Get this from PyPI (at the hash link)
  license "MIT"

  depends_on "python@3.12"
  depends_on "uv" # Optional, if you want to enforce uv presence

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/viperx", "--version"
  end
end
```

### Step 3: Usage
Users can now run:
```bash
brew tap kpihx/viperx
brew install viperx
```
*Boom. You look like a pro.*

---

## 🐍 Conda Forge (The Science Standard)

For Data Scientists, `conda install viperx` is mandatory.

### Step 1: Fork & Recipe
1. Fork [conda-forge/staged-recipes](https://github.com/conda-forge/staged-recipes).
2. Create a folder `recipes/viperx/`.
3. Add `meta.yaml`:

```yaml
{% set name = "viperx" %}
{% set version = "1.4.0" %}

package:
  name: {{ name|lower }}
  version: {{ version }}

source:
  url: https://pypi.io/packages/source/{{ name[0] }}/{{ name }}/{{ name }}-{{ version }}.tar.gz
  sha256: ...

build:
  number: 0
  noarch: python
  script: {{ PYTHON }} -m pip install . -vv

requirements:
  host:
    - python >=3.8
    - pip
  run:
    - python >=3.8
    - typer
    - rich
    - jinja2
    - pyyaml
    - tomlkit

test:
  imports:
    - viperx
  commands:
    - viperx --help

about:
  home: https://github.com/KpihX/viperx
  license: MIT
  summary: 'Professional Python Project Initializer'
```

### Step 2: Pull Request
Submit the PR to `staged-recipes`. A bot will check it. Once merged, the `viperx` feedstock is created automatically, and you are on channel `conda-forge`.

---

## 🐧 AUR (Arch Linux)

For the brave. Create a `PKGBUILD`.

```bash
# Maintainer: KpihX <...>
pkgname=viperx
pkgver=1.4.0
pkgrel=1
pkgdesc="Professional Python Project Initializer"
arch=('any')
url="https://github.com/KpihX/viperx"
license=('MIT')
depends=('python' 'python-typer' 'python-rich' 'python-jinja' 'python-yaml' 'python-tomlkit')
source=("https://files.pythonhosted.org/packages/source/v/viperx/viperx-$pkgver.tar.gz")
sha256sums=('...')

build() {
  cd "$pkgname-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$pkgname-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl
}
```
Submit to `aur.archlinux.org`.
