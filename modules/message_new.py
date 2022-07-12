import time
import random
from vk_api import VkUpload
from datetime import datetime
from modules.stats import Stats
from vk_api.utils import get_random_id

class MessageNew():
    def __init__(self, session, vk_session, vk, event):
        speech_dict = {
            "hello":{"question": "привет", "answer": "Пошол ты нахуй"},
            "thx":{"question": "спасибо", "answer": "Пошол ты нахуй"},
            "flat":{"question": "на флэте?", "answer": "НА ФЛЭТЕ НАХУУУУУЙ 🤙"},
            "rain":{"question": "ливня?", "answer": "Долбоеб"},
            "pray":{"question": "помолимся", "answer": "video67219698_456244596"},
            "understand?":{"question": "понимаешь?", "answer": "photo-73935802_457240008"},
            "understand":{"question": "понимаю", "answer": "photo-73935802_457240008"},
            "you":{"question": "ты", "answer": "Пидор"},
            "yes":{"question": "да", "answer": "Пизда"},
            "yes?":{"question": "да?", "answer": "Пизда"},
            "gn":{"question": "спок", "answer": "Спок!"},
            "aight":{"question": "ладно", "answer": "Шоколадно, бля"},
            "crazy":{"question": "ебанутый", "answer": "photo-73935802_457240009"},
            "popeye":{"question": "попаянный", "answer": "photo-73935802_457240009"},
            "su":{"question": "закрой рот", "answer": "Лан"},
            "stfu":{"question": "завали ебало", "answer": "Лан"}
        }

        support_dict = {
            "/статы - вывод сообщений за всё время",
            "/перешли + [изображение] - пересылка приложенного изображения"
        }

        #можно запилить функцию для рандомизации шанса ответа
        
        for key, value in speech_dict.items():
            if event.obj.message["text"].lower() == value["question"]:
                if random.randint(0, 3) == 1:
                    self.speech(value, vk, event)

        if event.obj.message["text"].lower() == "/перешли":
            if random.randint(0, 3) == 1:
                vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                            message="Пошёл нахуй!")

                time.sleep(3)

                vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                            message="Та лан)")
                self.forward(session, vk_session, vk, event)
            else:
                self.forward(session, vk_session, vk, event)

        if event.obj.message["text"].lower() == "/статы":
            self.stats(vk, event, vk_session)

        if event.obj.message['text'].lower() == '/помощь' or event.obj.message['text'].lower() == '/хелп':
            self.support(support_dict, vk, event)

    def speech(self, value, vk, event):
        if "video" in value["answer"] or "photo" in value["answer"]:
            message_attach = value["answer"]
            message_text = ""
        else:
            message_attach = ""
            message_text = value["answer"]

        vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                        message=message_text, attachment=message_attach)
    
    def forward(self, session, vk_session, vk, event):
        try:
            upload = VkUpload(vk_session)
            lastUrl = len(event.obj.message["attachments"][0]["photo"]["sizes"]) - 1
            sunLink = event.obj.message["attachments"][0]["photo"]["sizes"][lastUrl]["url"]
            image = session.get(sunLink, stream=True)
            photo = upload.photo_messages(photos=image.raw)[0]
            attachment = "photo{}_{}".format(photo["owner_id"], photo["id"])
                    
            vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"], 
                            message="Держи, брат", attachment=f"{attachment}")
        except IndexError:
            vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                            message="Прикрепи пикчу, опездал")
        except KeyError:
            vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                            message="Нахуй ты не пикчу прикрепил?")

    def stats(self, vk, event, vk_session):
        now = datetime.now()
        now = int(now.strftime("%d%m%Y"))
        
        count_raw = vk.messages.search(peer_id=event.obj.message["peer_id"], date=now, q="")

        #надо провести тесты и узнать, реальное ли это число сообщение
        count = (count_raw["count"])
        
        vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
            message="Колличество сообщений за всё время: {}".format(count))

        vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
            message="Щя подвезу более подробную стату")
        
        vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
            message="Настало время считать...")
        
        try:
            Stats(vk, event).main(vk, event, vk_session)
        except:
            vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.message["peer_id"],
                            message="Хуйня какая-то случилась, так шо статистика отменяется")

    def support(self, support_dict, vk, event):
        support_dict = "\n \n 🔵 ".join(support_dict)

        vk.messages.send(random_id=get_random_id(), chat_id=event.chat_id, peer_id=event.obj.peer_id,
                    message="ШО БОТЯРА МОЖЕ 🐗: \n \n 🔵 {}".format(support_dict))