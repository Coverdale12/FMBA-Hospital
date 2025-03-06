class Slider{
  selectors = {
    slider: "[data-js-slider]",
    buttonPrev: "[data-js-slider-button-prev]",
    buttonNext: "[data-js-slider-button-next]",
    sliderContainer: "[data-js-slider-container]",
    slide: "[data-js-slide]"
  }
  stateClasses = {
    show: "show"
  }
  constructor(){
    this.bindEvents()
    this.autoSlide()
  }
  nextSlide(sliderContainer){
    let currentElement = sliderContainer.querySelectorAll(`.${this.stateClasses.show}`)

    if(currentElement.length > 1){
      if(currentElement[0].previousElementSibling === null && currentElement[1].nextElementSibling === null){
        currentElement[0].nextElementSibling.classList.add(this.stateClasses.show)
        currentElement[1].classList.remove(this.stateClasses.show)
        return
      }
      if(currentElement[1].nextElementSibling === null){
        currentElement[0].classList.remove(this.stateClasses.show)
        currentElement = sliderContainer.querySelector(this.selectors.slide)
        currentElement.classList.add(this.stateClasses.show)
        return
      }
      currentElement[0].classList.remove(this.stateClasses.show)
      currentElement[1].nextElementSibling.classList.add(this.stateClasses.show)
      return
    }

    currentElement = currentElement[0]
    const next = currentElement.nextElementSibling
    
    currentElement.classList.remove(this.stateClasses.show)
    if(next){
      next.classList.add(this.stateClasses.show)
    }else{
      sliderContainer.firstElementChild.classList.add(this.stateClasses.show)
    }
    
  }
  deleteIntervalAutoSlide(){
    clearTimeout(this.timeOutSlideStart)
    this.timeOutSlideStart = setTimeout(() => {
      this.autoSlide()
    }, 11000)
  }
  autoSlide(){
    const sliderContainer = document.querySelector(this.selectors.sliderContainer)
    this.intervalChangeSlide = setInterval(() => {
      this.nextSlide(sliderContainer)
    }, 4000)
  }
  prevSlide(sliderContainer){
    let currentElement = sliderContainer.querySelectorAll(`.${this.stateClasses.show}`)

    if(currentElement.length > 1){
      if(currentElement[0].previousElementSibling === null && currentElement[1].nextElementSibling === null){
        currentElement[1].previousElementSibling.classList.add(this.stateClasses.show)
        currentElement[0].classList.remove("show")
        return
      }
      if(currentElement[0].previousElementSibling === null){
        currentElement[1].classList.remove(this.stateClasses.show)
        currentElement = sliderContainer.querySelectorAll(this.selectors.slide)
        currentElement[currentElement.length - 1].classList.add(this.stateClasses.show)
        return
      }
      currentElement[1].classList.remove(this.stateClasses.show)
      currentElement[0].previousElementSibling.classList.add(this.stateClasses.show)
      return
    }

    currentElement = currentElement[0]
    const prev = currentElement.previousElementSibling

    currentElement.classList.remove(this.stateClasses.show)
    if(prev){
      prev.classList.add(this.stateClasses.show)
    }else{
      sliderContainer.lastElementChild.classList.add(this.stateClasses.show)
    }
  }
  changeSlide(event){
    const { target } = event
    const slider = target.closest(this.selectors.slider)
    const sliderContainer = slider.querySelector(this.selectors.sliderContainer)
    
    const isButton = target.closest(this.selectors.buttonNext) || target.closest(this.selectors.buttonPrev)
    if(!isButton){
      return
    }
    if('jsSliderButtonNext' in isButton.dataset){
      this.nextSlide(sliderContainer)
    }else{
      this.prevSlide(sliderContainer)
    }
  }
  bindEvents(){
    document.addEventListener("click", (event) => {
      if(!event.target.closest(this.selectors.slider)){
        return
      }
      this.changeSlide(event)
    })
    document.addEventListener('pointerover', (event) => {
      if(!event.target.closest(this.selectors.slider)){
        return
      }
      clearInterval(this.intervalChangeSlide)
      this.deleteIntervalAutoSlide()
    })
  }
}

new Slider()