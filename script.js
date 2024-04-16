let currentQuestion = 1;
const totalQuestions = 19;

const nextButton = document.getElementById('next-button');
const prevButton = document.getElementById('prev-button');
const toggleButton = document.getElementById('toggleButton');
const questionnaireLink = document.getElementById('questionnaireLink'); // Add this line

toggleButton.addEventListener('click', function () {
    toggleSidebar();
});

nextButton.addEventListener('click', function () {
    showNextQuestion();
});

prevButton.addEventListener('click', function () {
    showPrevQuestion();
});

questionnaireLink.addEventListener('click', function (e) { // Add this block
    e.preventDefault(); // Prevent the default action of the link
    document.getElementById('questionnaireForm').style.display = 'block'; // Show the questionnaire form
});

function toggleSidebar() {
    $('#sidebarMenu').toggleClass('d-lg-block');
}

function showNextQuestion() {
    document.getElementById(`question${currentQuestion}`).style.display = 'none';

    if (currentQuestion < totalQuestions) {
        currentQuestion++;
        document.getElementById(`question${currentQuestion}`).style.display = 'block';
        prevButton.style.display = 'block';
    }

    if (currentQuestion === totalQuestions) {
        nextButton.textContent = 'Submit';
        nextButton.addEventListener('click', function () {
            alert('Successfully submitted!');
        });
    }

    if (currentQuestion === 1) {
        document.getElementById('questionnaireForm').style.display = 'none'; // Hide the questionnaire form
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

    if (currentQuestion === 1) {
        document.getElementById('questionnaireForm').style.display = 'none'; // Hide the questionnaire form
    }
}
