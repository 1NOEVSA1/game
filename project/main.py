import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size


    def render(self, screen):
        for i in range(self.height):
            for j in range(self.width):
                screen.blit(bg_surf,
                            ((self.left + j * self.cell_size, self.top + i * self.cell_size),
                             (self.cell_size, self.cell_size)))

if __name__ == '__main__':
    pygame.init()
    size = 700, 700
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Игра")
    screen.fill((0, 0, 0))
    board = Board(22, 22)
    board.set_view(20, 20, 30)
    running = True
    x = 50
    y = 50
    width = 30
    height = 30
    vel = 10
    gg = pygame.image.load("resours/GG1.png")
    al_mario = pygame.transform.scale(gg, (gg.get_width() // 4, gg.get_height() // 4))
    grass = pygame.image.load("resours/grass.png").convert()
    bg_surf = pygame.transform.scale(grass, (grass.get_width() // 35, grass.get_height() // 35))
    # run = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.time.delay(100)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel

        if keys[pygame.K_RIGHT]:
            x += vel

        if keys[pygame.K_UP]:
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel
        screen.fill((0, 0, 0))
        board.render(screen)
        screen.blit(al_mario, (x, y))
        pygame.display.update()

    pygame.quit()