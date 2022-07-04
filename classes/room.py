class Room:
    def __init__(self, _room_name, _capacity, _entry_fee):
        self.room_name = _room_name
        self.capacity = _capacity
        self.entry_fee = _entry_fee
        self.guest_list = []
        self.song_playlist = []
        self.room_revenue = 0.0

    def check_in(self, guest):
        if len(self.guest_list) >= self.capacity:
            return "The room is at capacity"
        else: 
            self.guest_list.append(guest)
            self.room_revenue += self.entry_fee

    def check_out(self, guest):
        self.guest_list.remove(guest)

    def add_song(self, song):
        self.song_playlist.append(song)


