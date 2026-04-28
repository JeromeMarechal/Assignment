const buttons = document.querySelectorAll('.choice-button')
const nextButton = document.getElementById('next-button');

function disableButtons(list_of_buttons) {
    list_of_buttons.forEach(button => {
        button.disabled = true;
        button.classList.add('cursor-not-allowed');
        button.classList.remove('hover:scale-105', 'shadow-lg');
        button.classList.add('opacity-20');
    })
}

function enableButtons(list_of_buttons) {
    list_of_buttons.forEach(button => {
        button.disabled = false;
        button.classList.remove('cursor-not-allowed');
        button.classList.add('hover:scale-105', 'shadow-lg');
        button.classList.remove('opacity-20');
    })
}

function visualFeedback(data, button) {
    button.classList.remove('opacity-20');
    if (data.is_correct) {
        button.classList.add('bg-emerald-500/30', 'border-emerald-500/50');
    } else {
        button.classList.add('bg-rose-500/30', 'border-rose-500/50');
    }
}

function resetVisualFeedback(list_of_buttons) {
    list_of_buttons.forEach(button => {
        button.classList.remove('bg-emerald-500/30', 'border-emerald-500/50', 'bg-rose-500/30', 'border-rose-500/50', 'opacity-20');
    })
}

function updateRound(data, list_of_buttons) {
    nextButton.addEventListener('click', () => {
        
        // check if quiz is end
        if (data.is_end) {
            window.location.href = '/quiz/meaning/play';
            return;
        }

        // reset buttons
        enableButtons(list_of_buttons);
        resetVisualFeedback(list_of_buttons);

        // hide next button
        nextButton.classList.add('hidden');

        document.getElementById('french-word').textContent = data.word_FR;
        document.getElementById('round').textContent = data.round;
        document.getElementById('score').textContent = data.score;
        document.getElementById('score-bar').style.width = (data.score / 10 * 100) + '%';
        choiceButtons = document.getElementsByClassName('choice-button');
        for (let i = 0; i < choiceButtons.length; i++) {
            choiceButtons[i].textContent = data.choices [i];
        }
    })
}



buttons.forEach(button => {
    button.addEventListener('click', async () => {
        const selectOption = button.textContent;

        try {
            const response = await fetch('/quiz/meaning/play', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    selected_option: selectOption,
                })
            })

            const data = await response.json();

            // disable buttons
            disableButtons(buttons);

            // visual feedback
            visualFeedback(data, button);

            // show next button
            nextButton.classList.remove('hidden');

            // update round after next being clicked
            updateRound(data, buttons);

        } catch (error) {
            console.log('Error:', error);
        }
        
    })
})