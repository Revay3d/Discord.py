from discord.ext import commands
from discord.ext import tasks
import discord
from colorama import Fore, init
import os
from tabulate import tabulate

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(Fore.GREEN + f"El bot ya esta en linea {Fore.BLUE + str(self.bot.user)}" + Fore.WHITE)

        eventos = os.listdir('./events')
        tabla = []

        for evento in eventos:
            if evento != "__pycache__":
                fila = [evento, "Ok"]
                tabla.append(fila)

        print(tabulate(tabla, headers=["Eventos", "Estado"], tablefmt="pretty"))

        await self.bot.change_presence(activity=discord.Game(name='RevayDev'), status=discord.Status.idle)
        await self.bot.sync_app_commands()

async def setup(bot):
    await bot.add_cog(OnReady(bot))
