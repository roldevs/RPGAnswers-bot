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

	text = []
	
	text.append("Available commands")
	text.append("/rpglist [lang][system][table]: this command lists the available languages, the available systems per language, available tables inside the system and generates a random result from a table")
	text.append("/help: lists this menu")

	return text

def fillHeader(options):

    header = []
    if len(options) == 0:
        header.append("These are the available languages:")
    elif len(options) == 1:
        header.append("These are the available systems for language " + options[0] + ":")
    elif len(options) == 2:
        header.append("These are the available tables for language " + options[0] + " and system " + options[1] + ":")
    elif len(options) == 3:
        header.append("Generating results:")
    else:
        header.append("Incorrect number of parameters for /rpglist command.")
        header += helpRequest()

    return header 

def listFunction(url):
    
    r = requests.get(url = url)
    response = []
    
    try:
        data = r.json()
    
        if ("success" in data and data["success"] == True):
            response += toTextList(data)
        else:
            response.append("No available data.")
    
    except ValueError:
        response.append("Could not process your request.")

    return response

def genFunction(url):

    url = url.replace("/api/types/", "/api/random/")
    r = requests.get(url)
    response = []

    try:
        data = r.json()
        if ("success" in data and data["success"] == True):
            response = jsonToTextGen(data)
        else:
            response.append("No available data.")

    except ValueError:
        response.append("Could not process your request.")

    return response

def listRequest(msg):
    command = msg
    basicurl = "https://hall.herokuapp.com/api/types"

    arguments = command.replace("/rpglist", "")
    options = arguments.split(" ")
    options.pop(0)
    listOrGenerate = "list"

    header = fillHeader(options)

    if len(options) == 3:
        listOrGenerate = "generate"

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"

    response = []
    if listOrGenerate == "list":
        response = header + listFunction(url)
    elif listOrGenerate == "generate":
        response = header + genFunction(url)
    
    return response
