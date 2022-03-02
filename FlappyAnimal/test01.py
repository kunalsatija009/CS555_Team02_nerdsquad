import unittest
import app
class Testing(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(app.loginPage, 0)
        
    def test2(self):
        self.assertIsNone(app.registerPage, message = None)
        
unittest.main()
