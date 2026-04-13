window.addEventListener('flutter-first-frame', function () {
  const loader = document.getElementById('boot-loader');
  if (loader) {
    loader.style.transition = 'opacity 220ms ease';
    loader.style.opacity = '0';
    setTimeout(() => loader.remove(), 240);
  }
});
