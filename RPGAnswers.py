import telepot
from telepot.loop import MessageLoop
import argparse
from configparser import SafeConfigParser
import requests
import json

def listRequest(msg):
    command = msg['text']
    basicurl = "https://hall.herokuapp.com/api/types"

    arguments = command.replace("/list", "")
    options = arguments.split(" ")
    options.pop(0)

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"

    if len(options) == 3:
        url = url.replace("/api/types/", "/api/random/")

    r = requests.get(url = url)
    data = r.json()

    sendData(msg, bot, data)

def formatTable(data):
    
    text = ""

    if type(data) == dict:
        pos = 0
        listForm = list(data.keys())

        for key, value in data.items():
            if key == "text":
                if pos + 1 < len(data) and (listForm[pos+1] == ("search" or "related")):
                    text = text + "Buscando: " + value + "\n"
                else:
                    text = text + value + "\n"
            else:
                text = text + str(formatTable(value))

            pos+=1

    if type(data) == list:
        for i in data:
            text = text + str(formatTable(i))

    return text

def genRequest(msg):
    command = msg['text']
    basicurl = "https://hall.herokuapp.com/api/random"

    arguments = command.replace("/gen", "")
    options = arguments.split(" ")
    options.pop(0)

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"
    r = requests.get(url)

    data = r.json()
    text = formatTable(data)
    
    sendData(msg, bot, text)

def sendData(msg, bot, data):
    content_type, chat_type, chat_id = telepot.glance(msg)
    bot.sendMessage(chat_id, data)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text' :
        if msg['text'].startswith("/list"):
           listRequest(msg) 
        if msg['text'].startswith("/gen"):
           genRequest(msg) 


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
