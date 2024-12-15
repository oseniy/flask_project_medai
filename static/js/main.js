document.addEventListener("scroll", function () {
    const parallax = document.querySelector(".parallax");
    const scrollPosition = window.scrollY;
    parallax.style.backgroundPositionY = `${scrollPosition * 0.5}px`; // Коэффициент 0.5 задаёт скорость
});
// Функция для обработки появления элемента в области видимости
function handleIntersection(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('visible'); // Добавляем класс, чтобы активировать анимацию
        }
    });
}

// Создаем наблюдателя
const observer = new IntersectionObserver(handleIntersection);

// Наблюдаем за блоком
const animatedBlock = document.getElementById('animated-block');
observer.observe(animatedBlock);

const animatedBlock2 = document.getElementById('animated-block2');
observer.observe(animatedBlock2);
