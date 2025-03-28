import pygame              
import random              

pygame.init() 

SW, SH = 600, 600 # screen size(playing area)
WW, WH = 600, 700 # window size

BLOCK_SIZE = 40
FONT = pygame.font.SysFont('Comic Sans MS', BLOCK_SIZE)    

screen = pygame.display.set_mode((WW, WH))
pygame.display.set_caption("snake")
clock = pygame.time.Clock() # to controlling the game's speed

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) # rectangle for the snake's head
        self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)] # snake's body as a list of rectangles
        self.dead = False # flag indicating whether the snake is dead
        self.restart = False # flag indicating whether the restart key has been pressed

    def update(self):
        global apple, wall, golden_apple

        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y: # checking for collision of the snake's head with its body
                self.dead = True
            if self.head.x not in range(0, SW) or self.head.y not in range(0, SH): # checking if the snake leaves the playing area
                self.dead = True
        # restarting the game if the snake is dead and the restart is true
        if self.dead and self.restart:
                self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
                self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                self.body = [pygame.Rect(self.x-BLOCK_SIZE, self.y, BLOCK_SIZE, BLOCK_SIZE)]
                self.xdir = 1
                self.ydir = 0
                self.dead = False
                self.restart = False
                apple = Apple() # creating a new apple
                wall = Wall() # creating a new wall
                golden_apple = GoldenApple(self.body, (apple.x, apple.y), [barrier for barrier in wall.barriers]) # creating a new golden apple
        # updating the snake's position
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.spawn_apple()
        self.spawn_time = pygame.time.get_ticks() 
    # method for generating a new position for the apple
    def spawn_apple(self):
        self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
    # method for updating the position and drawing the apple
    def update(self, snake_body): 
        if pygame.time.get_ticks() - self.spawn_time >= 5000: # 5000 => milliseconds 
            self.spawn_apple() 
            self.spawn_time = pygame.time.get_ticks()
        while (self.x, self.y) in [(square.x, square.y) for square in snake_body]:
            self.spawn_apple()
        self.new_apple = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, "red", self.new_apple)

class GoldenApple:
    def __init__(self, snake_body, apple_pos, wall_barriers):
        # initializing the golden apple's spawn time and its rectangle
        self.spawn_time = pygame.time.get_ticks()
        self.golden_apple_rect = None
        if random.random() <= 0.1: # call spawn_golden_apple if a random number is less than or equal to 0.1 (probability 10%)
            self.spawn_golden_apple(snake_body, apple_pos, wall_barriers) 
    # method for spawning a golden apple
    def spawn_golden_apple(self, snake_body, apple_pos, wall_barriers):
        while True:
            self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
            # checking if the generated coordinates do not overlap with the snake's body, regular apple, or wall barriers
            if (self.x, self.y) not in apple_pos and \
               (self.x, self.y) not in [(square.x, square.y) for square in snake_body] and \
               (self.x, self.y) not in [(barrier.x, barrier.y) for barrier in wall_barriers]:
                # creating a rectangle representing the golden apple
                self.golden_apple_rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
                break
    # method for updating the golden apple's position and appearance
    def update(self, snake_body, apple_pos, wall_barriers):
        current_time = pygame.time.get_ticks()

        if self.golden_apple_rect is not None: # checking if a golden apple exists 
            if current_time - self.spawn_time >= 3000: # if it exists, checking if it's time to despawn it (3 seconds)
                self.golden_apple_rect = None  
        else: # if does not exist, checks whether a new one needs to be created
            if random.random() <= 0.1:  
                self.spawn_golden_apple(snake_body, apple_pos, wall_barriers)
                self.spawn_time = current_time

        if self.golden_apple_rect is not None: # drawing the golden apple if it exists
            pygame.draw.rect(screen, "gold", self.golden_apple_rect)

class Wall:
    def __init__(self):
        self.barriers = []
    # method for generating new barriers (walls)
    def spawn_barrier(self, snake_body, apple_pos, snake_head_pos):
        while True:
            self.x = int(random.randint(0, SW) / BLOCK_SIZE) * BLOCK_SIZE
            self.y = int(random.randint(0, SH) / BLOCK_SIZE) * BLOCK_SIZE
            new_barrier = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE) 
            # condition ensures that the newly generated barrier does not collide with any part of the snake's body and does not overlap with the position of the apple 
            if new_barrier.collidelist(snake_body) == -1 and new_barrier.collidepoint(apple_pos) == False:
                # condition ensures that the new barrier is not placed too close to the snake's head. (barrier is at least three blocks away from the snake's head)  
                if abs(snake_head_pos[0] - new_barrier.x) > 3 * BLOCK_SIZE or abs(snake_head_pos[1] - new_barrier.y) > 3 * BLOCK_SIZE:
                    self.barriers.append(new_barrier)
                    break    
    # method for updating and drawing the walls
    def update(self, snake_body, apple_pos, snake_head_pos, eaten_fruits):
        for barrier in self.barriers:
            pygame.draw.rect(screen, "blue", barrier)
            if barrier.colliderect(snake_head_pos): # checking for collision with added barriers
                snake.dead = True

        eaten_fruits = eaten_fruits // 2 # this means that a new barrier is added after every second fruit eaten.
        if eaten_fruits > len(self.barriers):
            for _ in range(eaten_fruits - len(self.barriers)):
                self.spawn_barrier(snake_body, apple_pos, snake_head_pos)
# function for drawing the game grid
def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, (60, 60, 60), rect, 1)

# initializing score, speed, and eaten fruits variables
score = speed = eaten_fruits = 0
scoretxt = speedtxt = leveltxt = FONT.render("0", True, "white")
score_rect = scoretxt.get_rect(center=(20, 620))
speed_rect = speedtxt.get_rect(center=(20, 660))
level_rect = leveltxt.get_rect(center=(480, 620))

drawGrid()
# creating a objects of game 
snake = Snake()
apple = Apple()
wall = Wall()
golden_apple = GoldenApple(snake.body, (apple.x, apple.y), [barrier for barrier in wall.barriers])

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    snake.update()

    screen.fill("black")

    drawGrid()

    wall.update(snake.body, (apple.x, apple.y), snake.head, eaten_fruits)

    pygame.draw.rect(screen, (42, 42, 42), [0, SH, WW, WH]) # drawing the surface for showing some statistics
    # drawing the current values of score, speed, and level 





    pygame.display.update() # updating the screen
    clock.tick(5 + speed) # using fps to control game speed
