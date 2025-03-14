// Chat
let chatMain = document.querySelector('.chat-main');
let FormChat = document.querySelector('.chat-form');
let chatBox = FormChat.querySelector('.chat-input');

chatMain.scrollTop = 1000;


let add_chat = document.getElementById('send_message');

add_chat.addEventListener('click',(e)=>{
    add_chatBox(e);
})

FormChat.addEventListener('submit',(e)=>{
    add_chatBox(e);
})


function add_chatBox(e){

        e.preventDefault();
        
        let textBox = document.createElement('div');
        textBox.classList.add('text-box','left');
    
        if(chatBox.value != ''){
            textBox.innerHTML = chatBox.value;
    
            chatMain.appendChild(textBox);
            chatMain.scrollTop += 100;
        }
        chatBox.value = '';
}