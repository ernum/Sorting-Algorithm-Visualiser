import pygame as py
from text import Text
py.init()

screen = py.display.set_mode((800, 700))
screen.fill((0, 0, 0))

text = Text('Game Over')
run = True

while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    screen.blit(text.TextSurf, text.TextRect)
    py.display.update()
