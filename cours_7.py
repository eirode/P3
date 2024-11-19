import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 182)
black = (0, 0, 0)
red = (255, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

largeur = 400
longueur = 600

dis = pygame.display.set_mode((longueur, largeur))
pygame.display.set_caption("Snake Game")
ico = pygame.surface.Surface((100, 100), masks=green)
pygame.display.set_icon(ico)

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont('Arial', 25)
score_font = pygame.font.SysFont('Arial', 35)


def your_score(score):
    value = score_font.render("your score : " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def draw_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(dis, black, [i[0], i[1], snake_block, snake_block])


def message(msg, color):
    text = font_style.render(msg, True, color)
    dis.blit(text, [longueur/6, largeur/3])


def gameloop():

    game_over = False
    game_close = False

    x1 = longueur/2
    y1 = largeur/2

    x1_modif = 0
    y1_modif = 0

    snake_list = []
    lenght_of_list = 1

    foodx = round(random.randrange(0, longueur - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, largeur - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("perdu: R pour rejouer et Q pour quitter", red)
            your_score(lenght_of_list - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        gameloop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    y1_modif = -snake_block
                    x1_modif = 0
                elif event.key == pygame.K_s:
                    y1_modif = snake_block
                    x1_modif = 0
                elif event.key == pygame.K_d:
                    x1_modif = snake_block
                    y1_modif = 0
                elif event.key == pygame.K_q:
                    x1_modif = -snake_block
                    y1_modif = 0

        if x1 >= longueur or x1 < 0 or y1 >= largeur or y1 < 0:
            game_close = True

        x1 += x1_modif
        y1 += y1_modif

        dis.fill(blue)

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > lenght_of_list:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        your_score(lenght_of_list - 1)
        draw_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, longueur - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, largeur - snake_block) / 10.0) * 10.0
            lenght_of_list += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()


gameloop()
