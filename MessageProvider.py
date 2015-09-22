import abc

class MessageProvider:

    @abc.abstractmethod
    def screen(self):
        """
        Gets the screen to display this message
        :return: Screen
        """
        pass