import discord
from discord import app_commands
from discord.ext import commands
from .menu import SurveyModal

class Survey(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Survey cog loaded.')

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)

        await ctx.send(
          f"Synced {len(fmt)} commands to the current guild."
        )
        return

    @commands.command()
    async def unsync(self, ctx) -> None:
        ctx.bot.tree.clear_commands(guild=ctx.guild)
        fmt = await ctx.bot.tree.sync(guild=ctx.guild)
        await ctx.send(
          f"Unsynced {len(fmt)} commands to the current guild."
        )
        return

    @app_commands.command(name="fillsurvey", description="survey form")
    async def fillsurvey(self, interaction: discord.Interaction, name: str, age: int):
        await interaction.response.send_modal(SurveyModal())

async def setup(bot):
    await bot.add_cog(Survey(bot), guilds=[discord.Object(id=997204563612401684)])
