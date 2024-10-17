import os
from dotenv import load_dotenv
from client import Foxglove
from db.local import LocalBotDatabase
import asyncio
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("TOKEN")
bot = Foxglove(LocalBotDatabase("local.db"))
bot.run_foxglove(DISCORD_BOT_TOKEN)