import pygame as py
from time import sleep


def insertion(screen, recs, arr_size):
    i = 1
    while i < len(recs):
        j = i
        while j > 0 and recs[j-1].height > recs[j].height:
            recs[j].height, recs[j-1].height = recs[j-1].height, recs[j].height
            recs[j].bottom = 700
            recs[j-1].bottom = 700
            j -= 1
        screen.fill((49, 51, 53))
        for rec in recs:
            py.draw.rect(screen, (0, 153, 76), rec)
        py.display.update()
        sleep(0.1)
        i += 1


def swap(recs, left, right):
    recs()
