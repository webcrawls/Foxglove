from db.database import guild_exists
from .module import Module

class CoreModule(Module):
    def __init__(self, bot):
        self.bot = bot

    def load(self):
        @self.bot.command(name='info')
        async def info(ctx):
            module_count = len(self.bot.bot_modules)
            await ctx.send(f"hi, i'm foxglove, running {module_count} modules in (idk) guilds.")

        @self.bot.command(name='guild')
        @guild_exists
        async def guild(ctx):
            print("test")

        @self.bot.command(name='setup')
        @guild_exists
        async def guild(ctx):
            print("test")

def create(bot):
     return CoreModule(bot)