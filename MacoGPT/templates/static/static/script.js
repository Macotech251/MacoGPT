
const input = document.getElementById("message-input");
const sendButton = document.getElementById("send-button");
const chatArea = document.getElementById("chat-area");
const welcome = document.getElementById("welcome");
const historyList = document.getElementById("history-list");

let messages = [];
let chats = [];

function addMessage(role, content) {
    if (welcome) welcome.style.display = "none";

    const message = document.createElement("div");
    message.className = `message ${role}`;

    // Render text safely
    message.textContent = content;

    chatArea.appendChild(message);
    chatArea.scrollTop = chatArea.scrollHeight;

    return message;
}

async function sendMessage() {
    const text = input.value.trim();

    if (!text) return;

    input.value = "";
    input.disabled = true;
    sendButton.disabled = true;

    messages.push({
        role: "user",
        content: text
    });

    addMessage("user", text);

    const loading = addMessage("assistant", "MacoGPT is thinking...");

    try {
        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                messages: messages
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong");
        }

        loading.textContent = data.reply;

        messages.push({
            role: "assistant",
            content: data.reply
        });

        if (messages.length === 2) {
            chats.push(text);
            updateHistory();
        }

    } catch (error) {
        loading.textContent = "Error: " + error.message;
        messages.pop();

    } finally {
        input.disabled = false;
        sendButton.disabled = false;
        input.focus();
    }
}

function updateHistory() {
    historyList.replaceChildren();

    chats.forEach((chat) => {
        const item = document.createElement("div");
        item.className = "history-item";
        item.textContent = chat;
        historyList.appendChild(item);
    });
}

sendButton.addEventListener("click", sendMessage);

input.addEventListener("keydown", (event) => {
    if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        sendMessage();
    }
});

document.querySelectorAll(".suggestion").forEach((button) => {
    button.addEventListener("click", () => {
        input.value = button.textContent;
        sendMessage();
    });
});

document.getElementById("new-chat").addEventListener("click", () => {
    messages = [];
    chatArea.replaceChildren();

    if (welcome) {
        chatArea.appendChild(welcome);
        welcome.style.display = "block";
    }
});

document.getElementById("theme-toggle").addEventListener("click", () => {
    document.body.classList.toggle("light");
});
