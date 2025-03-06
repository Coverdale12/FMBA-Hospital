class FormsValidation {
  selectors = {
    form: '[data-js-form]',
    formReset: '[data-js-form-reset]',
    fieldErrors: '[data-js-form-field-errors]',
    fieldCountSymbols: '[data-js-form-field-count-sym]',
    fieldPassword: '[data-js-form-password]'
  }
  errorMessages = {
    customError: () => 'Пароли не совпадают',
    valueMissing: ({ title }) => title || "Пожалуйста, заполните это поле!",
    patternMismatch: ({ title }) => title || "Данные не соответсвуют формату!",
    typeMismatch: ({ title }) => title,
    tooShort: ({ minLength }) => `Слишком короткое значение, минимум символов - ${minLength}`,
    tooLong: ({ maxLength }) => `Слишком длинное значение, максимум символов - ${maxLength}`
  }
  constructor() {
    this.bindEvents()
  }
  manageErrors(fieldControlElement, errorMessages) {
    const fieldErrorsElement = fieldControlElement.parentElement.querySelector(this.selectors.fieldErrors)

    fieldErrorsElement.innerHTML = errorMessages
      .map((message) => `<span class="field__error">${message}</span>`)
      .join("")

  }
  manageCountElement(fieldControlElement, length) {
    const fieldCountSymElement = fieldControlElement.parentElement.querySelector(this.selectors.fieldCountSymbols)

    fieldCountSymElement.innerHTML = `
      <span class="form__field--count-symbols-rel">${length}</span> / <span class="form__field--count-symbols-max-sym"> ${fieldControlElement.maxLength} </span>
    `

  }
  checkRetryPassword(fieldControlElement) {

  }
  validateField(fieldControlElement) {
    if (fieldControlElement.closest(this.selectors.fieldPassword)) {
      const form = fieldControlElement.closest(this.selectors.form)
      const passwords = form.querySelectorAll(this.selectors.fieldPassword)

      const isContent = Boolean(passwords[0].value) && Boolean(passwords[1].value)
      if(isContent){
        if (passwords[0].value != passwords[1].value) {
          fieldControlElement.setCustomValidity("Пароли не совпадают")
        } else {
          fieldControlElement.setCustomValidity("")
        }
      }
    }

    let errors = fieldControlElement.validity
    const errorMessages = []
    
  
    Object.entries(this.errorMessages).forEach(([errorType, getErrorMessage]) => {
      if (errors[errorType]) {
        errorMessages.push(getErrorMessage(fieldControlElement))
      }
    })
    this.manageErrors(fieldControlElement, errorMessages)

    const isValid = errorMessages.length === 0

    fieldControlElement.ariaInvalid = !isValid

    return isValid
  }
  onChange(event) {
    const { target } = event
    const isRequired = target.required
    const isToggleType = ["radio", "checkbox"].includes(target.type)

    if (isRequired && isToggleType) {
      this.validateField(target)
    }
  }
  onInput(event) {
    const { target } = event
    const isTextarea = ["textarea"].includes(target.type)
    if (isTextarea) {
      this.manageCountElement(target, target.value.length)
    }
  }
  onBlur(event) {
    const isFormField = event.target.closest(this.selectors.form)
    const isRequired = event.target.required
    if (isFormField && isRequired) {
      this.validateField(event.target)
    }


  }
  onSubmit(event) {
    const { target } = event
    const isFormElement = target.matches(this.selectors.form)

    if (!isFormElement) {
      return
    }
    const requiredControlElements = [...target.elements].filter(({ required }) => required)
    let isFormValide = true
    let firstInvalidFieldControl = null

    requiredControlElements.forEach((element) => {
      const isFieldValid = this.validateField(element)

      if (!isFieldValid) {
        isFormValide = false

        if (!firstInvalidFieldControl) {
          firstInvalidFieldControl = element
        }
      }
    })

    if (!isFormValide) {
      event.preventDefault()
      firstInvalidFieldControl.focus()
      return
    }
    //Проверка на наличие предупреждающих модальных окон
    if (target.closest("[data-js-form-warning]")) {
      const modal = document.querySelector("[data-js-modal-warning-form]")
      event.preventDefault()
      modal.showModal()
      modal.addEventListener("close", () => {
        const accept = modal.returnValue
        if (accept === "true") {
          target.submit()
        } else {
          return
        }
      })
    }
    //
  }
  onReset(event) {
    const isFormElement = event.target.matches(this.selectors.formReset)
    if (!isFormElement) {
      return
    }

    const form = event.target.closest(this.selectors.form)
    const countSymElement = form.querySelector(this.selectors.fieldCountSymbols)
    try {
      countSymElement.querySelector("span").innerHTML = 0
    } catch (error) {
      return
    }

  }
  bindEvents() {
    document.addEventListener("click", (event) => { this.onReset(event) })
    document.addEventListener("blur", (event) => { this.onBlur(event) }, { capture: true })
    document.addEventListener("change", (event) => { this.onChange(event) })
    document.addEventListener("input", (event) => { this.onInput(event) })
    document.addEventListener("submit", (event) => { this.onSubmit(event) })
  }
}
new FormsValidation()