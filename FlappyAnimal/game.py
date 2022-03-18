import sys
import pygame
from datetime import date
from gameSettings import *
import shelve # shelve is One of the standardLibrary to communicate with directory file.

# Initialization of pygame
pygame.init()

# Setting of clock for game
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((SCREENWIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Intialize of Fonts variable
BigFont = pygame.font.SysFont("dejavusans", 100)
MedFont = pygame.font.SysFont("dejavusans", 50)
SmallFont = pygame.font.SysFont("dejavusans", 25)

# BackGround image   
BackGround = pygame.image.load("assets/sprites/BackGround.png")
BackGround = pygame.transform.scale(BackGround, (SCREENWIDTH, SCREEN_HEIGHT))

# Players image
BIRDIMAGE = pygame.image.load('assets/sprites/Bird.png')
PLANEIMAGE = pygame.image.load('assets/sprites/Plane01.png')
FISHIMAGE = pygame.image.load('assets/sprites/Fish01.png')
