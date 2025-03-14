

let homeSwiper = new Swiper('.swiper-container1', {
    freeMode: true,
    // slidesPerView: 7,
    spaceBetween: 30,
    breakpoints: {
        480: {
            slidesPerView: 2,
            spaceBetween: 5,
        },
        576: {
            slidesPerView: 3,
            spaceBetween: 9,
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 9,
        },
        992: {
            slidesPerView: 4,
            spaceBetween: 40,
        },
        1200: {
            slidesPerView: 6,
            spaceBetween: 7,
        }
    },
})

let postSwiper = new Swiper('.swiper-container2', {
    pagination: {
        el: '.swiper-pagination',
    },
    loop: true,
    spaceBetween: 10,
    breakpoints: {
        480: {
            slidesPerView: 1,
            spaceBetween: 5,
        },
        576: {
            slidesPerView: 1,
            spaceBetween: 9,
        },
        768: {
            slidesPerView: 1,
            spaceBetween: 9,
        },
        992: {
            slidesPerView: 1,
            spaceBetween: 40,
        },
        1200: {
            slidesPerView: 1,
            spaceBetween: 7,
        }
    },
})


let cast = new Swiper('.swiper-container3', {
    freeMode: true,
    // slidesPerView: 7,
    spaceBetween: 30,
    breakpoints: {
        480: {
            slidesPerView: 2,
            spaceBetween: 5,
        },
        576: {
            slidesPerView: 3,
            spaceBetween: 9,
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 9,
        },
        992: {
            slidesPerView: 4,
            spaceBetween: 40,
        },
        1200: {
            slidesPerView: 5,
            spaceBetween: 7,
        }
    },
})

let swiper = new Swiper('.swiper-container4', {
    scrollbar: {
        el: '.swiper-scrollbar',
        hide: true,
    },
    breakpoints: {
        480: {
            slidesPerView: 2,
            spaceBetween: 5,
        },
        576: {
            slidesPerView: 3,
            spaceBetween: 9,
        },
        768: {
            slidesPerView: 3,
            spaceBetween: 9,
        },
        992: {
            slidesPerView: 4,
            spaceBetween: 40,
        },
        1200: {
            slidesPerView: 4,
            spaceBetween: 20,
        }
    },
});