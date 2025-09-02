// This file contains JavaScript functions for managing the user dashboard.

document.addEventListener('DOMContentLoaded', function() {
    const progressContainer = document.getElementById('progress-container');
    const userId = getUserId(); // Function to get the logged-in user's ID

    // Fetch user progress from the backend
    fetch(`/api/dashboard/progress/${userId}`)
        .then(response => response.json())
        .then(data => {
            displayProgress(data);
        })
        .catch(error => {
            console.error('Error fetching progress:', error);
        });

    function displayProgress(data) {
        // Clear existing progress
        progressContainer.innerHTML = '';

        // Create progress elements
        data.forEach(subject => {
            const subjectElement = document.createElement('div');
            subjectElement.classList.add('subject-progress');
            subjectElement.innerHTML = `
                <h3>${subject.name}</h3>
                <p>Completed: ${subject.completedTopics} / ${subject.totalTopics}</p>
                <div class="progress-bar">
                    <div class="progress" style="width: ${subject.progressPercentage}%;"></div>
                </div>
            `;
            progressContainer.appendChild(subjectElement);
        });
    }

    function getUserId() {
        // Placeholder function to get user ID
        // In a real application, this might come from a session or token
        return localStorage.getItem('userId');
    }
});