import unittest
import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((250, 250))
class Test(unittest.TestCase):
    
    def test01(self):
        run = True
        while run:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                
                if self.event.type == pygame.KEYDOWN:
                    print("A keyboard key is pressed")
                
pygame.display.update()
clock.tick(64)
        


if __name__ == "__main__":
    unittest.main()
    pygame.quit()
    
