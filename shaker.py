import pygame
pygame.init()

# game colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (36, 160, 237)
red = (255, 0, 0)
green = (0, 128, 0)

# display
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 800
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
pygame.display.set_caption('Shaker')


class Container:
    def __init__(self):
        # create rectangular object with (position), (width & length)
        self.rectWidth = 200
        self.rectHeight = 200
        self.rect = pygame.Rect(((DISPLAY_WIDTH / 2) - self.rectWidth / 2, (DISPLAY_HEIGHT / 2) - self.rectHeight / 2), (self.rectWidth, self.rectHeight))

    def draw(self):
        pygame.draw.rect(gameDisplay, black, self.rect, 5)

    def drawRed(self):
        pygame.draw.rect(gameDisplay, red, self.rect, 5)

    def drawGreen(self):
        pygame.draw.rect(gameDisplay, green, self.rect, 5)

    def move(self):
        self.rect.center = event.pos


class Bead:
    def draw(self):
        pygame.draw.circle(gameDisplay, blue, (400, 400), 20)


container = Container()
bead = Bead()

gameExit = False

# for loop for events & display
while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)  # display's color

    # draw bead
    bead.draw()

    # draw container (platform, color, where, outline width)
    container.draw()

    # turns rect red when mouse collides with the rect
    if container.rect.collidepoint(pygame.mouse.get_pos()):
        container.drawRed()

        # turns rect green when clicked
        pygame.event.get()  # need this for left click to work
        click = pygame.mouse.get_pressed()
        if click[0]:  # 0 is left click
            container.drawGreen()

            # move the mouse while holding left button and drag rect to desired location
            if event.type == pygame.MOUSEMOTION:
                container.move()

    pygame.display.update()
pygame.quit()
quit()


