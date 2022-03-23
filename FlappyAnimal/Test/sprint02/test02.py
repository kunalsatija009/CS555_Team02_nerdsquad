import unittest
import pygame
from gameSettings import*
import game as G 

pygame.init()    
pygame.event.get()

class TestWelcomePAge(unittest.TestCase):
    event = G.pygame.event
    def space(e):
        if e == pygame.pygame.K_SPACE:
            print("Space Key")
        elif e == pygame.pygame.K_RETURN:
            print("Enter or Return Key")
    pygame.quit()
if __name__ == '__main__':
        unittest.main()

