import discord
import asyncio
import time

from discord.ext import commands, tasks


print("Attempting to start...")
token = ""
client = commands.Bot(command_prefix="-",self_bot=True)
client.remove_command("help")
async def status_task():
    while True:
        await client.change_presence(activity=discord.Streaming(name='X', url='https://www.twitch.tv/4xr'))
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X Y', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X Y Z', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X Y', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X', url='https://www.twitch.tv/4xr'))
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X Y', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X Y Z', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X Y', url='https://www.twitch.tv/4xr')) 
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Streaming(name='X', url='https://www.twitch.tv/4xr'))
        await asyncio.sleep(3)
@client.event
async def on_connect():
    print(f"Connected to => {client.user.name}")
    await status_task()




    
client.run(token, reconnect=True, bot=False)
