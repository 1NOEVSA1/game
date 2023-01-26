import pygame
import sys
import os
from random import randint
import sqlite3

pygame.init()
# size = width, height = 800, 600
# значения выставленные ниже, размеры моего экрана, сделал это для удобства
FPS = 60
# screen = pygame.display.set_mode(size)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
size = width, height = pygame.display.get_surface().get_size()
pygame.display.set_caption('Перемещение героя')
clock = pygame.time.Clock()


def sizescreen():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    size = width, height = pygame.display.get_surface().get_size()
    return


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


def terminate():
    pygame.quit()
    sys.exit()


walkUp = [pygame.image.load("resours/back2.png"), pygame.image.load("resours/back1.png"),
          pygame.image.load("resours/back3.png"), pygame.image.load("resours/back1.png")]
walkDown = [pygame.image.load("resours/front2.png"), pygame.image.load("resours/front1.png"),
            pygame.image.load("resours/front3.png"), pygame.image.load("resours/front1.png")]
walkLeft = [pygame.image.load("resours/left2.png"), pygame.image.load("resours/left1.png"),
            pygame.image.load("resours/left3.png"), pygame.image.load("resours/left1.png")]
walkRight = [pygame.image.load("resours/right2.png"), pygame.image.load("resours/right1.png"),
             pygame.image.load("resours/right3.png"), pygame.image.load("resours/right1.png")]
playerStand = pygame.image.load("resours/front1.png")
run = pygame.image.load('data/startanim.png')


def start_screen():
    fon = pygame.transform.scale(load_image('FON.png'), (width, height))
    screen.blit(fon, (0, 0))
    frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        frame = (frame + 0.2) % 4
        image = run.subsurface(580 * int(frame), 0, 580, 45)
        screen.blit(image, ((width // 2) - 265, height - 80))
        pygame.display.update()
        clock.tick(FPS)


def start():
    fon = pygame.transform.scale(load_image('systempng/startmenu.png'), (width, height))
    screen.blit(fon, (0, 0))
    frame = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        frame = (frame + 0.2) % 4
        image = run.subsurface(580 * int(frame), 0, 580, 45)
        screen.blit(image, (width // 2, height - 80))
        pygame.display.update()
        clock.tick(FPS)


def story_screen2():
    q = 0
    a = ['storyscreen2/storyscreen1.png', 'storyscreen2/storyscreen2.png', 'storyscreen2/storyscreen3.png',
         'storyscreen2/storyscreen5.png', 'storyscreen2/storyscreen6.png', 'storyscreen2/storyscreen7.png',
         'storyscreen2/storyscreen8.png', 'storyscreen2/storyscreen9.png', 'storyscreen2/storyscreen10.png',
         'storyscreen2/storyscreen11.png', 'storyscreen2/storyscreen12.png', 'storyscreen2/storyscreen13.png']
    fon = pygame.transform.scale(load_image(a[q]), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    q += 1
                    fon = pygame.transform.scale(load_image(a[q]), (width, height))
                    screen.blit(fon, (0, 0))
                except Exception:
                    return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def story_screen():
    q = 0
    a = ['storyscreen/storyscreen1.png', 'storyscreen/storyscreen2.png', 'storyscreen/storyscreen3.png',
         'storyscreen/storyscreen4.png', 'storyscreen/storyscreen5.png', 'storyscreen/storyscreen6.png',
         'storyscreen/storyscreen7.png',
         'storyscreen/storyscreen8.png', 'storyscreen/storyscreen9.png', 'storyscreen/storyscreen10.png',
         'storyscreen/storyscreen11.png', 'storyscreen/storyscreen12.png', 'storyscreen/storyscreen13.png',
         'storyscreen/storyscreen14.png']
    fon = pygame.transform.scale(load_image(a[q]), (width, height))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    q += 1
                    fon = pygame.transform.scale(load_image(a[q]), (width, height))
                    screen.blit(fon, (0, 0))
                except Exception:
                    return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    max_width = max(map(len, level_map))

    # дополняем каждую строку пустыми клетками ('.')
    return list(map(lambda x: x.ljust(max_width, '.'), level_map))


tile_images = {
    'wall': load_image('setka.png'),
    'wall2': load_image('setka2.png'),
    'empty': load_image('grass/15.png'),
    '1': load_image('grass/1.png'),
    '2': load_image('grass/2.png'),
    '3': load_image('grass/3.png'),
    '4': load_image('grass/4.png'),
    '5': load_image('grass/5.png'),
    '6': load_image('grass/6.png'),
    '7': load_image('grass/7.png'),
    '8': load_image('grass/8.png'),
    '9': load_image('grass/9.png'),
    '0': load_image('grass/10.png'),
    '!': load_image('grass/11.png'),
    '*': load_image('grass/12.png'),
    '£': load_image('grass/13.png'),
    '$': load_image('grass/14.png'),
    '%': load_image('grass/16.png'),
    '^': load_image('grass/17.png'),
    '?': load_image('grass/18.png'),
    'a': load_image('arcade.png'),
    'b': load_image('run.png'),
    'c': load_image('grass/20.png'),
    'd': load_image('grass/19.png'),
    'i': load_image('grass/tree.png'),
    'f': load_image('clear.png'),
    'g': load_image('churka_stand.png')
}
player_image = load_image('sprites/stand.png')
frame = 0
tile_width = tile_height = 100
image = pygame.image.load('data/sprites/left.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image1 = tile_images[tile_type]
        self.image = pygame.transform.scale(self.image1, (100, 100))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x, tile_height * pos_y)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image1 = player_image
        self.image = pygame.transform.scale(self.image1, (100, 100))
        self.rect = self.image.get_rect().move(
            tile_width * pos_x + 15, tile_height * pos_y + 5)

    def up(self):
        self.image = pygame.transform.scale(load_image('resours/back1.png'), (100, 100))

    def down(self):
        self.image = pygame.transform.scale(load_image('resours/front1.png'), (100, 100))

    def left(self):
        self.image = pygame.transform.scale(load_image('resours/left1.png'), (100, 100))

    def right(self):
        self.image = pygame.transform.scale(load_image('resours/right1.png'), (100, 100))

    def ugl(self, screen):
        fon = pygame.transform.scale(load_image('systempng/mainmenu.png'), (width * 0.5, height * 0.5))
        screen.blit(fon, (0, 0))


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


# основной персонаж
player = None
# группы спрайтов
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
camera = Camera()


def generate_level(level):
    new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == '.':
                Tile('empty', x, y)
            elif level[y][x] == '1':
                Tile('1', x, y)
            elif level[y][x] == '2':
                Tile('2', x, y)
            elif level[y][x] == '3':
                Tile('3', x, y)
            elif level[y][x] == '4':
                Tile('4', x, y)
            elif level[y][x] == '5':
                Tile('5', x, y)
            elif level[y][x] == '6':
                Tile('6', x, y)
            elif level[y][x] == '7':
                Tile('7', x, y)
            elif level[y][x] == '8':
                Tile('8', x, y)
            elif level[y][x] == '9':
                Tile('9', x, y)
            elif level[y][x] == '0':
                Tile('0', x, y)
            elif level[y][x] == '!':
                Tile('!', x, y)
            elif level[y][x] == '*':
                Tile('*', x, y)
            elif level[y][x] == '"':
                Tile('£', x, y)
            elif level[y][x] == ';':
                Tile('$', x, y)
            elif level[y][x] == '%':
                Tile('%', x, y)
            elif level[y][x] == '^':
                Tile('^', x, y)
            elif level[y][x] == '?':
                Tile('?', x, y)
            elif level[y][x] == '#':
                Tile('wall', x, y)
            elif level[y][x] == 'x':
                Tile('wall2', x, y)
            elif level[y][x] == 'a':
                Tile('a', x, y)
            elif level[y][x] == 'b':
                Tile('b', x, y)
            elif level[y][x] == 'f':
                Tile('f', x, y)
            elif level[y][x] == 'i':
                Tile('i', x, y)
            elif level[y][x] == 'd':
                Tile('c', x, y)
            elif level[y][x] == 'c':
                Tile('d', x, y)
            elif level[y][x] == 'g':
                Tile('g', x, y)
            elif level[y][x] == '@':
                level[y][x] = '.'
                x0, y0 = x, y
                Tile('empty', x, y)
                new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    return new_player, x0, y0


def start_screen1():
    pygame.init()
    width, height = 1200, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Flappy bird')
    pygame.display.set_icon(pygame.image.load('data/FB/icon.png'))
    font1 = pygame.font.Font(None, 35)
    imgBG = pygame.image.load('data/FB/bg.png')
    imgBird = pygame.image.load('data/FB/vorona.png')
    imgPT = pygame.image.load('data/FB/pipe_top.png')
    imgPB = pygame.image.load('data/FB/pipe_bottom.png')
    pygame.mixer.music.load('data/FB/music.mp3')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    sndFall = pygame.mixer.Sound('data/FB/fall.wav')
    py, sy, ay = height // 2, 0, 0
    player = pygame.Rect(width // 3, py, 34, 24)
    frame = 0
    state = 'start'
    timer = 10
    pipes = []
    bges = []
    pipesScores = []
    pipeSpeed = 3
    pipeGateSize = 200
    pipeGatePos = height // 2
    bges.append(pygame.Rect(0, 0, 288, 600))
    lives = 1
    scores = 0
    play = True
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
        press = pygame.mouse.get_pressed()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            if exit(1200, 600):
                state = 'game over'
        click = press[0] or keys[pygame.K_SPACE]
        if timer:
            timer -= 1
        frame = (frame + 0.2) % 6
        for i in range(len(bges) - 1, -1, -1):
            bg = bges[i]
            bg.x -= pipeSpeed // 2
            if bg.right < 0:
                bges.remove(bg)
            if bges[len(bges) - 1].right <= width:
                bges.append(pygame.Rect(bges[len(bges) - 1].right, 0, 288, 600))
        for i in range(len(pipes) - 1, -1, -1):
            pipe = pipes[i]
            pipe.x -= pipeSpeed
            if pipe.right < 0:
                pipes.remove(pipe)
                if pipe in pipesScores:
                    pipesScores.remove(pipe)
        if state == 'start':
            if click and not timer and not len(pipes):
                state = 'play'
            py += (height // 2 - py) * 0.1
            player.y = py
        elif state == 'play':
            if click:
                ay = -2
            else:
                ay = 0
            py += sy
            sy = (sy + ay + 1) * 0.98
            player.y = py
            if not len(pipes) or pipes[len(pipes) - 1].x < width - 200:
                pipes.append(pygame.Rect(width, 0, 52, pipeGatePos - pipeGateSize // 2))
                pipes.append(
                    pygame.Rect(width, pipeGatePos + pipeGateSize // 2, 52, height - pipeGatePos + pipeGateSize // 2))
                pipeGatePos += randint(-100, 100)
                if pipeGatePos < pipeGateSize:
                    pipeGatePos = pipeGateSize
                elif pipeGatePos > height - pipeGateSize:
                    pipeGatePos = height - pipeGateSize
            if player.top < 0 or player.bottom > height:
                state = 'fall'
            for pipe in pipes:
                if player.colliderect(pipe):
                    state = 'fall'
                if pipe.right < player.left and pipe not in pipesScores:
                    pipesScores.append(pipe)
                    scores += 5
                    pipeSpeed = 3 + scores // 100
        elif state == 'fall':
            sndFall.play()
            sy, ay = 0, 0
            pipeGatePos = height // 2

            lives -= 1
            if lives:
                state = 'start'
                timer = 60
            else:
                state = 'game over'
                timer = 240
        else:
            py += sy
            sy = (sy + ay + 1) * 0.98
            player.y = py

            if not timer:
                gameover(screen, scores, 'flappy bird')
                return
        # Отрисовка
        for bg in bges:
            screen.blit(imgBG, bg)

        for pipe in pipes:
            if not pipe.y:
                rect = imgPT.get_rect(bottomleft=pipe.bottomleft)
                screen.blit(imgPT, rect)
            else:
                rect = imgPB.get_rect(topleft=pipe.topleft)
                screen.blit(imgPB, rect)
        image = imgBird.subsurface(64 * int(frame), 0, 64, 64)
        image = pygame.transform.rotate(image, -sy * 2)
        screen.blit(image, player)
        text = font1.render('Очки: ' + str(scores), 1, 'black')
        screen.blit(text, (10, 10))
        text = font1.render('Максимальный результат: ' + str(BD('flappy bird')), 1, 'black')
        screen.blit(text, (10, height - 30))
        pygame.display.update()
        clock.tick(FPS)


def BD(name):
    x = 'data/game.sqlite'
    # Подключение к БД
    con = sqlite3.connect(x)
    # Создание курсора
    cur = con.cursor()
    # Выполнение запроса и получение всех результатов
    result = cur.execute("""SELECT record FROM spisok
                WHERE name = '""" + str(name) + """'""").fetchall()
    con.close()
    result = result[0]
    return result[0]


def start_screen2(q):
    pygame.init()
    screen = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("google dino")
    clock = pygame.time.Clock()
    a = 0
    screen2 = pygame.Surface(screen.get_size())

    def collisions(dino, cactus):
        if cactus:
            for cactus_rect in cactus:
                if dino.colliderect(cactus_rect):
                    return False
        return True

    f4 = pygame.font.Font(None, 35)

    def display_score(x):
        current_time = (x // 100) - start_time
        score_surf = f4.render(f'Score:    {current_time}', True, (64, 64, 64))
        score_rect = score_surf.get_rect(topleft=(10, 10))
        screen.blit(score_surf, score_rect)
        display_max()
        return current_time

    def display_max():
        score_surf1 = f4.render(f'Max:    {BD("dino")}', True, (64, 64, 64))
        score_rect1 = score_surf1.get_rect(topleft=(10, 30))
        screen.blit(score_surf1, score_rect1)
        return BD("dino")

    score = 0
    start_time = 0
    dino_walk1 = pygame.image.load("resours/right2.png").convert_alpha()
    dino_walk2 = pygame.image.load("resours/right1.png").convert_alpha()
    dino_walk3 = pygame.image.load("resours/right3.png").convert_alpha()
    dino_walk4 = pygame.image.load("resours/right1.png").convert_alpha()
    dino_walk = [dino_walk1, dino_walk2, dino_walk3, dino_walk4]
    dino_index = 0
    dino_jump = pygame.image.load("resours/right3.png").convert_alpha()
    dino_surf = dino_walk[dino_index]
    dino_rect = dino_surf.get_rect(midbottom=(200, 450))
    dino_gravity = 0
    cactus_frame1 = pygame.image.load("data/Dino/cactus1.png").convert_alpha()
    cactus_frame2 = pygame.image.load("data/Dino/cactus2.png").convert_alpha()
    cactus_frames = [cactus_frame2, cactus_frame1]
    cactus_frame_index = 0
    cactus_surf = cactus_frames[cactus_frame_index]
    cactus_spawn_speed = 1500
    cactus_rect_list = []
    cactus_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cactus_timer, cactus_spawn_speed)
    cactus_speed = 4
    level_sound = pygame.mixer.Sound("data/Dino/sound2.mp3")
    jump_sound = pygame.mixer.Sound("data/Dino/sound1.mp3")

    def cactus_movement(cactus_list):
        if cactus_list:
            for cactus_rect in cactus_list:
                cactus_rect.x -= int(cactus_speed)
                screen.blit(cactus_frame1, cactus_rect)
            cactus_list = [obstacle for obstacle in cactus_list if obstacle.x > -100]
            return cactus_list
        else:
            return []

    cloud = pygame.image.load("data/Dino/cloud.png").convert_alpha()
    cloud_rect = cloud.get_rect(midbottom=(randint(1200, 1500), randint(100, 200)))
    cloud_list = []
    cloud_rect_list = []

    def cloud_movement(cloud_list):
        if cloud_list:
            for cloud_rect in cloud_list:
                cloud_rect.x -= 1
                screen.blit(cloud, cloud_rect)
            return cloud_list
        else:
            return []

    cactus_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cactus_timer, cactus_spawn_speed)
    cactus_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(cactus_animation_timer, 600)
    cloud_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(cloud_timer, 4000)
    level_timer = pygame.USEREVENT + 4
    pygame.time.set_timer(level_timer, 10000)
    game_active = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if game_active:
                if event.type == pygame.MOUSEBUTTONDOWN or (
                        event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    dino_gravity = -23
                    jump_sound.play()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_active = False
                if event.type == cactus_timer:
                    cactus_rect_list.append(cactus_surf.get_rect(bottomright=(randint(1200, 1400), 450)))
                if event.type == cactus_animation_timer:
                    if cactus_frame_index == 0:
                        cactus_frame_index = 1
                    else:
                        cactus_frame_index = 0
                    cactus_surf = cactus_frames[cactus_frame_index]
                if event.type == cloud_timer:
                    cloud_rect_list.append(cloud.get_rect(midbottom=(randint(1200, 1500), randint(100, 200))))
                if event.type == level_timer:
                    cactus_speed += 1
                    level_sound.play()
        if game_active:
            pygame.draw.rect(screen, (240, 240, 240), (0, 0, 1200, 450))
            score = display_score(a)
            if q:
                if score == 50:
                    if BD('dino') < score:
                        x = 'data/game.sqlite'
                        con = sqlite3.connect(x)
                        cur = con.cursor()
                        # Выполнение запроса и получение всех результатов
                        cur.execute("""UPDATE spisok
                                    SET record = '""" + str(score) + """' """ +
                                    """WHERE name = '""" + str('dino') + """'""").fetchall()
                        con.commit()
                        con.close()
                    final(1200, 600)
            if dino_rect.bottom < 300:
                dino_surf = dino_jump
            else:
                dino_index += 0.1
                if dino_index >= len(dino_walk):
                    dino_index = 0
                dino_surf = dino_walk[int(dino_index)]
            dino_gravity += 0.8
            dino_rect.y += dino_gravity
            if dino_rect.bottom >= 450:
                dino_rect.bottom = 450
            screen.blit(dino_surf, dino_rect)
            cactus_rect_list = cactus_movement(cactus_rect_list)
            game_active = collisions(dino_rect, cactus_rect_list)
            pygame.draw.rect(screen, (230, 230, 230), (0, 450, 1200, 150))
            cloud_rect_list = cloud_movement(cloud_rect_list)
            pygame.draw.line(screen, (100, 100, 100), (0, 450), (1200, 450), 4)
        else:
            screen2.blit(screen, (0, 0))
            gameover(screen2, score, 'dino')
            return
        a += 1
        pygame.display.update()
        clock.tick(130)


class Dino(pygame.sprite.Sprite):
    image = pygame.transform.scale(load_image("gameover.png"), (1204, 602))

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Dino.image
        self.rect = self.image.get_rect()
        self.rect.x = -1300
        self.rect.y = 0
        self.score = 0

    def add_score(self, score):
        self.score = score

    def update(self, *args):
        if self.rect.right + args[0][0] <= 1203:
            self.rect = self.rect.move(args[0][0], args[0][1])


def gameover(screen2, score, name):
    pygame.mouse.set_visible(False)
    all_sprite = pygame.sprite.Group()
    Dino(all_sprite)
    if BD(name) < score:
        x = 'data/game.sqlite'
        con = sqlite3.connect(x)
        cur = con.cursor()
        # Выполнение запроса и получение всех результатов
        cur.execute("""UPDATE spisok
                    SET record = '""" + str(score) + """' """ +
                    """WHERE name = '""" + str(name) + """'""").fetchall()
        con.commit()
        con.close()
    running = True
    fps = 60
    v = 200
    a = 0
    clock = pygame.time.Clock()
    while running:
        screen.blit(screen2, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                a += 1
        if a == 1:
            dog_surf = pygame.transform.scale(load_image("gameover.png"), (1204, 602))
            dog_rect = dog_surf.get_rect(topleft=(0, 0))
            screen.blit(dog_surf, dog_rect)
            pygame.display.update()
        elif a > 1:
            return
        else:
            all_sprite.draw(screen)
            all_sprite.update((v / fps, 0))
        pygame.display.flip()
        clock.tick(60)


def exit(wid, hei):
    fon = pygame.transform.scale(load_image('systempng/exit.png'), (wid, hei))
    screen.blit(fon, (0, 0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return False
        pygame.display.flip()
        clock.tick(FPS)


def final(wid, hei):
    fon = pygame.transform.scale(load_image('final.png'), (wid, hei))
    screen.blit(fon, (0, 0))
    a = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                fon = pygame.transform.scale(load_image('systempng/endscreen.png'), (wid, hei))
                screen.blit(fon, (0, 0))
                a += 1
            if a >= 2:
                terminate()
        pygame.display.flip()
        clock.tick(FPS)


q = False
start_screen()
story_screen()
map = [list(row) for row in load_level('levelex.txt')]
player, player_x, player_y = generate_level(map)
running = True
b = ['b', 'a', '#', 'c', 'd', 'g', 'x', 'i']
pygame.mouse.set_visible(False)
while running:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if int(BD('flappy bird')) > 30 and (map[player_y][player_x - 1] == 'b' or
                                                map[player_y][player_x + 1] == 'b' or map[player_y - 1][
                                                    player_x] == 'b' or map[player_y + 1][player_x] == 'b'):
                start_screen2(False)
                sizescreen()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if map[player_y][player_x - 1] == 'a' or map[player_y][player_x + 1] == 'a' or \
                    map[player_y - 1][player_x] == 'a' or map[player_y + 1][player_x] == 'a':
                if q or int(BD('dino')) > 0:
                    start_screen1()
                    sizescreen()
            elif map[player_y][player_x - 1] == 'b' or map[player_y][player_x + 1] == 'b' or \
                    map[player_y - 1][player_x] == 'b' or map[player_y + 1][player_x] == 'b':
                if int(BD('flappy bird')) > 50:
                    start_screen2(True)
                    sizescreen()
            elif map[player_y][player_x - 1] == 'g' or map[player_y][player_x + 1] == 'g' or \
                    map[player_y - 1][player_x] == 'g' or map[player_y + 1][player_x] == 'g':
                if int(BD('flappy bird')) <= 50:
                    q = True
                    story_screen2()
    pygame.time.delay(20)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        if exit(width, height):
            running = False
    elif keys[pygame.K_a] and map[player_y][player_x - 1] not in b:
        player.rect.x -= tile_width
        player_x -= 1
        player.left()
    elif keys[pygame.K_d] and map[player_y][player_x + 1] not in b:
        player.rect.x += tile_width
        player_x += 1
        player.right()
    elif keys[pygame.K_w] and map[player_y - 1][player_x] not in b:
        player.rect.y -= tile_height
        player_y -= 1
        player.up()
    elif keys[pygame.K_s] and map[player_y + 1][player_x] not in b:
        player.rect.y += tile_height
        player_y += 1
        player.down()
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    screen.fill((132, 141, 39))
    tiles_group.draw(screen)
    player_group.draw(screen)
    player.ugl(screen)
    pygame.display.update()
    clock.tick(60)
