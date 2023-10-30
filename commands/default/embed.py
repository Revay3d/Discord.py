import discord
import interactions
from discord.ext import commands
from discord import app_commands



class Embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.color
   
    @app_commands.command(name="embed", description="dire lo que quieras en embeds")
    async def embed(self, interaction: discord.Interaction,  titulo: str, descripcion: str):
        embed = discord.Embed(title=titulo,
                              description=descripcion, color=self.color)
        if interaction.user.avatar:
         embed.set_thumbnail(url=interaction.user.avatar.url)
         embed.set_footer(text=interaction.user.name,
                         icon_url=interaction.user.avatar.url)
        await interaction.response.send_message("El anuncio ya esta listo", ephemeral=True)
        await interaction.channel.send(embed=embed)

        


async def setup(bot):

 await bot.add_cog(Embed(bot))
