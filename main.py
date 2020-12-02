import pygame
import random


def draw(screen):
    font = pygame.font.Font(None, 50)
    text = font.render('Hello, Pygame', True, (255, 0, 0))
    text_x = w // 2 - text.get_width() // 2
    text_y = 0
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 0, 255), (text_x - 15, text_y - 15, text_w + 30, text_h + 30), 1)


def draw_circle(screen):
    color = pygame.Color(255, 0, 10)
    pygame.draw.circle(screen, color, (640 // 2 - 25, 480 // 2 - 25), 100, 0)
    hsv = color.hsva
    color.hsva = (hsv[0], hsv[1], hsv[2] - 30, hsv[3])
    pygame.draw.circle(screen, color, (640 // 2 + 15, 480 // 2 + 15), 100, 0)


def draw_points(screen):
    for i in range(random.randint(1000, 10000)):
        screen.fill(pygame.Color('black'), (random.random() * w, random.random() * h, 1, 1))


if __name__ == '__main__':
    pygame.init()
    size = w, h = 640, 480
    screen = pygame.display.set_mode(size)
    screen.fill((255, 255, 255))

    # draw(screen)
    # draw_circle(screen)
    draw_points(screen)
    while pygame.event.wait().type != pygame.QUIT:
        pygame.display.flip()

    pygame.quit()
