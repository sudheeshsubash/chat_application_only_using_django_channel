
        
function getCurrentTime() {
    var now = new Date();
    var hours = now.getHours();
    var minutes = now.getMinutes();
    var amPm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12 || 12; 
    minutes = minutes < 10 ? '0' + minutes : minutes; 
    return hours + ':' + minutes + ' ' + amPm;
}


function incomingMessageCreateNewElement(message){

    if (message !== null && message !== ""){
    var incoming_message = document.createElement('div');
    incoming_message.className = 'd-flex justify-content-start mb-4 incoming_message';

    var img_cont_msg = document.createElement('div');
    img_cont_msg.className = 'img_cont_msg';

    var img = document.createElement('img');
    img.src = 'https://static.turbosquid.com/Preview/001292/481/WV/_D.jpg';
    img.className = 'rounded-circle user_img_msg'
    
    img_cont_msg.appendChild(img);

    var msg_cotainer = document.createElement('div');
    msg_cotainer.className = 'msg_cotainer';
    msg_cotainer.textContent = message;

    var msg_time = document.createElement('span');
    msg_time.className = 'msg_time';
    msg_time.textContent = getCurrentTime();

    msg_cotainer.appendChild(msg_time);

    incoming_message.appendChild(img_cont_msg);
    incoming_message.appendChild(msg_cotainer);

    var parentElement = document.getElementById('msg_history');
    parentElement.appendChild(incoming_message);

    }

}


function outgoingMessageCreateNewElement(message, time) {

    var outgoing_messages = document.createElement('div');
    outgoing_messages.className = 'd-flex justify-content-end mb-4 outgoing_messages';

    var img_cont_msg = document.createElement('div');
    img_cont_msg.className = 'img_cont_msg';

    var img = document.createElement('img');
    img.src = 'https://static.turbosquid.com/Preview/001214/650/2V/boy-cartoon-3D-model_D.jpg';
    img.className = 'rounded-circle user_img_msg'
    
    img_cont_msg.appendChild(img);

    var msg_cotainer_send = document.createElement('div');
    msg_cotainer_send.className = 'msg_cotainer_send';
    msg_cotainer_send.textContent = message;

    var msg_time_send = document.createElement('span');
    msg_time_send.className = 'msg_time_send';
    msg_time_send.textContent = getCurrentTime();

    msg_cotainer_send.appendChild(msg_time_send);

    outgoing_messages.appendChild(msg_cotainer_send);
    outgoing_messages.appendChild(img_cont_msg);

    var parentElement = document.getElementById('msg_history');
    parentElement.appendChild(outgoing_messages);
}





function fetch_history_messages(messages, user){

    for (index in messages){
        if (messages[index].user === user){
            outgoingMessageCreateNewElement(messages[index].message)
        }else{
            incomingMessageCreateNewElement(messages[index].message)
        }
    }
}





