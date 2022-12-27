const test = document.querySelector('.test');
const bottom = document.querySelector('.test2');

test.addEventListener("click", () => {
    bottom.classList.toggle("active");
  });