import discord
from discord import app_commands
from discord.ext import commands

class Survey(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Survey cog loaded.')

    @app_commands.command(name="survey", description="survey form")
    async def fillsurvey(self, interaction: discord.Interaction, name: str, age: int):
        await interaction.response.send_message(f"Name {name} Age {age}")


async def setup(bot):

    await bot.add_cog(Survey(bot), guilds=[discord.Object(id=997204563612401684)])
