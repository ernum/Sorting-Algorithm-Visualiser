import pygame as py


class Text():
    """A simple class for generating text on screen for pygame."""

    def __init__(self, text, **kwargs):
        self.process_kwargs(kwargs)
        self.text = text
        self.text_width = self.position[0]
        self.text_height = self.position[1]
        self.generate_text()

    def process_kwargs(self, kwargs):
        settings = {
            "text_size": 100,
            "position": (800, 700),
            "font_colour": (255, 255, 255),
            "background_colour": (0, 0, 0)
        }

        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError(
                    f"{self.__class__.__name__} has no keyword: {kwarg}")
        self.__dict__.update(settings)

    def text_objects(self, font):
        textSurface = font.render(self.text, True, self.font_colour)
        return textSurface, textSurface.get_rect()

    def generate_text(self):
        self.background = py.Rect()
        font = py.font.Font(None, self.text_size)
        self.TextSurf, self.TextRect = self.text_objects(font)
        self.TextRect.center = ((self.text_width/2), (self.text_height/2))
