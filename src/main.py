import pygame as py
from numpy.random import randint
from os import environ
from button import Button

environ['SDL_VIDEO_WINDOW_POS'] = "500,200"
py.init()

screen = py.display.set_mode((800, 700))

py.display.set_caption("Visualising Sorting Algorithms")
py.display.set_icon(py.image.load("images/icon.png"))


# Values
run = True
arr_size = 60
arr_range = [50, 300]
rec_width = 10
start_pos = 50
border_width = 2


def gen_arr_btn_action():
    global arr, arr_visualised
    arr_visualised = False
    arr = randint(arr_range[0], arr_range[1], arr_size)


arr, arr_visualised = randint(arr_range[0], arr_range[1], arr_size), False
recs = dict()  # Dictionary contains the number and it's rectangle
gen_arr_btn = Button(rect=(10, 10, 115, 25),
                     click_action=gen_arr_btn_action, text='Generate New Array', font=py.font.Font(None, 16))

while run:

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        gen_arr_btn.get_event(event)

    gen_arr_btn.draw(screen)

    if arr_visualised == False:
        screen.fill((49, 51, 53))
        for i in range(arr_size):
            recs[arr[i]] = py.Rect(start_pos, 0, rec_width, arr[i]*2)
            recs[arr[i]].bottom = 700
            py.draw.rect(screen, (0, 153, 76),
                         recs[arr[i]])
            start_pos += rec_width + border_width
        arr_visualised = True

    start_pos = 50
    py.display.update()

py.quit()
