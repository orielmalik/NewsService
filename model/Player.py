import datetime
class Player:
    def __init__(self, birthdate: datetime.date, rank: int, player_type: str, details: dict):
        self.birthdate = birthdate
        self.rank = rank
        self.player_type = player_type
        self.details = details

