// Camera functionality for food logging
document.addEventListener('DOMContentLoaded', function() {
    const video = document.getElementById('cameraFeed');
    const canvas = document.getElementById('canvas');
    const captureBtn = document.getElementById('captureBtn');
    const resultsBox = document.getElementById('resultsBox');
    const ctx = canvas.getContext('2d');
    let stream = null;

    // Access camera
    async function initCamera() {
        try {
            stream = await navigator.mediaDevices.getUserMedia({ 
                video: { 
                    width: { ideal: 1280 },
                    height: { ideal: 720 },
                    facingMode: 'environment' 
                },
                audio: false 
            });
            video.srcObject = stream;
            video.onloadedmetadata = () => {
                captureBtn.disabled = false;
                captureBtn.querySelector('.button-text').textContent = 'Capture Food Image';
            };
        } catch (err) {
            console.error('Camera error:', err);
            const errorMessage = document.createElement('div');
            errorMessage.className = 'error-message';
            errorMessage.innerHTML = `
                <p>Could not access camera. Please:</p>
                <ul>
                    <li>Ensure camera permissions are granted</li>
                    <li>Check if another app is using the camera</li>
                    <li>Try refreshing the page</li>
                </ul>
            `;
            document.querySelector('.camera-container').appendChild(errorMessage);
            captureBtn.querySelector('.button-text').textContent = 'Camera Error';
        }
    }

    // Capture image
    captureBtn.addEventListener('click', function() {
        // Show loading state
        const icon = captureBtn.querySelector('.button-icon');
        const text = captureBtn.querySelector('.button-text');
        icon.textContent = '🔍';
        text.textContent = 'Analyzing...';
        captureBtn.disabled = true;
        
        // Capture frame
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
        
        // Mock analysis (would be replaced with actual API call)
        setTimeout(() => {
            // Identify food (mock response)
            const foodData = {
                name: 'Apple',
                emoji: '🍎',
                calories: 52,
                protein: 0.3,
                carbs: 14,
                fat: 0.2
            };

            // Update results display
            document.getElementById('foodEmoji').textContent = foodData.emoji;
            document.getElementById('foodName').textContent = foodData.name;
            document.getElementById('calories').textContent = foodData.calories;
            document.getElementById('protein').textContent = foodData.protein;
            document.getElementById('carbs').textContent = foodData.carbs;
            document.getElementById('fat').textContent = foodData.fat;

            // Show results
            resultsBox.style.display = 'block';
            icon.textContent = '🔄';
            text.textContent = 'Capture Again';
            captureBtn.disabled = false;
            
            // Scroll to results
            resultsBox.scrollIntoView({ behavior: 'smooth' });
            
            // Play success sound
            new Audio('{% static "sounds/success.mp3" %}').play().catch(e => console.log(e));
        }, 1500);
    });

    // Save to dashboard
    document.querySelector('.confirm-button').addEventListener('click', function() {
        const foodName = document.getElementById('foodName').textContent;
        const calories = document.getElementById('calories').textContent;
        
        // Send data to server (mock implementation)
        fetch('/api/log-food/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': '{{ csrf_token }}'
            },
            body: JSON.stringify({
                food: foodName,
                calories: calories,
                date: new Date().toISOString()
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(`${foodName} (${calories} kcal) logged successfully!`);
                window.location.href = '/dashboard/';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Failed to log food. Please try again.');
        });
    });

    // Initialize camera when page loads
    initCamera();

    // Clean up camera stream when leaving page
    window.addEventListener('beforeunload', function() {
        if (stream) {
            stream.getTracks().forEach(track => track.stop());
        }
    });
});
