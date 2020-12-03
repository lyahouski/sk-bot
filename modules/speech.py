def main(session, vk_session, longpoll, vk, random_id, event):
    
    speechDict = {
        'hello':{'question': 'привет', 'answer': 'Пошол ты нахуй'},
        'thx':{'question': 'спасибо', 'answer': 'Пошол ты нахуй'},
        'flat':{'question': 'на флэте?', 'answer': 'НА ФЛЭТЕ НАХУУУУУЙ 🤙'},
        'rain':{'question': 'ливня?', 'answer': 'Долбоеб'},
        'pray':{'question': 'помолимся', 'answer': 'video67219698_456244596'},
        'understand?':{'question': 'понимаешь?', 'answer': 'photo-73935802_457240008'},
        'understand':{'question': 'понимаю', 'answer': 'photo-73935802_457240008'},
        'you':{'question': 'ты', 'answer': 'Пидор'},
        'yes':{'question': 'да', 'answer': 'Пизда'},
        'yes?':{'question': 'да?', 'answer': 'Пизда'},
        'gn':{'question': 'спок', 'answer': 'Спок!'},
        'aight':{'question': 'ладно', 'answer': 'Шоколадно, бля'},
        'crazy':{'question': 'ебанутый', 'answer': 'photo-73935802_457240009'},
        'popeye':{'question': 'попаянный', 'answer': 'photo-73935802_457240009'},
        'su':{'question': 'закрой рот', 'answer': 'Лан'},
        'stfu':{'question': 'завали ебало', 'answer': 'Лан'}
    }

    for key, value in speechDict.items():

        if event.obj.text.lower() == value['question']:
                if value['answer'][0:5] == 'video' or value['answer'][0:5] == 'photo':
                    inputAttach = value['answer']
                    inputMessage = ''
                else:
                    inputAttach = ''
                    inputMessage = value['answer']

                vk.messages.send(
                    random_id=random_id,
                    peer_id=event.obj.peer_id,
                    chat_id=event.chat_id,
                    message=inputMessage,
                    attachment=inputAttach
                )