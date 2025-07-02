
import pygame

def draw_objects(screen, snake, food, score):
    screen.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(s[0], s[1], 10, 10))
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(food[0], food[1], 10, 10))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

def check_collision(snake, width, height):
    head = snake[0]
    if head[0] < 0 or head[0] >= width or head[1] < 0 or head[1] >= height or head in snake[1:]:
        return True
    return False
