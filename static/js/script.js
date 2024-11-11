// Mobile menu toggle functionality
// const navbarToggler = document.getElementById('navbar-toggler');
// const navbarNav = document.getElementById('navbarNav');

// navbarToggler.addEventListener('click', () => {
//     navbarNav.classList.toggle('hidden');
// });




// navbar scroll 
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) {
        document.getElementById("navbar").classList.add("p-5");
        document.getElementById("navbar").classList.remove("p-8");
        document.getElementById("navbar").style.backgroundColor = "white"; // Change background color on scroll
    } else {
        document.getElementById("navbar").classList.add("p-8");
        document.getElementById("navbar").classList.remove("p-5");
        document.getElementById("navbar").style.backgroundColor = "rgba(241, 241, 241, 0.8)"; // Reset background color
    }
}



// carousel slider js
    let currentSlide = 0;
    const slides = document.querySelectorAll('.carousel-item');
    const totalSlides = slides.length;

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.classList.toggle('hidden', i !== index); 
            slide.classList.toggle('block', i === index); 
        });
    }

    function nextSlide() {
        currentSlide = (currentSlide + 1) % totalSlides;
        showSlide(currentSlide);
    }

    function prevSlide() {
        currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
        showSlide(currentSlide);
    }

    showSlide(currentSlide);

    setInterval(nextSlide, 5000);





  
    document.addEventListener("DOMContentLoaded", function () {
        let currentSlide = 0;
        const slides = document.querySelectorAll(".first-card .slider-container img");

        function showSlide(index) {
            slides.forEach((slide, i) => {
                slide.style.opacity = i === index ? "1" : "0";
            });
        }

        function nextSlide() {
            currentSlide = (currentSlide + 1) % slides.length;
            showSlide(currentSlide);
        }

        // Change image every 3 seconds
        setInterval(nextSlide, 3000);
    });




    // for slider effect of  Newly arrive Collection

    document.addEventListener("DOMContentLoaded", function () {
        const mainImage = document.getElementById("main-product-image");
        const thumbnails = document.querySelectorAll(".thumbnail");
    
        if (mainImage && thumbnails.length > 0) {
            thumbnails.forEach(thumbnail => {
                thumbnail.addEventListener("click", function () {
                    // Get the image URL from the data-image attribute
                    const newImageSrc = thumbnail.getAttribute("data-image");
                    
                    if (newImageSrc) {
                        // Update the main image's src attribute
                        mainImage.src = newImageSrc;
                    } else {
                        console.error("No data-image attribute found for the clicked thumbnail.");
                    }
                });
            });
        } else {
            console.error("Main image or thumbnails not found.");
        }
    });
    