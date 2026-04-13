{{flutter_js}}
{{flutter_build_config}}

const loaderEl = document.getElementById('boot-loader');
const barEl = document.getElementById('progress-bar');
const textEl = document.getElementById('progress-text');
const statusEl = document.getElementById('boot-status');

function setProgress(percent, status) {
  if (barEl) barEl.style.width = `${percent}%`;
  if (textEl) textEl.textContent = `${percent}%`;
  if (statusEl && status) statusEl.textContent = status;
}

function removeLoader() {
  if (!loaderEl) return;
  loaderEl.classList.add('fade-out');
  window.setTimeout(() => loaderEl.remove(), 450);
}

function showSlowLoadingHint() {
  if (statusEl && statusEl.textContent !== 'Launching…') {
    statusEl.textContent = 'Still loading…';
  }
}

setProgress(10, 'Loading bootstrap…');
window.setTimeout(showSlowLoadingHint, 8000);

_flutter.loader.load({
  onEntrypointLoaded: async function (engineInitializer) {
    setProgress(45, 'Downloading application…');
    const appRunner = await engineInitializer.initializeEngine();
    setProgress(80, 'Initializing renderer…');
    await appRunner.runApp();
    setProgress(100, 'Launching…');
    window.setTimeout(removeLoader, 250);
  },
});
