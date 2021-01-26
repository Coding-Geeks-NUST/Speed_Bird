import sys, random  # Import sys module to Quit our game.
import pygame  # import pygame Library.
from pygame.locals import *

from os.path import isfile

pygame.init()  # Initialize All the modules in pygame
clock = pygame.time.Clock()  # Set a clock to control Frame/Seconds of moving objects.
pygame.display.set_caption('  Speed Bird')
# Main Game Window.
screen = pygame.display.set_mode((1280, 720))


def background_change(click_sound, dict_data):
    """This is the function which shows the background menu to the user from where he can change the background.
    In this function the background will be unlocked on the basis of the Golden coins collected by the user. The user
    will not able to choose locked background. There is a back button from where the user can exit the background menu."""

    run = True  # Initializing a variable which will be used to exit the player selection menu.
    Click = False  # Initializing a Variable to check the state of the click button.

    G_coins = dict_data['Score_G']
    while run:
        # Importing the images for the backgroung menu.
        welcome_screen = pygame.image.load('Gallery\\welcome.png').convert_alpha()
        screen.blit(welcome_screen, (0, 0))
        back_img = pygame.image.load('Gallery\\Back.png')
        text_img = pygame.image.load('Gallery\\text.png')
        bg1 = pygame.image.load('Gallery\\bg1s.png')
        bg2 = pygame.image.load('Gallery\\bg2s.jpg')
        bg3 = pygame.image.load('Gallery\\bg3s.jpg')
        bg4 = pygame.image.load('Gallery\\bg4s.jpg')
        bg5 = pygame.image.load('Gallery\\bg5s.jpg')
        bg6 = pygame.image.load('Gallery\\bg6s.jpg')
        lock_img = pygame.image.load('Gallery\\lock.png')

        # making a rectangle and giving the position by using rect function.
        back_img_rect = back_img.get_rect(topleft=(1080, 620))
        text_rect = text_img.get_rect(topleft=(400, 550))
        bg1_rect = bg1.get_rect(topleft=(50, 450))
        bg2_rect = bg2.get_rect(topleft=(250, 450))
        bg3_rect = bg3.get_rect(topleft=(450, 450))
        bg4_rect = bg4.get_rect(topleft=(650, 450))
        bg5_rect = bg5.get_rect(topleft=(850, 450))
        bg6_rect = bg6.get_rect(topleft=(1050, 450))

        # Bliting the images on the required position.
        screen.blit(back_img, back_img_rect)
        screen.blit(text_img, text_rect)
        screen.blit(bg1, bg1_rect)
        screen.blit(bg2, bg2_rect)
        screen.blit(bg3, bg3_rect)
        screen.blit(bg4, bg4_rect)
        screen.blit(bg5, bg5_rect)
        screen.blit(bg6, bg6_rect)
        pygame.display.update()
        # Getting the mouse position and checking its status.
        mx, my = pygame.mouse.get_pos()
        if back_img_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                run = False
        # Applying if else condition to blit the lock image on the locked background.
        if G_coins < 200:
            screen.blit(lock_img, bg2_rect)
            screen.blit(lock_img, bg3_rect)
            screen.blit(lock_img, bg4_rect)
            screen.blit(lock_img, bg5_rect)
            screen.blit(lock_img, bg6_rect)

        elif G_coins < 400:
            screen.blit(lock_img, bg3_rect)
            screen.blit(lock_img, bg4_rect)
            screen.blit(lock_img, bg5_rect)
            screen.blit(lock_img, bg6_rect)
        elif G_coins < 600:
            screen.blit(lock_img, bg4_rect)
            screen.blit(lock_img, bg5_rect)
            screen.blit(lock_img, bg6_rect)
        elif G_coins < 800:
            screen.blit(lock_img, bg5_rect)
            screen.blit(lock_img, bg6_rect)
        elif G_coins < 1000:
            screen.blit(lock_img, bg6_rect)

        # Using if else condition to allow the user to only click on the unlocked background.
        if G_coins < 200:
            if bg1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg1'
        elif G_coins < 400:
            if bg1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg1'
            if bg2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg2'
        elif G_coins < 600:
            if bg1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg1'
            if bg2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg2'
            if bg3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg3'
        elif G_coins < 800:
            if bg1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg1'
            if bg2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg2'
            if bg3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg3'
            if bg4_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg4'
        elif G_coins < 1000:
            if bg1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg1'
            if bg2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg2'
            if bg3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg3'
            if bg4_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg4'
            if bg5_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg5'
        else:
            if bg1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg1'
            if bg2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg2'
            if bg3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg3'
            if bg4_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg4'
            if bg5_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg5'
            if bg6_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bg6'
        # To change the state of the click variable depending on the user input and exiting the menu by escape button.
        Click = False
        for item in pygame.event.get():
            if item.type == MOUSEBUTTONDOWN:
                if item.button == 1:
                    Click = True
        pygame.display.update()


def Change_bird(click_sound, dict_data):
    """This is the function which shows the players menu to the user from where he can change the bird.
    In this function the bird will be unlocked on the basis of the Silver coins collected by the user. The user
    will not able to choose locked birds. There is a back button from where the user can exit the player selection menu."""

    run = True  # Initializing a variable which will be used to exit the player selection menu.
    Click = False  # Initializing a Variable to check the state of the click button.

    S_coins = dict_data['Score_S']
    while run:
        # Importing images for the player selection menu.
        welcome_screen = pygame.image.load('Gallery\\welcome.png').convert_alpha()
        screen.blit(welcome_screen, (0, 0))
        back_img = pygame.image.load('Gallery\\Back.png')
        text_img = pygame.image.load('Gallery\\text_b.png')
        bird1 = pygame.image.load('Gallery\\bird1.png')
        bird2 = pygame.image.load('Gallery\\bird2.png')
        bird3 = pygame.image.load('Gallery\\bird3.png')
        bird4 = pygame.image.load('Gallery\\bird4.png')
        bird5 = pygame.image.load('Gallery\\bird5.png')
        bird6 = pygame.image.load('Gallery\\bird6.png')
        lock_img = pygame.image.load('Gallery\\locks.png')
        # making a rectangle and giving the position by using rect function.
        back_img_rect = back_img.get_rect(topleft=(1080, 620))
        text_rect = text_img.get_rect(topleft=(400, 550))
        bird1_rect = bird1.get_rect(topleft=(50, 450))
        bird2_rect = bird2.get_rect(topleft=(250, 450))
        bird3_rect = bird3.get_rect(topleft=(450, 450))
        bird4_rect = bird4.get_rect(topleft=(650, 450))
        bird5_rect = bird5.get_rect(topleft=(850, 450))
        bird6_rect = bird6.get_rect(topleft=(1050, 450))

        # Bliting the images on the required position.
        screen.blit(back_img, back_img_rect)
        screen.blit(text_img, text_rect)
        screen.blit(bird1, bird1_rect)
        screen.blit(bird2, bird2_rect)
        screen.blit(bird3, bird3_rect)
        screen.blit(bird4, bird4_rect)
        screen.blit(bird5, bird5_rect)
        screen.blit(bird6, bird6_rect)
        pygame.display.update()

        # Getting the mouse position and checking its status.
        mx, my = pygame.mouse.get_pos()
        if back_img_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                run = False

        # Applying if else condition to blit the lock image on the locked player.
        if S_coins < 200:
            screen.blit(lock_img, bird2_rect)
            screen.blit(lock_img, bird3_rect)
            screen.blit(lock_img, bird4_rect)
            screen.blit(lock_img, bird5_rect)
            screen.blit(lock_img, bird6_rect)

        elif S_coins < 400:
            screen.blit(lock_img, bird3_rect)
            screen.blit(lock_img, bird4_rect)
            screen.blit(lock_img, bird5_rect)
            screen.blit(lock_img, bird6_rect)
        elif S_coins < 600:
            screen.blit(lock_img, bird4_rect)
            screen.blit(lock_img, bird5_rect)
            screen.blit(lock_img, bird6_rect)
        elif S_coins < 800:
            screen.blit(lock_img, bird5_rect)
            screen.blit(lock_img, bird6_rect)
        elif S_coins < 1000:
            screen.blit(lock_img, bird6_rect)

        # Using if else condition to allow the user to only click on the unlocked background.
        if S_coins < 200:
            if bird1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird1'
        elif S_coins < 400:
            if bird1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird1'
            if bird2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird2'
        elif S_coins < 600:
            if bird1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird1'
            if bird2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird2'
            if bird3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird3'
        elif S_coins < 800:
            if bird1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird1'
            if bird2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird2'
            if bird3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird3'
            if bird4_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird4'
        elif S_coins < 1000:
            if bird1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird1'
            if bird2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird2'
            if bird3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird3'
            if bird4_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird4'
            if bird5_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird5'
        else:
            if bird1_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird1'
            if bird2_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird2'
            if bird3_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird3'
            if bird4_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird4'
            if bird5_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird5'
            if bird6_rect.collidepoint(mx, my):
                if Click:
                    click_sound.play()
                    return 'bird6'
        # To change the state of the click variable depending on the user input and exiting the menu by escape button.
        Click = False
        for item in pygame.event.get():
            if item.type == MOUSEBUTTONDOWN:
                if item.button == 1:
                    Click = True
        pygame.display.update()


def Sure(click_sound):
    '''This function will show the warning to the user before quiting the game.'''
    run = True  # Initializing a variable which will be used to exit the player selection menu.
    Click = False  # Initializing a Variable to check the state of the click button.
    while run:
        # Importing images for the button options.
        welcome_screen = pygame.image.load('Gallery\\welcome.png').convert_alpha()
        screen.blit(welcome_screen, (0, 0))
        Sure_button = pygame.image.load('Gallery\\sure.png').convert_alpha()
        yes_button = pygame.image.load('Gallery\\Yes.png').convert_alpha()
        No_button = pygame.image.load('Gallery\\No.png').convert_alpha()

        # Making the rectangles around the buttons and giving the position using the rect function.
        Sure_button_rect = Sure_button.get_rect(topleft=(500, 400))
        yes_button_rect = yes_button.get_rect(topleft=(540, 500))
        No_button_rect = No_button.get_rect(topleft=(670, 500))

        # Getting the position of the mouse.
        mx, my = pygame.mouse.get_pos()
        if yes_button_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                pygame.quit()
                sys.exit()
        if No_button_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                welcome_function()
        # To change the state of the click variable depending on the user input and exiting the menu by escape button.
        Click = False
        for item in pygame.event.get():
            if item.type == MOUSEBUTTONDOWN:
                if item.button == 1:
                    Click = True
        screen.blit(Sure_button, Sure_button_rect)
        screen.blit(yes_button, yes_button_rect)
        screen.blit(No_button, No_button_rect)

        pygame.display.update()


def welcome_function():
    '''The is the function which shows the menu to the user from where he can go into the change background menu,
     the player selection menu, go into exit menu and can play the game.'''

    # Importing images of the buttons, welcome screen and the sounds.
    welcome_screen = pygame.image.load('Gallery\\welcome.png').convert_alpha()
    bg_button = pygame.image.load('Gallery\\bg_change.png').convert_alpha()
    play_button = pygame.image.load('Gallery\\play.png').convert_alpha()
    player_button = pygame.image.load('Gallery\\bird_change.png').convert_alpha()
    Exit_button = pygame.image.load('Gallery\\Exit.png').convert_alpha()
    click_sound = pygame.mixer.Sound('Gallery\\click.mp3')

    # Making the rectangles around the button and giving them the condition by using rect function.
    bg_button_rect = bg_button.get_rect(topleft=(120, 430))
    player_button_rect = player_button.get_rect(topleft=(900, 430))
    play_button_rect = play_button.get_rect(topleft=(570, 430))
    Exit_button_rect = Exit_button.get_rect(topleft=(1080, 620))

    welcome = True  # Initializing a variable which will be used to exit the welcome menu.
    Click = False  # Initializing a Variable to check the state of the click button.
    bg = 'bg1'
    bird = 'bird1'
    while welcome:
        if isfile("Gallery\\file.txt"):  # Checking the presence of the score file.
            file = open("Gallery\\file.txt")
            data = file.readline()
            dict_data = eval(data)
            file.close()
        else:
            dict_data = {'Score_G': 0, 'Score_S': 0, 'Score_M': 0}
            data = str(dict_data)
            file = open("Gallery\\file.txt", "x")  # If the file is not present then making a new file.
            file.writelines(data)
            file.close()

        Store_G, Store_S, M_points = dict_data['Score_G'], dict_data['Score_S'], dict_data['Score_M']

        mx, my = pygame.mouse.get_pos()  # Getting the mouse position.

        # Checking the mouse position and the click status to enter in the required menu.
        if play_button_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                Game(bg, bird, dict_data)
        if bg_button_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                bg = background_change(click_sound, dict_data)

        if player_button_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                bird = Change_bird(click_sound, dict_data)
        if Exit_button_rect.collidepoint(mx, my):
            if Click:
                click_sound.play()
                Sure(click_sound)

        # Getting the events from the pygame and doing the tasks.
        Click = False
        for item in pygame.event.get():
            if item.type == pygame.KEYDOWN:
                if item.key == pygame.K_SPACE:
                    Game(bg, bird, dict_data)
            if item.type == MOUSEBUTTONDOWN:
                if item.button == 1:
                    Click = True
        Text_Font_Tg = pygame.font.SysFont("Times New Roman", 40)
        Text_Font_Ts = pygame.font.SysFont("Times New Roman", 40)
        # Bliting the welcome image and on that Showing different buttons and the scores.
        screen.blit(welcome_screen, (0, 0))
        screen.blit(bg_button, bg_button_rect)
        Text_Msg_Tg = Text_Font_Tg.render(f"Gold   coins ={Store_G} ", True, (255, 255, 255))  # Total Gold Coins
        Text_Msg_Ts = Text_Font_Ts.render(f"Silver coins ={Store_S} ", True, (255, 255, 255))  # Total Silver Coins
        screen.blit(Text_Msg_Tg, (950, 3))  # Blit Gold coin Msg+value on screen
        screen.blit(Text_Msg_Ts, (950, 35))  # Blit Silver coin Msg+value on screen
        screen.blit(player_button, player_button_rect)
        screen.blit(play_button, play_button_rect)
        screen.blit(Exit_button, Exit_button_rect)
        pygame.display.update()


# D_Store = {}                                                                           # Empty Dic store Scores.
def Game(bg, bird, dict_data):
    '''This is our main game in which we are calling different function according to need and bliting all the images.
    In this function we are playing sounds ,counting scores ,storing in the file, moving images, checking collision
    collection of coins and incresing speed.'''

    # Importing the images of the backgrounds.
    bg1 = pygame.image.load('Gallery\\bg1.png').convert_alpha()
    bg2 = pygame.image.load('Gallery\\bg2.jpg').convert_alpha()
    bg3 = pygame.image.load('Gallery\\bg3.jpg').convert_alpha()
    bg4 = pygame.image.load('Gallery\\bg4.jpg').convert_alpha()
    bg5 = pygame.image.load('Gallery\\bg5.jpg').convert_alpha()
    bg6 = pygame.image.load('Gallery\\bg6.jpg').convert_alpha()

    # Applying the backgroung according to the cammand from the welcome function.
    if bg == 'bg2':
        background = bg2
    elif bg == 'bg3':
        background = bg3
    elif bg == 'bg4':
        background = bg4
    elif bg == 'bg5':
        background = bg5
    elif bg == 'bg6':
        background = bg6
    else:
        background = bg1

    # Importing images of the birds.
    bird1 = pygame.image.load('Gallery\\bird1.png').convert_alpha()
    bird2 = pygame.image.load('Gallery\\bird2.png').convert_alpha()
    bird3 = pygame.image.load('Gallery\\bird3.png').convert_alpha()
    bird4 = pygame.image.load('Gallery\\bird4.png').convert_alpha()
    bird5 = pygame.image.load('Gallery\\bird5.png').convert_alpha()
    bird6 = pygame.image.load('Gallery\\bird6.png').convert_alpha()

    # Using the bird according to the cammand from the welcome function.
    if bird == 'bird2':
        player = bird2
    elif bird == 'bird3':
        player = bird3
    elif bird == 'bird4':
        player = bird4
    elif bird == 'bird5':
        player = bird5
    elif bird == 'bird6':
        player = bird6
    else:
        player = bird1

    pygame.display.set_icon(bird6)

    # Load All images.
    coin_img = pygame.image.load("Gallery\\coin.png").convert_alpha()  # Load Coin Image.
    S_coin = pygame.image.load("Gallery\\Silver.png").convert_alpha()  # Load S_coin_Image.
    base = pygame.image.load('Gallery\\base.jpg ').convert_alpha()  # Load base Image.
    pipe = pygame.image.load('Gallery\\pipe.png').convert_alpha()  # Loading the Image of pipe.
    # Rotating the pipes according to need.
    pipe1 = pipe
    pipe2 = pygame.transform.rotate(pipe, 180)
    pipe3 = pygame.transform.rotate(pipe, 30)
    pipe4 = pygame.transform.rotate(pipe, 210)
    pipe5 = pygame.transform.rotate(pipe, 330)
    pipe6 = pygame.transform.rotate(pipe, 150)
    # Making mask which will use in collision function.
    pipe1_mask = pygame.mask.from_surface(pipe1)
    pipe2_mask = pygame.mask.from_surface(pipe2)

    player_x = 480  # Bird Initial_X co-ordinate.
    player_y = 240  # Bird Initial_Y co-ordinate.
    # Create Rectangular Surface for Bird.
    player_rect = player.get_rect(topleft=(player_x, player_y))
    player_mask = pygame.mask.from_surface(player)  # Making mask which will be use in collision function.

    # Create Font for Silver and Gold Coins.
    Text_Font_G = pygame.font.SysFont("Times New Roman", 40)
    Text_Font_S = pygame.font.SysFont("Times New Roman", 40)
    Text_Font_L = pygame.font.SysFont("Times New Roman", 50)
    Text_Font_Points = pygame.font.SysFont("Times New Roman", 35)
    Text_Font_B_Points = pygame.font.SysFont("Times New Roman", 35)

    # Importing sound for the game.
    die_sound = pygame.mixer.Sound('Gallery\\die.wav')
    hit_sound = pygame.mixer.Sound('Gallery\\hit.wav')
    point_sound = pygame.mixer.Sound('Gallery\\point.wav')
    wing_sound = pygame.mixer.Sound('Gallery\\wing.wav')
    Golden_sound = pygame.mixer.Sound('Gallery\\G_collection.mp3')
    Silver_sound = pygame.mixer.Sound('Gallery\\S_collection.mp3')

    def Rect_Coins_G():
        # Create Rectangular Surface Gold coins.
        Coin_Y = random.randint(40, 600)
        Coins = coin_img.get_rect(center=(random.randint(2000, 3000), Coin_Y))
        return (Coins)

    def Rect_Coins_S():
        # Create Rectangular Surface Silver coins.
        S_Coin_Y = random.randint(200, 500)
        S_Coin = S_coin.get_rect(center=(random.randint(1280, 2000), S_Coin_Y))
        return S_Coin

    def collision(Type, pipe1_rect, pipe2_rect):
        '''This function will check collision of bird with the pipe. In this function we are using mask function to
        Check collision with pipe.'''

        if player_rect.top <= 0 or player_rect.bottom >= 620:  # Boundry for the game.
            player_rect.y = 240
            collision = 'True'
            return collision

        # Getting the points of the upper and lower pipe from the rect function and the points of the bird.
        pipe1x, pipe1y = pipe1_rect.topleft
        birdx, birdy = player_rect.topleft
        pipe2x, pipe2y = pipe2_rect.topleft
        if Type == 'a':  # Checking the kind of pipe set.
            offset1 = (
                pipe1x - birdx, pipe1y + 5 - birdy)  # Difference of rectangular coodinates of lower pipe and the bird.
            offset2 = (
                pipe2x - birdx,
                birdy - pipe2y - 400)  # Difference of rectangular coodinates of upper pipe and the bird.
            if player_mask.overlap(pipe2_mask, offset2):  # Using mask to check for collision.
                collision = 'True'
            elif player_mask.overlap(pipe1_mask, offset1):  # Using mask to check for collision.
                collision = 'True'
            else:
                collision = 'False'  # Returning false if there is no collision.
            return collision
        if Type == 'b':  # Checking the kind of pipe set.
            offset1 = (pipe1x + 20 - birdx,
                       pipe1y - birdy + 10)  # Difference of rectangular coodinates of lower pipe and the bird.
            offset2 = (pipe2x - birdx + 190,
                       birdy - pipe2y - 360)  # Difference of rectangular coodinates of upper pipe and the bird.
            if player_mask.overlap(pipe2_mask, offset2):  # Using mask to check for collision.
                collision = 'True'
            elif player_mask.overlap(pipe1_mask, offset1):  # Using mask to check for collision.
                collision = 'True'
            else:
                collision = 'False'
            return collision
        else:
            offset1 = (pipe1x + 220 - birdx,
                       pipe1y - birdy + 20)  # Difference of rectangular coodinates of lower pipe and the bird.
            offset2 = (pipe2x - birdx + 20,
                       birdy - pipe2y - 360)  # Difference of rectangular coodinates of upper pipe and the bird.
            if player_mask.overlap(pipe2_mask, offset2):  # Using mask to check for collision.
                collision = 'True'
            elif player_mask.overlap(pipe1_mask, offset1):  # Using mask to check for collision.
                collision = 'True'
            else:
                collision = 'False'
            return collision

    def random_pipes():
        '''This function gives only the coordinates of the random pipes and tell the type of the pipe. '''
        a = random.randint(0, 100)  # getting a random intiger to select the kind of the pipe.
        if a <= 80:  # Applying this condition so that 80 % pipes will be vertical.
            space = 140  # Space between the pipes.
            lower_pipe_x = 1280  # X-coordinate of lower pipe.
            lower_pipe_y = random.randint(240, 550)  # Choosing randomly Y-coordinate.
            pipe1_rect = pipe1.get_rect(topleft=(lower_pipe_x, lower_pipe_y))  # making rect around the pipe.
            upper_pipe_x = 1280  # X-coordinate of upper pipe.
            upper_pipe_y = lower_pipe_y - space - 520  # Choosing Y-coordinates depending on the coordinates of the lower pipe.
            pipe2_rect = pipe2.get_rect(topleft=(upper_pipe_x, upper_pipe_y))  # making rect around the pipe.
            return pipe1_rect, pipe2_rect, 'a'
        else:
            if a % 2 == 0:
                space = 70
                lower_pipe_x = 1280  # X-coordinate of lower pipe.
                lower_pipe_y = random.randint(400, 520)  # Choosing randomly Y-coordinate.
                pipe1_rect = pipe3.get_rect(topleft=(lower_pipe_x, lower_pipe_y))
                upper_pipe_x = 952  # X-coordinate of upper pipe.
                upper_pipe_y = lower_pipe_y - space - 520
                pipe2_rect = pipe4.get_rect(topleft=(upper_pipe_x, upper_pipe_y))  # making rect around the pipe.
                return pipe1_rect, pipe2_rect, 'b'  # returning the rects and the type of the pipe.
            else:
                space = 70
                lower_pipe_x = 951  # X-coordinate of lower pipe.
                lower_pipe_y = random.randint(400, 520)  # Choosing randomly Y-coordinate.
                pipe1_rect = pipe5.get_rect(topleft=(lower_pipe_x, lower_pipe_y))  # making rect around the pipe.
                upper_pipe_x = 1280  # X-coordinate of upper pipe.
                upper_pipe_y = lower_pipe_y - space - 520  # Choosing Y-coordinates depending on the coordinates of the lower pipe.
                pipe2_rect = pipe6.get_rect(topleft=(upper_pipe_x, upper_pipe_y))  # making rect around the pipe.
                return pipe1_rect, pipe2_rect, 'c'  # returning the rects and the type of the pipe.

    def display(basex, Type, Score_1, Score_2, pipe1_rect, pipe2_rect, G_coin_rect, S_coin_rect):
        screen.blit(background, (0, 0))  # Blil background.
        screen.blit(player, (player_rect))  # Blit player
        screen.blit(base, (basex, 620))  # Blit Base.
        screen.blit(base, (basex + 1280, 620))  # Blit another base at end of first for ground movmnt. .
        screen.blit(coin_img, G_coin_rect)
        screen.blit(S_coin, S_coin_rect)
        Text_Msg_G = Text_Font_G.render(f"x{Score_1}", True, (255, 255, 255))  # Score1 text(Gold) on screen.
        Text_Msg_S = Text_Font_S.render(f"x{Score_2}", True, (255, 255, 255))  # Score2 text(Silver) on screen.
        Text_Msg_B_Points = Text_Font_B_Points.render(f"Best  :{dict_data['Score_M']}", True,
                                                      (255, 255, 255))  # Creating txt for Best points.
        screen.blit(Text_Msg_B_Points, (1100, 40))  # Blit best point.
        screen.blit(Text_Msg_G, (60, 3))  # Blit Gold updatind score on Screen
        screen.blit(coin_img, (5, 4))  # Blit Coin Img(Gold) On screen
        screen.blit(Text_Msg_S, (60, 60))  # Blit Silver updated on screen
        screen.blit(S_coin, (0, 55))  # Blit Silver Img on Screen
        # Getting the type of the pipes from the random pipes function and blit the images according to the cammand.
        if Type == 'a':
            screen.blit(pipe1, pipe1_rect)
            screen.blit(pipe2, pipe2_rect)
        elif Type == 'b':
            screen.blit(pipe3, pipe1_rect)
            screen.blit(pipe4, pipe2_rect)
        else:
            screen.blit(pipe5, pipe1_rect)
            screen.blit(pipe6, pipe2_rect)

    def main_function():
        '''This function run as a main loop that blit the game window countinously'''
        player_acceleration = 0.25  # Variable for the producing gravity force.
        player_velocity = 0
        pipe1_rect, pipe2_rect, Type = random_pipes()  # Getting the pipes and their type from the random function.
        base_x = 0  # X-coordinates of the base image.

        points = 0
        Level = 1
        Speed = 90  # FPS actually speed of game/
        run = True
        Score_G = 0  # Score For Gold Coins
        Score_S = 0  # Score For Silver Coins.
        G_coin_rect = Rect_Coins_G()
        S_coin_rect = Rect_Coins_S()
        while run:
            # Change Value of Level and FPS of Game according to the levels.
            if points == 10:
                Level = 2
                Speed = 92
            if points == 20:
                Level = 3
                Speed = 94
            if points == 30:
                Level = 4
                Speed = 96
            if points == 40:
                Level = 5
                Speed = 98
            if points == 60:
                Level = 6
                Speed = 100
            if points == 70:
                Level = 7
                Speed = 102
            if points == 80:
                Level = 8
                Speed = 104
            if points == 90:
                Level = 9
                Speed = 106
            if points == 100:
                Level = 10
                Speed = 108

            for items in pygame.event.get():  # Get Events happening in pygame.
                if items.type == pygame.KEYDOWN:  # Check any key is pressed or not?
                    if items.key == pygame.K_ESCAPE:  # Check key is Esc or not?
                        run = False
                    elif items.key == pygame.K_SPACE:  # Check key is Space or not?
                        wing_sound.play()
                        player_velocity = 0
                        player_velocity -= 6.5
            player_velocity += player_acceleration  # Increasing the velocity of the bird in downward direction in each loop.
            player_rect.centery += player_velocity  # Changing the bird position with respect to its velocity.

            base_x -= 8  # moving the base towards left.
            if base_x <= -1280:  # We are moving two bases so when the first base will reach at -1280 then its position will be shifted to 0.
                base_x = 0

            # These the condition to check the score of the user when the bird pass through the space between the hurdles.
            if Type == 'a' or Type == 'b':
                if player_rect.x == pipe1_rect.x:
                    points += 1
                    point_sound.play()
            if Type == 'c':
                if player_rect.x == pipe2_rect.x:
                    points += 1
                    point_sound.play()

            pipe1_rect.centerx -= 8  # Moving the lower pipe towards left.
            pipe2_rect.centerx -= 8  # Moving the upper pipe towards left.
            if pipe1_rect.right < 0 and pipe2_rect.right < 0:  # If the X-coordinates of the pipes are less then zero then random function will call to get new pipes.
                pipe1_rect, pipe2_rect, Type = random_pipes()
            G_coin_rect.centerx -= 4
            S_coin_rect.centerx -= 4
            if G_coin_rect.colliderect(player_rect):
                Score_G += 1
                Golden_sound.play()
                G_coin_rect = Rect_Coins_G()
            elif G_coin_rect.centerx < 0:
                G_coin_rect = Rect_Coins_G()
            if S_coin_rect.colliderect(player_rect):
                Score_S += 1
                Silver_sound.play()
                S_coin_rect = Rect_Coins_S()
            elif S_coin_rect.centerx < 0:
                S_coin_rect = Rect_Coins_S()

            if collision(Type, pipe1_rect, pipe2_rect) == 'True':  # Condition to end the game.
                dict_data['Score_G'] += Score_G
                dict_data['Score_S'] += Score_S
                if points > dict_data['Score_M']:
                    dict_data['Score_M'] = points
                data = str(dict_data)
                file = open("Gallery\\file.txt", "w")
                file.writelines(data)
                file.close()
                run = False

            display(base_x, Type, Score_G, Score_S, pipe1_rect, pipe2_rect, G_coin_rect,
                    S_coin_rect)  # Calling the display function to blit the images.
            Text_Msg_L = Text_Font_L.render(f"Level:{Level}", True, (255, 255, 255))  # Level Text Msg for screen.
            screen.blit(Text_Msg_L, (580, 0))  # Blit Msg on screen.
            Text_Msg_Points = Text_Font_Points.render(f"Score:{points}", True,
                                                      (255, 255, 255))  # Creating txt for the Score.
            screen.blit(Text_Msg_Points, (1100, 2))  # Bliting the score.

            pygame.display.update()  # Update Display Continuously
            clock.tick(Speed)  # Set Speed for Blitting images.

    main_function()  # Calling the main function.
    hit_sound.play()  # Playing the sound.
    die_sound.play()  # Playing the sound.


welcome_function()  # Calling the main function.

pygame.quit()  # Close Everything after game window.
