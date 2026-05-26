const chatBox = document.getElementById("chat-box");

async function sendMessage() {

    const input = document.getElementById("user-input");

    const message = input.value;

    if (!message) return;

    addMessage(message, "user");

    input.value = "";

    const loadingDiv = addMessage(
        "Typing...",
        "bot"
    );

    const response = await fetch(
        "http://127.0.0.1:8000/api/chat",
        {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                sessionId: "123",
                message: message
            })
        }
    );

    const data = await response.json();

    loadingDiv.innerText = data.reply;
}

function addMessage(text, sender) {

    const div = document.createElement("div");

    div.classList.add("message");

    div.classList.add(sender);

    div.innerText = text;

    chatBox.appendChild(div);

    chatBox.scrollTop = chatBox.scrollHeight;

    return div;
}

document
    .getElementById("user-input")
    .addEventListener(
        "keypress",
        function(event) {

            if (event.key === "Enter") {

                sendMessage();
            }
        }
    );