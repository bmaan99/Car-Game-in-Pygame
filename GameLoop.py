import pygame
import random

pygame.init()
pygame.font.init()
crash_sound = pygame.mixer.Sound("Assets/crash_sound.wav")
pygame.mixer.music.load("Assets/car_music.mp3")
# Pause variable used for unpausing or pause the game
pause = False

d_width = 800
d_height = 600
screen = pygame.display.set_mode((d_width,d_height))

clock = pygame.time.Clock()

# All the colors to be used in the game
black = (0,0,0)
white = (255,255,255)
blue = (0,0,255)
red = (210,0,0)
green = (0,210,0)
pause_button =(136,223,17)

brightgreen = (0,255,0)
brightred = (255,0,0)

# Function for drawing different images of the game
def car_draw(x,y,car_file):
    """
    Draws the player's car on the game screen.
    
    Args:
        x (int): X-coordinate position to draw the car
        y (int): Y-coordinate position to draw the car
        car_file (str): File path of the car image to be loaded and displayed
    """
    car_img = pygame.image.load(car_file)
    screen.blit(car_img,(x,y))

# Function to show the score on the screen
def dogde_score(count):
    """
    Renders and displays the player's current score on the game screen.
    
    Args:
        count (int): The current score of the player
    """
    font = pygame.font.SysFont(None,40)
    score = font.render("Your Score : " + str(count),True,black)
    screen.blit(score,(10,10))

# Function for drawing the obstacles 
def thing_draw(cho,thingx,thingy):
    """
    Draws randomly selected obstacles on the game screen.
    
    Args:
        cho (int): Random index to select which obstacle image to draw
        thingx (int): X-coordinate position to draw the obstacle
        thingy (int): Y-coordinate position to draw the obstacle
    """
    thing = pygame.image.load("Assets/11.png")
    thing2 = pygame.image.load("Assets/12.png")
    thing3 = pygame.image.load("Assets/13.png")
    l = [thing,thing2,thing3]
    final = l [cho]
    screen.blit(final,(thingx,thingy))

def text_objects(text,font):
    """
    Creates a text surface and its rectangular area for rendering text.
    
    Args:
        text (str): The text to be rendered
        font (pygame.font.Font): The font to use for rendering the text
    
    Returns:
        tuple: A surface containing the rendered text and its rectangular area
    """
    textSurf = font.render(text,True,black)
    return textSurf , textSurf.get_rect()

def exitgame():
    """
    Properly closes the Pygame window and exits the game.
    """
    pygame.quit()
    quit()

def crash ():
    """
    Handles the game crash sequence when the player's car collides with an obstacle.
    Plays a crash sound, displays a crash message, and provides options to restart or quit.
    """
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    crash = False
    while not crash:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crash = True
                exitgame()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            game_loop()
        if pressed[pygame.K_ESCAPE]:
            exitgame()
        
        text = "You Crashed !!"
        font = pygame.font.SysFont("comicsansms" , 120)
        textSurf , textRect = text_objects(text,font)
        textRect.center = ((d_width/2),(d_height/2))
        screen.blit(textSurf,textRect)
        car_draw(300,20,"Assets/car_crash.png")
        button(200,450,100,60,brightgreen,green,"Play Again",game_loop)
        button(500,450,100,60,brightred,red,"Quit",exitgame)

        pygame.display.update()
        clock.tick(60)

def button(x,y,b_width,b_height,activecolor,inactivecolor,msg,command=None):
    """
    Creates an interactive button with hover and click functionality.
    
    Args:
        x (int): X-coordinate of the button's top-left corner
        y (int): Y-coordinate of the button's top-left corner
        b_width (int): Width of the button
        b_height (int): Height of the button
        activecolor: Color of the button when hovered
        inactivecolor: Color of the button when not hovered
        msg (str): Text to display on the button
        command (function, optional): Function to call when button is clicked
    """
    mouse = pygame.mouse.get_pos()
    mouse_key = pygame.mouse.get_pressed()
    
    if x < mouse[0] < x+b_width and y < mouse[1] < y+b_height:
        pygame.draw.rect(screen,activecolor,(x,y,b_width,b_height))
        if command!=None and mouse_key[0] == 1:
            command()
    else:
        pygame.draw.rect(screen,inactivecolor,(x,y,b_width,b_height))
    font = pygame.font.SysFont("comicsansms",20)
    textSurf ,textRect = text_objects(msg,font)
    textRect.center = (x+45,y+30)
    screen.blit(textSurf,textRect)

def unpause():
    """
    Resumes the game from a paused state.
    Sets the global pause variable to False.
    """
    global pause
    pygame.mixer.music.unpause()
    pause = False

def pause_screen():
    """
    Displays the pause screen when the game is paused.
    Allows the player to resume or quit the game.
    """
    global pause
    pygame.mixer.music.pause()
    pause = True
    while pause :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause = False
                exitgame()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            unpause()
        if pressed[pygame.K_ESCAPE]:
            exitgame()
            
        screen.fill(white)
        button(200,450,100,60,brightgreen,green,"Continue",unpause)
        button(500,450,100,60,brightred,red,"Quit",exitgame)
        car_draw(300,110,"Assets/pause.png")
        pygame.display.update()
        clock.tick(60)

def game_intro():
    """
    Displays the game's introduction/start screen.
    Provides options to start the game or quit.
    """
    done = False
    while not done :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                exitgame()
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RETURN]:
            game_loop()
        if pressed[pygame.K_ESCAPE]:
            exitgame()
                
        screen.fill(white)
        font = pygame.font.SysFont("comicsansms",120)
        textSurf ,textRect = text_objects("Car Game",font)
        textRect.center = ((d_width/2),(d_height/2))
        screen.blit(textSurf,textRect)

        button(200,450,100,60,brightgreen,green,"Play",game_loop)
        button(500,450,100,60,brightred,red,"Quit",exitgame)
        car_draw(140,40,"Assets/intro_car.jpg")
        
        pygame.display.update()
        clock.tick(60)

def game_loop():
    """
    The main game loop that handles game mechanics, player movement, 
    obstacle generation, collision detection, and scoring.
    """
    pygame.mixer.music.play(-1)
    # for drawing the Photo
    thing_width = 100
    thing_height = 100
    thingx = random.randint(10,(d_width-thing_width))
    thingx2 = (thingx + random.randint(150,600))%(800)
    thingy = -300
    thing_speed = 4
    #for decision of type of thing
    cho = 0
    cho1 = 2
    dogde=0
    
    car_width = 58
    x = d_width * 0.3
    y = d_height * 0.85
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                exitgame()

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x-=4
        if pressed[pygame.K_RIGHT]:
            x+=4
        if pressed[pygame.K_SPACE]:
            pause_screen()
            
        if x > d_width - car_width or x < 0:
            crash()
            
            
        screen.fill(white)

        car_draw(x,y,"Assets/car.png")
        # for obsatacles
        button(740,8,50,50,white,white,"",pause_screen)
        car_draw(740,8,"Assets/pause_button.png")
        thing_draw (cho,thingx,thingy)
        thing_draw (cho1,thingx2,thingy)
        thingy += thing_speed

        # To know if car crashed or not 
        if y < thingy + thing_height:
            if x > thingx and x < thingx + thing_width or x + car_width > thingx and x + car_width < thingx + thing_width:
                crash()
            if x > thingx2 and x < thingx2 + thing_width or x + car_width > thingx2 and x + car_width < thingx2 + thing_width: 
                crash()    
        dogde_score(dogde)

        # To show next obstacle when earlier obstacle is off the screen
        if thingy > d_height:
            
            thingx = random.randint(10,(d_width-thing_width))
            thingx2 = (thingx + random.randint(150,600))%(800)
            thingy = -100
            cho = random.randint (0,2)
            cho1 =  random.randint (0,2)
            dogde += 2
            if dogde % 12 == 0:
                thing_speed +=1
            
        pygame.display.update()
        clock.tick(60)


# Calling the game intro screen function
game_intro()
exitgame()
