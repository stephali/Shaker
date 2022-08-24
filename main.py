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

# for loop for events & display
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)     # display's color

    rect = pygame.Rect(0, 0, 200, 200)      # create rect object with desired width and length
    rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)        # set the center at x&y
    pygame.draw.rect(gameDisplay, black, rect, 5)      # (platform, color, where, outline width)

    pygame.display.update()

pygame.quit()
quit()
