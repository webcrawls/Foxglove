from util.decorators import guild_setup
from .module import Module
import discord
from discord.ext.commands import has_permissions

class CoreModule(Module):
    def __init__(self, bot):
        self.bot = bot

    def load(self):
        @self.bot.command(name='info', alias=['help'])
        async def info(ctx):
            module_count = len(self.bot.bot_modules)
            await ctx.send(f"hi, i'm foxglove, running {module_count} modules in (idk) guilds.")

        @self.bot.command(name='modules')
        async def modules(ctx):
            embed = discord.Embed(colour=discord.Colour.blue(), title="Foxglove Modules")
            for module in self.bot.bot_modules:
                embed.add_field(inline=False, name=str(module), value=str(module))
            await ctx.send(embed=embed)

        @self.bot.command(name='guild')
        @guild_setup()
        async def guild(ctx):
            print("test")

        @self.bot.command(name='setup')
        @guild_setup(invert=True)
        @has_permissions(administrator=True)
        async def setup(ctx):
            self.bot.db.create_guild(ctx.guild.id)
            await ctx.send("uhh i think guild has been setup?")

def create(bot):
     return CoreModule(bot)