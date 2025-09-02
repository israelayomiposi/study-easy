// This file contains the main JavaScript functionality for the frontend application.

document.addEventListener('DOMContentLoaded', function() {
    // Initialize the application
    console.log("Study Tool Application Loaded");

    // Add event listeners for navigation
    setupNavigation();
});

function setupNavigation() {
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetPage = this.getAttribute('href');
            loadPage(targetPage);
        });
    });
}

function loadPage(page) {
    const contentArea = document.getElementById('content');
    fetch(page)
        .then(response => response.text())
        .then(data => {
            contentArea.innerHTML = data;
        })
        .catch(error => {
            console.error('Error loading page:', error);
        });
}