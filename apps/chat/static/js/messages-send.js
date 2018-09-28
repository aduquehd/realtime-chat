function initMessageInputTextActions() {
    document.querySelector('#message-text').focus();
    document.querySelector('#message-text').onkeyup = function (e) {
        if (e.keyCode === 13) {
            document.querySelector('#chat-message-submit').click();
        }
    };
}