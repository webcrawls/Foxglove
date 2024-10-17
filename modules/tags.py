import discord
from discord.ext import commands
from db.database import BotDatabase
from .module import Module

class TagsModule(Module):
    def __init__(self, bot):
        self.bot = bot

    def load(self):
        @self.bot.command()
        async def tags(ctx):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  title="Foxglove Tags",
                                  description="> Save messages and information for later!\n\nTo create a tag, you can also reply to\na message with `@foxglove tag <name>`.\n\nTo recall a tag, `@foxglove <tagname>`.")
            embed.add_field(name="$tags", value="Shows this help message", inline=False)
            embed.add_field(name="$tags create <name> ...content...", value="Create a tag.", inline=False)
            embed.add_field(name="$tags list [@user]", value="List all tags created by a user or the guild.", inline=False)
            embed.add_field(name="$tags delete <name>", value="Delete a tag", inline=False)
            await ctx.send(embed=embed)

def create(bot):
    return TagsModule(bot)