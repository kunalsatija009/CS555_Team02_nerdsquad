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

# BackGround images   
BackGround = pygame.image.load("assets/sprites/BackGround.png")
BackGround = pygame.transform.scale(BackGround, (SCREENWIDTH, SCREEN_HEIGHT))

# Players images
BIRDIMAGE = pygame.image.load('assets/sprites/Bird.png')
PLANEIMAGE = pygame.image.load('assets/sprites/Plane01.png')
FISHIMAGE = pygame.image.load('assets/sprites/Fish01.png')

# To save and load User data
UserData = shelve.open("UserData")

#  Variables used in game
Is_Score = True
Ground = pygame.image.load('assets/sprites/base.png').convert_alpha()
Ground = pygame.transform.scale(Ground, (int(SCREENWIDTH), int(168)))
GroundX_Pos = 0

# Player Variables and settings
UserBird = pygame.transform.scale2x(pygame.image.load('assets/sprites/Bird1.png').convert_alpha())
BirdFrames = [UserBird, UserBird, UserBird]
BirdSprites = BirdFrames[PLAYER_INDEX]
BirdRect = BirdSprites.get_rect(center = (100,325))

# Obstecle VAriables and settings
GreenPipe = pygame.image.load('assets/sprites/GreenPipe.png')
GreenPipe = pygame.transform.scale2x(GreenPipe)
#GreenPipe = pygame.transform.scale(GreenPipe, (int(168), int(568)))
GreenPipeList = []
PipeHeight = [400,450,500]

# Events
BirdEvent = pygame.USEREVENT + 1
pygame.time.set_timer(BirdEvent,225)
PipeEvent = pygame.USEREVENT
pygame.time.set_timer(PipeEvent,2500)
SCOREEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SCOREEVENT,100)

# audio
WingSound = pygame.mixer.Sound('assets/audio/wing.wav')
HitSound= pygame.mixer.Sound('assets/audio/hit.wav')
PointSound = pygame.mixer.Sound('assets/audio/point.wav')

# Welcome page on the screen 
def WelcomePage():
    TitleText = SmallFont.render("Flappy Animal", True, NAVYBLUE)
    today = date.today()
    todayText =  today.strftime("%A , %B  %D") 
    todayText = SmallFont.render(todayText, True, NAVYBLUE)
    HIGH_SCORE = SmallFont.render("HighestScore",True, NAVYBLUE)
   

    while True:
        screen.fill((105,213,238))
        screen.blit(BackGround, [0, 0])
        screen.blit(todayText, (5, 10))
        screen.blit(TitleText, ((SCREENWIDTH - TitleText.get_width()) / 2, 10))
        screen.blit(HIGH_SCORE, (SCREENWIDTH -  125, 10)) 

        BackGround_rect = BackGround.get_rect()
        screen.blit(BackGround, (BackGround_rect.width, 0))

        TxtLine1 = SmallFont.render("Space key to start as Guest User", True, NAVYBLUE)
        TxtLine2 = SmallFont.render("Enter or Return key to choose settings ", True, NAVYBLUE)
        TxtLine3 = SmallFont.render("Use Space key to move", True, NAVYBLUE)
        tl1_rct = TxtLine1.get_rect(midbottom = (SCREENWIDTH / 2, SCREENHEIGHT / 2))
        tl2_rct = TxtLine2.get_rect(midbottom = (SCREENWIDTH / 2, SCREENHEIGHT * 2.5 / 4))
        tl3_rct = TxtLine3.get_rect(midbottom = (SCREENWIDTH / 2, SCREENHEIGHT * 3 / 4))
        screen.blit(TxtLine1,  tl1_rct)
        screen.blit(TxtLine2, tl2_rct)
        screen.blit(TxtLine3,  tl3_rct)

        pygame.display.flip()
        KeyWait()
