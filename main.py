import os
from dotenv import load_dotenv
from client import Foxglove
from storage.local.sqlite import LocalStorage
import asyncio
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("TOKEN")
bot = Foxglove(LocalStorage("local.db"))
bot.run_foxglove(DISCORD_BOT_TOKEN)