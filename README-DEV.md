# Local Development Setup

This guide helps you run the Contexture Lab website locally for development.

## Method 1: Using Jekyll (Recommended for Simple Edits)

### Prerequisites
- Ruby 3.x or higher
- Bundler

### Quick Start (Without Live Reload)

Due to compatibility issues with `eventmachine` on newer Ruby versions and macOS, the simplest approach is to run Jekyll without live-reload:

```bash
# Run the development server script
./serve.sh
```

The site will be available at `http://localhost:4000`. You'll need to manually refresh your browser after making changes.

### Alternative: Manual Jekyll Command

```bash
jekyll serve --port 4000 --livereload false --incremental
```

## Method 2: Using Docker (Recommended for Full Features)

Docker provides a consistent environment and avoids Ruby dependency issues.

### Prerequisites
- Docker Desktop installed

### Setup and Run

```bash
# Build the Docker image
docker run --rm -it \
  -v "$PWD:/srv/jekyll" \
  -p 4000:4000 \
  jekyll/jekyll:4 \
  jekyll serve --watch --force_polling --verbose

# Or create an alias:
alias jekyll-serve='docker run --rm -it -v "$PWD:/srv/jekyll" -p 4000:4000 jekyll/jekyll:4 jekyll serve --watch --force_polling'
```

Visit `http://localhost:4000` in your browser. The site will automatically reload when you make changes.

## Method 3: Fix eventmachine (For Advanced Users)

If you want live-reload functionality and are comfortable debugging native gem compilation:

```bash
# Install Xcode Command Line Tools if not already installed
xcode-select --install

# Set up build flags
bundle config build.eventmachine --with-cppflags="-I$(brew --prefix)/include"

# Install dependencies
bundle install

# Run Jekyll with live reload
bundle exec jekyll serve --livereload
```

## Editing Content

### Adding News Items
Edit `_data/news.yml`:

```yaml
- date: 2026-01-18
  title: "Your News Title"
  description: "Optional description"
```

### Adding Team Members
Edit `_data/people.yml` under the appropriate section (faculty, students, postdocs, alumni).

### Editing Pages
- Landing page: `index.md`
- People: `people.md`
- Code & Data: `code-data.md`
- Slides: `slides.md`

### Modifying Styles
Edit `assets/css/main.scss` for custom CSS.

## Troubleshooting

### Port 4000 Already in Use
```bash
# Kill process on port 4000
lsof -ti:4000 | xargs kill -9

# Or use a different port
jekyll serve --port 4001
```

### Changes Not Showing
1. Do a hard refresh: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows/Linux)
2. Clear Jekyll cache: `rm -rf _site .jekyll-cache`
3. Restart the server

### Ruby Version Issues
Use a Ruby version manager like `rbenv` or `rvm` to manage Ruby versions:

```bash
# Using rbenv
rbenv install 3.3.0
rbenv local 3.3.0
```

## Deployment

The site automatically deploys to GitHub Pages when you push to the `main` branch. No manual deployment needed.

## Resources

- [Jekyll Documentation](https://jekyllrb.com/docs/)
- [Liquid Template Language](https://shopify.github.io/liquid/)
- [Markdown Guide](https://www.markdownguide.org/)
