from ctypes.wintypes import RGB
from json import load
import pygame
import random
import os
pygame.mixer.init()
pygame.init()

# color 
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

# Variables
screen_width = 900
screen_height = 600

# creating window
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# game background 
bgimg = pygame.image.load("snake8.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

# gameover background
firstpage = pygame.image.load("10.JPG")
firstpage= pygame.transform.scale(firstpage, (screen_width, screen_height)).convert_alpha()

# welcome page background 
secondpage= pygame.image.load("snake7.jpg")
secondpage= pygame.transform.scale(secondpage, (screen_width, screen_height)).convert_alpha()

# game title 
pygame.display.set_caption("Snakes_With_Shivam")
pygame.display.update()#for change or update the program

# CLOCK define
clock = pygame.time.Clock()

# globel variable 
font = pygame.font.SysFont(None,55)

# function 
def text_screen(text,color,x,y):
    screen_text = font.render(text,True,color)
    gameWindow.blit (screen_text,[x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False

# exit game loop 
    while not exit_game:
        gameWindow.blit(secondpage, (0, 0))
        text_screen("Welcome To Snakes",(RGB(157, 145, 8)),260,10)
        text_screen("Press Space Bar To Play",(RGB(5, 165, 37)),230,550)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('back.mp3')
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(60)

#game loop 
def gameloop():

    # game variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1
    
    # check if hiscore file exists 
    if (not os.path.exists("high_score.txt")):
        with open ('high_score.txt',"w") as f:
            f.write("0")

    # high score 
    with open("high_score.txt","r") as f:
        hiscore = f.read()

    food_x = random.randint(20,screen_width/2)
    food_y = random.randint(20,screen_height/2)
    score = 0
    init_velocity = 5
    snake_size = 20
    fps = 60
        
    while not exit_game:
        if game_over: 
            with open("high_score.txt","w") as f:
                f.write(str(hiscore))
            gameWindow.blit(firstpage, (0, 0))
            
            text_screen("game_over! Press Enter to Continue",(RGB(226, 210, 33)),100,200)
            text_screen("Your Score: " + str(score),(RGB(226, 210, 33)),300,250)
            text_screen("  High score: "+str(hiscore),(RGB(226, 210, 33)),283,300)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

                        # cheat codes 
                    if event.key == pygame.K_m:
                        score +=10

                    if event.key == pygame.K_g:
                        score +=-10

            snake_x = snake_x + velocity_x 
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x)<10 and abs(snake_y - food_y)<10:
                score +=10
                food_x = random.randint(20,screen_width/2)
                food_y = random.randint(20,screen_height/2)
                snk_length +=5
                if score>int(hiscore):
                    hiscore = score

            gameWindow.fill(white)
            gameWindow.blit(bgimg, (0, 0))
        
            text_screen("score: " + str(score),red,700,550)
            pygame.draw.rect(gameWindow,red,[food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
                
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('beep.mp3')
                pygame.mixer.music.play()
        
            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()