import os
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
import argparse
from configparser import SafeConfigParser
from botlogic import *


def sendData(msg, bot, data):
    if bot != None:
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id, data)

#def on_chat_message(msg):
#    content_type, chat_type, chat_id = telepot.glance(msg)
#
#    keyboard = InlineKeyboardMarkup(inline_keyboard=[
#                   [InlineKeyboardButton(text='Press me', callback_data='Nada que ver')],
#               ])
#
#    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

#def handle(msg):
def on_chat_message(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text' :
        response = processCommand(msg["text"])

    else:
        response = "error"

    sendData(msg, bot, response)


# Main starts here
token = str(os.environ["telegram_token"])
bot = telepot.Bot(token) # Bot is created from the telepot class
    
MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()
    
while(1):
    pass
