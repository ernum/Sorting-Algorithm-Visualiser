import pygame as py
from math import floor

FPS = 30
clock = py.time.Clock()


def insertion(screen, rects):
    i = 1
    while i < len(rects):
        j = i
        while j > 0 and rects[j-1].height > rects[j].height:
            swap(screen, rects, j-1, j, True)
            visualisation(screen, rects, i)
            j -= 1
        i += 1
    draw_rects(rects, screen)


def quickSort(screen, rects, lo, hi):
    if lo < hi:
        p = partition(screen, rects, lo, hi)
        quickSort(screen, rects, lo, p)
        quickSort(screen, rects, p + 1, hi)
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

        swap(screen, rects, i, j, True)
        visualisation(screen, rects, pivot_pos)


def heapSort(screen, rects):
    n = len(rects)
    buildMaxHeap(screen, rects, n)
    for i in range(n-1, 0, -1):
        swap(screen, rects, 0, i, True)
        heapify(screen, rects, i, 0)
        visualisation(screen, rects, i)
    draw_rects(rects, screen)


def buildMaxHeap(screen, rects, n):
    for i in range(floor(n/2) - 1, -1, -1):
        heapify(screen, rects, n, i)


def heapify(screen, rects, n, i):
    max = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < n and rects[left].height > rects[i].height:
        max = left

    if right < n and rects[right].height > rects[max].height:
        max = right

    if max != i:
        swap(screen, rects, i, max, True)
        draw_rects(rects, screen)
        heapify(screen, rects, n, max)


def swap(screen, rects, left, right, visualise):
    rects[left].height, rects[right].height = rects[right].height, rects[left].height
    rects[left].bottom = 700
    rects[right].bottom = 700

    if visualise:
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
