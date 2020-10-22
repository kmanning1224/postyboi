import os
from discord.ext import commands
bot = commands.Bot(command_prefix="!")
path = "/bot/cogs"
dirs = os.listdir( path )
for filename in dirs:
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')


bot.run(DISCORD_TOKEN)