# AUR Package for ViperX

This directory contains files for publishing ViperX to the Arch User Repository.

## Setup (Repository Owner)

1. Create AUR account at https://aur.archlinux.org
2. Add SSH key to your AUR account
3. Clone AUR package (first time):
   ```bash
   git clone ssh://aur@aur.archlinux.org/viperx.git aur-viperx
   ```
4. Copy `PKGBUILD` and `.SRCINFO` to the repo
5. Push changes

## Updating

After each PyPI release:

1. Update `pkgver` in `PKGBUILD`
2. Regenerate `.SRCINFO`:
   ```bash
   makepkg --printsrcinfo > .SRCINFO
   ```
3. Commit and push to AUR

## Usage (End Users)

```bash
# With yay (AUR helper)
yay -S viperx

# Manual
git clone https://aur.archlinux.org/viperx.git
cd viperx
makepkg -si
```
