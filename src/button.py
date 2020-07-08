import pygame as py


class Button():
    def __init__(self, rect, click_action, **kwargs):
        self.rect = py.Rect(rect)
        self.click_action = click_action
        self.clicked = False
        self.hovered = False
        self.process_kwargs(kwargs)
        self.render_text()

    def process_kwargs(self, kwargs):
        settings = {
            "colour": py.Color('red'),
            "text": None,
            "font": py.font.SysFont('Arial', 16),
            "font_colour": py.Color("white"),
            "call_on_release": True,
            "clicked_colour": None,
            "clicked_font_colour": None,
            "border_colour": py.Color('black'),
            "border_hover_colour": py.Color('yellow'),
            "radius": 3
        }

        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError(
                    f"{self.__class__.__name__} has no keyword: {kwarg}")
        self.__dict__.update(settings)

    def render_text(self):
        if self.text:
            self.text = self.font.render(self.text, True, self.font_colour)

    def get_event(self, event):
        if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == py.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self, event):
        if self.check_hover():
            self.clicked = True
            if not self.call_on_release:
                self.click_action()

    def on_release(self, event):
        if self.clicked and self.call_on_release:
            if self.check_hover():
                self.click_action()
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(py.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
            return True
        else:
            self.hovered = False
            return False

    def _render_region(self, image, rect, colour, rad):
        corners = rect.inflate(-2*rad, -2*rad)
        for attribute in ("topleft", "topright", "bottomleft", "bottomright"):
            py.draw.circle(image, colour, getattr(corners, attribute), rad)
        image.fill(colour, rect.inflate(-2*rad, 0))
        image.fill(colour, rect.inflate(0, -2*rad))

    def round_rect(self, screen, rect, colour, rad=20, border=0, inside=(0, 0, 0, 0)):
        rect = py.Rect(rect)
        zeroed_rect = rect.copy()
        zeroed_rect.topleft = 0, 0
        image = py.Surface(rect.size).convert_alpha()
        image.fill((0, 0, 0, 0))
        self._render_region(image, zeroed_rect, colour, rad)
        if border:
            zeroed_rect.inflate_ip(-2*border, -2*border)
            self._render_region(image, zeroed_rect, inside, rad)
        screen.blit(image, rect)

    def draw(self, screen):
        colour = self.colour
        text = self.text
        border = self.border_colour
        self.check_hover()

        if self.clicked and self.clicked_colour:
            colour = self.clicked_colour
            if self.clicked_font_colour:
                text = self.clicked_text
        if self.hovered and not self.clicked:
            border = self.border_hover_colour

        self.round_rect(screen, self.rect, border, self.radius, 1, colour)
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            screen.blit(text, text_rect)
