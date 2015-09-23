import abc

class MessageProvider:

    __slots__ = ("duration", "animation")

    def __init__(self, duration, animation):
        self.duration = duration
        self.animation = animation

    @abc.abstractmethod
    def screen(self):
        """
        Gets the screen to display this message
        :return: Screen
        """
        pass