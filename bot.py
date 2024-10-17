import discord

class Bot(discord.Client):

    def __init__(self, token: str):
        self.token = token

    def start(self):
        intents = discord.Intents.default()
        intents.message_content = True

        client = discord.Client(intents=intents)
        client.run(self.token)

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')