import unittest
import game as G 

class TestGame(unittest.TestCase):
    def test_PipesMotion(self):
        pipe = []
        p = G.dCollision(pipe)
        self.assertEqual(p, [])
    
if __name__ == '__main__':
        unittest.main()