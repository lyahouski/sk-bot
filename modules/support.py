def main(session, vk_session, longpoll, vk, random_id, event, descDict):
    
    if event.obj.text.lower() == '/помощь' or event.obj.text.lower() == '/хелп':
        
        descDict = "\n \n 🔵 ".join(descDict)

        vk.messages.send(
                    random_id=random_id,
                    chat_id=event.chat_id,
                    peer_id=event.obj.peer_id,
                    message=f'ШО БОТЯРА МОЖЕ 🐗: \n \n 🔵 {descDict}'
        )