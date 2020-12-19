import discord
import asyncio
import time

from discord.ext import commands, tasks
token = ""
client = commands.Bot(command_prefix="-",self_bot=True)
client.remove_command("help")
async def status_task():
    while True:
        await client.change_presence(activity=discord.Streaming(name='lol', url='https://www.twitch.tv/4xr'))
        await asyncio.sleep(2)
        await client.change_presence(activity=discord.Streaming(name='fuck', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(2)
        await client.change_presence(activity=discord.Streaming(name='cord api', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(2)
@client.event
async def on_ready():
    print("rofl")
    await status_task()
try: 
    client.run(token, reconnect=True, bot=False)
except Exception:
    pass