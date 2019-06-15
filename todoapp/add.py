from datetime import datetime as dt

import pytz

from todoapp.command import Command


class Add(Command):

    def __init__(self, flag, desc):
        super().__init__(flag, desc)
        self.__required_format = "You can add tasks with the format below: \n" \
                                 "todo -a [description with spaces]_[yyyy:mm:dd hh:mm]"
        self.__format = '%Y:%m:%d %H:%M'

    def execute(self, parts, file_name):
        desc, date = tuple(str(parts).split('_'))
        if desc is not None and date is not None:
            local = pytz.timezone('Europe/Paris')
            try:
                naive = dt.strptime(date, self.__format)
                local_dt = local.localize(naive, is_dst=True)
                utc_dt = local_dt.astimezone(pytz.utc)
                with open(file_name, 'a+') as todos:
                    todos.write(desc + ';0;' + str(utc_dt) + '\n')
                    print('Successfully added new todo')
            except ValueError:
                print('Input date does not match format')
        else:
            print('Unable to add new task description or due date missing')
            print(self.__required_format)
