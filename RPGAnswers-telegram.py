import telepot
from telepot.loop import MessageLoop
import argparse
from configparser import SafeConfigParser
from botlogic import *

def sendData(msg, bot, data):
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
# Argument parsing.
parser = argparse.ArgumentParser(description='Welcome to RPGAnswers bot')
 
parser.add_argument('configFile', help='Config file for loading all parameters')
args = parser.parse_args()


# Using config file for parameters
parser = SafeConfigParser()
parser.read(args.configFile)

token = parser.get('token', 'telegram_token')

bot = telepot.Bot(token) # Bot is created from the telepot class


MessageLoop(bot, handle).run_as_thread()

while(1):
    pass
