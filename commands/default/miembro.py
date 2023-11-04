import discord
import interactions
from discord.ext import commands
from discord import app_commands

class Miembro(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.color
   
    @app_commands.command(name="miembro", description="informacion de algun miembro")
    async def miembro(self, interaction: discord.Interaction, miembro: discord.User = None):
        if miembro is None:
            miembro = interaction.user
        roles = [role.name for role in miembro.roles]
        embed = discord.Embed(
            title=f"Informacion de {miembro.name}",
            description=f"> 👑 Nombre: {miembro.name}\n> 🎈 ID:{miembro.id}\n> 📜 Mencion: {miembro.mention}\n> Creado: {miembro.created_at.strftime('%d/%B/%Y')}\n> Se unio: {miembro.joined_at.strftime('%d/%B/%Y')}\n> 💎 Roles: ```{', '.join(roles)}```",
            color=self.color  
        )
        if miembro.avatar:
            embed.set_thumbnail(url=miembro.avatar.url)
        embed.set_footer(text="Pedido por: "+interaction.user.name,
                         icon_url=interaction.user.avatar.url)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(Miembro(bot))
