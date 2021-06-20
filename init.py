#!/usr/bin/env python3

import os
import sys
import discord
import keyring
import random

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

# Disable output buffering
PYTHONUNBUFFERED = 1

# Discord bot configuration magic
intents = discord.Intents.default()
client = discord.Client(intents=intents)
service_id='QUOTE_BOT'
TOKEN=keyring.get_password(service_id, service_id)

# On message arrival, test to see if it's one we care about.
@client.event
async def on_message(message):
    guild = message.guild
    if message.author == client.user:
        return
    if message.content.startswith('!quote'):
        await message.channel.send(random_line('quotes.txt'))

client.run(TOKEN)
