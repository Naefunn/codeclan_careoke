import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    
    def setUp(self):
        self.room1 = Room("Smooth Booth", 3, 10.00)
        self.guest1 = Guest("Joe Blogs", 10, "I will survive")
        self.song1 = Song("I will survive")

    def test_room_has_name(self):
        self.assertEqual("Smooth Booth", self.room1.room_name)

    def test_room_has_capacity(self):
        self.assertEqual(3, self.room1.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10.00, self.room1.entry_fee)

    def test_can_check_in_guest(self):
        self.room1.check_in(self.guest1)
        self.assertEqual([self.guest1], self.room1.guest_list)

    def test_can_check_out_guest(self):
        self.room1.check_in(self.guest1)
        self.room1.check_out(self.guest1)
        self.assertEqual([], self.room1.guest_list)

    def test_can_add_song_to_playlist(self):
        self.room1.add_song(self.song1)
        self.assertEqual([self.song1], self.room1.song_playlist)

    def test_room_is_full(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.assertEqual("The room is at capacity", self.room1.check_in(self.guest1))

    def test_revenue_increases(self):
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.room1.check_in(self.guest1)
        self.guest1.pays_entry_fee(self.room1)
        self.assertEqual(40.00, self.room1.room_revenue)
