import unittest
import Game


class gameTest(unittest.TestCase):
	
		
	
	def test_room_exists(self):
		self.assertEqual(Game.room_exists(0,0), True)    
		
	

unittest.main()