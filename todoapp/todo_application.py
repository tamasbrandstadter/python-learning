from todoapp.add import Add
from todoapp.complete import Complete
from todoapp.help import Help
from todoapp.list import List
from todoapp.quit import Quit
from todoapp.remove import Remove
from todoapp.validate import Validate


class TodoApplication:

    def __init__(self):
        self.__available_commands = {'-h': Help('-h', 'Print out application usage'),
                                     '-l': List('-l', 'List all the tasks'),
                                     '-q': Quit('-q', 'Quit the application'),
                                     '-a': Add('-a', 'Add new todo'),
                                     '-r': Remove('-r', 'Remove a todo'),
                                     '-c': Complete('-c', 'Complete a task')
                                     }
        self.__file = 'todos.csv'
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            user_input = input('Type a command: ')
            valid = Validate.execute(user_input)
            if valid:
                flag = user_input[5:7]
                if flag in self.__available_commands:
                    command = self.__available_commands[flag]
                    if flag == '-h':
                        command.execute(list(self.__available_commands.values()))
                    elif flag == '-l':
                        command.execute(self.__file)
                    elif flag == '-a':
                        command.execute(user_input[8:], self.__file)
                    elif flag == '-r':
                        command.execute(user_input[8], self.__file)
                    elif flag == '-c':
                        command.execute(user_input[8], self.__file)
                    else:
                        self.running = Quit.execute()
                else:
                    print('Flag and command not found')


app = TodoApplication()
app.run()
