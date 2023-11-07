from discord.ext import commands
from discord.ext import tasks
import discord
from discord.ui import Button, View

class Onmessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        
        modmail_channel = discord.utils.get(
            self.bot.get_all_channels(), name="bot-log")
        if message.author == self.bot.user:
            return
        if str(message.channel.type) == "private":
            button = Button(label="Canal de youtube", url="https://www.youtube.com/@revaydev",
                            style=discord.ButtonStyle.danger, emoji="💙")

            view = View()
            view.add_item(button)
            await message.reply("Porque me quieres hablar por aqui 😳, prefiero hablar en un server. ¿conoces a mi creador? Porfavor ¡mira su canal!", view=view)

async def setup(bot):
    await bot.add_cog(Onmessage(bot))
