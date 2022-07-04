import unittest
from classes.guest import Guest
from classes.room import Room


class TestGuest(unittest.TestCase):
    
    
    def setUp(self):
        self.guest1 = Guest("Joe Blogs", 50, "I will survive")
        self.room1 = Room("Smooth Booth", 3, 10.00)

    def test_guest_has_name(self):
        self.assertEqual("Joe Blogs", self.guest1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest1.wallet)

    def test_guest_has_fav_song(self):
        self.assertEqual("I will survive", self.guest1.fav_song)

    def test_pays_entry_fee(self):
        self.guest1.pays_entry_fee(self.room1)
        self.assertEqual(40, self.guest1.wallet)