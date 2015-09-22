from Line import Line
from MessageProvider import MessageProvider
from Screen import Screen

class StaticMessageProvider(MessageProvider):

    __slots__ = ("lines", "duration")

    def __init__(self, *args, **kwargs):

        if "center" not in kwargs:
            kwargs["center"] = False

        if "duration" not in kwargs:
            kwargs["duration"] = 10

        self.duration = kwargs["duration"]
        self.lines = []
        for line in args:
            self.lines.append(Line(line, center=kwargs["center"]))

    def screen(self):
        return Screen(self.lines, self.duration)
