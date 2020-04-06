import os
import sys
import requests
from random import random
from vk_api import vk_api
from vk_api import VkUpload
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
sys.path.append(os.path.abspath('../modules'))
from modules import speech
from modules import forward
from modules import support

def main():

    print('Бот робит')
    
    session = requests.Session()

    vk_session = vk_api.VkApi(token='0ea77560657fcb9c2b97078030a80473860b4ee440cc9f20edc0f413e6e8637c5db672e0acbe589bcf15d')

    longpoll = VkBotLongPoll(vk_session, 73935802)
    vk = vk_session.get_api()
    
    descDict = [forward.forward_desc]
    
    for event in longpoll.listen():

        print('Произошла прослушка')

        if event.type == VkBotEventType.MESSAGE_NEW:
            
            print('Поступило сообщение')
            
            random_id = round(random() * 10 ** 9)
            
            forward.main(session, vk_session, longpoll, vk, random_id, event)
            speech.main(session, vk_session, longpoll, vk, random_id, event)
            support.main(session, vk_session, longpoll, vk, random_id, event, descDict)
                                                
if __name__ == '__main__':
    main()
