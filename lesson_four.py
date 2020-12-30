import os
import sys
import pygame
import random


def load_image(name, image_size, colorkey=None):
    path = os.path.join('data', name)
    if not os.path.isfile(path):
        print('не найдено')
        sys.exit()
    image = pygame.image.load(name)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    # else:
    #     image = image.convert_alpha()
    image = pygame.transform.scale(image, image_size)
    image = pygame.transform.rotate(image, 30)
    return image


class DeadPool(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)
        self.image = load_image('/Users/dsponer/PycharmProjects/pygame_ya/warrior.png', (100, 100))
        self.robot = load_image('/Users/dsponer/PycharmProjects/pygame_ya/lovepool.png', (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(w)
        self.rect.y = random.randrange(h)

    def update(self, *args):
        self.rect = self.rect.move(random.randrange(3) - 1, random.randrange(3) - 1)

        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.robot


if __name__ == '__main__':
    pygame.init()

    size = w, h = (640, 480)

    # image = pygame.Surface((100, 100))
    # image.fill(pygame.Color('blue'))

    # image = load_image('/Users/dsponer/PycharmProjects/pygame_ya/neon-genesis-evangelion-1.jpg', (400, 400))
    group_sprites = pygame.sprite.Group()

    for _ in range(50):
        DeadPool(group_sprites)

    screen = pygame.display.set_mode(size)
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for robot in group_sprites:
                    robot.update(event)
        group_sprites.draw(screen)
        group_sprites.update(event)

        clock.tick(120)
        # screen.blit(image, (10, 10))
        pygame.display.flip()
    pygame.quit()
