import os

from todoapp.command import Command


class Complete(Command):

    def __init__(self, flag, desc):
        super().__init__(flag, desc)
        self.__error_message = 'Todo not found, cannot update'

    def execute(self, todo_number, file_name):
        index = int(todo_number) - 1
        if os.stat(file_name).st_size < index:
            print(self.__error_message)
        else:
            with open(file_name, "r") as f:
                lines = f.readlines()
            with open(file_name, "w") as todos:
                for i, line in enumerate(lines):
                    if i == index:
                        line = line.replace(';0;', ';1;')
                    todos.write(line)
