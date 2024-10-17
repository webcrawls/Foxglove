class FoxGuild:
    discord_id: str
    date_created: str
    settings: object

    def __init__(self, id: str,
                 settings: object,
                 meta: object):
        self.id = id
        self.settings = settings