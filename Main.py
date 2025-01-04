import math
import random
import pygame


screen_width = 800
screen_height = 500

player_start_x = 370
player_start_y = 380

enemy_start_y_min = 50
enemy_start_y_max = 150

enemy_speed_x = 4
enemy_speed_y = 40

bullet_speed_y = 10

collision_distance = 27


pygame.init()


screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load('Background.png')


pygame.display.set_caption("Space Invader")
icon = pygame.image.load('UFO.png')
pygame.display.set_icon(icon)


player_image = pygame.image.load('Player.png')

playerX = player_start_x
playerY = player_start_y

playerX_change = 0


enemy_image = []

enemyX = []
enemyY = []

enemyX_change = []
enemyY_change = []

num_of_enemies =  4


for _i in range(num_of_enemies):

    enemy_image.append(pygame.image.load('Enemy.png'))

    enemyX.append(random.randint(0, screen_width - 64))
    enemyY.append(random.randint(enemy_start_y_min, enemy_start_y_max))

    enemyX_change.append(enemy_speed_x)
    enemyY_change.append(enemy_speed_y)


bullet_image = pygame.image.load('Bullet.png')

bulletX = 0
bulletY = player_start_y

bulletX_change = 0
bulletY_change = bullet_speed_y

bullet_state = "ready"


score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10



