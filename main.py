import telebot
from telebot import types
from datetime import datetime, timedelta
from random import shuffle

bot=telebot.TeleBot('6926034247:AAFzY2GSJZkNOSLdVXS1P7g9gtCHoilkRL4')

chats_list = {}
date_now= datetime.now()

def player_in_the_game(player_id):
    global chats_list
    for elements in chats_list:
        if player_id in chats_list[elements]['players']:
            return False
        else:
            return True
def role(player_id, player_dict, new_role, text):
    player_dict[player_id].update({'role': new_role})
    bot.send_message(player_id,text)
def btn_names(player_dict, game_id, player_role, text):
    chat_id=''
    players_btn=types.InlineKeyboardMarkup()
    for key, val in player_dict.items():
        if val['role']!=player_role:
            chat_id=key
    message_id=bot.send_mwssage(chat_id,text,reply_markup=players_btn)
    return message_id.message_id
def checking_selection(chat_id, chat, player_role):
    if not chat[player_role]:
        bot.edit_message_text(chat_id=chat_id, message_id=chat[f'{player_role[0]}List_id'],
                              text='Время выбора истекло...', reply_markup=None)
        chat.update({player_role: True})
def timer(chat_id, sec):
    global chats_list, time_now
    chat_list[chat_id].update({'time_interval': datetime.now()+timedelta(second=sec)})
    while chats_list[chat_id]['time_interval']>time.now:
        time_now=datetime.now()
        