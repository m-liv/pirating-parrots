import pygame
import random
from datetime import datetime
import pytz
pygame.mixer.pre_init(44100, 16,2,4096)

#initialize the pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))

#music
pygame.mixer.music.load("song.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)
cdsound = pygame.mixer.Sound("cdsound2.mp3")
dsound = pygame.mixer.Sound("deathsound2.mp3")

#time
tz_NY = pytz.timezone('America/New_York')
tz_JP = pytz.timezone('Japan')
tz_LA = pytz.timezone('America/Los_Angeles')
datetime_NY = datetime.now(tz_JP)
h = datetime_NY.strftime("%H")
hour = int(h)
clock = pygame.time.Clock()

#background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
if hour >= 6 and hour < 18:
    image = "daybeach.png"
elif hour >= 18 and hour < 20:
    image = "sunsetbeach.png"
else:
    image = "nightbeach.png"
BackGround = Background(image, [0,0])

#Title
pygame.display.set_caption("Pirating Parrots")

#Player
playerImg = pygame.image.load("right1.png")
DEFAULT_IMAGE_SIZE = (50, 70)
playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)
playerX = 300
playerY = 350
xChange = 0
yChange = 0
images1 = ["left1.png","left2.png","left3.png"]
images2 = ["right1.png","right2.png","right3.png"]
images3 = ["front1.png","front2.png","front3.png"]
images4 = ["back1.png","back2.png","back3.png"]
counter = 0

#movie
movie1 = pygame.image.load("cd.png")
x1 = -10000
y1 = -10000
DEFAULT_IMAGE_SIZE = (50, 50)
movie1 = pygame.transform.scale(movie1, DEFAULT_IMAGE_SIZE)

movie2 = pygame.image.load("cd.png")
x2 = -10000
y2 = -10000
movie2 = pygame.transform.scale(movie2, DEFAULT_IMAGE_SIZE)

movie3 = pygame.image.load("cd.png")
x3 = -10000
y3 = -10000
movie3 = pygame.transform.scale(movie3, DEFAULT_IMAGE_SIZE)

movie4 = pygame.image.load("cd.png")
x4 = -10000
y4 = -10000
movie4 = pygame.transform.scale(movie4, DEFAULT_IMAGE_SIZE)

movie5 = pygame.image.load("cd.png")
x5 = -10000
y5 = -10000
movie5 = pygame.transform.scale(movie5, DEFAULT_IMAGE_SIZE)

movie6 = pygame.image.load("cd.png")
x6 = -10000
y6 = -10000
movie6 = pygame.transform.scale(movie6, DEFAULT_IMAGE_SIZE)

movie7 = pygame.image.load("cd.png")
x7 = -10000
y7 = -10000
movie7 = pygame.transform.scale(movie7, DEFAULT_IMAGE_SIZE)

movie8 = pygame.image.load("cd.png")
x8 = -10000
y8 = -10000
movie8 = pygame.transform.scale(movie8, DEFAULT_IMAGE_SIZE)

#counter
count = 0

#pirate
pirateImg = pygame.image.load("pirate.png")
DEFAULT_IMAGE_SIZE = (60, 80)
pirateImg = pygame.transform.scale(pirateImg, DEFAULT_IMAGE_SIZE)
pirateX = -100000000
pirateY = -100000000
xPChange = 0
yPChange = 0
steps = 0
steps2 = 0

#NPC Elizabeth
playerImg2 = pygame.image.load("NPC1.png")
DEFAULT_IMAGE_SIZE = (60, 70)
playerImg2 = pygame.transform.scale(playerImg2, DEFAULT_IMAGE_SIZE)
NPCX = 400
NPCY = 350

#Elizabeth Dialogue
#dialogue = pygame.image.load("Intro1Dialogue.png")

dialogue3 = pygame.image.load("Intro3Dialogue.png")
dialogue2 = pygame.image.load("Intro2Dialogue.png")
dialogue = pygame.image.load("Intro1Dialogue.png")

DEFAULT_IMAGE_SIZE = (600, 200)
dialogue = pygame.transform.scale(dialogue, DEFAULT_IMAGE_SIZE)
dialogue2 = pygame.transform.scale(dialogue2, DEFAULT_IMAGE_SIZE)
dialogue3 = pygame.transform.scale(dialogue3, DEFAULT_IMAGE_SIZE)

dialogueX = 100
dialogueY = 400

#Interstellar Dialogue
interstellarDialogue = pygame.image.load("InterstellarDialogue.png")
DEFAULT_IMAGE_SIZE = (600, 200)
interstellarDialogue = pygame.transform.scale(interstellarDialogue, DEFAULT_IMAGE_SIZE)
interstellarX = -10000
interstellarY = -10000

#agree and disagree
agree = pygame.image.load("Agree.png")
agreeX = -1000
agreeY = -1000
disagreeX = -1000
disagreeY = -1000
DEFAULT_IMAGE_SIZE = (80, 30)
agree = pygame.transform.scale(agree, DEFAULT_IMAGE_SIZE)
disagree = pygame.image.load("disagree.png")
DEFAULT_IMAGE_SIZE = (80, 30)
disagree = pygame.transform.scale(disagree, DEFAULT_IMAGE_SIZE)

#makes it so sprites x and y values can change
def player(x, y):
    screen.blit(playerImg, (x, y))
def playerNPC(x, y):
    screen.blit(playerImg2, (x, y))
def playerDialogue(x, y):
    screen.blit(dialogue, (x, y))
def accept(x, y):
    screen.blit(agree, (x, y))
def decline(x, y):
    screen.blit(disagree, (x, y))
def pirate(x, y):
    screen.blit(pirateImg, (x, y))
def movie1CC(x, y):
    screen.blit(movie1, (x, y))
def movie2CC(x, y):
    screen.blit(movie2, (x, y))
def movie3CC(x, y):
    screen.blit(movie3, (x, y))
def interstellarCC(x, y):
    screen.blit(interstellarDialogue, (x, y))
def movie4CC(x, y):
    screen.blit(movie4, (x, y))
def movie5CC(x, y):
    screen.blit(movie5, (x, y))
def movie6CC(x, y):
    screen.blit(movie6, (x, y))
def movie7CC(x, y):
    screen.blit(movie7, (x, y))
def movie8CC(x, y):
    screen.blit(movie8, (x, y))

running = True
notdead = True
while running:
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    movie1CC(x1, y1)
    movie2CC(x2, y2)
    movie3CC(x3, y3)
    movie4CC(x4, y4)
    movie5CC(x5, y5)
    movie6CC(x6, y6)
    movie7CC(x7, y7)
    movie8CC(x8, y8)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                xChange = -5
                playerImg = pygame.image.load(images1[counter])
                DEFAULT_IMAGE_SIZE = (50, 70)
                playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)
                counter = (counter + 1) % len(images1)
            if event.key == pygame.K_RIGHT:
                xChange = 5
                playerImg = pygame.image.load(images2[counter])
                DEFAULT_IMAGE_SIZE = (50, 70)
                playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)
                counter = (counter + 1) % len(images1)
            if event.key == pygame.K_UP:
                yChange = -5
                playerImg = pygame.image.load(images4[counter])
                DEFAULT_IMAGE_SIZE = (50, 70)
                playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)
                counter = (counter + 1) % len(images4)
            if event.key == pygame.K_DOWN:
                yChange = 5
                playerImg = pygame.image.load(images3[counter])
                DEFAULT_IMAGE_SIZE = (50, 70)
                playerImg = pygame.transform.scale(playerImg, DEFAULT_IMAGE_SIZE)
                counter = (counter + 1) % len(images3)
            if event.key == pygame.K_SPACE:
                running = False
        if event.type == pygame.KEYUP:
            xChange = 0
            yChange = 0

        #checks if player hit pirate
        pirateRect = pirateImg.get_rect(topleft = (pirateX, pirateY))
        playerRect = playerImg.get_rect(topleft = (playerX, playerY))
        if pirateRect.colliderect(playerRect):
            pygame.mixer.Sound.play(dsound)
            pirateX = -10000
            pirateY = -10000
            steps = 0.1
            steps2 = 0.1
            NPCX = 0
            NPCY = 0
            playerImg2 = pygame.image.load("youDied.png")
            DEFAULT_IMAGE_SIZE = (800, 600)
            playerImg2 = pygame.transform.scale(playerImg2, DEFAULT_IMAGE_SIZE)
            x1 = -10000
            y1 = -10000
            x2 = -10000
            y2 = -10000
            x3 = -10000
            y3 = -10000
            quitX = 450
            quitY = 400
            #running = False
        #checks if player hit movie part
        movie1Rect = movie1.get_rect(topleft = (x1, y1))
        movie2Rect = movie2.get_rect(topleft = (x2, y2))
        movie3Rect = movie3.get_rect(topleft = (x3, y3))
        movie4Rect = movie4.get_rect(topleft = (x4, y4))
        movie5Rect = movie5.get_rect(topleft = (x5, y5))
        movie6Rect = movie6.get_rect(topleft = (x6, y6))
        movie7Rect = movie7.get_rect(topleft = (x7, y7))
        movie8Rect = movie8.get_rect(topleft = (x8, y8))
        if playerRect.colliderect(movie1Rect):
            pygame.mixer.Sound.play(cdsound)
            x1 = -10000
            y1 = -10000
            movie1Rect = movie1.get_rect(topleft = (x1, y1))
            count+=1
        elif playerRect.colliderect(movie2Rect):
            pygame.mixer.Sound.play(cdsound)
            x2 = -10000
            y2 = -10000
            movie2Rect = movie2.get_rect(topleft = (x2, y2))
            count+=1
        elif playerRect.colliderect(movie3Rect):
            pygame.mixer.Sound.play(cdsound)
            x3 = -10000
            y3 = -10000
            movie3Rect = movie3.get_rect(topleft = (x3, y3))
            count+=1
        elif playerRect.colliderect(movie4Rect):
            pygame.mixer.Sound.play(cdsound)
            x4 = -10000
            y4 = -10000
            movie4Rect = movie4.get_rect(topleft = (x4, y4))
            count+=1
        elif playerRect.colliderect(movie5Rect):
            pygame.mixer.Sound.play(cdsound)
            x5 = -10000
            y5 = -10000
            movie5Rect = movie5.get_rect(topleft = (x5, y5))
            count+=1
        elif playerRect.colliderect(movie6Rect):
            pygame.mixer.Sound.play(cdsound)
            x6 = -10000
            y6 = -10000
            movie6Rect = movie6.get_rect(topleft = (x6, y6))
            count+=1
        elif playerRect.colliderect(movie7Rect):
            pygame.mixer.Sound.play(cdsound)
            x7 = -10000
            y7 = -10000
            movie7Rect = movie7.get_rect(topleft = (x7, y7))
            count+=1
        elif playerRect.colliderect(movie8Rect):
            pygame.mixer.Sound.play(cdsound)
            x8 = -10000
            y8 = -10000
            movie8Rect = movie8.get_rect(topleft = (x8, y8))
            count+=1
        #checks if 3 movies have been hit and then shows interstellar textbox
        if count ==1:
            interstellarX = 100
            interstellarY = 400
        if count ==3:
            interstellarDialogue = pygame.image.load("JackDialogue.png") #change to Jack
            DEFAULT_IMAGE_SIZE = (600, 200)
            interstellarDialogue = pygame.transform.scale(interstellarDialogue, DEFAULT_IMAGE_SIZE)
        if count == 5:
            interstellarDialogue = pygame.image.load("Fact1Dialogue.png")
            DEFAULT_IMAGE_SIZE = (600, 200)
            interstellarDialogue = pygame.transform.scale(interstellarDialogue, DEFAULT_IMAGE_SIZE)
        if count == 7:
            interstellarDialogue = pygame.image.load("Fact2Dialogue.png")
            DEFAULT_IMAGE_SIZE = (600, 200)
            interstellarDialogue = pygame.transform.scale(interstellarDialogue, DEFAULT_IMAGE_SIZE)
        if count == 8:
            pirateX = -10000
            pirateY = -10000
            steps = 0.1
            steps2 = 0.1
            NPCX = 400
            NPCY = 350
            interstellarDialogue = pygame.image.load("endingDialogue.png")
            DEFAULT_IMAGE_SIZE = (600, 200)
            interstellarDialogue = pygame.transform.scale(interstellarDialogue, DEFAULT_IMAGE_SIZE)
            quitX = 400
            quitY = 200
    #checks is user is pressing mouse down
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Set the x, y positions of the mouse click
        dialogueRect = dialogue.get_rect(topleft = (dialogueX, dialogueY))
        agreeRect = agree.get_rect(topleft = (agreeX,agreeY))
        disagreeRect = disagree.get_rect(topleft = (disagreeX,disagreeY))
        x, y = event.pos
        if dialogueRect.collidepoint(x,y):
            l, m = event.pos
            dialogue = dialogue2
            if dialogueRect.collidepoint(l,m):
                j, k = event.pos
                dialogue = dialogue3
                n, o = event.pos
                agreeX = 430
                agreeY = 535
                disagreeX = 550
                disagreeY = 535
                if agreeRect.collidepoint(n, o):
                    #moves NPC, dialogue, agree button, and disagree button off screen
                    NPCX = -1000
                    NPCY = -1000
                    dialogueX = -1000
                    dialogueY = -1000
                    agreeX = -1000
                    agreeY = -1000
                    disagreeX = -1000
                    disagreeY = -1000
                    #randomly generates pirate x and y position
                    pirateX = random.randint(0, 550)
                    pirateY = random.randint(0,750)
                    #sets x and y positins of movies randomly
                    x1 = random.randint(0,750)
                    y1 = random.randint(0,550)
                    x2 = random.randint(0,750)
                    y2 = random.randint(0,550)
                    x3 = random.randint(0,750)
                    y3 = random.randint(0,550)
                    x4 = random.randint(0,750)
                    y4 = random.randint(0,550)
                    x5 = random.randint(0,750)
                    y5 = random.randint(0,550)
                    x6 = random.randint(0,750)
                    y6 = random.randint(0,550)
                    x7 = random.randint(0,750)
                    y7 = random.randint(0,550)
                    x8 = random.randint(0,750)
                    y8 = random.randint(0,550)
                elif disagreeRect.collidepoint(x,y):
                    #changes dialogue to show Rejection Dialogue
                    dialogue = pygame.image.load("RejectionDialogue.png")
                    DEFAULT_IMAGE_SIZE = (600, 200)
                    dialogue = pygame.transform.scale(dialogue, DEFAULT_IMAGE_SIZE)
    #makes player move smoothly
    playerX += xChange
    playerY += yChange
    pirateX += steps
    pirateY += steps2
    #makes sure player is in bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750
    if playerY <=0:
        playerY = 0
    elif playerY >=530:
        playerY = 530
    #makes sure pirate is in bounds
    if pirateX <= 0:
        steps = 3
    elif pirateX >= 750:
        steps = -3
    if pirateY <= 0:
        steps2 = 3
    elif pirateY >= 550:
        steps2 = -3
    #updates position of player, pirate, dialogue, agree button, and disagree button
    player(playerX, playerY)
    pirate(pirateX, pirateY)
    playerDialogue(dialogueX, dialogueY)
    accept(agreeX, agreeY)
    decline(disagreeX, disagreeY)
    interstellarCC(interstellarX, interstellarY)
    playerNPC(NPCX, NPCY)
    #refreshes screen
    pygame.display.update()
    clock.tick(60)

