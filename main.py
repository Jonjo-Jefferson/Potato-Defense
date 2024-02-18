import pygame as pg
import constants as c
from enemy import Enemy

# init game
pg.init()

# clock
clock = pg.time.Clock()

# window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Potato Defense")

# load images
enemy_image = pg.image.load("assets/images/enemies/enemy_1.png").convert_alpha()


enemy = Enemy((200, 300), enemy_image)

# groups
enemy_group = pg.sprite.Group()
enemy_group.add(enemy)

print(enemy)
# game loop
run = True
while run:

    clock.tick(c.FPS)

    screen.fill("grey100")
    # update groups
    enemy_group.update()

    # draw groups
    enemy_group.draw(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # update display
    pg.display.flip()
