def main(session, vk_session, longpoll, vk, random_id, event):
            
    if event.obj.text.lower() == 'привет' or event.obj.text.lower() == 'спасибо':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='Пошол ты нахуй'
        )
        
    if event.obj.text.lower() == 'на флэте?':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='ЭЭЭЭЙ НА ФЛЭЭЭТЕ'
        )
        
    if event.obj.text.lower() == 'ливня':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='Долбоеб'
        )
        
    if event.obj.text.lower() == 'помолимся':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            attachment='video67219698_456244596'
        )
        
    if event.obj.text.lower() == 'ты':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='Пидор'
        )
        
    if event.obj.text.lower() == 'да' or event.obj.text.lower() == 'да?':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='Пизда'
        )
        
    if event.obj.text.lower() == 'спок':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='Спок!'
        )
        
    if event.obj.text.lower() == 'ладно':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='Шоколадно бля'
        )
    
    if event.obj.text.lower() == 'понимаю' or event.obj.text.lower() == 'понимаешь?':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            attachment='photo-73935802_457240008'
        )
    
    if event.obj.text.lower() == 'ебанутый' or event.obj.text.lower() == 'попаянный':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            attachment='photo-73935802_457240009'
        )
    
    if event.obj.text.lower() == 'закрой рот' or event.obj.text.lower() == 'завали ебало':
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message='Лан'
        )

# if __name__ == '__main__':
#     b()