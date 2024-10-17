import sqlite3
from .database import BotDatabase

class LocalBotDatabase(BotDatabase):
    def __init__(self, path: str):
        self.path = path
        self._connect_db()

    def create_guild(self, guild_id) -> bool:
        pass # TODO TODO
        # return super().create_guild(guild_id)
    
    def guild_exists(self, guild_id) -> bool:
        stmt = "SELECT * FROM guilds WHERE guild_id = ?"
        con = self._get_connection()
        res = con.execute(stmt, [guild_id])
        if len(res.fetchall()) == 0:
            return False
        return True
    
    def user_exists(self, user_id) -> bool:
        return super().user_exists(user_id)
    
    def _get_connection(self):
        return sqlite3.connect(self.path)

    def _connect_db(self):
        con = self._get_connection()
        self._setup_guilds_table(con)
        self._setup_users_table(con)
        con.close()

    def _setup_guilds_table(self, con):
        stmt = """CREATE TABLE IF NOT EXISTS guilds (guild_id TEXT PRIMARY KEY,
                                                     created TEXT,
                                                     settings TEXT,
                                                     meta TEXT,
                                                     users TEXT);
        """
        con.execute(stmt)

    def _setup_users_table(self, con):
        # stmt = """CREATE TABLE IF NOT EXISTS users (guild_id TEXT PRIMARY KEY,
        #                                             created TEXT,
        #                                             settings TEXT,
        #                                             meta TEXT);
        # """
        # con.execute(stmt)
        pass