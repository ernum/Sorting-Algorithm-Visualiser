import pygame as py
from os import environ

environ['SDL_VIDEO_WINDOW_POS'] = "500,200"
py.init()

win = py.display.set_mode((800, 600))
py.display.set_caption("Visualising Sorting Algorithms")
py.display.set_icon(py.image.load("images/icon.png"))

run = True

while run:

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

py.quit()
