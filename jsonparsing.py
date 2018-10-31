import json

def indent(level):
    indentation = ""

    for i in range(0, level):
        indentation += "-"

    return indentation

def toTextList(data):
    text = ""

    for node in data["data"]:
        mynode = node.replace(".yml", "")
        text = text + mynode + "\n"

    return text


def jsonToTextGen(data):
    node = data["data"][0]

    return formatJSON(node, None, 0)

def formatJSON(node, parent, level):
    text = ""

    if "children" not in node:
        text += indent(level) + node["title"] + ": " + node["text"] + "\n"
    else:
        text += indent(level) + "[" + node["title"] + "]" + "\n"
        for children in node["children"]:
            text += formatJSON(children, node, level+1)

    return text

