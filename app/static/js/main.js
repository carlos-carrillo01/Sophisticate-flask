// Menú móvil
document.querySelector('.mobile-menu-button')?.addEventListener('click', function() {
    const menu = document.querySelector('.md\\:flex');
    menu?.classList.toggle('hidden');
});


// Smooth scrolling para todos los enlaces
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth'
            });
        }
    });
});


// Efecto parallax para la imagen hero
window.addEventListener('scroll', function() {
    const hero = document.querySelector('.hero-image');
    if (hero) {
        const scrollPosition = window.pageYOffset;
        hero.style.backgroundPositionY = scrollPosition * 0.3 + 'px';
    }
});
