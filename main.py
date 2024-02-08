import telebot
from telebot import types
from datetime import datatime, timedelta
from random import shuffle

bot=telebot.TeleBot('6926034247:AAFzY2GSJZkNOSLdVXS1P7g9gtCHoilkRL4')

chats_list = {}
date_now= datatime.now()

def player_in_the_game(player_id):
    global chats_list
    for elements in chats_list:
        if player_id in chats_list[elements]['players']:
            return False
        else:
            return True
        