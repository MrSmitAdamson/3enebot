# -*- coding: utf-8 -*-
import requests
import vk_api
import time

vk_session = vk_api.VkApi(token='02d23799d5fcd74ab5c28e8ca9b1d268dc43308b34d0918332da3316c60a5762bb467d4c9641a0fc0cdcd')
vk = vk_session.get_api()

admin_list = {
    'admin_AIDAR'   :   '197427433',
    'admin_SADZIP'  :   '491258611',
    'admin_LINAR'   :   '108127462'
}

def bot_started_message_func():
    print(f'Бот запущен в {time.strftime("%X", time.localtime())}')
    for key, value in admin_list.items():
        vk.messages.send( #Бот запущен
                    user_id = str(value),
                    message = f'Бот запущен в {time.strftime("%X", time.localtime())}',
                    random_id = '0'
                        )

def bot_stopped_message_func(admin):
    print(f'Бот выключен  в {time.strftime("%X", time.localtime())} пользователем ' + vk.users.get(user_id=admin)[0]['first_name'])
    for key, value in admin_list.items():
        vk.messages.send( #Бот выключен
                    user_id = str(value),
                    message = f'Бот выключен  в {time.strftime("%X", time.localtime())} пользователем ' + vk.users.get(user_id=admin)[0]['first_name'],
                    random_id = '0'
                        )

def message_get_func(user_id, mes_text):
    print(f'Пришло сообщение от {vk.users.get(user_id=user_id, name_case="gen")[0]["first_name"]}: {mes_text}')

def message_reply_func(user_id, reply_text):
    print(f'Ответ для {vk.users.get(user_id=user_id, name_case="gen")[0]["first_name"]}: {reply_text}')

def mes2admin_func(user_id, mes_text):
    print(mes_text)
    for key, value in admin_list.items():
        vk.messages.send( #Бот выключен
                    user_id = str(value),
                    message = mes_text,
                    random_id = '0'
                        )
