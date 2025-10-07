// Initialize Swiper for service cards
document.addEventListener('DOMContentLoaded', function() {
    const swiper = new Swiper('.services-slider', {
        // Optional parameters
        slidesPerView: 1,
        spaceBetween: 20,
        loop: true,
        centeredSlides: true,
        autoplay: {
            delay: 3000,
            disableOnInteraction: false,
        },
        // Enable navigation arrows
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        // Enable touch and mouse drag
        allowTouchMove: true,
        grabCursor: true,
        // Responsive breakpoints
        breakpoints: {
            // when window width is >= 640px
            640: {
                slidesPerView: 2,
            },
            // when window width is >= 1024px
            1024: {
                slidesPerView: 3,
            }
        }
    });
});
