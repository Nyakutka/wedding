// Smooth scrolling and active nav highlighting
document.addEventListener('DOMContentLoaded', function(){
  const navLinks = document.querySelectorAll('#main-nav .nav-link');
  const sections = Array.from(document.querySelectorAll('section[id]'));

  function onScroll(){
    const y = window.scrollY + 120; // offset for fixed nav
    let current = sections[0];
    for(const sec of sections){
      if(sec.offsetTop <= y) current = sec;
    }
    navLinks.forEach(a => a.classList.remove('active'));
    const activeLink = document.querySelector('#main-nav .nav-link[href="#' + current.id + '"]');
    if(activeLink) activeLink.classList.add('active');

    // navbar background when scrolled past hero
    const nav = document.querySelector('.navbar');
    const hero = document.querySelector('.section-hero');
    if(nav && hero){
      if(window.scrollY > (hero.offsetHeight - 80)) nav.classList.add('scrolled');
      else nav.classList.remove('scrolled');
    }
  }

  // smooth anchor behavior for older browsers
  navLinks.forEach(link => {
    link.addEventListener('click', function(e){
      e.preventDefault();
      const id = this.getAttribute('href').substring(1);
      const el = document.getElementById(id);
      if(el){
        window.scrollTo({ top: el.offsetTop - 72, behavior: 'smooth' });
      }
    });
  });

  window.addEventListener('scroll', onScroll);
  onScroll();
  // Initialize AOS (Animate On Scroll)
  if(window.AOS){
    AOS.init({
      duration: 700,
      easing: 'ease-out-cubic',
      once: true,
      offset: 100,
    });
  }
});
