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

    left = False
    right = False
    up = False
    down = False
    animCount = 0

    walkUp = [pygame.image.load("resours/GG_2.png"), pygame.image.load("resours/GG_1.png"),
              pygame.image.load("resours/GG_3.png")]
    walkDown = [pygame.image.load("resours/GG2.png"), pygame.image.load("resours/GG1.png"),
              pygame.image.load("resours/GG3.png")]
    walkLeft = [pygame.image.load("resours/GG-2.png"), pygame.image.load("resours/GG-1.png"),
              pygame.image.load("resours/GG-3.png")]
    playerStand = pygame.image.load("resours/GG1.png")

    clock =pygame.time.Clock()

    # al_mario = pygame.transform.scale(gg, (gg.get_width() // 4, gg.get_height() // 4)) 12
    grass = pygame.image.load("resours/grass.png").convert()
    bg_surf = pygame.transform.scale(grass, (grass.get_width() // 35, grass.get_height() // 35))

    def drawWindow():
        global animCount
        screen.fill((0, 0, 0))
        board.render(screen)
        pygame.display.update()

        if animCount + 1 >= 15:
            animCount = 0

        if left:
            screen.blit(pygame.transform.scale(walkLeft[animCount // 5],
                                               (walkLeft[animCount // 5].get_width() // 4,
                                                walkLeft[animCount // 5].get_height() // 4)), (x, y))
            animCount += 1
        if right:
            screen.blit(pygame.transform.scale(walkLeft[animCount // 5],
                                               (walkLeft[animCount // 5].get_width() // 4,
                                                walkLeft[animCount // 5].get_height() // 4)), (x, y))
            animCount += 1
        else:
            screen.blit(playerStand, (x, y))


    while running:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel
            left = True
            right = False
            up = False
            down = False

        elif keys[pygame.K_RIGHT]:
            x += vel
            left = False
            right = True
            up = False
            down = False

        elif keys[pygame.K_UP]:
            y -= vel
            left = False
            right = False
            up = True
            down = False

        elif keys[pygame.K_DOWN]:
            y += vel
            left = False
            right = False
            up = False
            down = True
        else:
            left = False
            right = False
            up = False
            down = False
            animCount = 0
        drawWindow()

    pygame.quit()