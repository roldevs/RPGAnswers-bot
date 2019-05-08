import requests
from jsonparsing import *
from botresponse import *

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

    response = botresponse()
	
    response.setHeader("Available commands:")
    line = botline()
    line2 = botline()
    line.lineType = "normal"
    line2.lineType = "normal"

    line.text="/rpglist [lang][system][table]: this command lists the available languages, the available systems per language, available tables inside the system and generates a random result from a table"
    line2.text="/help: lists this menu"

    response.addLine(line)
    response.addLine(line2)

    return response

def fillHeader(options):
    header = ""

    if len(options) == 0:
        header = "These are the available languages:"
    elif len(options) == 1:
        header = "These are the available systems for language " + options[0] + ":"
    elif len(options) == 2:
        header = "These are the available tables for language " + options[0] + " and system " + options[1] + ":"
    elif len(options) == 3:
        header = "Generating results:"
    else:
        header = "Incorrect number of parameters for /rpglist command."
        #header += helpRequest()

    return header 

def listFunction(url):
    
    r = requests.get(url = url)
    lines = []
    
    try:
        data = r.json()
    
        if ("success" in data and data["success"] == True):
            lines = toTextList(data)
        else:
            line = botline()
            line.lineType = "normal"
            line.text = "No available data"
            lines.append(line)
    
    except ValueError:
            line = botline()
            line.lineType = "normal"
            line.text = "Could not process your request"
            lines.append(line)

    return lines

def genFunction(url):

    url = url.replace("/api/types/", "/api/random/")
    r = requests.get(url)
    lines = []

    try:
        data = r.json()
        if ("success" in data and data["success"] == True):
            lines = jsonToTextGen(data)
        else:
            line = botline()
            line.lineType = "normal"
            line.text = "No available data."
            lines.append(line)

    except ValueError:
        line = botline()
        line.lineType = "normal"
        line.text = "Could not process your request."
        lines.append(line)

    return lines

def listRequest(msg):
    command = msg
    basicurl = "https://hall.herokuapp.com/api/types"

    arguments = command.replace("/rpglist", "")
    options = arguments.split(" ")
    options.pop(0)
    listOrGenerate = "list"

    response = botresponse()
    response.header = fillHeader(options)

    if len(options) == 3:
        listOrGenerate = "generate"

    for parameter in options:
        basicurl+="/" + parameter

    url = basicurl + ".json"

    if listOrGenerate == "list":
        response.lines = listFunction(url)
        response.setQuery(msg)
    elif listOrGenerate == "generate":
        response.lines = genFunction(url)
    
    return response
