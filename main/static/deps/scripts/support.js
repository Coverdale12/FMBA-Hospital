class SupportModal{
  selectors = {
    supportModal: "[data-js-support-modal]",
    supportModalClose: "[data-js-support-modal-close]",
  }

  stateClasses = {
    showSupport: 'show',
    hideSupport: 'hide',
  }
  showModal(){
    const modal = document.querySelector(this.selectors.supportModal)
    modal.classList.add(this.stateClasses.showSupport)
  }
  showModalTimeOut(timeOut){
    setTimeout(() => {
      this.showModal()
    }, timeOut)
  }
  closeModal(event){
    const modal = event.target.closest(this.selectors.supportModal)
    modal.classList.add(this.stateClasses.hideSupport)
  }
  constructor(){
    this.bindEvents()
    this.showModalTimeOut(0)
  }
  bindEvents(){
    document.addEventListener("click", (event) => {
      if(!event.target.closest(this.selectors.supportModalClose)){
        return
      }
      this.closeModal(event)
    })
  }
}

new SupportModal()