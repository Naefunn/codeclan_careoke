import unittest
from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song1 = Song("I will survive")
    
    
    def test_song_has_name(self):
        self.assertEqual("I will survive", self.song1.song_name)
