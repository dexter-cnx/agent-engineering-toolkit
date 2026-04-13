# Flutter Web Loading Checklist

## Visual
- Loader appears immediately on page load
- No blank white page before first paint
- Loader is centered and stable
- Loader disappears once Flutter UI is visible

## Performance
- Test in release mode
- Test with browser cache disabled
- Test with slow network throttling
- Confirm fonts and assets do not cause obvious flicker

## Integration
- `web/index.html` includes loader markup
- `web/style.css` is linked
- Bootstrap script is compatible with current Flutter build output
- Hosting config does not break asset paths
