# efeamadasun.github.io

Personal website for [efeamadasun.com](https://efeamadasun.com), hosted with GitHub Pages.

The site is a small Jekyll project based on the Solo theme.

## Editing

- Homepage copy lives in `_includes/index.md`.
- The local quote rotator lives in `_includes/scripts.html`.
- Shared layout lives in `_layouts/default.html`.
- Site metadata lives in `_config.yml`.
- Styles live in `css/solo.css`.

## Content approach

- Contact links are intentionally compact: email, LinkedIn, GitHub, and Twitter / X.
- Quotes are stored locally instead of loaded from a third-party API. This avoids privacy, reliability, mixed-content, and JSONP security issues while keeping the page dynamic.
- Keep at least 50 quotes in `_includes/scripts.html` so the rotation has enough variety.
- Within a single page session, the “Show another” button should not repeat a quote until the visitor has cycled through the full local quote list.

## Local preview

If Jekyll is installed locally, run:

```sh
jekyll serve
```

Then open <http://localhost:4000>.

GitHub Pages will build and publish the site from the repository automatically.

## Checks

Run the lightweight repository sanity checks with:

```sh
python3 check_site.py
```

## Credits

Theme: [Solo](http://solo.chibi.io), by [Shu Uesugi](https://github.com/chibicode).
