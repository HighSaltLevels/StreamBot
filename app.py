#!/usr/bin/env python3

import os
import traceback
import discord
from lib import msg_parser
from lib import email

client = discord.Client()
BOT_TOKEN = os.getenv('BOT_TOKEN')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Nothing Right Now"))
    print('Launching StreamBot')

@client.event
async def on_message(msg):
    if msg.author != client.user:
        response = await msg_parser.parse_message(client, msg)
        await client.send_message(msg.channel, response)

try:
    client.run(BOT_TOKEN)
except Exception:
    email.send_failure(EMAIL_PASSWORD, traceback.format_exc())
