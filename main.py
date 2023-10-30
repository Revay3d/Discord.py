import os
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
from discord import Intents
import discord

load_dotenv()
TOKEN = os.getenv('Token')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
#Variables
class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.color = 0xTU_COLOR
        self.bienvenidas = ID_CHANNEL
        self.chat = ID_CHANNEL
        self.despedidas = ID_CHANNEL

bot = MyBot(command_prefix="+", intents=discord.Intents.all(), help_command=None)

# cargar comandos
async def load():
   import os

async def load():
   for root, dirs, files in os.walk('./commands'):
        for filename in files:
            if filename.endswith('.py'):
                path = os.path.join(root, filename)
                module_name = path.replace('/', '.').replace('\\', '.')[2:-3]

                if not bot.get_cog(module_name.split('.')[-1]):
                    await bot.load_extension(module_name)


   for filename in os.listdir('./events'):
        if filename.endswith('.py'):
            if not bot.get_cog(filename[:-3]):
                await bot.load_extension(f'events.{filename[:-3]}')

async def main():
    await load()
    await bot.start(TOKEN)

asyncio.run(main())
