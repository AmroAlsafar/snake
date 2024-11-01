import pygame
import time
import random

# Initialiser pygame
pygame.init()

# Farver
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
grey = (128, 128, 128)

# Spil vindue størrelse
dis_width = 600
dis_height = 400

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def score(score_value):
    value = score_font.render("score " + str(score_value), True, yellow)
    dis.blit(value, [0, 0])

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(dis, grey, [obstacle[0], obstacle[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

    score_value = 0

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1
    

    # Spawn af mad
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    obstacles = []
    for _ in range(5):  # Antallet af forhindringer
            obstacle_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            obstacle_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            obstacles.append([obstacle_x, obstacle_y])

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("Du tabte! Tryk Q for at afslutte eller C for at spille igen", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        

        # Tegn maden
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])

        draw_obstacles(obstacles)


        for obstacle in obstacles:
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_close = True

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        
        score(score_value)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            score_value += 1
        
        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
