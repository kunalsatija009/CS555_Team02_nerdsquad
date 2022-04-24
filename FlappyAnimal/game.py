import sys
import pygame
from pygame.locals import *
from pygame import mixer
import random
from datetime import date
from gameSettings import *
import shelve # shelve is One of the standardLibrary to communicate with directory file.

# Initialization of pygame
pygame.init()

# Initialization of mixer for music
mixer.init()

# Setting of clock for game
clock = pygame.time.Clock()

# Create the screen
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption(TITLE)

# Intialize of Fonts variable
BigFont = pygame.font.SysFont("dejavusans", 55)
MedFont = pygame.font.SysFont("dejavusans", 40)
SmallFont = pygame.font.SysFont("dejavusans", 25)

# BackGround image   
BackGround = pygame.image.load("assets/sprites/BackGround.png").convert()
BackGround = pygame.transform.scale(BackGround, (SCREENWIDTH, SCREENHEIGHT))

# Players Image
BIRDIMAGE = pygame.image.load('assets/sprites/Bird.png')
PLANEIMAGE = pygame.image.load('assets/sprites/Plane01.png')
FISHIMAGE = pygame.image.load('assets/sprites/Fish01.png')
ASTRNTIMAGE = pygame.image.load('assets/sprites/astronaut01.png')

# Theme Image
SKYBG = pygame.image.load('assets/sprites/SkyBG.png')
SPACEBG = pygame.image.load('assets/sprites/space1.jpg')
WTRBG = pygame.image.load('assets/sprites/WtrBg1.png')
DARKBG = pygame.image.load('assets/sprites/DrkBg.png')

# To save and load User data
UserData = shelve.open("UserData")

#  Variables used in game
Is_Score = True
Ground = pygame.image.load('assets/sprites/base.png').convert_alpha()
Ground = pygame.transform.scale(Ground, (int(SCREENWIDTH), int(168)))
GroundX_Pos = 0

# Obstecle VAriables and settings
GreenPipe = pygame.image.load('assets/sprites/GreenPipe.png')
GreenPipe = pygame.transform.scale2x(GreenPipe)
GreenPipeList = []
PipeHeight = [400,450,500]

# Events
XUserEvent = pygame.USEREVENT + 1
pygame.time.set_timer(XUserEvent,225)
PipeEvent = pygame.USEREVENT
pygame.time.set_timer(PipeEvent,2500)
SCOREEVENT = pygame.USEREVENT + 2
pygame.time.set_timer(SCOREEVENT,100)

# audio
WingSound = pygame.mixer.Sound('assets/audio/wing.wav')
HitSound= pygame.mixer.Sound('assets/audio/hit.wav')
PointSound = pygame.mixer.Sound('assets/audio/point.wav')
GameoverSound = pygame.mixer.Sound('assets/audio/Gameover.wav')
GameoverSound.set_volume(0.3)

# Player Variables and settings
class XUser:
    def __init__(self, img):
        self.UserX = pygame.transform.scale2x(pygame.image.load(img).convert_alpha())
        self.XFrames = [self.UserX, self.UserX, self.UserX]
        self.XSprites =  self.XFrames[PLAYER_INDEX]
        self.XRect = self.XSprites.get_rect(center = (100,325))
        self.dXUser = self.XFrames[PLAYER_INDEX]
        self.dXUserRect = self.dXUser.get_rect(center = (100,self.XRect.centery))

    def UserTransform(self, XSprites):
        XUserSprites = pygame.transform.rotozoom(XSprites, (PLAYER_MOVEMENT * -2) ,1)
        return XUserSprites

def Back_Ground(lnk):
    bg = pygame.image.load(lnk).convert()
    bg = pygame.transform.scale(bg, (SCREENWIDTH, SCREENHEIGHT)) 
    return bg 

# wait function 
def KeyWait():
    waiting = True
    run = False
    while  waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                UserData.close()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYUP:
		if event.key == pygame.K_1:
                    mixer.music.load('assets/audio/SoftPiano.wav')
                    mixer.music.play()
                if event.key == pygame.K_2:
                    mixer.music.load('assets/audio/summer.ogg')
                    mixer.music.play()
                if event.key == pygame.K_3:
                    mixer.music.load('assets/audio/FridayNight.wav')
                    mixer.music.play()
                if event.key == pygame.K_4:
                    mixer.music.load('assets/audio/Symphony.wav')
                    mixer.music.play()
                if event.key == pygame.K_5:
                    mixer.music.stop()
                if event.key == pygame.K_SPACE:
                    USERNAME == "GuestUser"
                    USERCHOICE == "Bird"
                    THEMECHOICE == "DayBg"
                    waiting = False
                    run = True
                    while run:
                        MainGame(USERNAME, USERCHOICE, THEMECHOICE)
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

# Text Function
def DText(txt, x, y):
    dTxt = SmallFont.render(str(txt), True, NAVYBLUE)
    TxtRct = dTxt.get_rect(midtop = (x , y))
    screen.blit(dTxt, TxtRct)

def BuildGround():
	screen.blit(Ground,(GroundX_Pos,610))
	screen.blit(Ground,(GroundX_Pos + SCREENWIDTH,610))
 
def Stars():
    StarPosition = random.choice(90,450,90)
    STARIMAGE = pygame.transform.scale2x(STARIMAGE)
    TopStar = STARIMAGE.get_rect(midbottom = (SCREENWIDTH +220 ,PipePosition-350))
    BottomStar = STARIMAGE.get_rect(midtop = (SCREENWIDTH +210 ,PipePosition))
    return TopStar,BottomStar

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

def dCollision(pipes):
	global Is_Score
	for p in pipes:
		if UserRect.colliderect(p):
			HitSound.play()
			return False

	if UserRect.bottom >= 995 or UserRect.top <= -105:
		Is_Score = True
		return False

	return True

def PipeScore():
    global SCORE, Is_Score
    if GreenPipeList:
        for p in GreenPipeList:
            if p.centerx < 0:
                Is_Score = True
            elif 105 > p.centerx > 95 and Is_Score:
                SCORE += 1
                PointSound.play()
                Is_Score = False

def ScoreBoard(IsGame, score):
	if IsGame == 'MainGame':
		ScoreBlock = SmallFont.render(str(int(SCORE)),True, WHITE)
		ScoreRect = ScoreBlock.get_rect(topleft = (20,20))
		screen.blit(ScoreBlock,ScoreRect)
	elif IsGame == 'GameOver':
         HSCORE = UserData['HIGHSCORE']
         if int(score) > HSCORE:
            UserData['HIGHSCORE'] = score

# Welcome page on the screen 
def WelcomePage():
    TitleText = SmallFont.render("Flappy Animal", True, NAVYBLUE)
    today = date.today()
    todayText =  today.strftime("%A , %B  %D") 
    todayText = SmallFont.render(todayText, True, NAVYBLUE)
    if not UserData['HIGHSCORE']:
        UserData['HIGHSCORE'] = HIGH_SCORE
    HSCORE = UserData['HIGHSCORE']
    HIGHSCORE = SmallFont.render("HighestScore: " + str(HSCORE) ,True, NAVYBLUE)
   

    while True:
        screen.fill((105,213,238))
        screen.blit(BackGround, [0, 0])
        screen.blit(todayText, (5, 10))
        screen.blit(TitleText, ((SCREENWIDTH - TitleText.get_width()) / 2, 10))
        screen.blit(HIGHSCORE, (SCREENWIDTH -  150, 10)) 

        BackGround_rect = BackGround.get_rect()
        screen.blit(BackGround, (BackGround_rect.width, 0))

        DText('Space key to start as Guest User', SCREENWIDTH *  0.5, SCREENHEIGHT * 0.25, NAVYBLUE)
        DText('Enter or Return key to choose settings', SCREENWIDTH *  0.5, SCREENHEIGHT * 0.375, NAVYBLUE)
        DText('Use Space key to move & Key p to pause - unpause the game', SCREENWIDTH *  0.5, SCREENHEIGHT * 0.5, NAVYBLUE)
        DText('Key:- 1, 2, 3, 4 for music options & 5 to stop BG Music', SCREENWIDTH *  0.5, SCREENHEIGHT * 0.625, NAVYBLUE)

        pygame.display.flip()
        KeyWait()	
def MainGame(USERNAME, USERCHOICE, THEMECHOICE):
    #TitleText = SmallFont.render(TITLE, True, MEDUIMBLUE)
    global IS_ACTIVE, PLAYER_MOVEMENT, UserSprites, UserRect, GreenPipeList, GroundX_Pos, PLAYER_INDEX, SCORE, HIGH_SCORE
    if USERCHOICE == 'Plane':
        dUser = XUser('assets/sprites/Plane.png')
    elif USERCHOICE == 'Fish':
        dUser = XUser('assets/sprites/Fish.png')
    elif USERCHOICE == 'Astronaut':
        dUser = XUser('assets/sprites/astronaut.png')
    else:
        dUser = XUser('assets/sprites/Bird1.png')
	
	
    if THEMECHOICE == 'Space':
        dBg = Back_Ground('assets/sprites/space.jpg')
    elif THEMECHOICE == 'UnderWater':
        dBg = Back_Ground('assets/sprites/WtrBg.png')
    elif THEMECHOICE == 'DarkBg':
        dBg = Back_Ground('assets/sprites/DarkBG.png')
    else:
        dBg = Back_Ground('assets/sprites/BackGround.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                UserData.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
		 if event.key == pygame.K_1:
                    mixer.music.load('assets/audio/SoftPiano.wav')
                    mixer.music.play()
                if event.key == pygame.K_2:
                    mixer.music.load('assets/audio/summer.ogg')
                    mixer.music.play()
                if event.key == pygame.K_3:
                    mixer.music.load('assets/audio/FridayNight.wav')
                    mixer.music.play()
                if event.key == pygame.K_4:
                    mixer.music.load('assets/audio/Symphony.wav')
                    mixer.music.play()
                if event.key == pygame.K_5:
                    mixer.music.stop() 
                if event.key == pygame.K_p:
                    IS_PAUSE = not IS_PAUSE
                    IS_ACTIVE = not IS_ACTIVE
                    GreenPipeList.clear()
                if event.key == pygame.K_SPACE and IS_ACTIVE:
                    PLAYER_MOVEMENT = 0
                    PLAYER_MOVEMENT -= 12
                    WingSound.play()
		
		if event.type == pygame.K_s:
                    pygame.mixer.music.stop()
		
                if event.key == pygame.K_SPACE and IS_ACTIVE == False:
                    IS_ACTIVE = True
                    GreenPipeList.clear()
                    UserRect.center = (100,325)
                    PLAYER_MOVEMENT = 0
                    SCORE = 0
                if event.key == pygame.K_ESCAPE:
                    USERCHOICE = 'Bird'
                    dUser = XUser('assets/sprites/Bird1.png')
		    dBg = Back_Ground('assets/sprites/BackGround.png')
                    IS_ACTIVE = True
                    GreenPipeList.clear()
                    UserRect.center = (100,325)
                    PLAYER_MOVEMENT = 0
                    SCORE = 0 
                    WelcomePage()
                    
            if event.type == PipeEvent:
                GreenPipeList.extend(BuildPipe())

            if event.type == XUserEvent:
                if PLAYER_INDEX < 2:
                    PLAYER_INDEX += 1
                else:
                    PLAYER_INDEX = 0
                
        screen.blit(dBg,(0,0))
        if IS_ACTIVE:
            # Player setting
            PLAYER_MOVEMENT += GRAVITY
            UserSprites = dUser.dXUser
            UserFlip = dUser.UserTransform(UserSprites)
            UserRect = dUser.dXUserRect
            UserRect.centery += PLAYER_MOVEMENT
            screen.blit(UserFlip,UserRect)
            IS_ACTIVE = dCollision(GreenPipeList)
	    # Pipes settings
            GreenPipeList = PipesMotion(GreenPipeList)
            PipeTransform(GreenPipeList)
	    # Score settings
            PipeScore()
            ScoreBoard('MainGame', 0)
        elif IS_PAUSE:  
            GroundX_Pos = 0
            screen.blit(dBg, [0, 0])
            DText("Paused!", SCREENWIDTH * 0.5, SCREENHEIGHT * 0.25, GREEN)
        else:
            screen.blit(BackGround, [0, 0])
            GameoverSound.play()
            import time
            time.sleep(2) # wait and let the sound play for 2 second
            GameoverSound.stop()
            UserData['SCORE'] = SCORE
            DText('Game Over', SCREENWIDTH * 0.5, SCREENHEIGHT * 0.25)
            DText('Your Score: ' + str(SCORE), SCREENWIDTH * 0.5, SCREENHEIGHT * 0.375)
            DText('Use "space" key to Replay or "esc" key to return Home', SCREENWIDTH * 0.5, SCREENHEIGHT * 0.5)
            ScoreBoard('GameOver', SCORE)
            
	# Ground - Base Setting
        GroundX_Pos -= 1
        BuildGround()
        if (SCREENWIDTH * -1) >= GroundX_Pos:
            GroundX_Pos = 0
        pygame.display.update()
        clock.tick(FPS)


def GameMenu():
    TitleText = SmallFont.render("The Flappy Animal Game", True, MEDUIMBLUE)
    
    global NEWUSER, USERCHOICE, USERNAME, THEMECHOICE

    # Active - deactive upon selection
    UNameActive = False
    BirdActive = False
    PlaneActive = False
    FishActive = False
    AstrntActive = False
    SkyBgActive = False
    SpaceBgActive = False
    WtrBgActive = False
    DarkBgActive = False
    
    UserChoicePrompt = SmallFont.render("Select your choices", True, MEDUIMBLUE)
    StartGame = SmallFont.render("Start Game", True, WHITE)

    while True:
        screen.fill((105,213,238))
        screen.blit(TitleText, ((SCREENWIDTH - TitleText.get_width()) / 2, 0))

        # UserName  TextBox
        UserNameText = SmallFont.render(NEWUSER, True, WHITE)
        UNTextBorder = pygame.Rect(((SCREENWIDTH - UserNameText.get_width()) / 2) - 10, SCREENHEIGHT * .20, UserNameText.get_width() + 10, 50)
        screen.blit(UserNameText, ((SCREENWIDTH - UserNameText.get_width()) / 2, SCREENHEIGHT * .20))

        # Border for User Images
        BirdBorder = pygame.Rect((SCREENWIDTH * .250) - 4, (SCREENHEIGHT * .45) - 4, BIRDIMAGE.get_width() + 8, BIRDIMAGE.get_height() + 8)
        PlaneBorder = pygame.Rect(((SCREENWIDTH - PLANEIMAGE.get_width()) * .462) - 4, (SCREENHEIGHT * .45) - 4, PLANEIMAGE.get_width() + 8, PLANEIMAGE.get_height() + 8)
        FishBorder = pygame.Rect(((SCREENWIDTH - FISHIMAGE.get_width()) * .650) - 4, (SCREENHEIGHT * .45) - 4, FISHIMAGE.get_width() + 8, FISHIMAGE.get_height() + 8)
        AstrntBorder = pygame.Rect(((SCREENWIDTH - ASTRNTIMAGE.get_width()) * .840) - 4, (SCREENHEIGHT * .45) - 4, ASTRNTIMAGE.get_width() + 8, ASTRNTIMAGE.get_height() + 8)
	
	# Border for Theme Images
        SkyBgBorder = pygame.Rect((SCREENWIDTH * .250) - 4, (SCREENHEIGHT * .65) - 4, SKYBG.get_width() + 8, SKYBG.get_height() + 8)
        SpaceBorder = pygame.Rect(((SCREENWIDTH - SPACEBG.get_width()) * .462) - 4, (SCREENHEIGHT * .65) - 4, SPACEBG.get_width() + 8, SPACEBG.get_height() + 8)
        WtrBorder =  pygame.Rect(((SCREENWIDTH - WTRBG.get_width()) * .650) - 4, (SCREENHEIGHT * .65) - 4, WTRBG.get_width() + 8, WTRBG.get_height() + 8)
        DarkBoder = pygame.Rect(((SCREENWIDTH - DARKBG.get_width()) * .840) - 4, (SCREENHEIGHT * .65) - 4, DARKBG.get_width() + 8, DARKBG.get_height() + 8)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                UserData.close()
                pygame.quit()
                sys.exit()

            # KeyBoard - Mouse Events
            if event.type == pygame.MOUSEBUTTONDOWN:
                if UNTextBorder.collidepoint(event.pos):
                    UNameActive = True
                elif BirdBorder.collidepoint(event.pos):
                    BirdActive = True
                    FishActive = False
                    PlaneActive = False
                    AstrntActive = False
                elif PlaneBorder.collidepoint(event.pos):
                    PlaneActive = True
                    FishActive = False
                    BirdActive = False
                    AstrntActive = False
                elif FishBorder.collidepoint(event.pos):
                    FishActive = True
                    BirdActive = False
                    PlaneActive = False
                    AstrntActive = False
                elif AstrntBorder.collidepoint(event.pos):
                    AstrntActive = True
                    FishActive = False
                    BirdActive = False
                    PlaneActive = False
		elif SkyBgBorder.collidepoint(event.pos):
                    SkyBgActive = True
                    SpaceBgActive = False
                    WtrBgActive = False
                    DarkBgActive = False
                elif SpaceBorder.collidepoint(event.pos):
                    SkyBgActive = False
                    SpaceBgActive = True
                    WtrBgActive = False
                    DarkBgActive = False
                elif WtrBorder.collidepoint(event.pos):
                    SkyBgActive = False
                    SpaceBgActive = False
                    WtrBgActive = True
                    DarkBgActive = False
                elif DarkBoder.collidepoint(event.pos):
                    SkyBgActive = False
                    SpaceBgActive = False
                    WtrBgActive = False
                    DarkBgActive = True
                else:
                    UNameActive = False
                    BirdActive = False
                    PlaneActive = False
                    FishActive = False
                    AstrntActive = False
		    SkyBgActive = False
                    SpaceBgActive = False
                    WtrBgActive = False
                    DarkBgActive = False

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

        if BirdActive:
            pygame.draw.rect(screen, WHITE, BirdBorder, 2)
            USERCHOICE = "Bird"
        else:
            pygame.draw.rect(screen, NAVYBLUE, BirdBorder, 2)
        
        if PlaneActive:
            pygame.draw.rect(screen, WHITE, PlaneBorder, 2)
            USERCHOICE = "Plane"
        else:
            pygame.draw.rect(screen, NAVYBLUE, PlaneBorder, 2)

        if FishActive:
            pygame.draw.rect(screen, WHITE, FishBorder, 2)
            USERCHOICE = "Fish"
        else:
            pygame.draw.rect(screen, NAVYBLUE, FishBorder, 2) 
        
        if AstrntActive:
            pygame.draw.rect(screen, WHITE, AstrntBorder, 2)
            USERCHOICE = "Astronaut"
        else:
            pygame.draw.rect(screen, NAVYBLUE, AstrntBorder, 2)
	
	if SkyBgActive:
            pygame.draw.rect(screen, WHITE, SkyBgBorder, 2)
            THEMECHOICE = "Sky"
        else:
            pygame.draw.rect(screen, NAVYBLUE, SkyBgBorder, 2)
	
        if SpaceBgActive:
            pygame.draw.rect(screen, WHITE, SpaceBorder, 2)
            THEMECHOICE = "Space"
        else:
            pygame.draw.rect(screen, NAVYBLUE, SpaceBorder, 2)
	
	if WtrBgActive:
            pygame.draw.rect(screen, WHITE, WtrBorder, 2)
            THEMECHOICE = "UnderWater"
        else:
            pygame.draw.rect(screen, NAVYBLUE, WtrBorder, 2)
        if DarkBgActive:
            pygame.draw.rect(screen, WHITE, DarkBoder, 2)
            THEMECHOICE = "DarkBg"
        else:
            pygame.draw.rect(screen, NAVYBLUE, DarkBoder, 2)

        screen.blit(USERNAMEPrompt, ((SCREENWIDTH - USERNAMEPrompt.get_width()) / 2, (SCREENHEIGHT * .05) + UserNameText.get_height()))
        screen.blit(UserChoicePrompt, ((SCREENWIDTH - UserChoicePrompt.get_width()) / 2, SCREENHEIGHT * .35))

        # User Selection
        UserText = MedFont.render("Users:", True, WHITE)
        screen.blit(UserText, (SCREENWIDTH * .075, SCREENHEIGHT * .45))
        screen.blit(BIRDIMAGE, (SCREENWIDTH * .250, SCREENHEIGHT * .45))
        screen.blit(PLANEIMAGE, (SCREENWIDTH * .425, SCREENHEIGHT * .45))
        screen.blit(FISHIMAGE, (SCREENWIDTH * .600, SCREENHEIGHT * .45))
        screen.blit(ASTRNTIMAGE, (SCREENWIDTH * .775, SCREENHEIGHT * .45))

        # Theme Selection
        ThemeText = MedFont.render("Theme:", True, WHITE)
        screen.blit(ThemeText, (SCREENWIDTH * .075, SCREENHEIGHT * .65))
        screen.blit(SKYBG, (SCREENWIDTH * .250, SCREENHEIGHT * .65))
        screen.blit(SPACEBG, (SCREENWIDTH * .425, SCREENHEIGHT * .65))
        screen.blit(WTRBG, (SCREENWIDTH * .600, SCREENHEIGHT * .65))
        screen.blit(DARKBG, (SCREENWIDTH * .775, SCREENHEIGHT * .65))
	
        submitButtton = Button((SCREENWIDTH / 2) - (StartGame.get_width() / 2) - 5, SCREENHEIGHT * .9,StartGame.get_width() + 10, StartGame.get_height(), MEDUIMBLUE, NAVYBLUE)

        screen.blit(StartGame, ((SCREENWIDTH / 2) - (StartGame.get_width() / 2), int(SCREENHEIGHT * .9)))

        if submitButtton:
            if NEWUSER != "":
                USERNAME = NEWUSER
                UserData['USERNAME'] = USERNAME
            else:
                USERNAME = 'GuestUser'
                UserData['USERNAME'] = USERNAME
            if USERCHOICE != "":
                UserData['USERCHOICE'] = USERCHOICE
            else:
                USERCHOICE = 'Bird'
                UserData['USERCHOICE'] = USERCHOICE
            if THEMECHOICE != "":
                UserData['THEMECHOICE'] = THEMECHOICE
            else:
                THEMECHOICE = 'Sky'
                UserData['THEMECHOICE'] = THEMECHOICE

            SuccessScreen(USERNAME, USERCHOICE, THEMECHOICE)

        pygame.display.update()
        clock.tick(FPS / 4)

def SuccessScreen(USERNAME, USERCHOICE, THEMECHOICE):
    TitleText = SmallFont.render(TITLE, True, MEDUIMBLUE)

    while True:
        screen.fill((105,213,238))
        screen.blit(TitleText, ((SCREENWIDTH - TitleText.get_width()) / 2, 0))

        DText("Hello, " + USERNAME + ".", SCREENWIDTH * 0.5, SCREENHEIGHT * 0.25)
        DText("Your User Choice is: " + USERCHOICE + ".", SCREENWIDTH * 0.5, SCREENHEIGHT * 0.375)
        DText("Your Theme Choice is: " + THEMECHOICE + ".", SCREENWIDTH * 0.5, SCREENHEIGHT * 0.5)
        DText("Press 'space' key to play game or 'esc' key to return Home.", SCREENWIDTH * 0.5, SCREENHEIGHT * 0.625)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                UserData.close()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
		if event.key == pygame.K_1:
                    mixer.music.load('assets/audio/SoftPiano.wav')
                    mixer.music.play()
                if event.key == pygame.K_2:
                    mixer.music.load('assets/audio/summer.ogg')
                    mixer.music.play()
                if event.key == pygame.K_3:
                    mixer.music.load('assets/audio/FridayNight.wav')
                    mixer.music.play()
                if event.key == pygame.K_4:
                    mixer.music.load('assets/audio/Symphony.wav')
                    mixer.music.play()
                if event.key == pygame.K_5:
                    mixer.music.stop()
                if event.key == pygame.K_SPACE:
                    MainGame(USERNAME, USERCHOICE, THEMECHOICE)
                elif event.key == pygame.K_ESCAPE:
                    UserData.clear()
                    WelcomePage()

        pygame.display.update()
        clock.tick(FPS / 4)

# Game loop
while True:
    WelcomePage()

