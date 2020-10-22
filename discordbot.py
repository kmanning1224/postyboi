import discord
from config import DISCORD_TOKEN
from discord.ext import commands

command_prefix = "-"
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        if message.author.bot:
            return

        if message.content == "-test":
            await message.channel.send("Testing")

client = MyClient()
client.run(DISCORD_TOKEN)
