export class Menu{
  selectors = {
    buttonId: function(id){ return `[data-js-button-menu="${id}"]`}, 
    menuId: function(id){return `[data-js-menu="${id}"]`},
    button: "[data-js-button-menu]",
  }
  stateClasses = {
    show: "show",
    current: "is-current",
  }
  constructor(){
    this.bindEvents()
  }
  showMenu(event){
    const { target } = event 
    const element = target.closest(this.selectors.button)
    const menuId = this.selectors.menuId(element.dataset.jsButtonMenu)
    const menu = document.querySelector(menuId)
    
    element.classList.toggle(this.stateClasses.current)
    menu.classList.toggle(this.stateClasses.show)
    // document.querySelector(menuId).classList.toggle(this.stateClasses.show)
  }
  bindEvents(){
    document.addEventListener("click", (event) => {
      if(!event.target.closest(this.selectors.button)){
        return
      }
      this.showMenu(event)
    })
  }
}