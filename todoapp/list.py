import os
from datetime import datetime as dt

from dateutil import tz

from todoapp.command import Command


class List(Command):

    def __init__(self, flag, desc):
        super().__init__(flag, desc)
        self.__header = 'You have the following todo items:'
        self.__format = '%Y-%m-%d %H:%M:%S%z'

    def execute(self, file_name):
        print(self.__header)
        with open(file_name) as todos:
            if os.stat(file_name).st_size == 0:
                print('No todos for today! :)')
            else:
                lines = todos.read().split('\n')
                count = 1
                for line in lines:
                    if len(line) > 0:
                        desc, completed, date = tuple(line.split(';'))
                        if completed == '1':
                            s = 'X'
                        else:
                            s = ' '
                        from_zone = tz.tzutc()
                        to_zone = tz.tzlocal()
                        utc = dt.strptime(date, self.__format)
                        utc = utc.replace(tzinfo=from_zone)
                        central = utc.astimezone(to_zone)
                        print("{} \t - {} \t [{}] \t {:%Y-%m-%d %H:%M:%S%z}".format(count, desc, s, central))
                        count += 1
