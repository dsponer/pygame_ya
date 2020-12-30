import pygame


def draw(screen):
    font = pygame.font.Font(None, 50)
    pygame.draw.polygon(screen, (255, 0, 0), [(1, h - 1), (1, 1), (w - 1, 1), (w - 1, h - 1)])


if __name__ == '__main__':
    pygame.init()
    try:
        print('введите 2 числа каждое в новой строке:)')
        size = w, h = int(input()), int(input())
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))

        draw(screen)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
    except:
        print('неверный формат ввода')
        pygame.quit()

    pygame.quit()
