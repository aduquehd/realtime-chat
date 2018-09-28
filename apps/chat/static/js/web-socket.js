function initChatSocketActions(chatSocket) {

    let currentUserId = document.getElementById('user-id').value.toString();
    chatSocket.onmessage = function (e) {
        let data = JSON.parse(e.data);

        messagesList.items.push({
            message: data['message'],
            user_id: data['user_id'],
            created_at: data['created_at'],
            publisher_full_name: data['publisher_full_name'],
            own: parseInt(currentUserId) === parseInt(data['user_id']),
        });
    };

    chatSocket.onclose = function (e) {
    };

    document.querySelector('#chat-message-submit').onclick = function (e) {
        let messageInputDom = document.querySelector('#message-text');
        let message = messageInputDom.value;
        if (message) {
            chatSocket.send(JSON.stringify({
                'message': message,
            }));
            messageInputDom.value = '';
        }
    };

}
