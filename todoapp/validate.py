from todoapp.command import Command


class Validate(Command):

    @staticmethod
    def execute(user_input):
        text = str(user_input)
        if not text.startswith('todo'):
            print('Invalid usage, commands must start with todo prefix.')
            return False
        elif len(text.split(' ')) < 2:
            print('Invalid usage, prefix must be followed by the flag with format: -[flag]')
        else:
            return True
