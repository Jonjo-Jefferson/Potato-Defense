import pygame as pg
import constants as c

# init game
pg.init()

# clock
clock = pg.time.Clock()

# window
screen = pg.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
pg.display.set_caption("Potato Defense")
# game loop
run = True
while run:
    clock.tick(c.FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False


pg.QUIT()
