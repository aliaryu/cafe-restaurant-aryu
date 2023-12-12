var scrollToTop = document.getElementById('scroll-to-top');

scrollToTop.addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});