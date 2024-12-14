let sessionId;
let currentQuestionId;
let base_url = "https://quizz-6vtz.onrender.com";

async function fetchQuestions() {
  const response = await fetch(
    `${base_url}/quiz/${sessionId}/question/`,
    {
      method: "GET",
    }
  );

  if (response.ok) {
    const data = await response.json();
    displayQuestion(data);
  }
}

function displayQuestion(ques) {
  const container = document.querySelector(".container");
  container.innerHTML = `
      <h1>Question</h1>
      <p class = question>${ques.question}</p>
      <label class="option">
          <input type="radio" name="option" value="${ques.optiona}" />
          ${ques.optiona}
      </label>
      <label class="option">
          <input type="radio" name="option" value="${ques.optionb}" />
          ${ques.optionb}
      </label>
      <label class="option">
          <input type="radio" name="option" value="${ques.optionc}" />
          ${ques.optionc}
      </label>
      <label class="option">
          <input type="radio" name="option" value="${ques.optiond}" />
          ${ques.optiond}
      </label>

      <button onclick="submitAnswer(${ques.id})">Submit Answer</button>
      
  `;
}

async function submitAnswer(questionId) {
  const chosenOption = document.querySelector(
    'input[name="option"]:checked'
  );
  if (!chosenOption) {
    alert("Please select an option");
    return;
  }

  const answer = chosenOption.value;
  const answerData = {
    chosen_option: answer,
  };

  const response = await fetch(
    `${base_url}/quiz/${sessionId}/question/${questionId}/submit/`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(answerData),
    }
  );

  if (response.ok) {
    console.log("Answer submitted successfully");
    fetchQuestions();
  }

  if (response.status == 400) {
    alert("Question Already Answered");
  }

  if (response.status == 404) {
    alert("Quiz has ended");
    window.location.href = `result.html?session_id=${sessionId}`;   
  }
}

window.onload = function () {
  const urlParams = new URLSearchParams(window.location.search);
  sessionId = urlParams.get("session_id");
  fetchQuestions();
};
