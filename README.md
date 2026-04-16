# NASA OPERA

A website for NASA OPERA built with [MyST Markdown](https://mystmd.org/) and automated deployment via GitHub Actions.

## Features

- **MyST Markdown** source format with Jupyter notebook integration
- **GitHub Pages** deployment on push to `main`
- **Netlify PR previews** for pull request review
- **Pre-commit hooks**: Black, codespell, nbstripout for code quality
- **Blog** with per-tag index pages and an auto-generated RSS/Atom feed
- **Giscus comments** on each blog post, backed by GitHub Discussions

## Quick Start

1. Click **Use this template** on GitHub to create a new repository
2. Update `myst.yml` with your site title, author, and table of contents
3. Replace placeholder content in `pages/` with your own pages
4. Push to GitHub to trigger automated builds

## Project Structure

```
.
├── myst.yml                    # MyST configuration
├── index.md                    # Landing page
├── requirements.txt            # Python dependencies
├── logo.png                    # Site logo
├── fav.ico                     # Favicon
├── CNAME                       # Custom domain (optional)
├── robots.txt                  # Search engine directives
├── pages/                      # Site content
│   ├── preface.md
│   ├── part01/
│   │   ├── getting-started.md
│   │   └── installation.md
│   ├── part02/
│   │   └── first-example.md
│   ├── references.bib          # Bibliography
│   ├── jupytext.toml
│   └── images/                 # Shared images
├── blog.md                     # Blog landing page
├── posts/                      # Blog posts (Markdown with frontmatter)
├── tags/                       # Per-tag index pages
├── custom.css                  # Site CSS overrides
├── giscus-light.css            # Giscus (comments) light theme
├── generate_rss.py             # RSS/Atom feed generator
├── inject_comments.py          # Injects Giscus widget into post HTML
├── .pre-commit-config.yaml     # Pre-commit hook configuration
├── CONTRIBUTING.md              # Contribution guidelines
├── CONDUCT.md                   # Code of conduct
└── .github/workflows/
    ├── build.yml               # PR preview builds (Netlify)
    └── deploy.yml              # Production deployment (GitHub Pages)
```

## Customization

### Site Metadata

Edit `myst.yml`:
- `project.title`: your site title
- `project.authors`: author name(s)
- `project.github`: your GitHub `username/repo`
- `project.toc`: table of contents structure

### Adding Pages

1. Create a new `.md` file in the appropriate `pages/` subdirectory
2. Add the file to `project.toc` in `myst.yml`

### Adding Blog Posts

1. Create a new Markdown file in `posts/` with a YAML frontmatter block. At minimum, include `title`, `date` (ISO format, e.g., `2026-04-16`), `description`, and `tags`.
2. Add a card for the new post to `blog.md`.
3. If the post uses a tag without an existing index page, create one in `tags/` and add it to `project.toc` under `blog.md`.

The RSS and Atom feeds are regenerated on each deploy from the frontmatter in `posts/*.md`.

### Enabling Giscus Comments

Each blog post renders a Giscus comments widget at the bottom. To enable it for this repository:

1. Enable **Discussions** on your GitHub repository (Settings → General → Features).
2. Install the [Giscus app](https://github.com/apps/giscus).
3. Visit [giscus.app](https://giscus.app) and fill in the form for your repo to obtain `data-repo-id` and `data-category-id`.
4. Replace the `REPLACE_WITH_REPO_ID` and `REPLACE_WITH_CATEGORY_ID` placeholders in `inject_comments.py`.

Update `SITE_URL`, `SITE_TITLE`, `SITE_SUBTITLE`, and `AUTHOR` in `generate_rss.py` to match your site.

## Building Locally

```bash
pip install -r requirements.txt
npm install -g mystmd
myst build --html
```

The built site will be in `_build/html/`.

## Deployment

### GitHub Pages (production)

Pushes to `main` automatically trigger the `deploy.yml` workflow, which builds the HTML site and deploys to GitHub Pages.

By default, `BASE_URL` is set to `/<repo-name>` so that asset paths work correctly when served at `username.github.io/repo-name/`. If you configure a custom domain (via `CNAME`), remove the `BASE_URL` environment variable from `deploy.yml` since the site will be served from the root.

### Netlify (PR previews)

Pull requests trigger the `build.yml` workflow, which builds a preview and posts the URL as a PR comment. Requires `NETLIFY_AUTH_TOKEN` and `NETLIFY_SITE_ID` secrets.

## GitHub Secrets

| Secret | Purpose |
|--------|---------|
| `NETLIFY_AUTH_TOKEN` | Netlify authentication for PR previews |
| `NETLIFY_SITE_ID` | Netlify site ID for PR previews |

## License

[MIT](LICENSE)
