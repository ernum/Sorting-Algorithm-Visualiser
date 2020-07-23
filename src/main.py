import pygame as pg
import sort
from random import randint
from os import environ
from button import Button
from gc import collect
from slider import Slider

environ['SDL_VIDEO_WINDOW_POS'] = "500,200"
pg.init()

screen = pg.display.set_mode((800, 700))

pg.display.set_caption("Visualising Sorting Algorithms")
pg.display.set_icon(pg.image.load("images/icon.png"))


# Sliders
arr_size = Slider(screen, "Rects", 10, 50, 1, 160, 12)
speed = Slider(screen, "Speed", 60, 120, 10, 275, 12)
slides = [arr_size, speed]

# Values
run = True
rect_width = 10
start_pos = pos = 50
end_pos = 770
border_width = 2


def gen_arr_btn_action():
    global arr_visualised, start_pos, pos
    arr_visualised = False
    pos = start_pos
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
        sort.quickSort(screen, rects, 0, len(rects) - 1)
        quick_sort_btn.amount_clicked += 1
        quick_sort_btn.change_disabled_status()
    elif index == 2:
        sort.heapSort(screen, rects)
        heap_sort_btn.amount_clicked += 1
        heap_sort_btn.change_disabled_status()
    elif index == 3:
        sort.mergeSort(screen, rects, 0, len(rects) - 1)
        merge_sort_btn.amount_clicked += 1
        merge_sort_btn.change_disabled_status()
    elif index == 4:
        sort.selectionSort(screen, rects)
        selection_sort_btn.amount_clicked += 1
        selection_sort_btn.change_disabled_status()
    elif index == 5:
        sort.bubbleSort(screen, rects)
        bubble_sort_btn.amount_clicked += 1
        bubble_sort_btn.change_disabled_status()

    change_sort_and_gen_status()


def insertion_sort_btn_action():
    evaluate_buttons(0)
    change_sort_and_gen_status()


def quick_sort_btn_action():
    evaluate_buttons(1)
    change_sort_and_gen_status()


def heap_sort_btn_action():
    evaluate_buttons(2)
    change_sort_and_gen_status()


def merge_sort_btn_action():
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


def check_sort_btns_disable_status(sort_btns):
    """ Returns false if any sort button is disabled. """
    for sort in sort_btns:
        if sort.disabled:
            return False
    return True


arr_visualised = False
gen_arr_btn = Button(rect=(10, 10, 125, 25),
                     click_action=gen_arr_btn_action, text='Generate New Array', font=pg.font.Font(None, 16), disabled=False)
sort_arr_btn = Button(rect=(10, 40, 125, 25), click_action=sort_arr_btn_action,
                      text='Sort Array', font=pg.font.Font(None, 16), disabled=True)
insertion_sort_btn = Button(rect=(650, 10, 125, 25), click_action=insertion_sort_btn_action,
                            text='Insertion Sort', font=pg.font.Font(None, 16), clicked_border_colour=pg.Color('yellow'), disabled=False)
quick_sort_btn = Button(rect=(650, 40, 125, 25), click_action=quick_sort_btn_action,
                        text='Quick Sort', font=pg.font.Font(None, 16), clicked_border_colour=pg.Color('yellow'), disabled=False)
merge_sort_btn = Button(rect=(520, 10, 125, 25), click_action=merge_sort_btn_action,
                        text='Merge Sort', font=pg.font.Font(None, 16), clicked_border_colour=pg.Color('yellow'), disabled=False)
heap_sort_btn = Button(rect=(520, 40, 125, 25), click_action=heap_sort_btn_action,
                       text='Heap Sort', font=pg.font.Font(None, 16), clicked_border_colour=pg.Color('yellow'), disabled=False)
selection_sort_btn = Button(rect=(390, 10, 125, 25), click_action=selection_sort_btn_action,
                            text='Selection Sort', font=pg.font.Font(None, 16), clicked_border_colour=pg.Color('yellow'), disabled=False)
bubble_sort_btn = Button(rect=(390, 40, 125, 25), click_action=bubble_sort_btn_action,
                         text='Bubble Sort', font=pg.font.Font(None, 16), clicked_border_colour=pg.Color('yellow'), disabled=False)

sort_btns = [insertion_sort_btn,
             quick_sort_btn, heap_sort_btn, merge_sort_btn, selection_sort_btn, bubble_sort_btn]
sort_boolean_val = [0] * len(sort_btns)

while run:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            m_pos = pg.mouse.get_pos()
            if check_sort_btns_disable_status(sort_btns):
                for s in slides:
                    if s.button_rect.collidepoint(m_pos):
                        s.hit = True
        elif event.type == pg.MOUSEBUTTONUP:
            if check_sort_btns_disable_status(sort_btns):
                for s in slides:
                    if s is arr_size and arr_size.hit:
                        pos = 50
                        arr_visualised = False
                    s.hit = False

        gen_arr_btn.get_event(event)
        sort_arr_btn.get_event(event)
        [sort.get_event(event) for sort in sort_btns]

    for s in slides:
        if s.hit:
            s.move()

    for s in slides:
        s.draw()

    sort_arr_btn.draw(screen)
    gen_arr_btn.draw(screen)
    [sort.draw(screen) for sort in sort_btns]

    rect_width = int(arr_size.val)
    sort.FPS = int(s.val)

    if not arr_visualised:
        rects = []
        screen.fill((0, 0, 0))
        while pos <= end_pos:
            change_in_pos = rect_width + border_width
            if pos + change_in_pos > end_pos:
                break
            else:
                rects.append(
                    pg.Rect(pos, 0, rect_width, randint(50, 300)*2))
                rects[-1].bottom = 700
                pg.draw.rect(screen, (255, 255, 255),
                             rects[-1])
                pos += change_in_pos
        arr_visualised = True
    pg.display.update()

pg.quit()
