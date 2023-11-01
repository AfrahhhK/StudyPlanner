let currentQuestion = 1;
const totalQuestions = 4;

const nextButton = document.getElementById('next-button');
const prevButton = document.getElementById('prev-button');

nextButton.addEventListener('click', function () {
    showNextQuestion();
});

prevButton.addEventListener('click', function () {
    showPrevQuestion();
});

function showNextQuestion() {
    document.getElementById(`question${currentQuestion}`).style.display = 'none';

    if (currentQuestion < totalQuestions) {
        currentQuestion++;
        document.getElementById(`question${currentQuestion}`).style.display = 'block';
        prevButton.style.display = 'block';
    }

    if (currentQuestion === totalQuestions) {
        nextButton.textContent = 'Submit';
    }
}

function showPrevQuestion() {
    document.getElementById(`question${currentQuestion}`).style.display = 'none';

    if (currentQuestion > 1) {
        currentQuestion--;
        document.getElementById(`question${currentQuestion}`).style.display = 'block';
    }

    if (currentQuestion === 1) {
        prevButton.style.display = 'none';
    }

    nextButton.textContent = 'Next';
}




