import discord
import subprocess
import time

addr = ""
# addr = input()

def wol():
    subprocess.call(["wakeonlan", str(addr)], shell=False)  

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!start!':
        wol()
        time.sleep(1)

client.run("")
