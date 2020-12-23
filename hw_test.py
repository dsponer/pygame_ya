import pygame


def draw(screen):
    b, x = 30, 15
    for i in range(12):
        if i % 2 == 0:
            for j in range(10):
                pygame.draw.polygon(screen, (255, 0, 0),
                                    [((b * j) + (2 * j), (x * i) + (2 * i) + x),
                                     ((b * j) + (2 * j), (x * i) + (2 * i)),
                                     ((b * j) + (2 * j) + b, (x * i) + (2 * i)),
                                     ((b * j) + (2 * j) + b, (x * i) + (2 * i) + x)])
        elif i % 2 == 1:
            pygame.draw.polygon(screen, (255, 0, 0),
                                [(0, (x * i) + (2 * i) + x),
                                 (0, (x * i) + (2 * i)),
                                 (15, (x * i) + (2 * i)),
                                 (15, (x * i) + (2 * i) + x)])
            for j in range(9):
                pygame.draw.polygon(screen, (255, 0, 0),
                                    [((b * j) + (2 * j) + 17, (x * i) + (2 * i) + x),
                                     ((b * j) + (2 * j) + 17, (x * i) + (2 * i)),
                                     ((b * j) + (2 * j) + b + 17, (x * i) + (2 * i)),
                                     ((b * j) + (2 * j) + b + 17, (x * i) + (2 * i) + x)])


if __name__ == '__main__':
    pygame.init()
    size = 300, 200
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))
    draw(screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
