import discord
import asyncio
import config
from discord.ext import commands
import os

intents = discord.Intents.all()
intents.message_content = True

#-------------------------ADDING IN APPLICATION ID
bot = commands.Bot(command_prefix='.', intents=intents, application_id=config.APP_ID)

@bot.event
async def on_ready():
    print('Online.')

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message[0] == '.':
        return
    if message.author == bot.user:
        return
    await message.channel.send("whats up!")

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

async def main():
    await load()
    await bot.start(config.TOKEN)

asyncio.run(main())
