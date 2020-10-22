from discord.ext import commands
from config import DISCORD_TOKEN
bot = commands.Bot(command_prefix="!")

@commands.command()
async def ping(ctx):
    await ctx.send("Pong")

bot.add_command(ping)

bot.run(DISCORD_TOKEN)
