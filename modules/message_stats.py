from datetime import datetime, timedelta

message_stats_desc = '/статы - вывод сообщений за всё время'

def main(session, vk_session, longpoll, vk, random_id, event):
    
    if event.obj.text.lower() == '/статы':
        
        # allTimeCount = vk.messages.getHistory(
        #     peer_id=event.obj.peer_id
        # )
        
        # count = (allTimeCount['items'][0]['conversation_message_id'])
        
        # vk.messages.send(
        #     random_id=random_id,
        #     peer_id=event.obj.peer_id,
        #     chat_id=event.chat_id,
        #     message=f'Колличество сообщений за всё время: {count}'
        # )

        dateActual = datetime.now()
        
        dateEnd = dateActual + timedelta(days=1)
        
        allTimeDate = int(dateEnd.strftime("%d%m%Y"))
        
        allTimeCount = vk.messages.search(
            peer_id=event.obj.peer_id, 
            date=allTimeDate,
            q=''
        )

        count = (allTimeCount['items'][0]['conversation_message_id'])
        
        vk.messages.send(
            random_id=random_id,
            peer_id=event.obj.peer_id,
            chat_id=event.chat_id,
            message=f'Колличество сообщений за всё время: {count}'
        )