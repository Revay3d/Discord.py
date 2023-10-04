import discord
import interactions
from discord.ext import commands
from discord import app_commands

class Avatar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.color
   
    @app_commands.command(name="avatar", description="ver tu avatar o de otro miembro")
    async def avatar(self, interaction: discord.Interaction, miembro: discord.User = None):
        
        if miembro is None:
            miembro = interaction.user
        if not miembro.avatar:
            await interaction.response.send_message(f"Ups... parece que {miembro.name} no tiene un avatar custom", ephemeral=True)
        else:
            embed = discord.Embed(
                title=f"Avatar de {miembro.name}",
                color=self.color  # Aquí se usa self.color en lugar de Color
            )
            embed.set_image(url=miembro.avatar.url)
            embed.set_footer(text="Pedido por: "+interaction.user.name,
                             icon_url=interaction.user.avatar.url)

            await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Avatar(bot))
