# Stephen Zweibel - Personal Website

Professional portfolio website built with Astro + Tailwind CSS.

## About

This site showcases my work as Digital Scholarship Librarian at CUNY Graduate Center, including:
- Projects (DHRIFT, DH Box, Reference Agent, and more)
- Publications and scholarly articles
- Complete CV
- Contact information

## Technology Stack

- **Astro 4.0** - Static site generator
- **Tailwind CSS** - Styling
- **Content Collections** - Markdown-based content management
- **GitHub Pages** - Hosting and deployment

## Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## Content Management

### Adding Projects

Create a new `.md` file in `src/content/projects/` with frontmatter:

```markdown
---
title: "Project Name"
description: "Brief description"
github: "https://github.com/user/repo"
featured: true
year: 2025
tags: ["tag1", "tag2"]
---

Project content here...
```

### Adding Publications

Create a new `.md` file in `src/content/publications/` with frontmatter:

```markdown
---
title: "Publication Title"
journal: "Journal Name"
year: 2025
type: "peer-reviewed"
authors: ["Author Name"]
url: "https://..."
---

Description...
```

## Deployment

The site automatically deploys to GitHub Pages when changes are pushed to the `main` branch. The GitHub Actions workflow is configured in `.github/workflows/deploy.yml`.

## Domain

The site is hosted at [zweibel.net](https://zweibel.net) via the CNAME file.

---

*Built with content curated from my Obsidian vault*
