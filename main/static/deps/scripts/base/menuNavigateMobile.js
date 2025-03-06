export class MobileMenu {
  selectors = {
    menu: `[data-js-menu="header-menu"]`,
    menuRow: `[data-js-menu-row]`,
    menuRowList: `[data-js-menu-row-list]`,
    buttonHideMenu: `[data-js-button-hide-current-menu]`,
  }
  stateClasses = {
    show: 'show',
    showAll: 'show-all'
  }
  constructor() {
    this.bindEvents()
  }
  isValid(event) {
    if (!event.target.closest("a")){
      return false
    }
    const row = event.target.closest(this.selectors.menuRow)
    if(row.querySelector(this.selectors.buttonHideMenu)){
      location.href = event.target.href
    }
  }
  createButtonBack(container) {
    const insertedContainer = container.querySelector(this.selectors.menuRowList)
    if (insertedContainer.querySelector(this.selectors.buttonHideMenu)) {
      return
    }
    const element = `
      <li class="link__item button">
        <button class="navigation__link" data-js-button-hide-current-menu>
          Назад
        </button>
      </li>
    `
    insertedContainer.insertAdjacentHTML('afterbegin', element)
  }
  closeList(listElement) {
    listElement.classList.remove(this.stateClasses.showAll)
    listElement.querySelector(this.selectors.buttonHideMenu).closest('li').remove()
  }
  openList(event) {
    const listElement = event.target.closest(this.selectors.menuRow)
    if (!listElement) {
      return
    }
    if (event.target.closest(this.selectors.buttonHideMenu)) {
      this.closeList(listElement)
      return
    }

    const menu = event.target.closest(this.selectors.menu)

    menu.querySelectorAll(this.selectors.menuRow).forEach(element => {
      element.classList.remove(this.stateClasses.showAll)
    });
    this.createButtonBack(listElement)
    listElement.classList.add(this.stateClasses.showAll)
  }
  isLink(event){
    if(event.target.closest(this.selectors.menuRowList)){
      return
    }
    location.href = event.target.href
  }
  bindEvents() {
    document.addEventListener("click", (event) => {
      if (!event.target.closest(this.selectors.menu)) {
        return
      }
      if (document.body.clientWidth < 800) {
        event.preventDefault()
      }
      this.isLink(event)
      this.isValid(event)
      this.openList(event)
    })
  }
}