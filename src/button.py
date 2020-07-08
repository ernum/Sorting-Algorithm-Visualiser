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
            "font": py.font.Font('Arial', 16),
            "font_colour": py.Color("white"),
            "call_on_release": True,
            "clicked_color": None,
            "border_colour": py.Color('black'),
            "border_hover_colour": py.Color('yellow'),
            "radius": 3,
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
        return False

    def draw(self):
        pass
