import pygame as pg
from math import floor
from time import sleep

FPS = 45
clock = pg.time.Clock()


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


def merge(screen, rects, start, mid, end):
    second_start = mid + 1
    original_start = start
    original_end = end

    if rects[mid].height <= rects[second_start].height:
        return

    while start <= mid and second_start <= end:
        if rects[start].height <= rects[second_start].height:
            start += 1
            merge_sort_visualisation(
                screen, rects, start, second_start, (255, 0, 0), original_start, original_end)
        else:
            merge_sort_visualisation(
                screen, rects, start, second_start, (255, 0, 0), original_start, original_end)
            value = rects[second_start].height
            index = second_start

            while index != start:
                rects[index].height = rects[index - 1].height
                index -= 1

            rects[start].height = value

            start += 1
            mid += 1
            second_start += 1


def mergeSort(screen, rects, left, right):
    if left < right:
        mid = left + (right - left) // 2
        mergeSort(screen, rects, left, mid)
        mergeSort(screen, rects, mid + 1, right)
        merge(screen, rects, left, mid, right)

    if left == 0 and right == len(rects) - 1:
        sort_completion_visualisation(rects, screen)


def swap(screen, rects, left, right, visualise):
    rects[left].height, rects[right].height = rects[right].height, rects[left].height
    rects[left].bottom = 700
    rects[right].bottom = 700

    if visualise:
        pg.draw.rect(screen, (255, 0, 0), rects[left])
        pg.draw.rect(screen, (255, 0, 0), rects[right])
        pg.display.update()

    clock.tick(FPS)


def merge_sort_visualisation(screen, rects, start, second_start, colour, left, right):
    screen.fill((0, 0, 0))
    draw_rects(rects, screen, left, right)
    pg.draw.rect(screen, colour, rects[start])
    pg.draw.rect(screen, colour, rects[second_start])
    pg.display.update()
    clock.tick(FPS)


def visualisation(screen, rects, i):
    screen.fill((0, 0, 0))
    draw_rects(rects, screen)
    pg.draw.rect(screen, (0, 255, 0), rects[i])
    pg.display.update()
    clock.tick(FPS)


def draw_rects(rects, screen, *exclude):
    excluded_rects = []
    if exclude:
        for val in exclude:
            excluded_rects.append(rects[val])

    for rect in rects:
        rect.bottom = 700
        if rect not in excluded_rects:
            pg.draw.rect(screen, (255, 255, 255), rect)
        else:
            pg.draw.rect(screen, (0, 255, 0), rect)


def sort_completion_visualisation(rects, screen):
    screen.fill((0, 0, 0))
    draw_rects(rects, screen)
    for rect in rects:
        pg.draw.rect(screen, (0, 255, 0), rect)
        pg.display.update()
        clock.tick(60)
    draw_rects(rects, screen)
