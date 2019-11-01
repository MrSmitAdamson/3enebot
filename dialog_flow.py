import vk_api,requests, apiai, json

vk_session = vk_api.VkApi(token='02d23799d5fcd74ab5c28e8ca9b1d268dc43308b34d0918332da3316c60a5762bb467d4c9641a0fc0cdcd')
vk = vk_session.get_api()

def textMessage(user, message):

    request = apiai.ApiAI('59c410806436481bb2a4bde9c435dd62').text_request() # Токен API к Dialogflow
    request.lang = 'ru' # На каком языке будет послан запрос
    request.session_id = '3ENEBot' # ID Сессии диалога (нужно, чтобы потом учить бота)
    request.query = message # Посылаем запрос к ИИ с сообщением от юзера
    responseJson = json.loads(request.getresponse().read().decode('utf-8'))
    response = responseJson['result']['fulfillment']['speech'] # Разбираем JSON и вытаскиваем ответ
    # Если есть ответ от бота - присылаем юзеру, если нет - бот его не понял

    if response:
        vk.messages.send(  # none
            user_id=user,
            message=response,
            random_id=0
        )

    else:
        vk.messages.send(  # none
            user_id=user,
            message='Не понял команду',
            random_id=0
        )
