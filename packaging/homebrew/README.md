# Homebrew Formula for ViperX

This directory contains the Homebrew formula for ViperX.

## Setup (Repository Owner)

1. Create a tap repository: `homebrew-tap`
   ```bash
   gh repo create homebrew-tap --public
   ```

2. Copy `viperx.rb` to `homebrew-tap/Formula/viperx.rb`

3. Update the `sha256` hash:
   ```bash
   curl -sL https://files.pythonhosted.org/packages/source/v/viperx/viperx-VERSION.tar.gz | shasum -a 256
   ```

## Usage (End Users)

```bash
# Add tap
brew tap kpihx/tap

# Install
brew install viperx

# Upgrade
brew upgrade viperx
```

## Updating

After each PyPI release:
1. Update `url` with new version
2. Update `sha256` hash
3. Commit and push to `homebrew-tap`
