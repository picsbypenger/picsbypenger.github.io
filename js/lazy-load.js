document.addEventListener("DOMContentLoaded", function() {
  const figures = [].slice.call(document.querySelectorAll("figure"));
  const lazyFigures = figures.filter(fig => fig.querySelector("img.lazy"));

  const loadImage = (img) => {
      const src = img.dataset.src ? img.dataset.src.trim() : '';
      const srcset = img.dataset.srcset ? img.dataset.srcset.trim() : '';

      if (src || srcset) {
          if (src) img.src = src;
          if (srcset) img.srcset = srcset;

          img.onload = () => {
              img.classList.remove('lazy');
              img.classList.add('loaded');
          };
          img.onerror = () => {
              img.classList.remove('lazy');
              img.classList.add('loaded'); 
          };
      } else {
          img.classList.remove('lazy');
          img.classList.add('loaded');
      }
  };

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries, self) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const fig = entry.target;
          const img = fig.querySelector("img.lazy");
          
          if (img) {
              loadImage(img);
          }
          
          self.unobserve(fig);
        }
      });
    }, {
      rootMargin: "400px 0px 400px 0px"
    });

    lazyFigures.forEach(fig => observer.observe(fig));
  } else {
    lazyFigures.forEach(fig => {
        const img = fig.querySelector("img.lazy");
        if (img) loadImage(img);
    });
  }
});