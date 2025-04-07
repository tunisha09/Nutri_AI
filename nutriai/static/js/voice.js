// Voice recognition for food logging
document.addEventListener('DOMContentLoaded', function() {
    const voiceBtn = document.getElementById('voiceBtn');
    const voiceStatus = document.getElementById('voiceStatus');
    const voiceResults = document.getElementById('voiceResults');
    const voiceText = document.getElementById('voiceText');
    
    // Check for browser support
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
        voiceStatus.textContent = 'Voice recognition not supported in this browser';
        voiceBtn.disabled = true;
        return;
    }

    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    const recognition = new SpeechRecognition();
    
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    voiceBtn.addEventListener('click', function() {
        if (voiceBtn.classList.contains('listening')) {
            recognition.stop();
            voiceBtn.classList.remove('listening');
            voiceStatus.textContent = 'Stopped listening';
            return;
        }

        recognition.start();
        voiceBtn.classList.add('listening');
        voiceStatus.textContent = 'Listening...';
        voiceResults.textContent = '';
    });

    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        voiceText.value = transcript;
        voiceResults.textContent = `You said: ${transcript}`;
        voiceBtn.classList.remove('listening');
        voiceStatus.textContent = 'Voice input received';
    };

    recognition.onerror = function(event) {
        voiceBtn.classList.remove('listening');
        voiceStatus.textContent = `Error occurred: ${event.error}`;
    };

    recognition.onend = function() {
        if (voiceBtn.classList.contains('listening')) {
            voiceBtn.classList.remove('listening');
            voiceStatus.textContent = 'Voice input timed out';
        }
    };
});
