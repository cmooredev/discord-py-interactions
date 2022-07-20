import discord
from discord.ext import commands

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)

    @discord.ui.button(label="Button",style=discord.ButtonStyle.gray)
    async def gray_button(self,interaction:discord.Interaction, button:discord.ui.Button,):
        print('inside button press')
        await interaction.response.send_message("Button clicked")

class Clickme(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Clickme cog loaded.')

    @commands.command()
    async def click(self, ctx):
        await ctx.send("This message has buttons!",view=Buttons())


async def setup(bot):
    await bot.add_cog(Clickme(bot))
