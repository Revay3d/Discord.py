import discord
from discord.ext import commands

class Sicronisar(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="sicro") 
    async def sicro(self, ctx):
      synced = await self.bot.tree.sync()
      await ctx.send(f"hay {len(synced)} Comando(s) de barra disponible(s).")

async def setup(bot):
 await bot.add_cog(Sicronisar(bot))
