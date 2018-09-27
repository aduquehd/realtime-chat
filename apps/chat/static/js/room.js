initActions();

function initActions() {
    initMessageInputTextActions();
    initChatSocketActions("lobby");
    initMessageListActions();

}

function initMessageInputTextActions() {
    document.querySelector('#message-text').focus();
    document.querySelector('#message-text').onkeyup = function (e) {
        if (e.keyCode === 13) {
            document.querySelector('#chat-message-submit').click();
        }
    };

}

function initMessageListActions() {
    let messageListDOM = document.getElementById('messages-list');
    if (window.addEventListener) {
        messageListDOM.addEventListener('DOMSubtreeModified', MessageListContentOnChange, false);
    } else if (window.attachEvent) {
        messageListDOM.attachEvent('DOMSubtreeModified', MessageListContentOnChange);
    }

    try {
        document.getElementById("messages-list").lastChild.scrollIntoView();
    }
    catch (e) {
    }

}

function MessageListContentOnChange() {
    document.getElementById("messages-list").lastChild.scrollIntoView();
}

function initChatSocketActions(roomName) {

    let chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');
    let userId = document.getElementById('user-id').value.toString();

    chatSocket.onmessage = function (e) {
        let data = JSON.parse(e.data);

        messagesList.items.push({
            message: data['message'],
            user_id: data['user_id'],
            created_at: data['created_at'],
            publisher_full_name: data['publisher_full_name'],
            own: parseInt(userId) === parseInt(data['user_id']),
        });
    };

    chatSocket.onclose = function (e) {
        console.error('Chat socket closed unexpectedly');
    };

    document.querySelector('#chat-message-submit').onclick = function (e) {
        let messageInputDom = document.querySelector('#message-text');
        let message = messageInputDom.value;
        if (message) {
            initMessageListActions();
            chatSocket.send(JSON.stringify({
                'message': message,
            }));
            messageInputDom.value = '';
        }
    };

}


let messagesList = new Vue({
    el: '#messages-list',
    data: {
        items: [
        ]
    },
});


