let questions = [];

fetch('questions.json')
    .then(response => response.json())
    .then(data => {
        questions = data;
        showQuestionAndAnswers();
    });

let currentQuestionIndex = 0;
let correctAnswers = 0;

function showQuestionAndAnswers() {
  const questionContainer = document.getElementById('questionContainer');
  const answersContainer = document.getElementById('answersContainer');
  const resultContainer = document.getElementById('result');

  if (resultContainer) {
    document.body.removeChild(resultContainer);
  }

  questionContainer.innerHTML = questions[currentQuestionIndex].question;

  answersContainer.innerHTML = '';
  questions[currentQuestionIndex].answers.forEach(answer => {
    const button = document.createElement('button');
    button.innerText = answer;
    button.onclick = function() {
      if (answer === questions[currentQuestionIndex].correctAnswer) {
        correctAnswers++;
      }
      if (currentQuestionIndex < 4) {
        currentQuestionIndex += 1;
        showQuestionAndAnswers();
      } else {
        const resultContainer = document.createElement('div');
        resultContainer.id = 'result';
        if (correctAnswers > 3) {
          resultContainer.innerHTML = `Congratulations! You have completed the test! Correct answers: ${correctAnswers} out of 5`;
        } else {
          resultContainer.innerHTML = `You have completed the test! Correct answers: ${correctAnswers} out of 5`;
        }
        document.body.appendChild(resultContainer);
        correctAnswers = 0;
        currentQuestionIndex = 0;
        questions.sort(() => Math.random() - 0.5);
      }
    };
    answersContainer.appendChild(button);
  });
}

// Shuffle the array on load
window.onload = function() {
  questions.sort(() => Math.random() - 0.5);
  showQuestionAndAnswers();
};
