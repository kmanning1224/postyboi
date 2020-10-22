from discord.ext import commands
from config import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!")

class CommandTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def hello(self,ctx):
        await ctx.send("Pong")