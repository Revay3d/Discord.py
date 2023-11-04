import discord
import interactions
from discord.ext import commands
from discord import app_commands



class myCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.color
   
    @app_commands.command(name="ping", description="comando de prueba")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.bot.latency * 1000)
        embed = discord.Embed(title=f"Ping", description=f"Pong! {bot_latency} ms.", color=self.color)
        if self.bot.user.avatar:
         embed.set_thumbnail(url=self.bot.user.avatar.url)
         embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        await interaction.response.send_message(embed=embed)


async def setup(bot):

 await bot.add_cog(myCog(bot))
