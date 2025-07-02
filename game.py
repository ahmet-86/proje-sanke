
import pygame
from ai import AI
from utils import draw_objects, check_collision

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

ai = AI()
snake = [(100, 50)]
direction = (10, 0)
food = (300, 200)
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    action = ai.choose_action(snake, food)
    direction = ai.action_to_direction(action, direction)

    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    if new_head == food:
        food = ai.generate_food(WIDTH, HEIGHT, snake)
        score += 10
    else:
        snake.pop()

    if check_collision(snake, WIDTH, HEIGHT):
        ai.train()
        running = False

    draw_objects(screen, snake, food, score)
    clock.tick(15)

pygame.quit()
