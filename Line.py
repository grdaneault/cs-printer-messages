import math

class Line:
    __slots__ = ('text', 'offset')

    CHARS_PER_LINE = 20

    def __init__(self, text, center=False):
        if len(text) < 20:
            spaces = (Line.CHARS_PER_LINE - len(text))
            if center:
                text = ' ' * math.floor(spaces / 2) + text + ' ' * math.ceil(spaces / 2)

            else:
                text += ' ' * spaces
        else:
            text += '   '

        self.text = text
        self.offset = 0

    def isScrolling(self):
        return len(self.text) > 20

    def show(self):
        if not self.isScrolling():
            return self.text
        else:
            string = self.rotated_line()
            self.offset = (self.offset + 1) % len(self.text)
            return string

    def rotated_line(self):
        rotated = self.text[self.offset:] + self.text[:self.offset]
        return rotated[:20]