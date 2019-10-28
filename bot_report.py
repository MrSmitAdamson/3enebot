# -*- coding: utf-8 -*-
import requests
import vk_api
import time
import traceback

import bot_logging

vk_session = vk_api.VkApi(token='02d23799d5fcd74ab5c28e8ca9b1d268dc43308b34d0918332da3316c60a5762bb467d4c9641a0fc0cdcd')
vk = vk_session.get_api()

admin_list = {
    'admin_AIDAR'   :   '197427433',
    'admin_SADZIP'  :   '491258611',
    'admin_LINAR'   :   '108127462'
}

def bot_started_message_func():
    bot_logging.logger(f'{time.strftime("%X", time.localtime())}: Бот запущен.\n')
    for key, value in admin_list.items():
        vk.messages.send( #Бот запущен
                    user_id = str(value),
                    message = f'{time.strftime("%X", time.localtime())}: Бот запущен.',
                    random_id = '0'
                        )

def bot_stopped_message_func(admin):
    bot_logging.logger(f'{time.strftime("%X", time.localtime())}: Бот выключен пользователем ' + vk.users.get(user_id=admin)[0]['first_name'] + '.\n')
    for key, value in admin_list.items():
        vk.messages.send( 
                    user_id = str(value),
                    message = f'{time.strftime("%X", time.localtime())}: Бот выключен пользователем ' + vk.users.get(user_id=admin)[0]['first_name'] + '.',
                    random_id = '0'
                        )

def bot_restart_message_func():
    None
    bot_logging.logger(f'{time.strftime("%X", time.localtime())}: Перезагрузка бота.\n')
    for key, value in admin_list.items():
        vk.messages.send( 
                    user_id = str(value),
                    message = f'{time.strftime("%X", time.localtime())}: Перезагрузка бота.',
                    random_id = '0'
                        )

def message_get_func(user_id, mes_text):
    bot_logging.logger(f'{time.strftime("%X", time.localtime())}: {vk.users.get(user_id=user_id, name_case="gen")[0]["first_name"]}')
    bot_logging.logger(f'          {mes_text}\n')

def message_reply_func(user_id, reply_text):
    bot_logging.logger(f'{time.strftime("%X", time.localtime())}: Бот для {vk.users.get(user_id=user_id, name_case="gen")[0]["first_name"]}')
    bot_logging.logger(f'          {reply_text}\n')

def message_error_func(user_id, mes_text):
    bot_logging.logger(f'{time.strftime("%X", time.localtime())}: Ошибка в отправки или получении сообщения от {vk.users.get(user_id=user_id, name_case="gen")[0]["first_name"]}.')
    bot_logging.logger(f'Сообщение: {mes_text}\n')
    for key, value in admin_list.items():
        vk.messages.send(
                    user_id = str(value),
                    message = f'{time.strftime("%X", time.localtime())}: Ошибка в отправки или получении сообщения от {vk.users.get(user_id=user_id, name_case="gen")[0]["first_name"]}.\nСообщение: {mes_text}',
                    random_id = '0'
                        )

def mes2admin_func(user_id, mes_text):
    bot_logging.logger(mes_text)
    for key, value in admin_list.items():
        vk.messages.send(
                    user_id = str(value),
                    message = mes_text,
                    random_id = '0'
                        )

def bot_error_func():
    bot_logging.logger(f'{time.strftime("%X", time.localtime())}: Ошибка.\n{traceback.format_exc()}')
    for key, value in admin_list.items():
        vk.messages.send(
                    user_id = str(value),
                    message = f'{time.strftime("%X", time.localtime())}: Ошибка.\n{traceback.format_exc()}',
                    random_id = '0'
                        )
