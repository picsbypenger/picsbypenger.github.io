document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll("main img").forEach(img => {
    if (img.complete) return;

    const reveal = () => {
      img.classList.remove('lazy');
      img.classList.add('loaded');
    };
    img.addEventListener('load', reveal, { once: true });
    img.addEventListener('error', reveal, { once: true });
    img.classList.add('lazy');
    if (img.complete) reveal();
  });

  // --- Image Protection ---
  // Disable right-click on images
  document.addEventListener('contextmenu', function(e) {
    if (e.target.tagName === 'IMG' || e.target.closest('figure')) {
        e.preventDefault();
    }
  }, false);

  // Disable dragging of images
  document.addEventListener('dragstart', function(e) {
    if (e.target.tagName === 'IMG' || e.target.closest('figure')) {
        e.preventDefault();
    }
  }, false);

});