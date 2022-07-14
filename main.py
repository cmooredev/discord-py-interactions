import discord
import asyncio
import config

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


#event 
#when bot is loaded and ready this will call
@client.event
async def on_ready():
    print('Online.')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send("whats up!")

#finishes running this before starting the bot
#fill this with any other work you need to do in the background
#notice this prints before "Online"
#like loading cogs
async def setup():
    print('setting up bot..')

async def main():
    await setup()
    await client.start(config.TOKEN)

asyncio.run(main())