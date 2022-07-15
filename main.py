import discord
import asyncio
import config
#--------- NEW LINE
from discord.ext import commands
import requests
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


#-------ADD
@bot.command()
async def facts(ctx, number):
    response = requests.get(f'http://numbersapi.com/{number}')
    await ctx.channel.send(response.text)

#finishes running this before starting the bot
#fill this with any other work you need to do in the background
#notice this prints before "Online"
#like loading cogs
async def setup():
    print('setting up bot..')

async def main():
    await setup()
    #await client.start(config.TOKEN)
    await bot.start(config.TOKEN)

asyncio.run(main())
