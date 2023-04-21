import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
name_of_game = pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Verdana", 25)

snake_size = 20

def current_level(level):
    level_str = font.render("Level:" + str(level), True, white)
    screen.blit(level_str, (700, 10))


def current_point(point):
    point_str = font.render("Points:" + str(point), True, white)
    screen.blit(point_str, (10, 10))


def Main_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, white, [x[0], x[1], snake_block, snake_block])


INC_SPEED1 = pygame.USEREVENT
pygame.time.set_timer(INC_SPEED1, 1000)


def GameStart():

    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    snake_speed = 15

    level = 0
    point = 0
    dissearing_food = False
    game_over = False


    x_corr_food = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
    y_corr_food = round(random.randrange(0, height - snake_size) / 20.0) * 20.0

    x_corr_for_diss_food = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
    y_corr_for_diss_food = round(random.randrange(0, height - snake_size) / 20.0) * 20.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == INC_SPEED1:
                if dissearing_food == False:
                    dissearing_food = True
                    pygame.time.set_timer(INC_SPEED1, 5000)
                elif dissearing_food == True:
                    dissearing_food = False
                    pygame.time.set_timer(INC_SPEED1, 10000)
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_over = True

        screen.fill(black)

        current_level(level)
        current_point(point)

        x1 += x1_change
        y1 += y1_change

        if dissearing_food == True:
            pygame.draw.rect(screen, red, [x_corr_for_diss_food, y_corr_for_diss_food, snake_size, snake_size])

        pygame.draw.rect(screen, white, [x_corr_food, y_corr_food, snake_size, snake_size])


        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)


        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True
        Main_snake(snake_size, snake_List)
        pygame.display.update()

        if x1 == x_corr_food and y1 == y_corr_food:
            x_corr_food = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
            y_corr_food = round(random.randrange(0, height - snake_size) / 20.0) * 20.0
            Length_of_snake += 1
            point += 1
            if point % 5 == 0:
                level += 1
                snake_speed += 5

        if x1 == x_corr_for_diss_food and y1 == y_corr_for_diss_food:
            x_corr_for_diss_food = round(random.randrange(0, width - snake_size) / 20.0) * 20.0
            y_corr_for_diss_food = round(random.randrange(0, height - snake_size) / 20.0) * 20.0
            Length_of_snake += 5
            dissearing_food = False
            pygame.time.set_timer(INC_SPEED1, 10000)
            point += 5
            level += 1
            snake_speed += 5

        clock.tick(snake_speed)
    pygame.quit()


GameStart()