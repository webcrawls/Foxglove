from .adapter import StorageAdapter
from core.guild import FoxGuild
from typing import Optional

class MemoryAdapter(StorageAdapter):
    def __init__(self):
        self.guilds = {}
    
    async def load_guild(self, id: str) -> Optional[FoxGuild]:
        if id not in self.guilds:
            return None
        return self.guilds[id]

    async def save_guild(self, guild: FoxGuild) -> Optional[bool]:
        self.guilds[guild.id] = guild