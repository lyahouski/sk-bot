import random
from vk_api.utils import get_random_id

class MessageTyping():
    def __init__(self, vk, event):
        if random.randint(0, 1) == 1:
            message_id = vk.messages.send(random_id=get_random_id(), peer_id=event.obj["from_id"],
                                        message="Чьмоха пишет сообщение :)")

            vk.messages.delete(message_ids=message_id, peer_id=event.obj["from_id"], delete_for_all=1)