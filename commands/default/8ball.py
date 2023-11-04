import discord
import interactions
from discord.ext import commands
from discord import app_commands
import random


class ball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.color = bot.color
   
   
    @app_commands.command(name="8ball", description="dire lo que el universo quiera que diga")
    async def random_command(self, interaction: discord.Interaction, pregunta: str):
        respuestas_posibles = ["Sí, sin duda", "Uff… no creo", "Puede ser…", "El destino dice que no", "Tal vez",
                               "Si te lo propones, sí", "Claro que no", "Sí, existe una pequeña probabilidad de que sí", "No, no"]
        respuesta = random.choice(respuestas_posibles)
        embed = discord.Embed(
            title=f"Pregunta de {interaction.user.name}",
            description=f"> tu pregunta fue: {pregunta}\n\n> y yo digo que: {respuesta}" + "\n\n",
           color=self.color
        )
        if self.bot.user.avatar:
         embed.set_thumbnail(url=self.bot.user.avatar.url)
         embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar.url)

        await interaction.response.send_message(embed=embed)



async def setup(bot):
    await bot.add_cog(ball(bot))

       


