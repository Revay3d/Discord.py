from discord.ext import commands
from discord.ext import tasks
import discord
from colorama import Fore, init
import os
import TableIt

class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(Fore.GREEN + f"El bot ya esta en linea {Fore.BLUE + str(self.bot.user)}" + Fore.WHITE)
     
        eventos = os.listdir('./events')

        tabla = [ ["Eventos", "Estado"]]

      
        for evento in eventos:
         if evento != "__pycache__":
          fila = [evento, "Ok"]
          tabla.append(fila)

   
        TableIt.printTable(tabla, useFieldNames=True)
        
        await self.bot.change_presence(activity=discord.Game(name='RevayDev'), status=discord.Status.idle)
        await self.bot.sync_app_commands()

async def setup(bot):
    await bot.add_cog(OnReady(bot))
