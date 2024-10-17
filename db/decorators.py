import discord
from .database import BotDatabase

def guild_setup(warn: bool=False, error: bool=True, invert: bool=False):
    def wrapper(func):
        async def wrapped(*ctx, **kwargs):
            db: BotDatabase = ctx[0].bot.db
            guild = ctx[0].guild
            guild_exists = db.guild_exists(str(guild.id))

            if guild_exists and invert and error:
                embed = discord.Embed(colour=discord.Colour.dark_red(),
                                      title="This command can only be used pre-setup.",
                                      description="Sorry.")
                await ctx[0].send(embed=embed)
                return

            if not guild_exists and not invert and error:
                embed = discord.Embed(colour=discord.Colour.dark_red(),
                                      title="I'm not ready for this!!",
                                      description="This command requires setup from a server owner/admin.\n"+
                                                  "Please let them know to setup Foxglove!")
                await ctx[0].send(embed=embed)
                return

            await func(*ctx, **kwargs)

            if not guild_exists and not invert and warn:
                embed = discord.Embed(colour=discord.Colour.yellow(),
                      title="This server is not setup!",
                      description="Parts of this feature may not be available.\nLet the server owner know!")
                await ctx[0].send(embed=embed)
        return wrapped
    return wrapper