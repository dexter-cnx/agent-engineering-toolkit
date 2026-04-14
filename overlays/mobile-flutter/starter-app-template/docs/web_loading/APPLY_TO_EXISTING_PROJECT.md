# Apply Web Loader To Existing Project

From the Flutter project root:

```bash
python3 tooling/apply_web_loader.py .
```

## What this does
- writes `web/index.html`
- writes `web/style.css`
- writes `web/flutter_bootstrap.js`

## Important
Review the generated `index.html` before commit if your project already has:
- custom meta tags
- branding
- PWA/service worker customizations
- analytics scripts
