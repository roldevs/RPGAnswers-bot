import os
import discord
import asyncio
from botlogic import *

client = discord.Client()

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

async def send_message(channel, message):
    await client.send_message(channel, message)

# Main starts here

token = str(os.environ["discord_token"])

client.run(token)
