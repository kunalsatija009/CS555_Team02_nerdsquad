import pygame
import sys
import unittest

pygame.init()    
pygame.event.get()


class Test(unittest.TestCase):
  def test01(self):
    self.post_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button = 1, pos = (10, 10))
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.MOUSEBUTTONDOWN)
    self.assertEqual(pygame.event.button  == 1)
    self.assertEqual(pygame.event.pos  == (10, 10))
  
  def test02(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_1})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_1)

  def test03(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_2})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_2)

  def test04(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_3})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_3)
  
  def test05(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_4})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_4)
  
  def test06(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_p})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_p)

pygame.quit()

if __name__ == "__main__":
    unittest.main()
