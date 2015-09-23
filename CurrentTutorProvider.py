from Line import Line
from MessageProvider import MessageProvider
from Screen import Screen

import json
import datetime


class CurrentTutorProvider(MessageProvider):

    DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    __slots__ = ("tutors")

    def screen(self):
        self.update_tutor_list()
        now = datetime.datetime.now()
        day = now.weekday()
        hour = now.hour

        lines = self.screen_lines_for_time(CurrentTutorProvider.DAYS[day], "%2d" % hour)
        return Screen(lines, self.duration, self.animation)

    def __init__(self, duration=30, animation=2):
        MessageProvider.__init__(self, duration, animation)
        self.tutors = {}
        self.update_tutor_list()

    def update_tutor_list(self):
        try:
            json_data = open("tutoring_hours.json").read()
            self.tutors = json.loads(json_data)
        except IOError:
            print("Could not open tutor list")
        except ValueError:
            print("Could not parse tutor list")

    def screen_lines_for_time(self, day, time):
        """
        Creates the screen display lines for a given date/time

        :param day:  The day (string: monday, tuesday, ...)
        :param time:  The hour (10, 11, 12, 13, ...)
        :return: Line[]
        """
        if day in self.tutors and time in self.tutors[day]:
            current = self.tutors[day][time]
        else:
            current = []

        if len(current) > 0:
            return [Line("Current Tutors:")] + [Line(person) for person in current]
        else:
            return [Line("No Tutors on Duty", center=True)]
