import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        cell_size_y = self.cell_size
        for i in range(self.height):
            cell_size_x = self.cell_size
            cell_size_y += self.cell_size
            for j in range(self.width):
                pygame.draw.rect(screen, (255, 255, 255),
                                 (cell_size_x, cell_size_y, self.cell_size, self.cell_size), 1)
                cell_size_x += self.cell_size


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    board = Board(5, 7)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.flip()
