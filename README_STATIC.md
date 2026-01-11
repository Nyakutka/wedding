# Static version — nikt-wedding (static)

This folder contains a static snapshot of the wedding invitation site.

How to serve locally (from project root):

```bash
# serve `static_site` on port 5000
cd nikt-wedding
python3 -m http.server 5000 --directory static_site

# then open http://localhost:5000
```

Notes:
- All site files, styles and images are in `static/` and `static_site/`.
- The dynamic backend (`app.py`) is no longer required to view the site.
