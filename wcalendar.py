import random
import math


class Calendar(object):

    """
    Calendar, that takes only weeks and months into account.
    Each month has 4 weeks. Some weeks and months are holidays.
    In these days tired tourist will try go to vacation.
    """
    def __init__(self, wcount=1, wholidays=[16], mholidays=[1, 6, 7, 8]):
        """
        Initialize a Calendar instance.
        Initialize weeks counter.
        wcount: current week number.
        wholidays: list of week numbers, that we assume as holidays
        mholidays: list of month numbers, that we assume as holidays
        """
        self.wcount = wcount
        self.wholidays = wholidays
        self.mholidays = mholidays

    def getCurrentWeek(self):
        """
        Returns current year's week number.
        Each year has 48 weeks and each month has 4 weeks.
        """
        return self.wcount % 48

    def getCurrentMonth(self):
        """
        Returns current year's month number.
        Each year has 48 weeks and each month has 4 weeks.
        """
        return math.ceil((self.wcount % 48) / 4)

    def getCurrentYear(self):
        """
        Returns current year number.
        Each year has 48 weeks.
        """
        return math.ceil(self.wcount / 48)

    def isHoliday(self):
        """
        Returns True or False about whether current week is a holiday .
        """
        if self.getCurrentWeek() in self.wholidays \
           or self.getCurrentMonth() in self.mholidays:
            return True

        return False

    def timesGoBy(self):
        """
        Increases weeks counter by 1.
        """
        self.wcount += 1
