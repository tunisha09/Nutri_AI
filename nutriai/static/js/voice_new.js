// Enhanced voice recognition for food logging
document.addEventListener('DOMContentLoaded', function() {
    const voiceBtn = document.getElementById('voiceBtn');
    const voiceStatus = document.getElementById('voiceStatus');
    const voiceResults = document.getElementById('voiceResults');
    const voiceText = document.getElementById('voiceText');
    
    // Check for browser support
    if (!('webkitSpeechRecognition' in window)) {
        voiceStatus.textContent = 'Voice recognition not supported';
        voiceBtn.disabled = true;
        return;
    }

    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    voiceBtn.addEventListener('click', toggleVoiceRecognition);

    function toggleVoiceRecognition() {
        if (voiceBtn.classList.contains('listening')) {
            recognition.stop();
            return;
        }
        
        recognition.start();
        voiceBtn.classList.add('listening');
        voiceStatus.textContent = 'Listening...';
        voiceResults.textContent = '';
    }

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript.toLowerCase();
        processVoiceInput(transcript);
    };

    function processVoiceInput(transcript) {
        voiceText.value = transcript;
        voiceResults.textContent = `You said: ${transcript}`;
        voiceBtn.classList.remove('listening');
        voiceStatus.textContent = 'Voice input received';

        const foodData = identifyFood(transcript);
        displayFoodResults(foodData);
    }

    function identifyFood(transcript) {
        // Simple food database - would be replaced with API call
        const foods = {
            'apple': {name: 'Apple', emoji: '🍎', calories: 52, protein: 0.3, carbs: 14, fat: 0.2},
            'banana': {name: 'Banana', emoji: '🍌', calories: 89, protein: 1.1, carbs: 23, fat: 0.3},
            'sandwich': {name: 'Sandwich', emoji: '🥪', calories: 300, protein: 15, carbs: 40, fat: 8}
        };

        for (const [keyword, data] of Object.entries(foods)) {
            if (transcript.includes(keyword)) {
                return data;
            }
        }

        return {name: 'Unknown Food', emoji: '❓', calories: 0, protein: 0, carbs: 0, fat: 0};
    }

    function displayFoodResults(food) {
        document.getElementById('foodEmoji').textContent = food.emoji;
        document.getElementById('foodName').textContent = food.name;
        document.getElementById('calories').textContent = food.calories;
        document.getElementById('protein').textContent = food.protein;
        document.getElementById('carbs').textContent = food.carbs;
        document.getElementById('fat').textContent = food.fat;
        document.getElementById('resultsBox').style.display = 'block';
    }

    recognition.onerror = function(event) {
        voiceBtn.classList.remove('listening');
        voiceStatus.textContent = `Error: ${event.error}`;
    };

    recognition.onend = function() {
        if (voiceBtn.classList.contains('listening')) {
            voiceBtn.classList.remove('listening');
            voiceStatus.textContent = 'Listening timed out';
        }
    };

    // Save to dashboard
    document.querySelector('.confirm-button').addEventListener('click', function() {
        const foodName = document.getElementById('foodName').textContent;
        const calories = document.getElementById('calories').textContent;
        
        // In a real implementation, this would call your backend API
        console.log(`Logging ${foodName} (${calories} kcal) to dashboard`);
        alert(`${foodName} logged successfully!`);
    });
});
