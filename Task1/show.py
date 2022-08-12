import pygame
from math import sqrt


def type_check(name, correct_type):
    """
    decorator function for checking correctness of input type
    name: attribute name --> str
    correct_type: correct_type of name attribute --> type
    Procedure：
    1. call type_check first，return prop setter，and convert name to private attribute. Store private_name  & correct_type information.
    2. class initializing attribute
    3. When initailize name attribute，it'll call prop and check type of input. If type is wrong, raise error; or set attribute by setattr function.
    """
    private_name = '_' + name

    @property
    def prop(self):
        return getattr(self, private_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, correct_type):
            raise ValueError("{} must be a {}".format(
                private_name, correct_type))
        setattr(self, private_name, value)

    return prop


class CirButton:
    """
    create circular Button object for different usage

    center: center of circle --> tuple
    top: radiuse of circle --> int
    text: text of button --> str
    textcolour: colour of text --> tuple, ex:(0,0,0)
    rectcolour: colour of button --> tuple, ex:(255, 255, 255)
    screen: pygame object "pygame.display.set_mode()"
    font: font of text
    """
    __slots__ = ["_center", "_radius", "_text",
                 "_textcolour", "_circolour",
                 "_screen", "_font"]

    textcolour = type_check("textcolour", tuple)
    circolour = type_check("circolour", tuple)

    def __init__(self, center: tuple, radius: int, text: str,
                 textcolour: tuple, circolour: tuple,
                 screen: pygame, font: pygame):
        self._radius = radius
        self._center = center
        self._text = text
        self._screen = screen
        self._font = font
        self.textcolour = textcolour
        self.circolour = circolour

    def __call__(self):
        button_text = self._font.render(self._text, True, self._textcolour)
        button_rect = button_text.get_rect()
        button_rect.center = self._center
        pygame.draw.circle(self._screen, self._circolour,
                           self._center, self._radius)
        self._screen.blit(button_text, button_rect)

    def colour_change(self, colour: tuple):
        """
        change colour of button

        colour: colour of button --> tuple, ex:(255, 255, 255)
        """
        self.circolour = colour

    def distance(self, mouse_pos: tuple) -> float:
        """
        compute distance between button and mouse

        mouse_pos: position of mouse --> tuple, ex:(x, y)
        """
        return sqrt((self._center[0]-mouse_pos[0])**2+(self._center[1]-mouse_pos[1])**2)


class RectButton:
    """
    create rectangular Button object for different usage

    left: left boundary of button --> int
    top: top boundary of button --> int
    width: width of button --> int
    height: height of button --> int
    text: text of button --> str
    textcolour: colour of text --> tuple, ex:(0,0,0)
    rectcolour: colour of button --> tuple, ex:(255, 255, 255)
    screen: pygame object "pygame.display.set_mode()"
    font: font of text
    """
    # 不允許新增其他屬性
    __slots__ = ["_left", "_top", "_width", "_height",
                 "_text", "_textcolour", "_rectcolour",
                 "_screen", "_font", "rect"]

    textcolour = type_check("textcolour", tuple)
    rectcolour = type_check("rectcolour", tuple)

    def __init__(self, left: int, top: int, width: int, height: int,
                 text: str, textcolour: tuple, rectcolour: tuple,
                 screen: pygame, font: pygame):
        self._left = left
        self._top = top
        self._width = width
        self._height = height
        self._text = text
        self._screen = screen
        self._font = font
        self.rect = pygame.Rect(self._left, self._top,
                                self._width, self._height)
        self.textcolour = textcolour
        self.rectcolour = rectcolour

    def __call__(self):
        button_text = self._font.render(self._text, True, self._textcolour)
        button_rect = button_text.get_rect()
        button_rect.center = self.rect.center
        pygame.draw.rect(self._screen, self._rectcolour, self.rect)
        self._screen.blit(button_text, button_rect)

    def colour_change(self, colour: tuple):
        """
        change colour of button
        colour: colour of button --> tuple, ex:(255, 255, 255)
        """
        self.rectcolour = colour


class ShowText:
    """
    create Text object for different usage

    center: center of text --> tuple, ex:(x, y)
    text: text to show --> list, each element for different row
    textcolour: colour of text --> tuple, ex:(0,0,0)
    screen: pygame object "pygame.display.set_mode()"
    font: font of text
    """
    # 不允許新增其他屬性
    __slots__ = ["_center", "_text", "_textcolour",
                 "_screen", "_font"]

    text = type_check("text", list)
    center = type_check("center", tuple)
    textcolour = type_check("textcolour", tuple)

    def __init__(self, center: tuple, text: list, textcolour: tuple, screen: pygame, font: pygame):
        self._screen = screen
        self._font = font
        self.center = center
        self.text = text
        self.textcolour = textcolour

    def __call__(self):
        for text in self._text:
            showtext = self._font.render(text, True, self._textcolour)
            textrect = showtext.get_rect()
            textrect.center = self._center
            self._screen.blit(showtext, textrect)
