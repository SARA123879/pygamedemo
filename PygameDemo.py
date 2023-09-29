#Name:Sara Perera
#Date: September 29, 2023
#Pygame demo. 

import sys, pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

#Sets the bottle in a rectanglular area.
bottle = pygame.image.load("bottleflip.gif")
bottlerect = bottle.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    bottlerect = bottlerect.move(speed)
    if bottlerect.left < 0 or bottlerect.right > width:
        speed[0] = -speed[0]
    if bottlerect.top < 0 or bottlerect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(bottle, bottlerect)
    pygame.display.flip()
