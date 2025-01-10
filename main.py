import discord
from discord.ext import commands
import config
import re
import asyncio
import random
from threading import Timer



# Set the command prefix for your selfbot
bot = commands.Bot(command_prefix="!", self_bot=True)
sleeping=config.sleep


async def spam():
    while sleeping==False:
        channel = bot.get_channel(config.SpamId)
        result = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=13))
        await channel.send(result)
        random_interval = random.uniform(1, 4)  # Random interval between 1 second and 5 seconds
        await asyncio.sleep(random_interval)



@bot.event
async def on_ready():
    print(f'\033[91mLOGGED IN AS {bot.user.name} ({bot.user.id})\033[0m')
    print(f'\033[91mSERVER STATUS: ONLINE\033[0m')
    print(f'\033[91mMade by amansingh903\033[0m')
    print(f'\033[91m------------------------------------------------------------------------------------------\033[0m')
    #spam function
    if config.SpamId:
        await spam()
        

bot.run(config.token)
