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



