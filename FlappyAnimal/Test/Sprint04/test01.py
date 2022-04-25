import pygame
import unittest

pygame.init()    
pygame.event.get()

# Keyboard key test for music Input key and Key - p for paused & unpuased

class TestInputKey(unittest.TestCase):
  def MouseClick(self):
    self.post_event = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button = 1, pos = (10, 10))
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.MOUSEBUTTONDOWN)
    self.assertEqual(pygame.event.button  == 1)
    self.assertEqual(pygame.event.pos  == (10, 10))
  
  def MusicKey_1(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_1})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_1)

  def MusicKey_2(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_2})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_2)

  def MusicKey_3(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_3})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_3)
  
  def MusicKey_4(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_4})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_4)
  
  def MusicKey_p(self):
    self.post_event = pygame.event.Event(pygame.KEYDOWN, {"key": pygame.K_p})
    pygame.event.post(self.post_event)
    self.event = pygame.event.poll()
    self.assertEqual(pygame.event.type == pygame.KEYDOWN)
    self.assertEqual(pygame.event.key  == pygame.K_p)
  
pygame.quit()
