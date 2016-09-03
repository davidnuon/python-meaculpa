import pygame
import time

pygame.init()

width   = 640
height  = 400
font    = pygame.font.Font('proggy.ttf', 33)
screen  = pygame.display.set_mode((width, height))
refresh = pygame.display.flip
mousemo = pygame.MOUSEMOTION
line    = pygame.draw.line
n = 1
x = y = 0
count = 0
tan = 'This is a test...'
n = 1
while 1:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        break
        
    elif event.type == mousemo :
        x, y =  event.pos

    screen.fill((100, 100, 205))
    text = font.render('%s' % (tan[:n]), True, (255,255, 255))
    
    textRect = text.get_rect()
    textRect.x = 0
    textRect.y = 0
    screen.blit(text, textRect)
    
    refresh()
    n = n + 1
    time.sleep(.08)
     