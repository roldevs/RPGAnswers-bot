import json

def indent(level):
    indentation = ""

    for i in range(0, level):
        indentation += "-"

    return indentation

def toTextList(data):
    text = ""

    for element in data["data"]:
        myelement = element.replace(".yml", "")
        text = text + myelement + "\n"

    return text


def jsonToTextGen(data):
    element = data["data"][0]

    return formatJSON(element, None, 0)

def formatJSON(element, parent, level):
    text = ""
    for key, value in element.items():
        if key == "text":
            if level < 1:
                text += value + "\n"
            else:
                text += indent(level) + parent["text"] + ": " + value + "\n"

        elif key == "related":
            for key2, value2 in value.items():
                text += formatJSON(value2["results"][0], value2, level+1)

    return text

