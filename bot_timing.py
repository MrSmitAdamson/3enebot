# -*- coding: utf-8 -*-
import requests
import bs4

import datetime
import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

def get_weekday_func():
    today = datetime.datetime.today().strftime("%A")
    return (today.lower())

def get_time_func():
    hours = datetime.datetime.today().hour
    minutes = datetime.datetime.today().minute
    return(f'{hours}:{minutes}')