class Guest:
    def __init__(self, _name, _wallet, _fav_song):
        self.name = _name
        self.wallet = _wallet
        self.fav_song = _fav_song

    def pays_entry_fee(self, room):
        self.wallet -= room.entry_fee