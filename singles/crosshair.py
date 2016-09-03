import pygame

pygame.init()

width   = 640
height  = 400
font    = pygame.font.Font(None, 30)
screen  = pygame.display.set_mode((width, height))
refresh = pygame.display.flip
mousemo = pygame.MOUSEMOTION
line    = pygame.draw.line
x = y = 0
count = 0

while 1:
    event = pygame.event.poll()
    
    if event.type == pygame.QUIT:
        break
        
    elif event.type == mousemo :
        x, y =  event.pos
        count = count + 1
    screen.fill((100, 100, 205))
    text = font.render('%s' % (count), True, (255,255, 255))
    
    textRect = text.get_rect()
    textRect.x = 0
    textRect.y = height - textRect.height
    screen.blit(text, textRect)

    line(screen, (0, 0, 0), (0, 0), (x, y))
    line(screen, (255, 0, 0), (width, height), (x, y))
    line(screen, (0, 225, 0), (0, height), (x, y))
    line(screen, (0, 0, 225), (width, 0),   (x, y))
    line(screen, (0, 100, 200), (width, y), (0, y))
    line(screen, (0, 100, 40), (x, height), (x, 0))
    refresh()