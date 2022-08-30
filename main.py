import pygame
pygame.init()

# game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)

# display size
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))      # set display size

pygame.display.set_caption('Shaker')        # game title

gameExit = False

# create rect object with desired position, width & length
rectWidth = 200
rectHeight = 200
rect = pygame.Rect(((DISPLAY_WIDTH / 2) - rectWidth / 2, (DISPLAY_HEIGHT / 2) - rectHeight / 2), (rectWidth, rectHeight))

# for loop for events & display
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)     # display's color
    pygame.draw.rect(gameDisplay, black, rect, 5)      # draw rectangle (platform, color, where, outline width)

    # turns rect red when mouse hovers the rect
    if rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(gameDisplay, red, rect, 5)
        # turns rect green when clicked
        pygame.event.get()      # need this for left click to work
        click = pygame.mouse.get_pressed()
        if click[0]:        # 0 is left click
            pygame.draw.rect(gameDisplay, green, rect, 5)
            # move the mouse while holding left button and drag rect to desired location
            if event.type == pygame.MOUSEMOTION:
                # rect.center = pygame.mouse.get_pos() # this works but it moves to rect's center
                print(rect.center)
                x, y = pygame.mouse.get_pos()
                rect.center = (((x - rect.centerx) + x), ((y - rect.centery) + y))
                print(rect.center)
                print(pygame.mouse.get_pos())
                print(rect.centerx-x)

    pygame.display.update()
pygame.quit()
quit()

