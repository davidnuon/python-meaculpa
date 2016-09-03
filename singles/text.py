import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((256, 256))
pygame.display.set_caption('Application')
screen.fill((159, 182, 205))

# Create a font
font = pygame.font.Font(None, 20)

# Render the text

text = font.render('Powered by Python and PyGame', True, (255,255, 255))

# Create a rectangle
textRect = text.get_rect()

# Center the rectangle
textRect.centerx = screen.get_rect().centerx
textRect.centery = screen.get_rect().centery

# Blit the text
screen.blit(text, textRect)

pygame.display.update()

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         sys.exit()