import requests
from random import random
from vk_api import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

def a():

    print('forward')

    session = requests.Session()

    vk_session = vk_api.VkApi(token='0ea77560657fcb9c2b97078030a80473860b4ee440cc9f20edc0f413e6e8637c5db672e0acbe589bcf15d')

    longpoll = VkBotLongPoll(vk_session, 73935802)
    vk = vk_session.get_api()
    
    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            
            random_id = round(random() * 10 ** 9)

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
                            message='прикрепи пикчу, опездал'
                        )

# if __name__ == '__main__':
#     a()