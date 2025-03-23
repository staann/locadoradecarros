document.addEventListener("DOMContentLoaded", function () {
    const socket = io();

    const messagesDiv = document.getElementById("messages");
    const messageInput = document.getElementById("message-input");
    const chatBox = document.getElementById("chat-box");
    const toggleChatButton = document.getElementById("toggle-chat");
    const chatHeader = document.getElementById("chat-header");

    let isChatOpen = false; // Inicialmente o chat está fechado
    let lastSender = null; // Armazena o remetente para resposta

    function addMessage(message, isUser = false) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", isUser ? "user-message" : "server-message");
        messageElement.textContent = message;
        messagesDiv.appendChild(messageElement);
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    }

    // Enviar mensagem ao pressionar "Enter"
    messageInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter" && this.value.trim() !== "") {
            socket.emit("chatMessage", { message: this.value }); // Envia para o servidor
            addMessage(`Você: ${this.value}`, true); // Exibe no próprio chat
            this.value = ""; // Limpa o input
        }
    });

    // Receber mensagens de outros usuários
    socket.on("receiveMessage", function (data) {
        lastSender = data.from; // Salva o remetente para poder responder
        addMessage(`Outro: ${data.message}`, false);
    });

    // Enviar resposta ao pressionar "R"
    document.addEventListener("keydown", function (e) {
        if (e.key === "r" && lastSender) {
            const replyMessage = prompt("Digite sua resposta:");
            if (replyMessage) {
                socket.emit("replyMessage", { message: replyMessage, to: lastSender });
                addMessage(`Você (respondendo): ${replyMessage}`, true);
            }
        }
    });

    // Mensagem do sistema
    socket.on("systemMessage", function (msg) {
        addMessage(`⚠️ ${msg}`, false);
    });

    // Botão para minimizar/maximizar o chat
    toggleChatButton.addEventListener("click", function (e) {
        e.stopPropagation(); // Impede que o evento de clique no cabeçalho seja acionado
        toggleChat();
    });

    // Clicar no cabeçalho para abrir/fechar o chat
    chatHeader.addEventListener("click", function () {
        toggleChat();
    });

    function toggleChat() {
        isChatOpen = !isChatOpen;
        chatBox.style.display = isChatOpen ? "flex" : "none";
        toggleChatButton.textContent = isChatOpen ? "-" : "+";
    }

    // Inicializa o chat fechado
    toggleChat(); // Fecha o chat ao carregar a página
});