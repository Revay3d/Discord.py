from discord.ext import commands
import discord

class On_member_remove(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.despedidas = bot.despedidas

    @commands.Cog.listener()
    async def on_member_remove(self, member):  # Añade 'self' aquí
        channel = self.bot.get_channel(self.despedidas)
        if channel is not None:
            embed = discord.Embed(title="Despedidas", description=f"""👋 ¡Adiós {member.name}! 

Hasta pronto, ¡cuídate mucho! 😊 """, color=self.bot.color)  # Usa self.bot.color aquí
            if member.avatar:
                embed.set_thumbnail(url=member.avatar.url)
            if self.bot.user.avatar:    
             embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar.url)

            await channel.send(embed=embed)
      
async def setup(bot):
    await bot.add_cog(On_member_remove(bot))
