# Import Pygame and random modules.
import random                        # For random objects(Pipes,Coins)
import pygame                        # Library for Game.
from pygame.locals import *
pygame.init()                        # Initialize all the 7 modules in pygame.
player_x = 480                       # Bird Initial_X co-ordinate.
player_y = 240                       # Bird Initial_Y co-ordinate.


# Lists for Store Rectangular Coordinates of Silver,Gold Coins.
Coin_List = []                        # Co-ordinates for Gold Coins.
S_coin_List=[]                        # Co-ordinates for Silver Coins.

# Main Game Window.
screen = pygame.display.set_mode((1280, 720))
#Importing sound for the game.
die_sound = pygame.mixer.Sound('Gallery\\die.wav')
hit_sound = pygame.mixer.Sound('Gallery\\hit.wav')
point_sound = pygame.mixer.Sound('Gallery\\point.wav')
wing_sound = pygame.mixer.Sound('Gallery\\wing.wav')
Golden_sound = pygame.mixer.Sound('Gallery\\G_collection.mp3')
Silver_sound = pygame.mixer.Sound('Gallery\\S_collection.mp3')

# Set timer for Gold Coins
Coin_Timer = pygame.USEREVENT                       # USEREVENT To create our own event.
pygame.time.set_timer(Coin_Timer, 4000)             # Own enent set timer for Gold_Coins.

# Set timer for Silver Coins

# Create Font for Silver and Gold Coins.
Text_Font_G = pygame.font.SysFont("Times New Roman",40 )
Text_Font_S = pygame.font.SysFont("Times New Roman",40)
Text_Font_Tg = pygame.font.SysFont("Times New Roman",40)
Text_Font_Ts = pygame.font.SysFont("Times New Roman",40)
Text_Font_L = pygame.font.SysFont("Times New Roman",50)
Text_Font_Points = pygame.font.SysFont("Times New Roman",35)
Text_Font_B_Points = pygame.font.SysFont("Times New Roman",35)



# Load All images.
coin_img = pygame.image.load("Gallery\\coin.png").convert_alpha()              # Load Coin Image.
player = pygame.image.load('Gallery\\bird1.png').convert_alpha()                # Load Bird Image.
S_coin= pygame.image.load("Gallery\\Silver.png").convert_alpha()              # Load S_coin_Image.
base = pygame.image.load('Gallery\\base.jpg ').convert_alpha()                #Load base Image.
pipe = pygame.image.load('Gallery\\pipe.png').convert_alpha()                 #Loading the Image of pipe.

#Rotating the pipes according to need.
pipe1 = pipe
pipe2 = pygame.transform.rotate(pipe, 180)
pipe3 = pygame.transform.rotate(pipe, 30)
pipe4 = pygame.transform.rotate(pipe, 210)
pipe5 = pygame.transform.rotate(pipe, 330)
pipe6 = pygame.transform.rotate(pipe, 150)
#Making mask which will use in collision function.
pipe1_mask = pygame.mask.from_surface(pipe1)
pipe2_mask = pygame.mask.from_surface(pipe2)

#Game_Over = pygame.image.load("Game Over.png")

# Create Rectangular Surface for Bird.
player_rect = player.get_rect(topleft=(player_x, player_y))
player_mask = pygame.mask.from_surface(player)   #Making mask which will be use in collision function.


# Create Rectangular Surface for Silver and Gold coins.
def Rect_Coins():
    Coin_Y = random.randint(40, 600)
    Coins = coin_img.get_rect(center=(1000, Coin_Y))
    return (Coins)

def Rect_S_Coins():
    S_Coin_Y = random.randint(200, 500)
    S_Coin = S_coin.get_rect(center=(800+1000, S_Coin_Y))
    return S_Coin



# Move Gold Coins Towards left.
def Move_Coins(coins):
    for coin in coins:
        coin.centerx -= 2
    return coins
# Move Silver Coins Towards left.
def Move_S_Coins(S_Coin_List):
    for S_Coin in S_Coin_List:
        S_Coin.centerx-=2
    return  S_Coin_List

# Blit Golden coins on main game window on rectangular surface.
def Draw_Coins(coins):
    for coin in coins:
        screen.blit(coin_img, coin)
# Blit Golden coins on main game window on rectangular surface..
def Draw_S_Coins(S_coins):
    for coin in S_coins:
        screen.blit(S_coin,coin)

# This function will handle the movement mechanics of silver and Golden coins.
def Mov_Mechanics(Coin_List,S_coin_List):
    Coin_List = Move_Coins(Coin_List)
    S_coin_List = Move_S_Coins(S_coin_List)

#This function will draw both silver and golden coins on screen.
def Objects(Coin_List,S_coin_List):
    Draw_Coins(Coin_List)
    Draw_S_Coins(S_coin_List)


