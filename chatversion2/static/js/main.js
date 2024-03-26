
function getCurrentTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var amPm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12 || 12; 
    minutes = minutes < 10 ? '0' + minutes : minutes; 
    return hours + ':' + minutes + ' ' + amPm;
}



function outgoingMessageCreateNewElement(message){

    if (message !== null && message !== ""){
    var outgoingMsgDiv = document.createElement('div');
    outgoingMsgDiv.className = 'outgoing_msg';
    
    var sentMsgDiv = document.createElement('div');
    sentMsgDiv.className = 'sent_msg';
    
    var messageParagraph = document.createElement('p');
    messageParagraph.textContent = message;
    
    var timeDateSpan = document.createElement('span');
    timeDateSpan.className = 'time_date';
    timeDateSpan.textContent = getCurrentTime();
    
    // Append elements
    sentMsgDiv.appendChild(messageParagraph);
    sentMsgDiv.appendChild(timeDateSpan);
    outgoingMsgDiv.appendChild(sentMsgDiv);


    var parentElement = document.getElementById('msg_history');
    parentElement.appendChild(outgoingMsgDiv);

    }

}



function incomingMessageCreateNewElement(message, time) {
    // Create incoming message elements
    var incomingMsgDiv = document.createElement('div');
    incomingMsgDiv.className = 'incoming_msg';

    var incomingMsgImgDiv = document.createElement('div');
    incomingMsgImgDiv.className = 'incoming_msg_img';
    var img = document.createElement('img');
    img.src = 'https://ptetutorials.com/images/user-profile.png';
    img.alt = 'sunil';
    incomingMsgImgDiv.appendChild(img);

    var receivedMsgDiv = document.createElement('div');
    receivedMsgDiv.className = 'received_msg';

    var receivedWithdMsgDiv = document.createElement('div');
    receivedWithdMsgDiv.className = 'received_withd_msg';

    var messageParagraph = document.createElement('p');
    messageParagraph.textContent = message;

    var timeDateSpan = document.createElement('span');
    timeDateSpan.className = 'time_date';
    timeDateSpan.textContent = time;

    // Append elements
    receivedWithdMsgDiv.appendChild(messageParagraph);
    receivedWithdMsgDiv.appendChild(timeDateSpan);
    receivedMsgDiv.appendChild(receivedWithdMsgDiv);

    incomingMsgDiv.appendChild(incomingMsgImgDiv);
    incomingMsgDiv.appendChild(receivedMsgDiv);

    // Append incomingMsgDiv to the parent element (where you want to add this dynamic message)
    var parentElement = document.getElementById('msg_history');
    parentElement.appendChild(incomingMsgDiv);
}