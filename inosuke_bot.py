#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Discord notification bot created by Elliot "Li" Bearden
# June 22nd, 2020
# Updated Aug. 14th, 2020


import discord
from datetime import datetime
import time
import asyncio
import getpass


# Prompting for  bot token and channel ID
TOKEN = getpass.getpass(prompt="Enter bot token")
channel_id = getpass.getpass(prompt="Enter channel ID")

# Time parameter assignment
right_now = datetime.now()
start_time = datetime.strptime('2020-08-14 23:00:00', "%Y-%m-%d %H:%M:%S")
right_now_timestamp = datetime.timestamp(right_now)
start_timestamp = datetime.timestamp(start_time)

# Discord client initiation
client = discord.Client()


@client.event
async def periodic():
    print("running...")
    while True:
        await client.wait_until_ready()
        channel = client.get_channel(int(channel_id))
        await channel.send("@here Code Junkies, assemble! ᕦ(ò_óˇ)ᕤ")
        await asyncio.sleep(86390)


while True:
    print("Sleeping... (∪｡∪)｡｡｡zzz")
    time.sleep(45)
    if right_now_timestamp < start_timestamp:
        right_now = datetime.now()
        right_now_timestamp = datetime.timestamp(right_now)
    elif right_now_timestamp == start_timestamp:
        client.loop.create_task(periodic())
        client.run(TOKEN)
    else:
        pass