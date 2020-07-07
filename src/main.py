import pygame as py
from numpy.random import randint
from os import environ

environ['SDL_VIDEO_WINDOW_POS'] = "500,200"
py.init()

DISPLAY = py.display.set_mode((800, 600))
py.display.set_caption("Visualising Sorting Algorithms")
py.display.set_icon(py.image.load("images/icon.png"))

# Values
run = True
arr_size = 10
arr_range = [0, 100]
rec_width = 10
start_pos = 200

arr = randint(arr_range[0], arr_range[1], arr_size)
recs = dict()  # Dictionary contains the number and it's rectangle

while run:

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

    for i in range(arr_size):
        recs[arr[i]] = py.Rect(start_pos, 100, rec_width, arr[i]*2)
        py.draw.rect(DISPLAY, (255, 255, 255),
                     (start_pos, 100, rec_width, arr[i]*2))
        start_pos += rec_width
    py.display.update()

print(recs)
print(arr)

for val in recs.values():
    print(val)
py.quit()
