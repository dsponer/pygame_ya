import pygame
import os
import sys

fps = 60
step = 10

# 0 - ноль
# 1 - стена
# e - враг
# p - персонаж

size = w, h = 640, 480
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

player = None
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '0':
                Tile('grass', x, y)
            elif level[y][x] == '1':
                Tile('wall', x, y)
            elif level[y][x] == 'p':
                Tile('grass', x, y)
                new_player = Player(x, y)
    return new_player, x, y


def load_level(filename):
    with open(filename, 'r') as map_level:
        level_map = [line.strip() for line in map_level]

    max_w = max(map(len, level_map))

    return list(map(lambda x: x.ljust(max_w, '0'), level_map))


def load_image(name, image_size, color_key=None):
    path = os.path.join('data', name)
    try:
        image = pygame.image.load(path).convert()
    except pygame.error as e:
        print('Cannot load image', name)
        raise SystemExit(name)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()

    image = pygame.transform.scale(image, image_size)
    return image


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["Hello",
                  "Game rules",
                  "Info"]

    font = pygame.font.Font(None, 30)
    text_coordinate = 10
    screen.fill(pygame.Color('black'))

    for line in intro_text:
        str_render = font.render(line, 1, pygame.Color('white'))
        intro_rect = str_render.get_rect()
        text_coordinate += 10
        intro_rect.top = text_coordinate
        intro_rect.x = 10
        text_coordinate += intro_rect.height
        screen.blit(str_render, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(fps)


tile_dictionary = {
    'wall': load_image('/Users/dsponer/PycharmProjects/pygame_ya/wall.png', (100, 100)),
    'grass': load_image('/Users/dsponer/PycharmProjects/pygame_ya/grass.png', (100, 100))
}

player_image = load_image('/Users/dsponer/PycharmProjects/pygame_ya/warrior.png', (100, 100))
tile_width = tile_height = 50


class Tile(pygame.sprite.Sprite):
    def __init__(self, type_tile, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_dictionary[type_tile]
        self.rect = self.image.get_rect().move(tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(tile_width * pos_x + 10, tile_height * pos_y + 10)

class Camera():
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - w // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - h // 2)

if __name__ == '__main__':
    pygame.init()

    start_screen()
    player, level_x, level_y = generate_level(load_level('level_one'))
    camera = Camera()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect.x -= step
                if event.key == pygame.K_RIGHT:
                    player.rect.x += step
                if event.key == pygame.K_UP:
                    player.rect.y += step
                if event.key == pygame.K_DOWN:
                    player.rect.y -= step

        camera.update(player)

        for sprite in all_sprites:
            camera.apply(sprite)

        screen.fill(pygame.Color('black'))
        tiles_group.draw(screen)
        player_group.draw(screen)

        pygame.display.flip()
        clock.tick(fps)

    terminate()
