let sessionId;
let base_url = "http://localhost:8000";

async function fetchResult() {
  const response = await fetch(`${base_url}/quiz/${sessionId}/result/`, {
    method: "GET",
  });

  if (response.ok) {
    const data = await response.json();
    console.log(data);
    displayResult(data);
  } else {
    console.error("Failed to fetch result");
  }
}

function displayResult(result) {
  const score = document.getElementById("score");
  const questionContainer = document.getElementById("questions");

  score.innerHTML = `Your score: ${result.score} / 5`;

  result.incorrect_questions.forEach((ques) => {
    const questionDiv = document.createElement("div");
    questionDiv.classList.add("question");

    questionDiv.innerHTML = `
      <div class="title">Question: ${ques.question}</div>
      <div class="answer"><strong>Your Answer:</strong> ${
        ques.user_answer
      }</div>
      <div class="answer"><strong>Correct Answer:</strong> ${
        ques.correct_answer
      }</div>
    `;
    questionContainer.appendChild(questionDiv);
  });
}

window.onload = function () {
  const urlParams = new URLSearchParams(window.location.search);
  sessionId = urlParams.get("session_id");
  fetchResult();
};
