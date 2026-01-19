# Contexture Lab Website

This is the official website for the Contexture Lab at Binghamton University. The site is built with Jekyll and hosted on GitHub Pages.

## How to Update the Website

### Adding Lab News

Edit `_data/news.yml` to add new news items. Add new entries at the top of the file in reverse chronological order.

```yaml
- date: 2026-01-19
  title: "Your news title here"
  description: "Description with optional [markdown links](https://example.com)"
```

### Updating the Navigation Menu

Edit `_data/menu.yml` to add, remove, or reorder navigation items.

```yaml
entries:
  - title: page name
    url: page-url

  - title: external link
    url: https://example.com
    external: true
```

### Updating People

Edit `_data/people.yml` to add or update lab members. Follow the existing format for different member types (PI, PhD students, etc.).

### Updating Slides

Edit `_data/slides.yml` to add presentation slides. Include title, date, event, and link to slides.

### Editing Content Pages

Content pages are markdown files in the root directory:
- `index.md` - Home page
- `research.md` - Research page
- `people.md` - People page
- `code-data.md` - Code & Data page
- `slides.md` - Slides page
- `artwork.md` - Artwork page

To edit a page, open the `.md` file and modify the content using markdown syntax.

### Creating a New Page

1. Create a new `.md` file in the root directory (e.g., `new-page.md`)
2. Add front matter at the top:
   ```yaml
   ---
   layout: page
   title: Page Title
   ---
   ```
3. Add your content below the front matter
4. Add the page to `_data/menu.yml` to make it appear in navigation

### Site Configuration

Edit `_config.yml` to update site-wide settings like title, author, email, and description.

## Local Development

To preview the site locally:

```bash
bundle exec jekyll serve
```

Then open your browser to `http://localhost:4000`.

## Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch.

To publish changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

## Theme

This site uses the [no-style-please](https://github.com/riggraz/no-style-please) Jekyll theme - a fast, minimalist theme with nearly no CSS.

## Support

For questions or issues, contact [skojaku@binghamton.edu](mailto:skojaku@binghamton.edu).
