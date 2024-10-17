import sqlite3
import datetime
from .database import BotDatabase

class LocalBotDatabase(BotDatabase):
    def __init__(self, path: str):
        self.path = path
        self._connect_db()

    def create_guild(self, guild_id) -> bool:
        stmt = """INSERT INTO guilds (guild_id, created, settings, meta, users) VALUES (?, ?, ?, ?, ?);"""
        con = self._get_connection()
        con.execute(stmt, [guild_id, str(datetime.datetime.now()), "{}", "{}", "[]"])
        con.commit() # IMPORTANT!!!!
        con.close()
        # return super().create_guild(guild_id)
    
    def guild_exists(self, guild_id) -> bool:
        stmt = "SELECT * FROM guilds WHERE guild_id = ?"
        con = self._get_connection()
        res = con.execute(stmt, [guild_id])
        if len(res.fetchall()) == 0:
            con.close()
            return False
        con.close()
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
        con.close()

    def _setup_users_table(self, con):
        # stmt = """CREATE TABLE IF NOT EXISTS users (guild_id TEXT PRIMARY KEY,
        #                                             created TEXT,
        #                                             settings TEXT,
        #                                             meta TEXT);
        # """
        # con.execute(stmt)
        pass