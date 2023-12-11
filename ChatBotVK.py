import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

class Bot:
    def __int__(self):
        self.token = token = "vk1.a.atdIug4lHrpR3PGpsny6nalpCoflacYRHzxDErMEWaAtWV8sz9yZd5PumEnlQtI-nceFVBDe1J6ULE0-t50S6vO_ylOspE_ieAuD-LulAsd9iGtwMg_ynwnYmEvgWXFSK3i4DHh4NS7dLQpmxf-E0gF1rZK528Ydv6p32eDMVraG5XK41bLsOAhVREa1bxovxSkQsC21rYhWQgpkVVSeVg"
        self.vk = vk = vk_api.VkApi(token=self.token)
        self.longpoll = VkLongPoll(vk)


    def write_msg(self, user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message})



# читаем сообщения от пользователей
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        usersMessage = event.text

        #обработка сообщений пользователя и ответы ему
        if usersMessage == "привет":
            write_msg(event.user_id, "Хай")
        elif usersMessage == "пока":
            write_msg(event.user_id, "Пока((")
        else:
            write_msg(event.user_id, "Не поняла вашего ответа...")
