import json

posting_desc = '/пост - вызов формы постинга в СК'

def main(session, 
    vk_session, 
    longpoll, 
    vk, 
    random_id, 
    event, 
    VkKeyboard, 
    VkKeyboardColor, 
    get_random_id, 
    VkBotLongPoll, 
    VkBotEventType):
    
    print('проверка')
    
    # Настройки для обоих клавиатур
    # settings = dict(one_time=False, inline=True)

    # # №1. Клавиатура с 3 кнопками: "показать всплывающее сообщение", "открыть URL" и изменить меню (свой собственный тип)
    # keyboard_1 = VkKeyboard(**settings)
    # # pop-up кнопка
    # keyboard_1.add_callback_button(
    #     label='Покажи pop-up сообщение', 
    #     color=VkKeyboardColor.SECONDARY, 
    #     payload={"type": "show_snackbar", "text": "Это исчезающее сообщение"})
    # keyboard_1.add_line()
    # # кнопка с URL
    # keyboard_1.add_callback_button(
    #     label='Откртыть Url', color=VkKeyboardColor.POSITIVE, 
    #     payload={"type": "open_link", "link": "https://vk.com/id126216417"})
    # keyboard_1.add_line()
    # # кнопка переключения на 2ое меню
    # keyboard_1.add_callback_button(
    #     label='Добавить красного ', 
    #     color=VkKeyboardColor.PRIMARY, 
    #     payload={"type": "my_own_100500_type_edit"})

    # # №2. Клавиатура с одной красной callback-кнопкой. Нажатие изменяет меню на предыдущее.
    # keyboard_2 = VkKeyboard(**settings)
    # # кнопка переключения назад, на 1ое меню.
    # keyboard_2.add_callback_button(
    #     'Назад', 
    #     color=VkKeyboardColor.NEGATIVE, 
    #     payload={"type": "my_own_100500_type_edit"})

    # print('шо хочешь')
    
    # f_toggle: bool = False
    # for event in longpoll.listen():
    #     # отправляем меню 1го вида на любое текстовое сообщение от пользователя
    #     if event.type == VkBotEventType.MESSAGE_NEW:
    #         if event.obj.message['/пост'] != '':
    #             if event.from_user:
    #                 # Если клиент пользователя не поддерживает callback-кнопки,
    #                 # нажатие на них будет отправлять текстовые
    #                 # сообщения. Т.е. они будут работать как обычные inline кнопки.
    #                 if 'callback' not in event.obj.client_info['button_actions']:
    #                     print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')

    #                 vk.messages.send(
    #                         user_id=event.obj.message['from_id'],
    #                         random_id=get_random_id(),
    #                         peer_id=event.obj.message['from_id'],
    #                         keyboard=keyboard_1.get_keyboard(),
    #                         message=event.obj.message['text'])
    #     # обрабатываем клики по callback кнопкам
    #     elif event.type == VkBotEventType.MESSAGE_EVENT:
    #         # если это одно из 3х встроенных действий:
    #         if event.object.payload.get('type') in CALLBACK_TYPES:
    #             # отправляем серверу указания как какую из кнопок обработать. Это заложено в 
    #             # payload каждой callback-кнопки при ее создании.
    #             # Но можно сделать иначе: в payload положить свои собственные
    #             # идентификаторы кнопок, а здесь по ним определить
    #             # какой запрос надо послать. Реализован первый вариант.
    #             r = vk.messages.sendMessageEventAnswer(
    #                     event_id=event.object.event_id,
    #                     user_id=event.object.user_id,
    #                     peer_id=event.object.peer_id,                                                   
    #                     event_data=json.dumps(event.object.payload))
    #         # если это наша "кастомная" (т.е. без встроенного действия) кнопка, то мы можем
    #         # выполнить edit сообщения и изменить его меню. Но при желании мы могли бы
    #         # на этот клик открыть ссылку/приложение или показать pop-up. (см.анимацию ниже)
    #         elif event.object.payload.get('type') == 'my_own_100500_type_edit':
    #             last_id = vk.messages.edit(
    #                     peer_id=event.obj.peer_id,
    #                     message='ola',
    #                     conversation_message_id=event.obj.conversation_message_id,
    #                     keyboard=(keyboard_1 if f_toggle else keyboard_2).get_keyboard())
    #             f_toggle = not f_toggle

    # if __name__ == '__main__':
    #     print()