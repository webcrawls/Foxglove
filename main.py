import os
from dotenv import load_dotenv
import client
import asyncio
load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("TOKEN")

client.run_foxglove(DISCORD_BOT_TOKEN)