import socket

import time


class Screen():
    __slots__ = ("lines", "max_duration", "animation_duration")

    JOB = """\
\x1b%%-12345X@PJL JOB
@PJL RDYMSG DISPLAY="%s"
@PJL EOJ
\x1b%%-12345X
"""

    def __init__(self, lines, max_duration=60, animation_duration=2):
        """
        Constructor.

        :param lines:  List of lines of text to display on the screen.  Maximum length 4
        :param max_duration:  The amount of time this message will be on screen
        :param animation_duration:  The duration of any animation effect.
        Essentially, how often the show command should be called on each line.
        """
        self.lines = lines
        self.max_duration = max_duration
        self.animation_duration = animation_duration

    def show(self, targets, verbose=False):
        """
        Sends the contents of the screen to the specified targets

        :param targets:  List of targets to print to.  Include None to print locally to console.
        """
        elapsed = 0
        last_sent = None
        while elapsed < self.max_duration:
            to_send = self.get_message()

            if to_send != last_sent:
                last_sent = to_send
                for target in targets:
                    if target is None:
                        print("Sent: '%s'" % to_send)
                    else:
                        try:
                            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((target, 9100))
                            s.send(bytes(Screen.JOB % to_send, 'UTF-8'))
                        except socket.timeout:
                            print("Error:  timeout when sending to %s." % target)
                        except socket.error:
                            print("Error:  could not connect to %s." % target)
            else:
                if verbose:
                    print("Not resending.")

            time.sleep(self.animation_duration)
            elapsed += self.animation_duration

    def get_message(self):
        """
        Gathers the messages from all lines
        :return: The combined message, with no separator characters between lines.
        """
        message = ""
        for line in self.lines:
            message += line.show()

        return message
