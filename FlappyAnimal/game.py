import sys
import pygame
from pygame.locals import *
import random
from datetime import date
from gameSettings import *
import shelve # shelve is One of the standardLibrary to communicate with directory file.

# Initialization of pygame
pygame.init()

# Setting of clock for game
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption(TITLE)

# Intialize of Fonts variable
BigFont = pygame.font.SysFont("dejavusans", 100)
MedFont = pygame.font.SysFont("dejavusans", 50)
SmallFont = pygame.font.SysFont("dejavusans", 25)

# BackGround images   
BackGround = pygame.image.load("assets/sprites/BackGround.png").convert()
BackGround = pygame.transform.scale(BackGround, (SCREENWIDTH, SCREENHEIGHT))

# Players images
BIRDIMAGE = pygame.image.load('assets/sprites/Bird.png')
PLANEIMAGE = pygame.image.load('assets/sprites/Plane01.png')
FISHIMAGE = pygame.image.load('assets/sprites/Fish01.png')
ASTRNTIMAGE = pygame.image.load('assets/sprites/astronaut01.png') 

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

# wait function 
def KeyWait():
    waiting = True
    run = False
    while  waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    USERNAME == "GuestUser"
                    waiting = False
                    run = True
                    while run:
                        MainGame()
                elif event.key == pygame.K_RETURN:
                    waiting = False
                    GameMenu()
            
# Button Function - To creates Button
def Button(x_pos, y_pos, width, height, color, hover):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed(3)
        if x_pos + width > mouse[0] > x_pos and y_pos + height > mouse[1] > y_pos:
            pygame.draw.rect(screen, hover, (x_pos, y_pos, width, height))
            if click[0] == 1:
                return True
        else:
             pygame.draw.rect(screen, color, (x_pos, y_pos, width, height))


def BuildGround():
	screen.blit(Ground,(GroundX_Pos,610))
	screen.blit(Ground,(GroundX_Pos + SCREENWIDTH,610))
	

def BuildPipe():
	PipePosition = random.choice(PipeHeight)
	TopPipe = GreenPipe.get_rect(midbottom = (SCREENWIDTH +200 ,PipePosition-350))
	BottomPipe = GreenPipe.get_rect(midtop = (SCREENWIDTH +200 ,PipePosition))
	return TopPipe,BottomPipe

def PipeTransform(pipes):
    for p in pipes:
        if p.bottom < SCREENHEIGHT:
            TossPipe = pygame.transform.flip(GreenPipe, False, True)
            screen.blit(TossPipe, p)
        else:
            screen.blit(GreenPipe, p)

def PipesMotion(pipes):
	for p in pipes:
		p.centerx -= 4
	dPipesList = [p for p in pipes if p.right > -25 ]
	return dPipesList

def CreateBird():
	dBird = BirdFrames[PLAYER_INDEX]
	dBirdRect = dBird.get_rect(center = (100,BirdRect.centery))
	return dBird,dBirdRect

def BirdTransform(bird):
	dBird = pygame.transform.rotozoom(bird, (PLAYER_MOVEMENT * -2) ,1)
	return dBird

def dCollision(pipes):
	global Is_Score
	for p in pipes:
		if BirdRect.colliderect(p):
			HitSound.play()
			return False

	if BirdRect.bottom >= 900 or BirdRect.top <= -100:
		Is_Score = True
		return False

	return True

def PipeScore():
    global SCORE, Is_Score
    if GreenPipeList:
        for p in GreenPipeList:
            if p.centerx < 0:
                Is_Score = True
            elif 110 > p.centerx > 90 and Is_Score:
                SCORE += 1
                PointSound.play()
                Is_Score = False

def ScoreBoard(IsGame):
	if IsGame == 'MainGame':
		ScoreBlock = SmallFont.render(str(int(SCORE)),True, WHITE)
		ScoreRect = ScoreBlock.get_rect(topleft = (20,20))
		screen.blit(ScoreBlock,ScoreRect)
	if IsGame == 'GameOver':
		ScoreBlock = SmallFont.render(f'Score: {int(SCORE)}' ,True, WHITE)
		ScoreRect = ScoreBlock.get_rect(center = (275,125))
		screen.blit(ScoreBlock,ScoreRect)
		
# Sprint 03 Work -Random generation of star in game for the points.- Malhar / Darshil		
def star():
def ScoreStar():
	
# Sprint 03 Work - Creattion of four types different Background Music and 
# play function to play in background while game is ON - Praveen / Aishwariya
def BackgroundMusic()


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
 def MainGame():
    #TitleText = SmallFont.render(TITLE, True, MEDUIMBLUE)
    global IS_ACTIVE, PLAYER_MOVEMENT, BirdSprites, BirdRect, GreenPipeList, GroundX_Pos, PLAYER_INDEX, SCORE, HIGH_SCORE
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and IS_ACTIVE:
                    PLAYER_MOVEMENT = 0
                    PLAYER_MOVEMENT -= 12
                    WingSound.play()
                if event.key == pygame.K_SPACE and IS_ACTIVE == False:
                    IS_ACTIVE = True
                    GreenPipeList.clear()
                    BirdRect.center = (100,325)
                    PLAYER_MOVEMENT = 0
                    SCORE = 0
            
            if event.type == PipeEvent:
                GreenPipeList.extend(BuildPipe())

            if event.type == BirdEvent:
                if PLAYER_INDEX < 2:
                    PLAYER_INDEX += 1
                else:
                    PLAYER_INDEX = 0
                
                BirdSprites,BirdRect = CreateBird()
        screen.blit(BackGround,(0,0))
        
        if IS_ACTIVE:
            # Player setting
            PLAYER_MOVEMENT += GRAVITY
            BirdFlip = BirdTransform(BirdSprites)
            BirdRect.centery += PLAYER_MOVEMENT
            screen.blit(BirdFlip,BirdRect)
            IS_ACTIVE = dCollision(GreenPipeList)

		    # Pipes settings
            GreenPipeList = PipesMotion(GreenPipeList)
            PipeTransform(GreenPipeList)

		    # Score settings
            PipeScore()
            ScoreBoard('MainGame')

        else:
            screen.blit(BackGround, [0, 0])
            TxtLine1 = SmallFont.render("Game Over", True, NAVYBLUE)
            TxtLine2 = SmallFont.render("Use Space key to Restart", True, NAVYBLUE)
            tl1_rct = TxtLine1.get_rect(midbottom = (SCREENWIDTH / 2, SCREENHEIGHT / 2))
            tl2_rct = TxtLine2.get_rect(midbottom = (SCREENWIDTH / 2, SCREENHEIGHT * 2.5 / 4))
            screen.blit(TxtLine1,  tl1_rct)
            screen.blit(TxtLine2, tl2_rct)

	    # Ground - Base Setting
        GroundX_Pos -= 1
        BuildGround()
        if (SCREENWIDTH * -1) >= GroundX_Pos:
            GroundX_Pos = 0
        pygame.display.update()
        clock.tick(FPS)
def GameMenu():
    TitleText = SmallFont.render("The Flappy Animal Game", True, MEDUIMBLUE)
    
    global NEWUSER

    # Active - deactive upon selection
    UNameActive = False
    BirdActive = False
    PlaneActive = False
    FishActive = False
    AstrntActive = False
    
  
    UserChoicePrompt = SmallFont.render("Select your choices", True, MEDUIMBLUE)
   
    StartGame = SmallFont.render("Start Game", True, WHITE)

    while True:
        screen.fill((105,213,238))
        screen.blit(TitleText, ((SCREENWIDTH - TitleText.get_width()) / 2, 0))

        # UserName  TextBox
        UserNameText = SmallFont.render(NEWUSER, True, WHITE)
        UNTextBorder = pygame.Rect(((SCREENWIDTH - UserNameText.get_width()) / 2) - 10, SCREENHEIGHT * .20, UserNameText.get_width() + 10, 50)
        screen.blit(UserNameText, ((SCREENWIDTH - UserNameText.get_width()) / 2, SCREENHEIGHT * .20))

        # Border for User Iamges
        BirdBorder = pygame.Rect((SCREENWIDTH * .250) - 4, (SCREENHEIGHT * .45) - 4, BIRDIMAGE.get_width() + 8, BIRDIMAGE.get_height() + 8)
        PlaneBorder = pygame.Rect(((SCREENWIDTH - PLANEIMAGE.get_width()) * .462) - 4, (SCREENHEIGHT * .45) - 4, PLANEIMAGE.get_width() + 8, PLANEIMAGE.get_height() + 8)
        FishBorder = pygame.Rect(((SCREENWIDTH - FISHIMAGE.get_width()) * .650) - 4, (SCREENHEIGHT * .45) - 4, FISHIMAGE.get_width() + 8, FISHIMAGE.get_height() + 8)
        AstrntBorder = pygame.Rect(((SCREENWIDTH - ASTRNTIMAGE.get_width()) * .840) - 4, (SCREENHEIGHT * .45) - 4, ASTRNTIMAGE.get_width() + 8, ASTRNTIMAGE.get_height() + 8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # KeyBoard - Mouse Events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNTextBorder.collidepoint(event.pos):
                    UNameActive = True
                elif BirdBorder.collidepoint(event.pos):
                    BirdActive = True
                elif PlaneBorder.collidepoint(event.pos):
                    PlaneActive = True
                elif FishBorder.collidepoint(event.pos):
                    FishActive = True
                elif AstrntBorder.collidepoint(event.pos):
                    AstrntActive = True
                else:
                    UNameActive = False
                    BirdActive = False
                    PlaneActive = False
                    FishActive = False
                    AstrntActive = False

            if event.type == pygame.KEYDOWN:
                if UNameActive:
                    if event.key == pygame.K_BACKSPACE:
                        NEWUSER = NEWUSER[:-1]
                    else:
                        NEWUSER += event.unicode

        # UserName TextBox Click Event
        if UNameActive:
            pygame.draw.rect(screen, WHITE, UNTextBorder, 2)
            USERNAMEPrompt = SmallFont.render("Enter UserName here", True, WHITE)
        else:
            pygame.draw.rect(screen, MEDUIMBLUE, UNTextBorder, 2)
            USERNAMEPrompt = SmallFont.render("Enter User-Name here", True, MEDUIMBLUE)
            
        # User Selection Activity
        if BirdActive:
            PlaneActive = False
            FishActive = False
            AstrntActive = False
            pygame.draw.rect(screen, WHITE, BirdBorder, 2)
            UserChoice = "Bird"
        else:
            pygame.draw.rect(screen, NAVYBLUE, BirdBorder, 2)

        if PlaneActive:
            BirdActive = False
            FishActive = False
            AstrntActive = False
            pygame.draw.rect(screen, WHITE, PlaneBorder, 2)
            UserChoice = "Plane"
        else:
            pygame.draw.rect(screen, NAVYBLUE, PlaneBorder, 2)

        if FishActive:
            BirdActive = False
            PlaneActive = False
            AstrntActive = False
            pygame.draw.rect(screen, WHITE, FishBorder, 2)
            UserChoice = "Fish"
        else:
            pygame.draw.rect(screen, NAVYBLUE, FishBorder, 2) 
        
        if AstrntActive:
            BirdActive = False
            PlaneActive = False
            FishActive
            pygame.draw.rect(screen, WHITE, AstrntBorder, 2)
            UserChoice = "Astronaut"
        else:
            pygame.draw.rect(screen, NAVYBLUE, AstrntBorder, 2) 


        screen.blit(USERNAMEPrompt, ((SCREENWIDTH - USERNAMEPrompt.get_width()) / 2, (SCREENHEIGHT * .05) + UserNameText.get_height()))
        screen.blit(UserChoicePrompt, ((SCREENWIDTH - UserChoicePrompt.get_width()) / 2, SCREENHEIGHT * .35))

        # User Selection
        UserText = MedFont.render("Users:", True, WHITE)
        screen.blit(UserText, (SCREENWIDTH * .075, SCREENHEIGHT * .45))
        screen.blit(BIRDIMAGE, (SCREENWIDTH * .250, SCREENHEIGHT * .45))
        screen.blit(PLANEIMAGE, (SCREENWIDTH * .425, SCREENHEIGHT * .45))
        screen.blit(FISHIMAGE, (SCREENWIDTH * .600, SCREENHEIGHT * .45))
        screen.blit(ASTRNTIMAGE, (SCREENWIDTH * .775, SCREENHEIGHT * .45))
        submitButtton = Button((SCREENWIDTH / 2) - (StartGame.get_width() / 2) - 5, SCREENHEIGHT * .9,StartGame.get_width() + 10, StartGame.get_height(), MEDUIMBLUE, NAVYBLUE)

        screen.blit(StartGame, ((SCREENWIDTH / 2) - (StartGame.get_width() / 2), int(SCREENHEIGHT * .9)))

        global USERNAME
        if submitButtton:
            if NEWUSER != "":
                USERNAME = NEWUSER
                UserData['USERNAME'] = USERNAME
            else:
                USERNAME = 'GuestUser'
                UserData['USERNAME'] = USERNAME

            UserData['UserChoice'] = UserChoice
            UserData.close()
            SuccessScreen(USERNAME, UserChoice)

        pygame.display.update()
        clock.tick(FPS / 4)

def SuccessScreen(USERNAME, UserChoice):
    TitleText = SmallFont.render(TITLE, True, MEDUIMBLUE)

    # Declare Variables
    welcomeName = SmallFont.render("Hello, " + USERNAME + ".", True, MEDUIMBLUE)
    welcomeChoices  = SmallFont.render("YourChoices " + UserChoice + ".", True, MEDUIMBLUE)

    while True:
        screen.fill((105,213,238))
        screen.blit(TitleText, ((SCREENWIDTH - TitleText.get_width()) / 2, 0))

        screen.blit(welcomeName, (20, 40))
        screen.blit(welcomeChoices , (20, welcomeName.get_height() + 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(FPS / 4)

       
# This is loop for Main Game
while True:
    WelcomePage()
