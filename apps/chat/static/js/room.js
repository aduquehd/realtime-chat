let roomName = "lobby";

let chatSocket = new WebSocket('ws://' + window.location.host + '/ws/chat/' + roomName + '/');

let userId = document.getElementById('user-id').value.toString();

chatSocket.onmessage = function (e) {
    let data = JSON.parse(e.data);

    console.log("DATA: ", data);

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

document.querySelector('#message-text').focus();

document.querySelector('#message-text').onkeyup = function (e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
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

let messagesList = new Vue({
    el: '#messages-list',
    data: {
        items: []
    },

});

try {
    document.getElementById("messages-list").lastChild.scrollIntoView();
}
catch (e) {

}

let myElement = document.getElementById('messages-list');
if (window.addEventListener) {
    myElement.addEventListener('DOMSubtreeModified', contentChanged, false);
} else if (window.attachEvent) {
    myElement.attachEvent('DOMSubtreeModified', contentChanged);
}

function contentChanged() {
    console.log("changed");
    document.getElementById("messages-list").lastChild.scrollIntoView();
}