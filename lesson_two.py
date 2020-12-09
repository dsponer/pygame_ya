import pygame


def draw(screen):
    pygame.draw.line(screen, (255, 255, 255), (0, 0), (w, h), width=5)
    pygame.draw.line(screen, (255, 255, 255), (w, 0), (0, h), width=5)


if __name__ == '__main__':
    pygame.init()
    try:
        a = input().split()
        size = w, h = int(a[0]), int(a[1])
        screen = pygame.display.set_mode(size)
        screen.fill((0, 0, 0))

        draw(screen)
        while pygame.event.wait().type != pygame.QUIT:
            pygame.display.flip()
    except:
        print('неверный формат ввода')
        pygame.quit()

    pygame.quit()
