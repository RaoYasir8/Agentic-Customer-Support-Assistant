const API_URL = "http://127.0.0.1:8000/api/support/chat";
const CLEAR_URL = "http://127.0.0.1:8000/api/support/chat";

const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");
const clearBtn = document.getElementById("clearBtn");

const sessionId =
    localStorage.getItem("support_session_id") || crypto.randomUUID();

localStorage.setItem("support_session_id", sessionId);

function addMessage(content, className) {
    const message = document.createElement("div");
    message.className = `message ${className}`;
    message.textContent = content;

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;

    return message;
}

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    addMessage(message, "user-message");
    userInput.value = "";

    const loadingMessage = addMessage(
        "Checking your request...",
        "bot-message"
    );

    const submitButton = chatForm.querySelector("button");
    submitButton.disabled = true;

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                message: message,
                session_id: sessionId,
            }),
        });

        if (!response.ok) {
            throw new Error("Support API request failed");
        }

        const data = await response.json();
        loadingMessage.textContent = data.response;

    } catch (error) {
        loadingMessage.textContent =
            "Sorry, I could not process your request right now. Please try again.";
        loadingMessage.classList.add("error-message");

    } finally {
        submitButton.disabled = false;
        userInput.focus();
    }
});

clearBtn.addEventListener("click", async () => {
    try {
        await fetch(`${CLEAR_URL}/${sessionId}`, {
            method: "DELETE",
        });

    } catch (error) {
        console.error("Failed to clear memory", error);
    }

    chatBox.innerHTML = "";

    addMessage(
        "Conversation cleared. How can I help you now?",
        "bot-message"
    );
});