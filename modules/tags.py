import discord
from discord.ext import commands
from db.database import BotDatabase
from db.decorators import guild_setup
from .module import Module

class TagsModule(Module):
    def __init__(self, bot):
        self.bot = bot

    def load(self):
        @self.bot.event
        async def on_message(message):
            print(message.reference)
            await self.bot.process_commands(message)

        @self.bot.group(name='tags', invoke_without_command=True)
        @guild_setup(warn=True, error=False)
        async def tags(ctx):
            embed = discord.Embed(colour=discord.Color.blue(),
                                  title="Foxglove Tags",
                                  description="> Save messages and information for later!\n\nTo create a tag, you can also reply to\na message with `@foxglove tag <name>`.\n\nTo recall a tag, `@foxglove <tagname>`.")
            embed.add_field(name="$tags", value="Shows this help message", inline=False)
            embed.add_field(name="$tags create <name> ...content...", value="Create a tag.", inline=False)
            embed.add_field(name="$tags list [@user]", value="List all tags created by a user or the guild.", inline=False)
            embed.add_field(name="$tags delete <name>", value="Delete a tag", inline=False)
            await ctx.send(embed=embed)

        @tags.command(name='list')
        async def tags_list(ctx):
            print("tags create!!")

        @tags.command(name='create')
        async def tags_create(ctx):
            print("tags create!!")

        @tags.command(name='delete')
        async def tags_delete(ctx):
            print("tags create!!")

    def _setup_database(self):
        con = self.bot.db.get_

def create(bot):
    return TagsModule(bot)