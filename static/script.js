  window.addEventListener('scroll', () => {
    document.getElementById('mainNav').classList.toggle('scrolled', window.scrollY > 10);
  });

  // Mobile menu
  function toggleMenu() {
    document.getElementById('mainNav').classList.toggle('menu-open');
  }
  document.querySelectorAll('.nav-links a').forEach(a => {
    a.addEventListener('click', () => document.getElementById('mainNav').classList.remove('menu-open'));
  });

  // FAQ
  function toggleFaq(el) {
    const item = el.parentElement;
    const isOpen = item.classList.contains('open');
    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('open'));
    if (!isOpen) item.classList.add('open');
  }

  // Reveal on scroll
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible'); });
  }, { threshold: 0.1 });
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Form submit
  function handleSubmit() {
    const btn = document.querySelector('.form-submit');
    btn.textContent = '✓ Mensagem enviada!';
    btn.style.background = '#1a6641';
    setTimeout(() => { btn.textContent = 'Enviar mensagem →'; btn.style.background = ''; }, 3000);
  }