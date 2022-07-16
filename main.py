import discord
import asyncio
import config
from discord.ext import commands
#--------- NEW LINE
import os
#---------

intents = discord.Intents.default()
intents.message_content = True
#----change this line
#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='.', intents=intents)


#event
#when bot is loaded and ready this will call

#change this from client to bot
#@client.event
@bot.event
async def on_ready():
    print('Online.')


#@client.event
@bot.event
async def on_message(message):
    #if message.author == client.user:
    await bot.process_commands(message)
    if message[0] == '.':
        return
    if message.author == bot.user:
        return
    await message.channel.send("whats up!")


#### delete all this, move to cog

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    #await client.start(config.TOKEN)
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())
