import os
import telepot
from telepot.loop import MessageLoop
import argparse
from configparser import SafeConfigParser
from botlogic import *


def sendData(msg, bot, data):
    if bot != None:
        content_type, chat_type, chat_id = telepot.glance(msg)
        bot.sendMessage(chat_id, data)

def handle(msg):

    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text' :
        response = processCommand(msg["text"])

    else:
        response = "error"

    sendData(msg, bot, response)


# Main starts here
token = str(os.environ["telegram_token"])
bot = telepot.Bot(token) # Bot is created from the telepot class
    
    
MessageLoop(bot, handle).run_as_thread()
    
while(1):
    pass
