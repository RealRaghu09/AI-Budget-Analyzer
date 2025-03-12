const form = document.getElementById('prompt-form');
const submitBtn = document.getElementById('submit-btn');
const promptInput = document.getElementById('prompt-input');
const responseDiv = document.getElementById('response');

form.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Disable input and button while generating
    submitBtn.disabled = true;
    promptInput.disabled = true;
    responseDiv.classList.add('loading');
    responseDiv.textContent = 'Generating response...';
    
    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `prompt=${encodeURIComponent(promptInput.value)}`
        });
        
        const data = await response.json();
        responseDiv.textContent = data.response;
    } catch (error) {
        responseDiv.textContent = 'Error generating response';
        console.error('Error:', error);
    } finally {
        // Re-enable input and button
        submitBtn.disabled = false;
        promptInput.disabled = false;
        responseDiv.classList.remove('loading');
    }
});

// Add theme toggle functionality
function toggleTheme() {
    const body = document.body;
    if (body.getAttribute('data-theme') === 'dark') {
        body.removeAttribute('data-theme');
        localStorage.setItem('theme', 'light');
    } else {
        body.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    }
}

// Load saved theme preference
const savedTheme = localStorage.getItem('theme');
if (savedTheme === 'dark') {
    document.body.setAttribute('data-theme', 'dark');
} 