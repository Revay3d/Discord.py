from discord.ext import commands
import discord
import random

class On_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bienvenidas = bot.bienvenidas
        self.chat = bot.chat

    @commands.Cog.listener()
    async def on_member_join(self, member): 
        embed = discord.Embed(title="Bienvenid@", description=f"""👋 ¡Hola! Bienvenido/a {member.mention}! a nuestro servidor de Discord. 👋

Somos una comunidad de personas con intereses comunes. Aquí podrás socializar, aprender y divertirte.
¡Que lo pases bien y te sientas cómodo/a! 😊 """, color=discord.Color.random())

        if member.avatar:
            embed.set_thumbnail(url=member.avatar.url)

        if self.bot.user.avatar:    
             embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar.url)
             
        message = [f"Que bien ya llego {member.mention}", f"uff... y ¿quien eres? {member.name}",
                   f"no ledigan a {member.mention} donde escondi las galletas..."]

        channel = self.bot.get_channel(self.bienvenidas)
        channel_Bienvenida = self.bot.get_channel(self.chat)

        await channel_Bienvenida.send(random.choice(message))
        await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(On_message(bot))
