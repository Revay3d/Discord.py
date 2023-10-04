import discord
import interactions
from discord.ext import commands
from discord import app_commands



class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.color
   
    @app_commands.command(name="say",  description="dire lo que me pidas")
    async def say(self, interaction: discord.Interaction, mensaje: str):
       await interaction.response.send_message(mensaje)
       
        

async def setup(bot):

  await bot.add_cog(Say(bot))
