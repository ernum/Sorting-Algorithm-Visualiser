import pygame as py

FPS = 60
clock = py.time.Clock()


def insertion(screen, rects):
    i = 1
    while i < len(rects):
        j = i
        while j > 0 and rects[j-1].height > rects[j].height:
            py.draw.rect(screen, (255, 255, 255), rects[j])
            py.draw.rect(screen, (255, 255, 255), rects[j-1])
            py.display.update()

            swap(rects, j-1, j)

            screen.fill((49, 51, 53))
            draw_rects(rects, screen)

            py.draw.rect(screen, (255, 255, 255), rects[i])
            py.draw.rect(screen, (255, 255, 255), rects[j])
            py.draw.rect(screen, (255, 255, 255), rects[j-1])

            py.display.update()
            clock.tick(FPS)
            j -= 1
        i += 1
        py.display.update()
    draw_rects(rects, screen)


def swap(rects, left, right):
    rects[left].height, rects[right].height = rects[right].height, rects[left].height
    rects[left].bottom = 700
    rects[right].bottom = 700


def draw_rects(rects, screen):
    for rect in rects:
        py.draw.rect(screen, (0, 153, 76), rect)
