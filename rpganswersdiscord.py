import os
import discord
import asyncio
from botlogic import *

client = discord.Client()

def indent(level):
    indentation = ""

    for i in range(0, level):
        indentation += "-"

    return indentation

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author != client.user:
        response = processCommand(message.content)
        await send_message(message.channel, response)

async def send_message(channel, response):
    if isinstance(response, botresponse) == False:
        return

    text = response.header + "\n"
    for textLine in response.lines:
        if textLine.lineType== "normal":
            text += textLine.text + "\n"
        if textLine.lineType == "table":
            text += indent(textLine.indent) + "[" + textLine.text + "]" + "\n"
        if textLine.lineType == "attribute":
            text += indent(textLine.indent) + textLine.attribute + ": " + textLine.attributeValue + "\n"

    await client.send_message(channel, text)


# Main starts here

#token = str(os.environ["discord_token"])
token = "NTA3MjE0NzgwODEwMDAyNDYz.DvELVw.73AhPsiAKqghU9YCewGAV7LSLWQ"

client.run(token)
