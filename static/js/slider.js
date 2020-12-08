const slides = document.querySelectorAll('.js__slide');
const controls = document.querySelectorAll('.js__control');
const timeOut = 3000;

for (let i = 0; i < controls.length; i++) {
	const button = controls[i];
	button.addEventListener('click', e => {
		clearInterval(sliderTimer)
		controls.forEach(el => {
			el.classList.remove("showing")
		});
		button.classList.add("showing")
		for (let ndx = 0; ndx < slides.length; ndx++) {
			const slide = slides[ndx];
			slide.classList.remove("showing")
			if (i==ndx) {
				slide.classList.add("showing")
			}
		}
		
	})
}
const sliderTimer = setInterval(() => {
	let showingSlide = document.querySelector(".js__slide.showing")
	let showingSlideButton = document.querySelector(".js__control.showing")
	if (showingSlide.nextElementSibling) {
		showingSlide.nextElementSibling.classList.add("showing")
		showingSlide.classList.remove("showing")
		showingSlideButton.nextElementSibling.classList.add("showing")
		showingSlideButton.classList.remove("showing")
	} else {
		slides[0].classList.add("showing")
		showingSlide.classList.remove("showing")
		controls[0].classList.add("showing")
		showingSlideButton.classList.remove("showing")

	}
}, timeOut);