const url = "http://localhost:8000"
async function getFeedbackToServer(url){
  try {
    const response = await fetch(url+"/comments/get");

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data
          
    }catch (error) {
      console.error('Ошибка при получении комментариев:', error);
    }
}
let counter = 0;

function feedbacksPlace(data) {
  if(data.message.length === 0){
    new NotFeedbacks()
    return false
  }
  data.message.forEach(feedback => {
    if (counter >= 4) {
      return; // Прерываем цикл, если уже отрисовано 4 отзыва
    }
    let { id, name, content, datatime } = feedback; // Исправлено datatime на created_at
    new Feedback(id, name, content, datatime);
    counter++;
  });
  return true
}
getFeedbackToServer(url).then(dataServer => {
  if(!feedbacksPlace(dataServer)){
    return
  }else{
    new Feedbacks()
    const elements = document.querySelectorAll("[data-js-feedback]")
    elements[0].classList.add("show")
  }
})
