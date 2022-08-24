import pygame
pygame.init()

# game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# display size
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))      # set display size

pygame.display.set_caption('Shaker')        # game title

gameExit = False

# create rect object with desired position, width & length
rectWidth = 200
rectHeight = 200
rect = pygame.Rect((DISPLAY_WIDTH / 2) - rectWidth / 2, (DISPLAY_HEIGHT / 2) - rectHeight / 2, rectWidth, rectHeight)

# for loop for events & display
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)     # display's color
    pygame.draw.rect(gameDisplay, black, rect, 5)      # draw rectangle with (platform, color, where, outline width)

    pygame.display.update()

pygame.quit()
quit()
