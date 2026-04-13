# Hosting Notes

## Static hosting
Suitable when your Flutter Web app is shipped as static files.

Check:
- correct `base href`
- asset path behavior
- SPA fallback or rewrite rules if needed

## CDN deployment
Check:
- cache headers for JS and assets
- invalidation strategy on deploy
- compression and content types

## GitHub Pages
If deployed under a subpath, update:
- `flutter build web --release --base-href /YOUR_REPO_NAME/`

## Smoke test after deploy
- open landing page
- verify loader appears
- verify first route loads
- verify reload/refresh on nested route
