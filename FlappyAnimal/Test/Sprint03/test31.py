import pygame
import unittest

from gameSettings import IS_ACTIVE

pygame.init()    
pygame.event.get()


class TestInputKey(unittest.TestCase):
    def MouseClick(self):
        self.post_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button = 2, pos = (10, 10))
        pygame.event.post(self.post_event)
        self.event = pygame.event.poll()
        if pygame.event.type == pygame.MOUSEBUTTONDOWN:
            result = True
        self.assertEqual('True' == result)
   
  
    def InputKeySpace(self):
        self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_SPACE})
        pygame.event.post(self.post_event)
        self.event = pygame.event.poll()
        if pygame.event.key == pygame.K_SPACE:
            result = True
        self.assertEqual('True' == result)
        
    def InputKeyEnter(self):
        self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_RETURN})
        pygame.event.post(self.post_event)
        self.event = pygame.event.poll()
        if pygame.event.key == pygame.K_RETURN:
            result = True
        self.assertEqual('True' == result)

    def InputKeyEscape(self):
        self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_ESCAPE})
        pygame.event.post(self.post_event)
        self.event = pygame.event.poll()
        if pygame.event.key == pygame.K_ESCAPE:
            result = True
        self.assertEqual('True' == result)
  
pygame.quit()
