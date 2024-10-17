import discord

class BotDatabase:
    def __init__(self):
        return
    
    def user_exists(self, user_id):
        return False
    
    def guild_exists(self, guild_id):
        return False
    
    def create_guild(self, guild_id):
        return False

def guild_exists(func):
    async def command_wrapper(*ctx, **kwargs):
        db: BotDatabase = ctx[0].bot.db
        guild = ctx[0].guild
        if not db.guild_exists(str(guild.id)):
            embed = discord.Embed(colour=discord.Colour.dark_red(),
                                  title="I'm not ready for this!!",
                                  description="This command requires setup from a server owner/admin.\n"+
                                              "Please let them know to setup Foxglove!")
            await ctx[0].send(embed=embed)
            return
        await func(ctx, kwargs)
    return command_wrapper

def guild_not_setup(func):
    async def command_wrapper(*ctx, **kwargs):
        db: BotDatabase = ctx[0].bot.db
        guild = ctx[0].guild
        if db.guild_exists(str(guild.id)):
            embed = discord.Embed(colour=discord.Colour.dark_red(),
                                  title="Too late, pal.",
                                  description="This command is only usable during the setup phase.")
            await ctx[0].send(embed=embed)
            return
        await func(ctx, kwargs)
    return command_wrapper