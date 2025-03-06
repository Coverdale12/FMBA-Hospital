class sizeTextElement{
  selectors = {
    controlElement: `[data-js-size-text="control"]`,
    textElement: `[data-js-size-text="text"]`,
    textSizeOutput: `[data-js-size-text-output]`,
    textSizeInput: `[data-js-size-text-input]`
  }
  constructor(){
    this.initControlElement()
    this.bindEvents()
  }
  initControlElement(){
    const cotrolElement = document.querySelector(this.selectors.controlElement)
    const text = document.querySelector(this.selectors.textElement)
    let fontSize = getComputedStyle(text).fontSize.replace("px", "")
    this.fontSizeTextBaseProcent = fontSize / 35
  }
  changeFontSize(event){
    const controlElement = event.target.closest(this.selectors.controlElement)
    const outputElement = controlElement.querySelector(this.selectors.textSizeOutput)
    const textElement = document.querySelector(this.selectors.textElement)
    outputElement.innerHTML = `${event.target.value}%`
    
    

    let fontSizeText = getComputedStyle(textElement).fontSize;
    if(event.target.value < 20){
      return
    }
    textElement.style.fontSize = `${this.fontSizeTextBaseProcent * event.target.value}px`


  }
  bindEvents(){
    document.addEventListener('input', (event) => {
      if(!event.target.closest(this.selectors.textSizeInput)){
        return
      }
      this.changeFontSize(event)
    })
  }
}
new sizeTextElement();