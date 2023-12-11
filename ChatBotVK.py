import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import filter_words

class Bot:
    def __init__(self):
        self.token = "vk1.a.atdIug4lHrpR3PGpsny6nalpCoflacYRHzxDErMEWaAtWV8sz9yZd5PumEnlQtI-nceFVBDe1J6ULE0-t50S6vO_ylOspE_ieAuD-LulAsd9iGtwMg_ynwnYmEvgWXFSK3i4DHh4NS7dLQpmxf-E0gF1rZK528Ydv6p32eDMVraG5XK41bLsOAhVREa1bxovxSkQsC21rYhWQgpkVVSeVg"
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = None

    def setup_longpoll(self):
        if not self.longpoll:
            self.longpoll = VkLongPoll(self.vk)

    def run(self):
        self.setup_longpoll()
        print("Bot is running...")
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.process_message(event.user_id, event.text)

    def write_msg(self, user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

    def process_message(self, user_id, user_message):
        # print(user_message, filter_words.check_message(user_message))
        # обработка сообщений пользователя и ответы ему
        if filter_words.check_message(user_message):
            self.write_msg(user_id, "Данное сообщение содержит некорректные выражения!")
        elif user_message.lower() == "привет":
            self.write_msg(user_id, "Хай")
        elif user_message.lower() == "пока":
            self.write_msg(user_id, "Пока((")
        else:
            self.write_msg(user_id, "Не поняла вашего ответа...")