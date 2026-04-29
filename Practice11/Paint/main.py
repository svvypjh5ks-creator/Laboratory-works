import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()

color = (255,255,255)
mode = "draw"

start_pos = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                mode = "square"
            if event.key == pygame.K_2:
                mode = "triangle_right"
            if event.key == pygame.K_3:
                mode = "triangle_eq"
            if event.key == pygame.K_4:
                mode = "rhombus"

        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            end = event.pos

            if mode == "square":
                size = 50
                pygame.draw.rect(screen, color, (*start_pos, size, size))

            elif mode == "triangle_right":
                pygame.draw.polygon(screen, color, [
                    start_pos,
                    (start_pos[0]+50, start_pos[1]),
                    (start_pos[0], start_pos[1]+50)
                ])

            elif mode == "triangle_eq":
                pygame.draw.polygon(screen, color, [
                    (start_pos[0], start_pos[1]),
                    (start_pos[0]+50, start_pos[1]),
                    (start_pos[0]+25, start_pos[1]-50)
                ])

            elif mode == "rhombus":
                pygame.draw.polygon(screen, color, [
                    (start_pos[0], start_pos[1]-40),
                    (start_pos[0]+40, start_pos[1]),
                    (start_pos[0], start_pos[1]+40),
                    (start_pos[0]-40, start_pos[1])
                ])

    pygame.display.update()
    clock.tick(60)

pygame.quit()