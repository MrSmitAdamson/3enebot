# -*- coding: utf-8 -*-
import requests
import vk_api
import time
from vk_api.longpoll import VkLongPoll, VkEventType
import openpyxl
from openpyxl import load_workbook

#Service
import bot_timing
import bot_stop
import bot_commands
import bot_report
import bot_users_check

#Ex
import schedule
import dialog_flow

vk_session = vk_api.VkApi(token='02d23799d5fcd74ab5c28e8ca9b1d268dc43308b34d0918332da3316c60a5762bb467d4c9641a0fc0cdcd')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

today = bot_timing.get_weekday_func()

def message_send_func(event, vk):
    if bot_commands.excel_messages_func(event.text.lower()):  
        vk.messages.send( #commands
            user_id=event.user_id,
            message=eval(bot_commands.excel_commands_func(event.text.lower())),
            random_id = 0
                        )
        bot_report.message_reply_func(event.user_id, eval(bot_commands.excel_commands_func(event.text.lower())))    
    elif schedule.schedule_day(event.text.lower()):
        vk.messages.send( #schedule
            user_id=event.user_id,
            message=schedule.lessons_func(event.text.lower()),
            random_id = 0
                        )
        bot_report.message_reply_func(event.user_id, schedule.lessons_func(event.text.lower()))
    elif bot_commands.excel_messages_func(event.text.lower()) == False:
        dialog_flow.textMessage(event.user_id, event.text)
    else:
        bot_report.message_error_func(event.user_id, event.text)

def defined_message_func(user_id, message):
    vk.messages.send(
            user_id=user_id,
            message=message,
            random_id = 0
                        )
    bot_report.message_reply_func(user_id, message)


def new_user_func(event, vk):
    user_id = event.user_id
    if event.text == '1':
        bot_users_check.user_add(user_id, "1")
        defined_message_func(user_id, 'Вы успешно добавлены в группу №1.')
    elif event.text == '2':
        bot_users_check.user_add(user_id, "2")
        defined_message_func(user_id, 'Вы успешно добавлены в группу №2.')
    else:
        defined_message_func(user_id, f'Привет, {vk.users.get(user_id=user_id)[0]["first_name"]}! Напиши мне номер своей группы("1" или "2").')

    
