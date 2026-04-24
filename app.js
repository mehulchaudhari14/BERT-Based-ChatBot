const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const chatBox = document.getElementById('chat-box');

// Keep track of previous chats to send up as context
let chatHistory = [];

function formatTime(date) {
    let hours = date.getHours();
    let minutes = date.getMinutes();
    const ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; 
    minutes = minutes < 10 ? '0' + minutes : minutes;
    return hours + ':' + minutes + ' ' + ampm;
}

function appendMessage(text, sender) {
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('message', sender);
    
    const contentDiv = document.createElement('div');
    contentDiv.classList.add('message-content');
    contentDiv.textContent = text;
    
    const timeSpan = document.createElement('span');
    timeSpan.classList.add('time');
    timeSpan.textContent = formatTime(new Date());
    
    messageDiv.appendChild(contentDiv);
    messageDiv.appendChild(timeSpan);
    
    chatBox.appendChild(messageDiv);
    scrollToBottom();
}

function showTyping() {
    const typingDiv = document.createElement('div');
    typingDiv.classList.add('message', 'bot');
    typingDiv.id = 'typing-indicator-msg';
    
    const indicatorDiv = document.createElement('div');
    indicatorDiv.classList.add('typing-indicator');
    indicatorDiv.innerHTML = '<div class="dot"></div><div class="dot"></div><div class="dot"></div>';
    
    typingDiv.appendChild(indicatorDiv);
    chatBox.appendChild(typingDiv);
    scrollToBottom();
}

function hideTyping() {
    const typingDiv = document.getElementById('typing-indicator-msg');
    if (typingDiv) {
        typingDiv.remove();
    }
}

function scrollToBottom() {
    chatBox.scrollTo({
        top: chatBox.scrollHeight,
        behavior: 'smooth'
    });
}

chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const message = userInput.value.trim();
    if (!message) return;
    
    // Add user message to UI
    appendMessage(message, 'user');
    userInput.value = '';
    
    // Append to history
    chatHistory.push({ role: 'user', content: message });
    
    // Show typing effect
    showTyping();
    
    try {
        // Send to local API
        const response = await fetch('http://127.0.0.1:8000/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ 
                message: message,
                history: chatHistory
            })
        });
        
        if (!response.ok) {
            throw new Error(`API error: ${response.status}`);
        }
        
        const data = await response.json();
        const botReply = data.answer;
        
        hideTyping();
        appendMessage(botReply, 'bot');
        
        // Append bot reply to history
        chatHistory.push({ role: 'bot', content: botReply });
        
    } catch (error) {
        hideTyping();
        console.error('Error communicating with backend:', error);
        appendMessage("I couldn't reach the server. Make sure the backend (app.py) is running on port 8000.", 'bot');
    }
});
