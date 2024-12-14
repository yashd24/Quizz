base_url = 'https://quizz-6vtz.onrender.com';
function startQuiz() {
    fetch(`${base_url}/start/`, {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        const sessionId = data.id;
        window.location.href = `question.html?session_id=${sessionId}`;
    })
    .catch(error => {
        console.error('Error starting quiz:', error);
        alert('Failed to start the quiz. Please try again later.');
    });
}
