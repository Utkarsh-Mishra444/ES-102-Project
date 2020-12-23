import pygame
import random
from pynput.keyboard import Key, Controller
keyboard = Controller()
pygame.font.init()
F1 = pygame.font.SysFont('Showcard Gothic',30)
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
#the above is imported so that we dont have to type pygame.K-UP everytime
ScreenW = 800
ScreenH = 600

screen = pygame.display.set_mode([ScreenW,ScreenH])
running = True      #The constant that controls main game loop
#making some colors into constants for conveniance
white = [255,255,255]
black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
color1 = [195, 163, 196]
Bsize = 50 #size of boxes
Snake = [(200,200),(200,250),(200,300)]  #a list of tuples that contains the postion of the snake body
food = (300,350) #position of food

presskey = 0 #constant that contains last key pressed
U = False
D = False
L = False
R = False
score = 0
MasterKey = K_RIGHT
presscheck = False
popcheck = False
while running:
    for event in pygame.event.get():
        popcheck = True
        presscheck = True
        if event.type == KEYDOWN:   #commanding the snake to move using these 4 if statements
            if event.key == K_UP:
                MasterKey = K_UP
                presskey = 'U'
                presscheck = False
            if event.key == K_DOWN:
                MasterKey = K_DOWN
                presskey = 'D'
                presscheck = False
            if event.key == K_LEFT:
                MasterKey = K_LEFT
                presskey = 'L'
                presscheck = False
            if event.key == K_RIGHT:
                MasterKey = K_RIGHT
                presskey = 'R'
                presscheck = False
            if event.key == K_ESCAPE:
                running = False
        if event.type == KEYDOWN:
            if MasterKey == K_UP:
               tempx = Snake[-1][0]
               tempy = Snake[-1][1]
               if (tempx,(tempy-50)%ScreenH) in Snake:
                   running = False
                   color1 = [0, 0, 0]
               Snake.append((tempx,(tempy-50)%ScreenH))
            if MasterKey == K_DOWN:
               tempx = Snake[-1][0]
               tempy = Snake[-1][1]
               if (tempx,(tempy+50)%ScreenH) in Snake:
                   running = False
                   color1 = [0, 0, 0]
               Snake.append((tempx,(tempy+50)%ScreenH))
            if MasterKey == K_LEFT:
               tempx = Snake[-1][0]
               tempy = Snake[-1][1]
               if ((tempx-50)%ScreenW,tempy) in Snake:
                   running = False
                   color1 = [0, 0, 0]
               Snake.append(((tempx-50)%ScreenW,tempy))
            if MasterKey == K_RIGHT:
               tempx = Snake[-1][0]
               tempy = Snake[-1][1]
               if ((tempx+50)%ScreenW,tempy) in Snake:
                   running = False
                   color1 = [0,0,0]
               Snake.append(((tempx+50)%ScreenW,tempy))
            if Snake[-1] == food:
                score += 1
                while food in Snake:
                    food = (50 * random.randint(1, 15), 50 * random.randint(1, 11))
                popcheck = False #this increases the snake length
            elif popcheck:
                Snake.pop(0)
    if event.type == QUIT:
        running = False
    screen.fill(color1)
    for pos in Snake:
        rect2 = pygame.Rect(pos[0],pos[1],Bsize,Bsize)
        if pos == Snake[-1]:
            pygame.draw.rect(screen,[0,0,255],rect2)
        else:
            pygame.draw.rect(screen,red, rect2)
    rect3 = pygame.Rect(food[0],food[1],Bsize,Bsize)
    pygame.draw.rect(screen,green,rect3)
    pygame.display.flip()
    # the below portion simulates key press to help snake move when you are not pressing anything
    if presscheck:
        if presskey == 'U':
            keyboard.press(Key.up)
            keyboard.release(Key.up)
        if presskey == 'D':
            keyboard.press(Key.down)
            keyboard.release(Key.down)
        if presskey == 'L':
            keyboard.press(Key.left)
            keyboard.release(Key.left)
        if presskey == 'R':
            keyboard.press(Key.right)
            keyboard.release(Key.right)
    pygame.time.delay(200)
    #code to change board color every time the food is eaten
    if score%3 == 0:
        color1 = [54, 125, 56]
    if score%3 == 1:
        color1 = [144, 3, 252]
    if score%3 == 2:
        color1 = [195, 163, 196]
srfc = F1.render(f'Game Over Your score is = {score}', True,[255, 225, 0]) #to display score at end
screen.blit(srfc,(30,20))
# messagebox._show('Game Over',f'Your score is = {score}')
pygame.display.flip()
pygame.time.delay(3000) # 3 second delay to see the score