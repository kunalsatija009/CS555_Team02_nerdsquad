import unittest
import game as G 

class TestGame(unittest.TestCase):
    def test_Collision(self):
        pipe = []
        a = G.dCollision(pipe)
        self.assertNotEqual(a, False)
    
if __name__ == '__main__':
        unittest.main()
