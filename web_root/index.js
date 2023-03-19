console.log("Hello from JS");

var ws = new WebSocket("ws://localhost:8000/api/ws");
ws.onmessage = function(event) {
    var messages = document.getElementById('messages')
    var message = document.createElement('li')
    var content = document.createTextNode(event.data)
    message.appendChild(content)
    messages.appendChild(message)
};

function sendMessage(event) {
    var input = document.getElementById("messageText")
    ws.send(input.value)
    input.value = ''
    event.preventDefault()
};

var pointCloudSocket = new WebSocket("ws://localhost:8000/api/point_cloud");
pointCloudSocket.onmessage = (event) => {
    let payload = JSON.parse(event.data);
    viewer.updatePoints(payload);
};

let viewer = new Viewer();
viewer.animate();
