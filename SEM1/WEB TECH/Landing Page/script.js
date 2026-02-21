// Get the button element by its ID
const buyButton = document.getElementById('buy-button');

// Add an event listener for a 'click' event
buyButton.addEventListener('click', function() {
    // 1. Give the user feedback
    alert('Thank you for your interest! We\'ve added Clarity X-900 to your cart.');

    // 2. Optional: Change the button text and style after click
    buyButton.textContent = 'Added to Cart!';
    buyButton.style.backgroundColor = '#28a745'; // Green color for success

    // 3. Optional: Add a smooth scroll to the buy section in the footer
    const footer = document.getElementById('buy');
    if (footer) {
        footer.scrollIntoView({ behavior: 'smooth' });
    }
});

// Optional: You could add code here for a carousel, form validation, etc.