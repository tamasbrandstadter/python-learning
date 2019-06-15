from todoapp.command import Command


class Quit(Command):

    @staticmethod
    def execute():
        print('Closing application.')
        return False
