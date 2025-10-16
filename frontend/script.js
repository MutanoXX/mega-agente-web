// API Configuration - use same origin for better deployment flexibility
const API_BASE_URL = window.location.origin;

// DOM Elements
const chatMessages = document.getElementById('chat-messages');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const clearBtn = document.getElementById('clear-btn');
const statusText = document.getElementById('status-text');
const statusDot = document.querySelector('.status-dot');

// Model selectors
const textModelSelect = document.getElementById('text-model');
const searchModelSelect = document.getElementById('search-model');
const reasoningModelSelect = document.getElementById('reasoning-model');
const imageModelSelect = document.getElementById('image-model');
const audioVoiceSelect = document.getElementById('audio-voice');

// State
let isProcessing = false;
let currentMessageElement = null;

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    setupEventListeners();
    autoResizeTextarea();
});

function setupEventListeners() {
    sendBtn.addEventListener('click', sendMessage);
    clearBtn.addEventListener('click', clearConversation);
    
    userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            sendMessage();
        }
    });
    
    userInput.addEventListener('input', autoResizeTextarea);
}

function autoResizeTextarea() {
    userInput.style.height = 'auto';
    userInput.style.height = userInput.scrollHeight + 'px';
}

function getSelectedModels() {
    return {
        text: textModelSelect.value,
        search: searchModelSelect.value,
        reasoning: reasoningModelSelect.value,
        image: imageModelSelect.value,
        audio: audioVoiceSelect.value
    };
}

async function sendMessage() {
    const message = userInput.value.trim();
    
    if (!message || isProcessing) return;
    
    // Clear welcome message if it exists
    const welcomeMessage = document.querySelector('.welcome-message');
    if (welcomeMessage) {
        welcomeMessage.remove();
    }
    
    // Add user message to chat
    addUserMessage(message);
    
    // Clear input
    userInput.value = '';
    autoResizeTextarea();
    
    // Set processing state
    setProcessingState(true);
    
    try {
        // Get selected models
        const models = getSelectedModels();
        
        // Send request to API
        const response = await fetch(`${API_BASE_URL}/chat`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                message: message,
                models: models
            })
        });
        
        if (!response.ok) {
            throw new Error('Failed to get response from server');
        }
        
        // Process SSE stream
        await processStream(response);
        
    } catch (error) {
        console.error('Error:', error);
        addErrorMessage('Desculpe, ocorreu um erro ao processar sua mensagem. Por favor, tente novamente.');
    } finally {
        setProcessingState(false);
    }
}

async function processStream(response) {
    const reader = response.body.getReader();
    const decoder = new TextDecoder();
    
    let buffer = '';
    let currentText = '';
    
    while (true) {
        const { done, value } = await reader.read();
        
        if (done) break;
        
        buffer += decoder.decode(value, { stream: true });
        
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';
        
        for (const line of lines) {
            if (line.startsWith('data: ')) {
                const data = line.slice(6);
                
                try {
                    const event = JSON.parse(data);
                    
                    switch (event.type) {
                        case 'tool_selection':
                            createAssistantMessage();
                            addToolBadge(event.tool);
                            break;
                        
                        case 'status':
                            addStatusMessage(event.message);
                            break;
                        
                        case 'text_chunk':
                            currentText += event.content;
                            updateMessageText(currentText);
                            break;
                        
                        case 'image':
                            addImageToMessage(event.url, event.prompt);
                            break;
                        
                        case 'audio':
                            addAudioToMessage(event.url, event.text);
                            break;
                        
                        case 'done':
                            finalizeMessage();
                            currentText = '';
                            break;
                        
                        case 'error':
                            addErrorMessage(event.message);
                            break;
                    }
                } catch (e) {
                    console.error('Error parsing event:', e);
                }
            }
        }
    }
}

function addUserMessage(text) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message user';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.textContent = text;
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function createAssistantMessage() {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message assistant';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    
    currentMessageElement = contentDiv;
    scrollToBottom();
}

function addToolBadge(toolName) {
    if (!currentMessageElement) return;
    
    const badge = document.createElement('div');
    badge.className = 'tool-badge';
    badge.textContent = toolName;
    
    currentMessageElement.appendChild(badge);
    scrollToBottom();
}

function addStatusMessage(status) {
    if (!currentMessageElement) return;
    
    const statusDiv = document.createElement('div');
    statusDiv.className = 'status-message';
    statusDiv.textContent = status;
    
    currentMessageElement.appendChild(statusDiv);
    
    // Add typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'typing-indicator';
    typingDiv.innerHTML = '<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>';
    
    currentMessageElement.appendChild(typingDiv);
    scrollToBottom();
}

function updateMessageText(text) {
    if (!currentMessageElement) return;
    
    // Remove typing indicator if exists
    const typingIndicator = currentMessageElement.querySelector('.typing-indicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
    
    // Find or create text container
    let textContainer = currentMessageElement.querySelector('.message-text');
    if (!textContainer) {
        textContainer = document.createElement('div');
        textContainer.className = 'message-text';
        currentMessageElement.appendChild(textContainer);
    }
    
    // Update text with markdown-like formatting
    textContainer.innerHTML = formatText(text);
    scrollToBottom();
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatText(text) {
    // Escape HTML first to prevent XSS, then apply markdown-like formatting
    const escaped = escapeHtml(text);
    return escaped
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        .replace(/`(.*?)`/g, '<code>$1</code>')
        .replace(/\n/g, '<br>');
}

function addImageToMessage(url, prompt) {
    if (!currentMessageElement) return;
    
    const imageContainer = document.createElement('div');
    imageContainer.className = 'image-container';
    
    const img = document.createElement('img');
    img.src = url;
    img.alt = prompt;
    img.loading = 'lazy';
    
    imageContainer.appendChild(img);
    currentMessageElement.appendChild(imageContainer);
    scrollToBottom();
}

function addAudioToMessage(url, text) {
    if (!currentMessageElement) return;
    
    const audioContainer = document.createElement('div');
    audioContainer.className = 'audio-container';
    
    const audio = document.createElement('audio');
    audio.controls = true;
    audio.src = url;
    
    audioContainer.appendChild(audio);
    currentMessageElement.appendChild(audioContainer);
    scrollToBottom();
}

function finalizeMessage() {
    currentMessageElement = null;
}

function addErrorMessage(errorText) {
    const messageDiv = document.createElement('div');
    messageDiv.className = 'message assistant';
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    contentDiv.style.borderColor = 'var(--error-color)';
    contentDiv.innerHTML = `<strong>❌ Erro:</strong> ${errorText}`;
    
    messageDiv.appendChild(contentDiv);
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

function setProcessingState(processing) {
    isProcessing = processing;
    sendBtn.disabled = processing;
    userInput.disabled = processing;
    
    if (processing) {
        statusText.textContent = 'Processando...';
        statusDot.classList.add('processing');
    } else {
        statusText.textContent = 'Pronto';
        statusDot.classList.remove('processing');
    }
}

async function clearConversation() {
    if (!confirm('Tem certeza que deseja limpar a conversa?')) {
        return;
    }
    
    try {
        await fetch(`${API_BASE_URL}/clear`, {
            method: 'POST'
        });
        
        // Clear chat messages
        chatMessages.innerHTML = `
            <div class="welcome-message">
                <div class="welcome-icon">🚀</div>
                <h2>Bem-vindo ao Mega Agent!</h2>
                <p>Eu posso ajudá-lo com:</p>
                <ul>
                    <li>💬 Conversas e respostas inteligentes</li>
                    <li>🎨 Geração de imagens</li>
                    <li>🔍 Pesquisas na web</li>
                    <li>🔊 Geração de áudio</li>
                    <li>🧠 Raciocínio complexo</li>
                </ul>
                <p class="tip">💡 <strong>Dica:</strong> Apenas escreva sua mensagem e eu decidirei qual ferramenta usar!</p>
            </div>
        `;
    } catch (error) {
        console.error('Error clearing conversation:', error);
        alert('Erro ao limpar a conversa. Por favor, tente novamente.');
    }
}

function scrollToBottom() {
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
