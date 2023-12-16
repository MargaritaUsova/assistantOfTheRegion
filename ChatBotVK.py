import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from google.cloud import dialogflow_v2beta1 as dialogflow
import filter_words
import model
from google.auth import exceptions, default
from google.protobuf.json_format import MessageToJson
# from google.protobuf.struct_pb2 import Struct, Value
import os
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/margaritausova/Downloads/helperofhead-mldt-487b9b9e45ec.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\belkalia\Downloads\helperofhead-mldt-487b9b9e45ec.json"


class Bot:
    def __init__(self):
        self.token = "vk1.a.atdIug4lHrpR3PGpsny6nalpCoflacYRHzxDErMEWaAtWV8sz9yZd5PumEnlQtI-nceFVBDe1J6ULE0-t50S6vO_ylOspE_ieAuD-LulAsd9iGtwMg_ynwnYmEvgWXFSK3i4DHh4NS7dLQpmxf-E0gF1rZK528Ydv6p32eDMVraG5XK41bLsOAhVREa1bxovxSkQsC21rYhWQgpkVVSeVg"
        self.vk = vk_api.VkApi(token=self.token)
        self.longpoll = None
        self.PROJECT_ID = "helperofhead-mldt"

    def setup_longpoll(self):
        if not self.longpoll:
            self.longpoll = VkLongPoll(self.vk)

    def run(self):
        self.setup_longpoll()
        print("Бот запущен")
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.process_message(event.user_id, event.text)

    def write_msg(self, user_id, message):
        self.vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

    def process_message(self, user_id, user_message):
        projectid = 'helperofhead-mldt'
        sessionid = f'vk-{user_id}'
        languagecode = 'ru-RU'
        try:
            credentials, project = default()
        except exceptions.DefaultCredentialsError:
            print("Could not find default credentials.")
            return
        client = dialogflow.SessionsClient()
        session = client.session_path(projectid, sessionid)

        # обработка сообщений пользователя и ответы ему
        text = user_message
        textinput = dialogflow.types.TextInput(text=text, language_code=languagecode)  # Set the language code
        queryinput = dialogflow.types.QueryInput(text=textinput)
        response = client.detect_intent(session=session, query_input=queryinput)

        # Отправка ответа от Dialogflow пользователю в ВКонтакте
        self.write_msg(user_id, response.query_result.fulfillment_text)
