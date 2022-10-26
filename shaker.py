import pygame
pygame.init()

# game colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 128, 0)

# display
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Shaker')

# create rect object with (position), (width & length)
rectWidth = 200
rectHeight = 200
rect = pygame.Rect(((DISPLAY_WIDTH / 2) - rectWidth / 2, (DISPLAY_HEIGHT / 2) - rectHeight / 2), (rectWidth, rectHeight))

gameExit = False

# for loop for events & display
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)     # display's color
    pygame.draw.rect(gameDisplay, black, rect, 5)      # draw rectangle (platform, color, where, outline width)

    # turns rect red when mouse collides with the rect
    if rect.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(gameDisplay, red, rect, 5)

        # turns rect green when clicked
        pygame.event.get()      # need this for left click to work
        click = pygame.mouse.get_pressed()
        if click[0]:        # 0 is left click
            pygame.draw.rect(gameDisplay, green, rect, 5)

            # move the mouse while holding left button and drag rect to desired location
            if event.type == pygame.MOUSEMOTION:
                rect.center = event.pos     # this works but cursor moves to rect's center
                # ---test 1--- x, y = pygame.mouse.get_pos()
                # ---test 1--- rect.center = (((x - rect.centerx) + x), ((y - rect.centery) + y))
                
    pygame.display.update()
pygame.quit()
quit()

