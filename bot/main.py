from discord.ext import commands
import discord
import os
cog_path = 'D:\\PersonalProjects\\postyboi\\cogs'
bot = commands.Bot(command_prefix="!")

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cogs.{extension}')

for filename in os.listdir(cog_path):
    filepath = os.path.join(cog_path,filename)
    f = open(filepath,'r')
    if f.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzY4ODMyMDIyNjkzMDE5NjY5.X5GMng.z0NoihGHroBvTv3_F9m1lWg4uS8')