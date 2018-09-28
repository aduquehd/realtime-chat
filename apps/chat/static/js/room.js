initActions();
let currentRealtimeChatSocket = null;
let currentRealtimeChatBotSocket = null;

let messagesList = new Vue({
    el: '#messages-list',
    data: {
        items: []
    },
});


function initActions() {
    initMessageInputTextActions();
    initRoomsActions();
}

function initRoomsActions() {
    $('.chat_list').click(function () {
        let roomId = $(this).data('room-id');
        let roomName = $(this).data('room-name');

        messagesList.items = [];

        let chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');
        let chatBotSocket = new WebSocket('ws://' + $('#realtime-chat-bot').val() + '/ws/chat/bot/' + roomName + '/');

        if (currentRealtimeChatSocket) {
            currentRealtimeChatSocket.close();
        }

        if (currentRealtimeChatBotSocket) {
            currentRealtimeChatBotSocket.close();
        }

        currentRealtimeChatSocket = chatSocket;
        currentRealtimeChatBotSocket = chatBotSocket;

        initChatSocketActions(chatSocket, chatBotSocket);

        $(".chat_list").removeClass('active_chat');
        this.classList.add('active_chat');

        let messageTextDOM = $('#message-text');

        messageTextDOM.removeAttr('disabled');
        messageTextDOM.attr('placeholder', "Write a message");

        updateRoomChats(roomId);
    });
}

function updateRoomChats(roomId) {
    let userId = document.getElementById('user-id').value.toString();
    let newData = [];

    axios
        .get(`/chat/rooms/${roomId}`)
        .then(response => {
            $.each(response.data, function (index, value) {
                newData.push({
                    message: value.message,
                    user_id: value.user_id,
                    publisher_full_name: value.publisher_full_name,
                    created_at: value.created_at,
                    own: parseInt(userId) === parseInt(value.user_id),
                })
            });
        });

    messagesList.items = newData;

}

$('#messages-list').bind("DOMSubtreeModified", function () {
    try {
        document.getElementById("messages-list").lastChild.scrollIntoView();
    }
    catch (e) {
    }
});

document.addEventListener('DOMContentLoaded', function () {
    if (!Notification) {
        alert('Desktop notifications not available in your browser. Try Chromium.');
        return;
    }

    if (Notification.permission !== "granted") {
        Notification.requestPermission();
    }
});
