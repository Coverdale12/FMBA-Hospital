class rangeElement{
  selectors = {
    rangeElementReset: "[data-js-form-field-count-reset]",
    rangeElement: "[data-js-range-element]",
    rangeElementId: function(id){return `[data-js-range-element="${id}"]`},
    dataElementButton: "[data-js-range-element-button]",
  }
  constructor(){
    this.bindEvents()   
  }
  changeValue(id, type){
    const rangeElement = document.querySelector(this.selectors.rangeElementId(id))
    const rangePrint = rangeElement.children[1]
    let number = Number(rangePrint.textContent)
    
    if(type === "add"){
      number += 1
    }else{
      if(number === 1) return
      number -= 1
    }

    rangePrint.textContent = number
  }
  isButton(event){
    const id = event.target.closest(this.selectors.rangeElement).dataset.jsRangeElement
    const typeButton = event.target.dataset.jsRangeElementButton
    this.changeValue(id, typeButton)
  }
  bindEvents(){
    document.addEventListener("click", (event) =>{
      if(!event.target.closest(this.selectors.dataElementButton)){
        return
      }
      this.isButton(event)
    })
  }
}

new rangeElement()