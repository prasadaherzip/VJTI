function checkAnswers() {
    // These are the correct answers for each question
    const correctAnswers = {
        q1: "b",
        q2: "a",
        q3: "a",
    };

    let score = 0;
    const totalQuestions = 3;

    // Loop through each question
    for (let i = 1; i <= totalQuestions; i++) {
        const questionName = 'q' + i;
        
        // Find the radio button that the user selected for this question
        const selectedOption = document.querySelector(`input[name="${questionName}"]:checked`);

        if (selectedOption) {
            // Check if the selected answer is the correct one
            if (selectedOption.value === correctAnswers[questionName]) {
                score++;
            }
        }
    }

    // Display the final score
    const resultContainer = document.getElementById('result');
    resultContainer.textContent = `You scored ${score} out of ${totalQuestions}!`;
}