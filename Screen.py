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
        self.lines = lines
        self.max_duration = max_duration
        self.animation_duration = animation_duration

    def show(self, *targets):

        elapsed = 0
        last_sent = None
        while elapsed < self.max_duration:
            to_send = self.get_message()

            if to_send != last_sent:
                last_sent = to_send
                for target in targets:
                    if target is None:
                        print("To send:", to_send)
                    else:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((target, 9100))
                        s.send(bytes(Screen.JOB % to_send, 'UTF-8'))
            else:
                print("Not resending.")

            time.sleep(self.animation_duration)
            elapsed += self.animation_duration

    def get_message(self):
        message = ""
        for line in self.lines:
            message += line.show()

        return message