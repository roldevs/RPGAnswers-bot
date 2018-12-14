import os
import discord
import asyncio
from response import getResponse

client = discord.Client()

async def sendData(channel, text):
  await client.send_message(channel, text)

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------')

@client.event
async def on_message(message):
  return if message.author == client.user:
  await sendData(message.channel, getResponse(message.content))

# Main starts here

token = str(os.environ["discord_token"])

client.run(token)
