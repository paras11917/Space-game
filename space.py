import pygame
import random
import math

# initilize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
background = pygame.image.load('background.jpeg')


# player
playerImg = pygame.image.load('player.png')
playerX = 376
playerY = 480
change = 0
score = 0


def player(x, y):
    screen.blit(playerImg, (playerX, playerY))


# enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
change_enemy = 0.2


def enemy(x, y):
    screen.blit(enemyImg, (enemyX, enemyY))


# bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
change_bullet = 1
bullet_state = "ready"





def bullet(x, y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg, (x+16, y+16))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Loop
running=True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change=-0.4
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change=0.4
        if event.type == pygame.KEYUP:
            change=0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if bullet_state =="ready":
                   p=playerX
                   bullet(p, bulletY)
                   bulletY -= change_bullet

    playerX += change
    if playerX <= 0:
        playerX=0
    elif playerX >= 736:
        playerX=736

    enemyX += change_enemy
    if enemyX >= 736:
        enemyX=736
        enemyY += 64
        change_enemy=-0.3
    elif enemyX <= 0:
        enemyX=0
        enemyY += 64
        change_enemy=0.3

    if bulletY <= 0:
        bulletY=480
        bullet_state="ready"

    if bullet_state == "fire":
        bullet(p, bulletY)
        bulletY -= change_bullet

        
    collision=isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY=480
        bullet_state="ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)



    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
