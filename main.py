import requests
from vk_api import vk_api
from datetime import datetime
from loguru import logger as lg
from modules.message_new import MessageNew
from modules.message_typing import MessageTyping
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

class sk_bot():
    def __init__(self):
        lg.add("logs/{} session.log".format(datetime.now().strftime("%Y-%m-%d@%H-%M-%S")), 
            format="{time:HH:mm:ss} | <level>{level: <8}</level> | {function} {line}: {message}", 
            level="DEBUG")

        self.session = requests.Session()
        self.vk_session = vk_api.VkApi(token="vk1.a.xKC-WYPQnJ6O4DYxC-UtudDjKEt21eSdrZe5Qk1aTz2GMkv_4pty5fUNLSrtUDpTzzuSSvaSscoMa97sSxH5ZqZ92qWAoXD5jzfcBUdPmWf5VYj8oi1xw4O2pDL8Gxd8EXpgrnlW8XgxJ2UzAKfNPdv8CCWkteKImekNsjFJDy6PNDsfhyN8fvqXwi8MSo2W")
        self.longpoll = VkBotLongPoll(self.vk_session, 73935802)
        self.vk = self.vk_session.get_api()

    def main(self):
        lg.info("Бот запущен")
        
        while True:
            for event in self.longpoll.listen():
                lg.info("Произошло событие")

                if event.type == VkBotEventType.MESSAGE_TYPING_STATE:
                    lg.info("Происходит набор сообщения")

                    MessageTyping(self.vk, event)

                if event.type == VkBotEventType.MESSAGE_NEW:
                    lg.info("Поступило сообщение")
                    
                    MessageNew(self.session, self.vk_session, self.vk, event)

if __name__ == "__main__":
    while True:
        try:
            sk_bot().main()
        except:
            lg.error("Шота навернулось")
            lg.exception("exception")