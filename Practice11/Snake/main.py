import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

snake = [(100,100)]
direction = (20,0)

# еда
def new_food():
    return {
        "pos": (random.randrange(0, WIDTH, 20),
                random.randrange(0, HEIGHT, 20)),
        "value": random.choice([1,3]),
        "color": random.choice([(255,0,0),(0,255,0)]),
        "time": pygame.time.get_ticks()
    }

food = new_food()
score = 0

running = True
while running:
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = (0,-20)
    if keys[pygame.K_DOWN]:
        direction = (0,20)
    if keys[pygame.K_LEFT]:
        direction = (-20,0)
    if keys[pygame.K_RIGHT]:
        direction = (20,0)

    head = (snake[0][0]+direction[0], snake[0][1]+direction[1])
    snake.insert(0, head)

    # съели еду
    if head == food["pos"]:
        score += food["value"]
        food = new_food()
    else:
        snake.pop()

    # исчезновение еды
    if pygame.time.get_ticks() - food["time"] > 5000:
        food = new_food()

    # отрисовка
    for s in snake:
        pygame.draw.rect(screen, (0,255,0), (*s,20,20))

    pygame.draw.rect(screen, food["color"], (*food["pos"],20,20))

    font = pygame.font.SysFont(None, 36)
    screen.blit(font.render(f"Score: {score}", True, (255,255,255)), (10,10))

    pygame.display.update()
    clock.tick(10)

pygame.quit()