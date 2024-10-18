from core.guild import FoxGuild
from typing import Optional
import discord

class StorageAdapter:
    async def load_guild(id: str) -> Optional[FoxGuild]:
        pass

    async def save_guild(guild: FoxGuild) -> Optional[bool]:
        pass

    async def load_guild_data(id: str, name: str) -> Optional[object]:
        pass

    async def save_guild_data(id: str, name: str, data: object) -> Optional[object]:
        pass