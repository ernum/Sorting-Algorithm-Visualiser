import pygame as py

FPS = 30
clock = py.time.Clock()


def insertion(screen, rects):
    i = 1
    while i < len(rects):
        j = i
        while j > 0 and rects[j-1].height > rects[j].height:
            swap(screen, rects, j-1, j)
            screen.fill((0, 0, 0))
            draw_rects(rects, screen)
            py.draw.rect(screen, (0, 255, 0), rects[i])
            py.display.update()
            clock.tick(FPS)
            j -= 1
        i += 1
        py.display.update()
    draw_rects(rects, screen)


def swap(screen, rects, left, right):
    rects[left].height, rects[right].height = rects[right].height, rects[left].height
    rects[left].bottom = 700
    rects[right].bottom = 700
    py.draw.rect(screen, (255, 0, 0), rects[left])
    py.draw.rect(screen, (255, 0, 0), rects[right])
    py.display.update()
    clock.tick(FPS)


def draw_rects(rects, screen):
    for rect in rects:
        py.draw.rect(screen, (255, 255, 255), rect)
