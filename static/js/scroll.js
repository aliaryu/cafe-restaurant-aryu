var scrollToTop = document.getElementById('scroll-to-top');

scrollToTop.addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

function scrollToTag(element) {
    var cat_id = element.getAttribute('cat_id');
    var target = document.querySelector('[target="' + cat_id + '"]');
    target.scrollIntoView({ behavior: 'smooth' });
}