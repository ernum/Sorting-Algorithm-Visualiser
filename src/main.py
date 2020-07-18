import pygame as py
import sort
from numpy.random import randint
from os import environ
from button import Button
from gc import collect

environ['SDL_VIDEO_WINDOW_POS'] = "500,200"
py.init()

screen = py.display.set_mode((800, 700))

py.display.set_caption("Visualising Sorting Algorithms")
py.display.set_icon(py.image.load("images/icon.png"))


# Values
run = True
arr_size = 60
arr_range = [50, 300]
rect_width = 10
start_pos = 50
border_width = 2


def gen_arr_btn_action():
    global arr, arr_visualised
    arr_visualised = False
    arr = randint(arr_range[0], arr_range[1], arr_size)
    [sort.change_disabled_status() for sort in sort_btns if sort.disabled]
    collect()


def sort_arr_btn_action():
    global sort_boolean_val
    index = sort_boolean_val.index(1)

    if index == 0:
        sort.insertion(screen, rects)
        insertion_sort_btn.amount_clicked += 1
        insertion_sort_btn.change_disabled_status()
    elif index == 1:
        sort.quicksort(screen, rects, 0, len(rects) - 1)
        quick_sort_btn.amount_clicked += 1
        quick_sort_btn.change_disabled_status()

    change_sort_and_gen_status()


def insertion_sort_btn_action():
    evaluate_buttons(0)
    change_sort_and_gen_status()


def quick_sort_btn_action():
    evaluate_buttons(1)
    change_sort_and_gen_status()


def merge_sort_btn_action():
    evaluate_buttons(2)
    change_sort_and_gen_status()


def heap_sort_btn_action():
    evaluate_buttons(3)
    change_sort_and_gen_status()


def selection_sort_btn_action():
    evaluate_buttons(4)
    change_sort_and_gen_status()


def bubble_sort_btn_action():
    evaluate_buttons(5)
    change_sort_and_gen_status()


def change_sort_and_gen_status():
    sort_arr_btn.change_disabled_status()
    gen_arr_btn.change_disabled_status()


def evaluate_buttons(pos):
    global sort_boolean_val

    if 1 in sort_boolean_val:
        sort_boolean_val = [0] * len(sort_btns)

    sort_boolean_val[pos] = 1
    [sort.change_disabled_status()
     for sort in sort_btns if sort != sort_btns[pos]]


arr, arr_visualised = randint(arr_range[0], arr_range[1], arr_size), False
gen_arr_btn = Button(rect=(10, 10, 125, 25),
                     click_action=gen_arr_btn_action, text='Generate New Array', font=py.font.Font(None, 16), disabled=False)
sort_arr_btn = Button(rect=(10, 40, 125, 25), click_action=sort_arr_btn_action,
                      text='Sort Array', font=py.font.Font(None, 16), disabled=True)
insertion_sort_btn = Button(rect=(650, 10, 125, 25), click_action=insertion_sort_btn_action,
                            text='Insertion Sort', font=py.font.Font(None, 16), clicked_border_colour=py.Color('yellow'), disabled=False)
quick_sort_btn = Button(rect=(650, 40, 125, 25), click_action=quick_sort_btn_action,
                        text='Quick Sort', font=py.font.Font(None, 16), clicked_border_colour=py.Color('yellow'), disabled=False)
merge_sort_btn = Button(rect=(520, 10, 125, 25), click_action=merge_sort_btn_action,
                        text='Merge Sort', font=py.font.Font(None, 16), clicked_border_colour=py.Color('yellow'), disabled=False)
heap_sort_btn = Button(rect=(520, 40, 125, 25), click_action=heap_sort_btn_action,
                       text='Heap Sort', font=py.font.Font(None, 16), clicked_border_colour=py.Color('yellow'), disabled=False)
selection_sort_btn = Button(rect=(390, 10, 125, 25), click_action=selection_sort_btn_action,
                            text='Selection Sort', font=py.font.Font(None, 16), clicked_border_colour=py.Color('yellow'), disabled=False)
bubble_sort_btn = Button(rect=(390, 40, 125, 25), click_action=bubble_sort_btn_action,
                         text='Bubble Sort', font=py.font.Font(None, 16), clicked_border_colour=py.Color('yellow'), disabled=False)

sort_btns = [insertion_sort_btn,
             quick_sort_btn, merge_sort_btn, heap_sort_btn, selection_sort_btn, bubble_sort_btn]
sort_boolean_val = [0] * len(sort_btns)

while run:

    for event in py.event.get():
        if event.type == py.QUIT:
            run = False

        gen_arr_btn.get_event(event)
        sort_arr_btn.get_event(event)
        [sort.get_event(event) for sort in sort_btns]

    sort_arr_btn.draw(screen)
    gen_arr_btn.draw(screen)
    [sort.draw(screen) for sort in sort_btns]

    if not arr_visualised:
        rects = []
        screen.fill((0, 0, 0))
        for i in range(arr_size):
            rects.append(py.Rect(start_pos, 0, rect_width, arr[i]*2))
            rects[i].bottom = 700
            py.draw.rect(screen, (255, 255, 255),
                         rects[i])
            start_pos += rect_width + border_width
        arr_visualised = True
        start_pos = 50
    py.display.update()

py.quit()
