import apiai, json
from google.cloud import dialogflow
#from google.cloud import storage

def model_answer(message, sessionid):
    request = apiai.ApiAI('AIzaSyDMZez19LuYN4aBSoeyuSkcWKot2DZu_4I').text_request()  # Токен API к Dialogflow
    request.lang = 'ru'  # На каком языке будет послан запрос
    request.session_id = 'HelperOfHead' #sessionid  # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message  # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    print(responseJson)#, responseJson['result']['fulfillment']['speech'])
    response = responseJson#['result']#['fulfillment']['speech']  # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял
    if response:
        return response
    else:
        return 'Я Вас не совсем понял!'

#
# def authenticate_implicit_with_adc(project_id="helperofhead-mldt"):
#     """
#     When interacting with Google Cloud Client libraries, the library can auto-detect the
#     credentials to use.
#
#     // to do Developer:
#     //  1. Before running this sample,
#     //  set up ADC as described in https://cloud.google.com/docs/authentication/external/set-up-adc
#     //  2. Replace the project variable.
#     //  3. Make sure that the user account or service account that you are using
#     //  has the required permissions. For this sample, you must have "storage.buckets.list".
#     Args:
#         project_id: The project id of your Google Cloud project.
#     """
#
#     # This snippet demonstrates how to list buckets.
#     # *NOTE*: Replace the client created below with the client required for your application.
#     # Note that the credentials are not specified when constructing the client.
#     # Hence, the client library will look for credentials using ADC.
#     storage_client = storage.Client(project=project_id)
#     buckets = storage_client.list_buckets()
#     print("Buckets:")
#     for bucket in buckets:
#         print(bucket.name)
#     print("Listed all storage buckets.")
#
# def detect_intent_texts(project_id, session_id, texts, language_code):
#     """Returns the result of detect intent with texts as inputs.
#
#     Using the same `session_id` between requests allows continuation
#     of the conversation."""
#     # from google.cloud import dialogflow
#
#     session_client = dialogflow.SessionsClient()
#
#     session = session_client.session_path(project_id, session_id)
#     print("Session path: {}\n".format(session))
#
#     for text in texts:
#         text_input = dialogflow.TextInput(text=text, language_code=language_code)
#
#         query_input = dialogflow.QueryInput(text=text_input)
#
#         response = session_client.detect_intent(
#             request={"session": session, "query_input": query_input}
#         )
#
#         print("=" * 20)
#         print("Query text: {}".format(response.query_result.query_text))
#         print(
#             "Detected intent: {} (confidence: {})\n".format(
#                 response.query_result.intent.display_name,
#                 response.query_result.intent_detection_confidence,
#             )
#         )
#         print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
#         return response