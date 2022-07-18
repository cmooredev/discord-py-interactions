import discord
from discord.ext import commands

class SurveyModal(discord.ui.Modal, title='Survey'):
    name = discord.ui.TextInput(label='Name')
    answer = discord.ui.TextInput(label='Reason for joining', style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message(f'Submission entered, {self.name}!', ephemeral=True)

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
        print(guild.id)

        ## update this
        if self.values[0] == "Blue":
            role = await guild.create_role(name="blue", colour=discord.Colour.blue())
        elif self.values[0] == "Red":
            role = await guild.create_role(name="Red", colour=discord.Colour.red())
        elif self.values[0] == "Green":
            role = await guild.create_role(name="Green", colour=discord.Colour.green())
        await user.edit(roles=[role])
        await interaction.response.send_modal(SurveyModal())

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 30):
        super().__init__(timeout=timeout)
        self.add_item(Select())


class Menu(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Menu cog loaded.')

    @commands.command()
    async def menu(self, ctx):
        await ctx.send("Pick a role",view=SelectView(), delete_after=15)

async def setup(bot):
    await bot.add_cog(Menu(bot))
