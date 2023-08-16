// Add JavaScript code here
// This file is used to implement any client-side functionality for the website.
// You can add event listeners, make AJAX requests, manipulate the DOM, etc.
// Remember to follow best practices and keep the code clean and modular.

// Example:
// Add an event listener to the submit button of the contact form
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting

    // Get the form data
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var projectDescription = document.getElementById('project-description').value;
    var budget = document.getElementById('budget').value;

    // Validate the form data
    if (name === '' || email === '' || projectDescription === '' || budget === '') {
        alert('Please fill out all fields');
        return;
    }

    // Make an AJAX request to submit the form data
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/contact/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            alert('Consultation request submitted successfully');
            document.getElementById('contact-form').reset(); // Reset the form
        } else {
            alert('Error submitting consultation request');
        }
    };
    xhr.send(JSON.stringify({
        name: name,
        email: email,
        project_description: projectDescription,
        budget: parseFloat(budget)
    }));
});
