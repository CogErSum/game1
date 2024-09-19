import pygame
from map import *
pygame.init()

#CONST
WIDHT = 800
HEIGHT = 600
BLOCK_WIDHT = 50
#screen
screen = pygame.display.set_mode((WIDHT,HEIGHT))

#background
bg = pygame.Surface((WIDHT*3,600))
bg_x = 0
bg_image = pygame.image.load('image/bg.png').convert_alpha()

#player
player_x = 0
player_y = 200
player_image_stand = pygame.image.load('image/player/stand.png').convert_alpha()
player_on_ground = False
player_images_right = [
    pygame.image.load('image/player/right/run1.png').convert_alpha(),
    pygame.image.load('image/player/right/run2.png').convert_alpha(),
    pygame.image.load('image/player/right/run3.png').convert_alpha(),
    ]
num_of_anim_right = 0
player_images_left = [
    pygame.image.load('image/player/left/run1.png').convert_alpha(),
    pygame.image.load('image/player/left/run2.png').convert_alpha(),
    pygame.image.load('image/player/left/run3.png').convert_alpha(),
    ]
num_of_anim_left = 0
player_jump = False
jump_count = 15
#blocks
block_upper_image = pygame.image.load('image/blocks/block_upper.png').convert_alpha()
block_under_image = pygame.image.load('image/blocks/under_block.png').convert_alpha()
#FPS
clock = pygame.time.Clock()
#main loop
running = True
while running:
    #buttons
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                    player_jump = True
    #drawing bg
    screen.blit(bg,(bg_x,0))
    bg.blit(bg_image, (0,0))
    bg.blit(bg_image, (WIDHT*2,0))
    #drawing player and moving
    player_rect = player_image_stand.get_rect(topleft = (player_x, player_y))
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_d]:
            if not player_x > WIDHT-300:
                player_x += 3
                if num_of_anim_right >= 2:
                    num_of_anim_right = 0
                num_of_anim_right += 1
                player = screen.blit(player_images_right[num_of_anim_right], (player_x, player_y))
            bg_x -= 5
    elif pressed[pygame.K_a]:
        if bg_x < 0:
            if not player_x < 00:
                player_x -= 3
                if num_of_anim_left >= 2:
                    num_of_anim_left = 0
                num_of_anim_left +=1
                player = screen.blit(player_images_left[num_of_anim_left], (player_x,player_y))
                bg_x += 5
            else:
                player = screen.blit(player_image_stand, (player_x, player_y))
    else:
        player = screen.blit(player_image_stand, (player_x, player_y))
    if bg_x <= -WIDHT*2:
        bg_x = 0
    
    #drawing map
    for index_row, row in enumerate(map):
        for index_cell, cell in enumerate(row.split(',')):
            if cell == '-':
                bl = bg.blit(block_upper_image, (index_cell*BLOCK_WIDHT,index_row*BLOCK_WIDHT))
                block_rect = block_upper_image.get_rect(topleft = (index_cell*BLOCK_WIDHT,index_row*BLOCK_WIDHT))
                block_rect.move_ip(bg_x, 0)
                if player_rect.colliderect(block_rect):
                    player_on_ground = True
            elif cell == 'u':
                bg.blit(block_under_image, (index_cell*BLOCK_WIDHT,index_row*BLOCK_WIDHT))
    #falling player
    if not player_on_ground:
        player_y += 5
    player_on_ground = False
    #jump
    if player_jump:
        if jump_count >= 0:
            player_y -= jump_count
            jump_count -=1
        else:
                player_jump = False
                jump_count = 15
    #updating screen and FPS
    pygame.display.flip()
    clock.tick(24)