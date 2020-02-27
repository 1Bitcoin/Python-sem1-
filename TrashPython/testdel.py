import pygame


class pyGameSetup:

def __init__(self, title, width, height):

    # initialize pygame library
    pygame.init()

    # set up specific display properties
    self.game_display = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)

    # update display
    pygame.display.update()

    # create new global variables for the class
    # game state
    self.running = True

    # colors, only main
    # TODO: implement more color RGB values, if updated, update corresponding method
    self.white = (255, 255, 255)
    self.black = (0, 0, 0)
    self.grey = (128, 128, 128)
    self.pink = (255, 102, 178)
    self.blue = (0, 0, 255)
    self.red = (255, 0, 0)
    self.green = (0, 255, 0)
    self.purple = (127, 0, 255)
    self.yellow = (255, 255, 0)
    self.teal = (0, 204, 204)
    self.orange = (255, 128, 0)

    # player coordinates and properties
    self.player_x = int(width / 2)
    self.player_y = int(height / 2)
    self.player_width = 100
    self.player_height = 50
    self.player_speed_x = 0
    self.player_speed_y = 0
    self.move_speed = 5

    # FPS controllers (note start speed should always be 60 / 5 so, 1 / 300
    self.clock = pygame.time.Clock()
    self.fps = 60

    # screen values
    self.width = width
    self.height = height

    # rotation for car
    self.angle = 200

    # car image
    self.car1 = pygame.image.load("Images\\Car1.png")
    self.update_size()
    self.car_rect = self.car1.get_rect()
    self.car_rect.center = (self.player_x, self.player_y)


def exit(self):
    pygame.quit()
    self.running = False
    quit()

def game_loop(self):
    while self.running:
        for event in pygame.event.get():
            self.event_handler(event)

        # update player position
        # self.player_x += self.player_speed_x
        self.angle = self.player_speed_x
        self.player_y += self.player_speed_y

        # check to make sure it in bounds
        self.check_valid_move()

        # reprint canvas
        self.game_display.fill(self.white)

        # update angle
        self.update_angle()

        # print player
        self.game_display.blit(self.car1, (self.player_x, self.player_y, self.player_width,
                                           self.player_height))

        # update display
        pygame.display.update()

        # FPS
        self.clock.tick(self.fps)

def event_handler(self, e):
    if e.type == pygame.QUIT:
        self.exit()
    if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                self.player_speed_x = -self.move_speed
            if e.key == pygame.K_RIGHT:
                self.player_speed_x = self.move_speed
            if e.key == pygame.K_UP:
                self.player_speed_y = -self.move_speed
            if e.key == pygame.K_DOWN:
                self.player_speed_y = self.move_speed
    if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT:
                self.player_speed_x = 0
            if e.key == pygame.K_RIGHT:
                self.player_speed_x = 0
            if e.key == pygame.K_UP:
                self.player_speed_y = 0
            if e.key == pygame.K_DOWN:
                self.player_speed_y = 0

def check_valid_move(self):
    if self.player_x <= 0:
        self.player_x = 0
    if self.player_x >= self.width - self.player_width:
        self.player_x = self.width - self.player_width
    if self.player_y <= 0:
        self.player_y = 0
    if self.player_y >= self.height - self.player_height:
        self.player_y = self.height - self.player_height

def update_size(self):
    self.car1 = pygame.transform.scale(self.car1, (self.player_width, self.player_height))
    self.car1 = pygame.transform.rotate(self.car1, -90)

def update_angle(self):
    old_center = self.car_rect.center
    self.car1 = pygame.transform.rotate(self.car1, self.angle)
    self.car_rect.center = old_center

x = pyGameSetup('Game', 800, 600)
x.game_loop()
