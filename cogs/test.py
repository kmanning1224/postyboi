from discord.ext import commands
import discord
bot = commands.Bot(command_prefix="!")

class CommandTest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    #Event
    @commands.Cog.listener()
    async def on_ready(self): #always place self within parameters for class
        print('Postyboi is Online')
    #Command
    @commands.Command()
    async def test(self,ctx): #ctx to rep context
        await ctx.send('Im working')
def setup(bot):
    bot.add_cog(CommandTest(bot))