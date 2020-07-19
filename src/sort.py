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
    sort_completion_visualisation(rects, screen)


def quickSort(screen, rects, lo, hi):
    n = len(rects)
    if lo < hi:
        p = partition(screen, rects, lo, hi)
        quickSort(screen, rects, lo, p)
        quickSort(screen, rects, p + 1, hi)
    if lo == 0 and hi == n-1:
        sort_completion_visualisation(rects, screen)


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
    sort_completion_visualisation(rects, screen)


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


def bubbleSort(screen, rects):
    n = len(rects)
    for i in range(n):
        for j in range(0, n-i-1):
            if rects[j].height > rects[j+1].height:
                swap(screen, rects, j, j+1, True)
                screen.fill((0, 0, 0))
                draw_rects(rects, screen)
                clock.tick(FPS)
    sort_completion_visualisation(rects, screen)


def selectionSort(screen, rects):
    n = len(rects)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if rects[min].height > rects[j].height:
                min = j
        swap(screen, rects, i, min, True)
        visualisation(screen, rects, i)
    sort_completion_visualisation(rects, screen)


def mergeSort(screen, rects):
    n = len(rects)
    if n > 1:
        mid = floor(n/2)
        L = rects[:mid]
        R = rects[mid:]

        mergeSort(screen, L)
        mergeSort(screen, R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i].height < R[j].height:
                rects[k].height = L[i].height
                i += 1
            else:
                rects[k].height = R[j].height
                j += 1
            k += 1
            visualisation(screen, rects, i)

        while i < len(L):
            rects[k].height = L[i].height
            i += 1
            k += 1

        while j < len(R):
            rects[k].height = R[j].height
            j += 1
            k += 1


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
        rect.bottom = 700


def sort_completion_visualisation(rects, screen):
    draw_rects(rects, screen)
    for rect in rects:
        py.draw.rect(screen, (0, 255, 0), rect)
        py.display.update()
        clock.tick(60)
    draw_rects(rects, screen)
