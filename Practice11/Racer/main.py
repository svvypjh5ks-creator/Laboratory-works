import pygame
import random

pygame.init()

WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer")

clock = pygame.time.Clock()

# Player
player = pygame.Rect(180, 500, 40, 60)
player_speed = 5

# Enemy
enemy = pygame.Rect(random.randint(0, WIDTH-40), 0, 40, 60)
enemy_speed = 5

# Coins (разные веса)
coins = []
score = 0

def spawn_coin():
    return {
        "x": random.randint(20, WIDTH-20),
        "y": -50,
        "value": random.choice([1, 3]),  # разные веса
        "radius": random.choice([8, 12])
    }

# стартовые монеты
for _ in range(3):
    coins.append(spawn_coin())

running = True
while running:
    screen.fill((30,30,30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # движение игрока
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed

    # движение врага
    enemy.y += enemy_speed
    if enemy.y > HEIGHT:
        enemy.y = 0
        enemy.x = random.randint(0, WIDTH-40)

    # увеличение скорости
    if score >= 5:
        enemy_speed = 7
    if score >= 10:
        enemy_speed = 10

    # монеты
    for coin in coins:
        coin["y"] += 4

        # отрисовка
        pygame.draw.circle(screen, (255, 215, 0),
                           (coin["x"], coin["y"]),
                           coin["radius"])

        coin_rect = pygame.Rect(coin["x"]-10, coin["y"]-10, 20, 20)

        if player.colliderect(coin_rect):
            score += coin["value"]  # учитываем вес
            coins.remove(coin)
            coins.append(spawn_coin())

        if coin["y"] > HEIGHT:
            coins.remove(coin)
            coins.append(spawn_coin())

    # рисуем
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.draw.rect(screen, (0,255,0), enemy)

    # счёт
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Coins: {score}", True, (255,255,255))
    screen.blit(text, (250, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()