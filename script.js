// Scroll reveal animation
const observer = new IntersectionObserver((entries) => {
  entries.forEach((entry) => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.18 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Gentle parallax on hero card
const heroCard = document.querySelector('.hero-card');
if (heroCard) {
  heroCard.addEventListener('mousemove', (e) => {
    const rect = heroCard.getBoundingClientRect();
    const x = ((e.clientX - rect.left) / rect.width - 0.5) * 6;
    const y = ((e.clientY - rect.top) / rect.height - 0.5) * 6;
    heroCard.style.transform = `translateY(-2px) rotateX(${y}deg) rotateY(${x}deg)`;
  });
  heroCard.addEventListener('mouseleave', () => {
    heroCard.style.transform = 'translateY(0) rotateX(0) rotateY(0)';
  });
}

// Cursor light trail
const trail = document.querySelector('.trail');
if (trail) {
  window.addEventListener('pointermove', (e) => {
    const x = (e.clientX / window.innerWidth) * 100;
    const y = (e.clientY / window.innerHeight) * 100;
    trail.style.setProperty('--x', `${x}%`);
    trail.style.setProperty('--y', `${y}%`);
  });
}

// Text reveal / staggered word animation on load
document.querySelectorAll('.reveal-text').forEach((text) => {
  const words = text.textContent.trim().split(' ');
  text.innerHTML = '';
  words.forEach((word, i) => {
    const span = document.createElement('span');
    span.textContent = word + ' ';
    span.style.animationDelay = `${i * 0.08}s`;
    text.appendChild(span);
  });
});

// Light mode toggle
const modeToggle = document.querySelector('.mode-toggle');
if (modeToggle) {
  modeToggle.addEventListener('click', () => {
    document.body.classList.toggle('light');
    const isLight = document.body.classList.contains('light');
    modeToggle.textContent = isLight ? 'Dark mode' : 'Light mode';
  });
}
