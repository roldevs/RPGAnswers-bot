import json

def indent(level):
    indentation = ""

    for i in range(0, level):
        indentation += "-"

    return indentation

def toTextList(data):
    text = []

    for node in data["data"]:
        mynode = node.replace(".yml", "")
        text.append(mynode)

    return text


def jsonToTextGen(data):
    node = data["data"][0]

    text = []
    return formatJSON(text, node, None, 0)

def formatJSON(text, node, parent, level):
    #text = ""
    textLocal = []

    if "children" not in node:
        #text += indent(level) + node["title"] + ": " + node["text"] + "\n"
        text.append(indent(level) + node["title"] + ": " + node["text"])
    else:
        text.append(indent(level) + "[" + node["title"] + "]")
        for children in node["children"]:
            text += formatJSON([], children, node, level+1)

    return text

