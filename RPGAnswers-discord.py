import discord
import asyncio
import argparse
from configparser import SafeConfigParser
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
# Argument parsing.
parser = argparse.ArgumentParser(description='Welcome to RPGAnswers bot')
 
parser.add_argument('configFile', help='Config file for loading all parameters')
args = parser.parse_args()


# Using config file for parameters
parser = SafeConfigParser()
parser.read(args.configFile)

token = parser.get('token', 'discord_token')

client.run(token)
