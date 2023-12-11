var sectionImgs = document.querySelectorAll('#section-menu img');

sectionImgs.forEach(function(img, index) {
    setTimeout(() => {
        img.classList.add("menu-animation");;
      }, index * 1678);
});
