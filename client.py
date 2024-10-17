import discord
from discord.ext import commands

class Foxglove(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        commands.Bot.__init__(self, command_prefix='$', intents=intents)
    
def run_foxglove(token):
    bot = Foxglove()
    
    @bot.command(name='test')
    async def test(ctx):
        print("test")

    bot.run(token)



# async def create_bot(token):
#     intents = discord.Intents.default()
#     intents.message_content = True

#     bot = commands.Bot(command_prefix='$', intents=intents)


#     await bot.login(token)