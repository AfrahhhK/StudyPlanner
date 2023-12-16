let currentQuestion = 1;
const totalQuestions = 19;

const nextButton = document.getElementById('next-button');
const prevButton = document.getElementById('prev-button');
const toggleButton = document.getElementById('toggleButton');

toggleButton.addEventListener('click', function () {
    toggleSidebar();
});

nextButton.addEventListener('click', function () {
    showNextQuestion();
});

prevButton.addEventListener('click', function () {
    showPrevQuestion();
});

function toggleSidebar() {
    // document.getElementById('sidebarMenu').style.display='none';
    $('#sidebarMenu').toggleClass('d-lg-block');
    // $('#sidebarMenu').toggle();
        // (sidebar.toggle())
    // if (sidebar.style.width === '240px') {
    //   sidebar.style.width = '0';
    // } else {
    //   sidebar.style.width = '240px';
    // }
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




