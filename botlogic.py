import requests
from jsonparsing import *

def processCommand(command):

    response = ""

    if command.startswith("/rpglist"):
        response = listRequest(command) 
    elif command.startswith("/help"):
        response = helpRequest()
    else:
        pass

    return response

def helpRequest():

	text = ""
	
	text += "Available commands" + "\n"
	text += "/rpglist [lang][system][table]: this command lists the available languages, the available systems per language, available tables inside the system and generates a random result from a table" + "\n"
	text += "/help: lists this menu" + "\n"

	return text

def listRequest(msg):
    command = msg
    basicurl = "https://hall.herokuapp.com/api/types"

    arguments = command.replace("/rpglist", "")
    options = arguments.split(" ")
    options.pop(0)
    listOrGenerate = ""

    checkError = False

    if len(options) == 0:
        header = "These are the available languages:\n"
        listOrGenerate = "list"
    elif len(options) == 1:
        header = "These are the available systems for language " + options[0] + ":\n"
        listOrGenerate = "list"
    elif len(options) == 2:
        header = "These are the available tables for language " + options[0] + " and system " + options[1] + ":\n"
        listOrGenerate = "list"
    elif len(options) == 3:
        header = "Generating results:\n"
        listOrGenerate = "generate"
    else:
        header = "Incorrect number of parameters for /rpglist command.\n"
        header += helpRequest()

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"

    if listOrGenerate == "list":
        r = requests.get(url = url)
    
        try:
            data = r.json()
    
            if ("success" in data and data["success"] == True):
                response = header + toTextList(data)
            else:
                response = header + "No available data."
    
        except ValueError:
            response = header + "Could not process your request."

    elif listOrGenerate == "generate":
        url = url.replace("/api/types/", "/api/random/")

        r = requests.get(url)

        try:
            data = r.json()
            if ("success" in data and data["success"] == True):
                response = header + jsonToTextGen(data)
            else:
                response = header + "No available data."

        except ValueError:
            response = header + "Could not process your request."
    
    return response
