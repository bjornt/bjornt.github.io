# bjornt.github.io

Source for [tillenius.me](https://tillenius.me), a Jekyll static site.

## Setup

### 1. Install rbenv

```bash
git clone https://github.com/rbenv/rbenv.git ~/.rbenv
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init - bash)"' >> ~/.bashrc
source ~/.bashrc
```

### 2. Install build dependencies

```bash
sudo apt install build-essential libssl-dev libreadline-dev zlib1g-dev
```

### 3. Install Ruby

Install the version specified in `.ruby-version`:

```bash
rbenv install
```

Verify the correct version is active:
```bash
ruby --version
```

### 4. Install dependencies

```bash
gem install bundler
bundle install
```

## Running locally

```bash
bundle exec jekyll serve
```

The site will be available at [http://localhost:4000](http://localhost:4000). Jekyll watches for file changes and rebuilds automatically.

To also render future-dated posts:
```bash
bundle exec jekyll serve --future
```

## Preparing Excalidraw SVGs

Diagrams under `_includes/diagrams/` are exported from Excalidraw and then
post-processed so their colors follow the visitor's `prefers-color-scheme`
setting. To prepare a freshly exported SVG, run:

```bash
python3 scripts/prepare_svg.py _includes/diagrams/your-diagram.svg
```

The script rewrites the file in place: it detects the SVG's dominant
background fill and foreground stroke, injects a `<style>` block that maps
those colors to CSS variables with light- and dark-mode values, sets
`width="100%"` so the diagram scales to its container, and strips the
`<?xml ?>` declaration and `<!DOCTYPE>` so the SVG can be inlined into
an HTML page without the browser rendering them as visible text.
