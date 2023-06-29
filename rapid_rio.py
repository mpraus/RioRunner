import random
import pygame

pygame.init()

# constants
HEIGHT = 300
WIDTH = 450
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BROWN = (139, 69, 19)
PURPLE = (255, 0, 255)
FLOOR_Y = 220
PLAYER_SIZE = 20
OBSTACLE_SIZE = 10
OBSTACLE_Y = FLOOR_Y - OBSTACLE_SIZE
GRAVITY = 1

# variables
score = 0
player_x = 10
player_y = FLOOR_Y - PLAYER_SIZE
jumping = False
jump_height = 0
alive = True
lives = 3

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Rapid Rio')
ft_font = pygame.freetype.SysFont(pygame.freetype.get_default_font(), 16)
background = BLACK
fps = 60
timer = pygame.time.Clock()
obstacles = [400, 600, 900]
bonuses = [500, 1100, 2000]
alex = 4000
obstacle_speed = 2

running = True


while running:
    timer.tick(fps)
    screen.fill(background)
    ft_font.render_to(screen, (5, 5), 'Score: ' + str(score), (250, 250, 250))
    floor = pygame.draw.rect(screen, WHITE, [0,FLOOR_Y, WIDTH, HEIGHT-FLOOR_Y])
    player = pygame.draw.rect(screen, RED, [player_x, player_y, PLAYER_SIZE, PLAYER_SIZE])
    pygame.draw.rect(screen, PURPLE, [alex, FLOOR_Y - 60, 20, 60])
    for i in range(lives):
        pygame.draw.circle(screen, RED, [WIDTH - (lives - i) * 15, 15], 5)
    for obstacle in obstacles:
        pygame.draw.rect(screen, YELLOW, [obstacle, OBSTACLE_Y, OBSTACLE_SIZE, OBSTACLE_SIZE])
    for bonus in bonuses:
        pygame.draw.rect(screen, BROWN, [bonus, OBSTACLE_Y, OBSTACLE_SIZE, OBSTACLE_SIZE])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
                jump_height = 18

    if jumping:
        if player_y < FLOOR_Y - PLAYER_SIZE or jump_height > 0:
            player_y -= jump_height
            jump_height -= GRAVITY
        if player_y >= FLOOR_Y - PLAYER_SIZE:
            player_y = FLOOR_Y - PLAYER_SIZE
            jump_height = 0
        if player_y == FLOOR_Y - PLAYER_SIZE and jump_height == 0:
            jumping = False

    for i in range(len(obstacles)):
        if alive:
            obstacles[i] -= obstacle_speed
            if obstacles[i] < 0 - OBSTACLE_SIZE:
                score += 10
                obstacle_speed += 0.1
                print(obstacle_speed)
                obstacles[i] = random.randint(400, 1000)
            if player.colliderect([obstacles[i], OBSTACLE_Y, OBSTACLE_SIZE, OBSTACLE_SIZE]):
                lives -= 1
                obstacles[i] = random.randint(400, 1000)
                if lives == 0:
                    alive = False

    for i in range(len(bonuses)):
        if alive:
            bonuses[i] -= obstacle_speed
            if bonuses[i] < 0 - OBSTACLE_SIZE:
                bonuses[i] = random.randint(700, 2500)
            if player.colliderect([bonuses[i], OBSTACLE_Y, OBSTACLE_SIZE, OBSTACLE_SIZE]):
                bonuses[i] = random.randint(700, 2500)
                score += 20
                print(score)
    if alive:
        alex -= obstacle_speed
        if alex < 0 - 20:
            alex = random.randint(2500, 8000)
        if player.colliderect([alex, FLOOR_Y - 60, 20, 60]):
            alex = random.randint(2500, 8000)
            if lives < 3:
                lives += 1
            else:
                score += 50

    pygame.display.flip()


pygame.quit()