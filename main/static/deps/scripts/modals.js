class WarningModal{
  selectors = {
    modal: "[data-js-modal-warning]",
    modalButtonOpen: "[data-js-warning]",
    formButtonSubmit: "[data-js-form-warning]",
    modalMessage: "[data-js-modal-message]",
  }
  constructor(){
    this.bindEvents()
  }
  showModalWindowWarning(event){
    const modal = document.querySelector(this.selectors.modal)
    let message = modal.querySelector(this.selectors.modalMessage) 
    message.innerHTML = event.target.dataset.jsWarning
    modal.showModal()
    modal.addEventListener("close", () => {
      const accept = modal.returnValue
      if(accept === "true"){
        location.href = event.target.href
      }else{
        return
      }
    })
  }
  bindEvents(){
    document.addEventListener("click", (event) => {
      if(!event.target.closest(this.selectors.modalButtonOpen)){
        return
      }
      event.preventDefault()
      this.showModalWindowWarning(event)
    })
  }
}

new WarningModal()