import discord
from discord.ext import commands


class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Blue",emoji="🟦",description="Team Blue"),
            discord.SelectOption(label="Red",emoji="🟥",description="Team Red"),
            discord.SelectOption(label="Green",emoji="🟩",description="Team Green")
            ]
        super().__init__(placeholder="Choose your team",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        user = interaction.user
        guild = interaction.guild
        if self.values[0] == "Blue":
            role = await guild.create_role(name="blue", colour=discord.Colour.blue())
            await user.edit(roles=[role])
            await interaction.response.send_message("Team Blue",ephemeral=True)
        elif self.values[0] == "Red":
            role = await guild.create_role(name="Red", colour=discord.Colour.red())
            await user.edit(roles=[role])
            await interaction.response.send_message("Team Red",ephemeral=True)
        elif self.values[0] == "Green":
            role = await guild.create_role(name="Green", colour=discord.Colour.green())
            await user.edit(roles=[role])
            await interaction.response.send_message("Third Green",ephemeral=False)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 30):
        super().__init__(timeout=timeout)
        self.add_item(Select())


class Menu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self, ctx):
        await ctx.send("Pick a role",view=SelectView(), delete_after=15)

async def setup(bot):
    await bot.add_cog(Menu(bot))
