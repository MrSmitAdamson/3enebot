# -*- coding: utf-8 -*-
import os
import sys
import requests
import vk_api
import bot_messages
import time
import bot_report
import bot_users_check

vk_session = vk_api.VkApi(token='02d23799d5fcd74ab5c28e8ca9b1d268dc43308b34d0918332da3316c60a5762bb467d4c9641a0fc0cdcd')

from vk_api.longpoll import VkLongPoll, VkEventType
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

bot_report.bot_started_message_func()
os.execl(sys.executable, sys.executable, * sys.argv)
try:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text and event.from_user:
            #Слушаем longpoll, если пришло сообщение то:			
            if bot_users_check.user_in_base_func(event.user_id):
                bot_report.message_get_func(event.user_id, event.text)
                bot_messages.message_send_func(event, vk)
            else:
                bot_report.message_get_func(event.user_id, event.text)
                bot_messages.new_user_func(event, vk)
except:
    os.execl(sys.executable, sys.executable, * sys.argv)

        

            
