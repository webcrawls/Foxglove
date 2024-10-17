import discord
from modules import core, tags
from discord.ext import commands

class Foxglove(commands.Bot):
    def __init__(self, db):
        self.db = db
        self.bot_modules = []
        intents = discord.Intents.default()
        intents.message_content = True
        commands.Bot.__init__(self, command_prefix='$', intents=intents)
    
    def load_modules(self):
        for module in core, tags:
            instance = module.create(self)
            instance.load()
            print("loaded "+str(instance))
            self.bot_modules.append(instance)

    def run_foxglove(self, token):
        self.load_modules()
        self.run(token=token)