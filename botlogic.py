import requests
from jsonparsing import *

def processCommand(command):

    response = ""

    if command.startswith("/rpglist"):
        response = listRequest(command) 
    elif command.startswith("/rpggen"):
        response = genRequest(command)
    elif command.startswith("/help"):
        response = helpRequest()
    else:
        pass

    return response

def helpRequest():

	text = ""
	
	text += "Available commands" + "\n"
	text += "/rpglist [lang][system]: this command lists the available languages, the available systems per language and the available random tables per systme" + "\n"
	text += "/rpggen [lang][system][table]: this command generates a result from the defined language, system and table" + "\n"
	text += "/help: lists this menu" + "\n"

	return text

def listRequest(msg):
    command = msg
    basicurl = "https://hall.herokuapp.com/api/types"

    arguments = command.replace("/rpglist", "")
    options = arguments.split(" ")
    options.pop(0)

    checkError = False

    if len(options) == 0:
        header = "These are the available languages:\n"
    elif len(options) == 1:
        header = "These are the available systems for language " + options[0] + ":\n"
    elif len(options) == 2:
        header = "These are the available tables for language " + options[0] + " and system " + options[1] + ":\n"
    elif len(options) == 3:
        header = "Incorrect number of parameters for /rpglist command. Are you trying to generate a result from a table? \nUse /rpggen command instead\n"
        header += helpRequest()
    else:
        header = "Incorrect number of parameters for /rpglist command.\n"
        header += helpRequest()

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"

    r = requests.get(url = url)

    try:
        data = r.json()

        text = ""

        if ("succes" in data and data["succes"] == True) or ("success" in data and data["success"] == True):
            response = header + toTextList(data)
        else:
            response = header + "No available data."

    except ValueError:
        response = header + "Could not process your request."

    return response

def genRequest(msg):
    command = msg
    basicurl = "https://hall.herokuapp.com/api/random"

    arguments = command.replace("/rpggen", "")
    options = arguments.split(" ")
    options.pop(0)

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"
    r = requests.get(url)

    data = r.json()
    text = jsonToTextGen(data)
    
    return text 
