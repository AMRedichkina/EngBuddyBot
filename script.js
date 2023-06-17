let questions = [];

fetch('questions.json')
    .then(response => response.json())
    .then(data => {
        questions = data;
        shuffleQuestions();
        showQuestionAndAnswers();
    });

let currentQuestionIndex = 0;
let correctAnswers = 0;

function shuffleQuestions() {
    questions.sort(() => Math.random() - 0.5);
}

function showQuestionAndAnswers() {
  const questionContainer = document.getElementById('questionContainer');
  const answersContainer = document.getElementById('answersContainer');
  const resultContainer = document.getElementById('result');
  const nextButton = document.getElementById('nextButton');

  if (resultContainer) {
    document.body.removeChild(resultContainer);
  }

  const currentQuestion = questions[currentQuestionIndex];
  questionContainer.innerHTML = currentQuestion.question;

  answersContainer.innerHTML = '';
  currentQuestion.answers.forEach((answer, index) => {
    const button = document.createElement('button');
    button.innerText = answer;
    button.classList.add('btn', 'btn-primary', 'mt-2');

    button.isCorrectAnswer = (answer === currentQuestion.correctAnswer);

    button.onclick = function() {
      for (let i = 0; i < answersContainer.children.length; i++) {
        const btn = answersContainer.children[i];
        if (btn.isCorrectAnswer) {
          btn.style.backgroundColor = 'green';
        } else if (btn === this) {
          btn.style.backgroundColor = 'red';
        }
        btn.disabled = true; // Disable the button after a selection has been made
      }
      if (button.isCorrectAnswer) {
        correctAnswers++;
      }
    };

    answersContainer.appendChild(button);
  });

  nextButton.onclick = function() {
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
      shuffleQuestions();
      this.disabled = true; // Disable the Next button
    }
  };

  if (currentQuestionIndex === 4) {
    nextButton.disabled = false; // Enable the Next button for the last question
  }
}

// Shuffle the array on load
window.onload = function() {
  showQuestionAndAnswers();
};
