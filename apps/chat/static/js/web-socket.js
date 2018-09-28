function initChatSocketActions(chatSocket, chatBotSocket) {
    let currentUserId = document.getElementById('user-id').value.toString();

    chatSocket.onmessage = function (e) {
        addNewMessage(e)
    };

    chatBotSocket.onmessage = function (e) {
        addNewMessage(e)
    };

    document.querySelector('#chat-message-submit').onclick = function (e) {
        let messageInputDom = $('#message-text');
        let message = messageInputDom.val();
        if (message) {
            if (message === '/stock=APPL') {
                chatBotSocket.send(JSON.stringify({
                    'user_id': currentUserId,
                }));

            } else {
                chatSocket.send(JSON.stringify({
                    'message': message,
                }));
            }
            messageInputDom.val('');
        }
    };

}

function addNewMessage(e) {
    let data = JSON.parse(e.data);
    let currentUserId = document.getElementById('user-id').value.toString();

    let isOwn = parseInt(currentUserId) === parseInt(data['user_id']);

    messagesList.items.push({
        message: data['message'],
        user_id: data['user_id'],
        created_at: data['created_at'],
        publisher_full_name: data['publisher_full_name'],
        own: isOwn,
    });
    if (!isOwn) {
        sendNotification()
    }
}


function sendNotification() {
    console.log("Sending alert")

    if (Notification.permission !== "granted")
        Notification.requestPermission();
    else {
        console.log("sent alert")
        new Notification('Realtime Chat Notification', {
            icon: 'http://cdn.sstatic.net/stackexchange/img/logos/so/so-icon.png',
            body: "You have new messages on Realtime chat!",
        });
    }
}