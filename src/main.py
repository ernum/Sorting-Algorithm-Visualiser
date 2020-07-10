import pygame as py
from numpy.random import randint
from os import environ
from button import Button
import sort

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


def sort_arr_btn_action():
    global screen, recs, arr_size
    sort.insertion(screen, recs)
    sort_arr_btn.change_disabled_status()
    gen_arr_btn.change_disabled_status()
    insertion_sort_btn.amount_clicked += 1


def insertion_sort_btn_action():
    sort_arr_btn.change_disabled_status()
    gen_arr_btn.change_disabled_status()


arr, arr_visualised = randint(arr_range[0], arr_range[1], arr_size), False
gen_arr_btn = Button(rect=(10, 10, 125, 25),
                     click_action=gen_arr_btn_action, text='Generate New Array', font=py.font.Font(None, 16), disabled=False)
sort_arr_btn = Button(rect=(10, 40, 125, 25), click_action=sort_arr_btn_action,
                      text='Sort Array', font=py.font.Font(None, 16), disabled=True)
insertion_sort_btn = Button(rect=(650, 10, 125, 25), click_action=insertion_sort_btn_action,
                            text='Insertion Sort', font=py.font.Font(None, 16), clicked_border_colour=py.Color('yellow'), disabled=False)


while run:

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        gen_arr_btn.get_event(event)
        sort_arr_btn.get_event(event)
        insertion_sort_btn.get_event(event)

    sort_arr_btn.draw(screen)
    gen_arr_btn.draw(screen)
    insertion_sort_btn.draw(screen)

    if not arr_visualised:
        recs = []
        screen.fill((49, 51, 53))
        for i in range(arr_size):
            recs.append(py.Rect(start_pos, 0, rec_width, arr[i]*2))
            recs[i].bottom = 700
            py.draw.rect(screen, (0, 153, 76),
                         recs[i])
            start_pos += rec_width + border_width
        arr_visualised = True
        start_pos = 50
    py.display.update()

py.quit()
