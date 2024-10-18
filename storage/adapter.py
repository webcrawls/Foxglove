from core.guild import FoxGuild
from typing import Optional
import discord

class StorageAdapter:
    async def load_guild(id: str) -> Optional[FoxGuild]:
        pass

    async def save_guild(guild: FoxGuild) -> Optional[bool]:
        pass

    async def save_tag(guild_id: str, tag_name: str):
        pass