from todoapp.command import Command


class Help(Command):

    def __init__(self, flag, desc):
        super().__init__(flag, desc)
        self.__header = "Command Line Todo application \n" \
                        " ============================= \n" \
                        "Command line arguments:"

    def execute(self, commands):
        print(self.__header)
        for command in commands:
            print("{:<3}\t {}".format(command.flag, command.description))
