var scrollToTop = document.getElementById('scroll-to-top');

scrollToTop.addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

function scrollToTag(element) {
    var subject = element.getAttribute('subject');
    var target = document.querySelector('[target="' + subject + '"]');
    target.scrollIntoView({ behavior: 'smooth' });
}