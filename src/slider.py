import pygame as pg

pg.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
TRANS = (1, 1, 1)

font = pg.font.SysFont("Verdana", 12)


class Slider():
    def __init__(self, screen, name, val, maxi, mini, xpos, ypos):
        self.screen = screen
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = xpos  # x-location on screen
        self.ypos = ypos
        self.surf = pg.surface.Surface((100, 50))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = font.render(name, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        self.surf.fill((100, 100, 100))
        pg.draw.rect(self.surf, GREY, [0, 0, 100, 50], 3)
        pg.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
        pg.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)

        # this surface never changes
        self.surf.blit(self.txt_surf, self.txt_rect)

        # dynamic graphics - button surface #
        self.button_surf = pg.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pg.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pg.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)

    def draw(self):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()

        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        # move of button box to correct screen position
        self.button_rect.move_ip(self.xpos, self.ypos)

        # screen
        self.screen.blit(surf, (self.xpos, self.ypos))

    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pg.mouse.get_pos()[
                    0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
