import pygame as py
from math import floor

FPS = 30
clock = py.time.Clock()


def insertion(screen, rects):
    i = 1
    while i < len(rects):
        j = i
        while j > 0 and rects[j-1].height > rects[j].height:
            swap(screen, rects, j-1, j)
            visualisation(screen, rects, i)
            j -= 1
        i += 1

    draw_rects(rects, screen)


def quicksort(screen, rects, lo, hi):
    if lo < hi:
        p = partition(screen, rects, lo, hi)
        quicksort(screen, rects, lo, p)
        quicksort(screen, rects, p + 1, hi)
    draw_rects(rects, screen)


def partition(screen, rects, lo, hi):
    pivot_pos = floor((hi + lo) / 2)
    pivot = rects[pivot_pos].height
    i, j = lo - 1, hi + 1

    while True:
        while True:
            i += 1
            if not rects[i].height < pivot:
                break
        while True:
            j -= 1
            if not rects[j].height > pivot:
                break
        if i >= j:
            return j

        swap(screen, rects, i, j)
        visualisation(screen, rects, pivot_pos)


def swap(screen, rects, left, right):
    rects[left].height, rects[right].height = rects[right].height, rects[left].height
    rects[left].bottom = 700
    rects[right].bottom = 700
    py.draw.rect(screen, (255, 0, 0), rects[left])
    py.draw.rect(screen, (255, 0, 0), rects[right])
    py.display.update()
    clock.tick(FPS)


def visualisation(screen, rects, i):
    screen.fill((0, 0, 0))
    draw_rects(rects, screen)
    py.draw.rect(screen, (0, 255, 0), rects[i])
    py.display.update()
    clock.tick(FPS)


def draw_rects(rects, screen):
    for rect in rects:
        py.draw.rect(screen, (255, 255, 255), rect)
