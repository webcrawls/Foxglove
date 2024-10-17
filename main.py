import os
import discord
import bot
from dotenv import load_dotenv
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("TOKEN")
bot_instance = bot.Bot(DISCORD_BOT_TOKEN)
bot_instance.start()