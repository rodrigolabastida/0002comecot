document.addEventListener('DOMContentLoaded', () => {
    // Add fade-in effect to body on load
    document.body.classList.add('fade-in');

    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navLinks = document.getElementById('nav-links');

    if (mobileMenuBtn && navLinks) {
        mobileMenuBtn.addEventListener('click', () => {
            mobileMenuBtn.classList.toggle('active');
            navLinks.classList.toggle('active');
        });
    }

    // Header Scroll Glassmorphism Effect
    const header = document.getElementById('header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // Determine Active Nav Link based on current page URL
    const currentLocation = location.pathname.split('/').pop() || 'index.html';
    const menuItems = document.querySelectorAll('.nav-links a');
    
    menuItems.forEach(item => {
        const itemPath = item.getAttribute('href');
        if (itemPath === currentLocation) {
            item.classList.add('active');
        }
    });

    // Floating Form Labels (Check if fields have data initially)
    const inputs = document.querySelectorAll('.form-group input, .form-group textarea');
    inputs.forEach(input => {
        // Just in case browsers auto-fill
        if (input.value.trim() !== '') {
            input.classList.add('has-value');
        }
        input.addEventListener('blur', () => {
            if (input.value.trim() !== '') {
                input.classList.add('has-value');
            } else {
                input.classList.remove('has-value');
            }
        });
    });

    // Form Submission Animation
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = contactForm.querySelector('button[type="submit"]');
            const originalText = btn.innerHTML;
            
            btn.innerHTML = 'Enviando...';
            btn.style.opacity = '0.7';
            
            setTimeout(() => {
                btn.innerHTML = '¡Mensaje Enviado!';
                btn.style.backgroundColor = '#4CAF50';
                btn.style.color = '#fff';
                contactForm.reset();
                
                setTimeout(() => {
                    btn.innerHTML = originalText;
                    btn.style.backgroundColor = '';
                    btn.style.color = '';
                    btn.style.opacity = '1';
                }, 3000);
            }, 1500);
        });
    }
});
