import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print("si, funsiona")
        await ctx.reply("¡Hola, este es mi comando!")

async def setup(bot):
 await bot.add_cog(Ping(bot))
