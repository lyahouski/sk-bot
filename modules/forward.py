from vk_api import VkUpload

def main(session, vk_session, longpoll, vk, random_id, event):

    if event.obj.text.lower() == '/перешли':
        if bool(event.obj.attachments):
            if event.obj.attachments[0]['type'] == 'photo':
                upload = VkUpload(vk_session)
                lastUrl = len(event.obj.attachments[0]['photo']['sizes']) - 1
                sunLink = event.obj.attachments[0]['photo']['sizes'][lastUrl]['url']
                image = session.get(sunLink, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]
                attachment = 'photo{}_{}'.format(photo['owner_id'], photo['id'])
                
                vk.messages.send(
                    random_id=random_id,
                    chat_id=event.chat_id,
                    peer_id=event.obj.peer_id,
                    message='Держи, брат',
                    attachment=f'{attachment}'
                ) 
            else:
                vk.messages.send(
                    random_id=random_id,
                    chat_id=event.chat_id,
                    peer_id=event.obj.peer_id,
                    message='Нахуй ты не пикчу прикрепил?'
            )
        else:
            vk.messages.send(
                random_id=random_id,
                chat_id=event.chat_id,
                peer_id=event.obj.peer_id,
                message='Прикрепи пикчу, опездал'
            )

# if __name__ == '__main__':
#     main()
