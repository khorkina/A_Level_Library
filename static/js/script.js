// Add smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Add loading state to PDF download buttons
document.querySelectorAll('.download-btn').forEach(button => {
    button.addEventListener('click', function() {
        this.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Downloading...';
        setTimeout(() => {
            this.innerHTML = 'Download PDF';
        }, 2000);
    });
});

// Add fade-in animation for content
document.addEventListener('DOMContentLoaded', function() {
    const fadeElements = document.querySelectorAll('.fade-in');
    fadeElements.forEach(element => {
        element.style.opacity = '1';
    });
});
