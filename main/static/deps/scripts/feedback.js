class Feedbacks{
  selectors = {
    feedback: "[data-js-feedback]",
    feedbacksList: "[data-js-feedback-list]",
    feedbacksShowAllButton: "[data-js-feedback-show-all-button]",
    feedbackDataTime: "[data-js-feedback-datatime]",
    feedbackParagrapth: "[data-js-feedback-paragrapth]"
  }
  stateClasses = {
    showFeedback: "show",
    showAll: "show-all",
  }
  constructor(){
    this.bindEvents()
  }
  showAll(event){
    if(!event.target.closest(this.selectors.feedbacksShowAllButton)){
      return
    }
    const { target } = event
    const feedback = target.closest(this.selectors.feedback)
    const feedbackParagrapth = feedback.querySelector(this.selectors.feedbackParagrapth)
    if(feedbackParagrapth.classList.contains(this.stateClasses.showAll)){
      target.innerHTML = "Показать полностью"
      feedbackParagrapth.classList.remove(this.stateClasses.showAll)
    }else{
      target.innerHTML = "Скрыть"
      feedbackParagrapth.classList.add(this.stateClasses.showAll)
    }
    
  }
  bindEvents(){
    document.addEventListener("click", (event) => {
      if(!event.target.closest(this.selectors.feedback)){
        return
      }
      this.showAll(event)
    })
  }
}// class is control show-all content feedback
class Feedback{
  selectors = {
    feedback: "[data-js-feedback]",
    feedbacksList: "[data-js-feedback-list]",
    feedbacksShowAllButton: "[data-js-feedback-show-all-button]",
    feedbackDataTime: "[data-js-feedback-datatime]",
    feedbackParagrapth: "[data-js-feedback-paragrapth]"
  }
  stateClasses = {
    showFeedback: "show",
    showAll: "show-all",
  }
  month = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня", 
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
  }
  constructor(id, name, content, datetime){
    this.setData(id, name, content, datetime)
    const container = document.querySelector(this.selectors.feedbacksList)
    if(container){
      this.createFeedback(container)
    }
  }
  setData(id, name, content, datetime){
    let datetimeTEXT = datetime.split("-").reverse()
    let datetimeFORMAT = []
    datetimeTEXT.forEach(element => {
      datetimeFORMAT.push(Number(element))
    });
    datetimeFORMAT[1] = `${this.month[datetimeFORMAT[1]]}` 
    datetimeFORMAT = datetimeFORMAT.join(" ")
    this.data = {id, name, content, datetime, datetimeFORMAT} 
  }
  createFeedback(container) {
    const { id, name, content, datetime, datetimeFORMAT } = this.data;
    container.innerHTML += `
      <li class="slider__item" data-js-slide data-js-feedback="${id}">
        <article class="feedback">
          <header class="feedback__header">
            <h2 class="feedback__title">Отзыв</h2>
            <time datetime="${datetime}" class="feedback__datetime" data-js-feedback-datatime>
              ${datetimeFORMAT}
            </time>
          </header>
          <div class="feedback__body">
            <p class="feedback__paragrapth" data-js-feedback-paragrapth>
              ${content}
            </p>
            <span class="feedback__name">${name}</span>
          </div>
          <button class="button-standart feedback__full-show-button" data-js-feedback-show-all-button>
            Показать полностью
          </button>
        </article>
      </li>
    `;
  }
}// class create a feedback
class NotFeedbacks{
  constructor(){
    const container = document.querySelector("[data-js-feedback-list]")
    this.createMessage(container)
  } 
  createMessage(container){
    container.innerHTML += `
      <li class="slider__item show" data-js-slide data-js-feedback="">
        <article class="feedback no-feedback">
          <h2 class="feedback__title">
            Похоже пока что нет отзывов!
          </h2>
          <p class="feedback__subtitle">
            Будьте первым)
          </p>
        </article>
      </li>
    `;
  }
}