from Line import Line
from MessageProvider import MessageProvider
from Screen import Screen

class StaticMessageProvider(MessageProvider):

    __slots__ = ("lines")

    def __init__(self, content, center=False, duration=30, animation=2):
        MessageProvider.__init__(self, duration, animation)
        self.lines = []

        for line in content:
            self.lines.append(Line(line, center=center))

    def screen(self):
        return Screen(self.lines, self.duration, self.animation)
