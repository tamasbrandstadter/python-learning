class Command:

    def __init__(self, flag, desc):
        self.flag = flag
        self.description = desc
        self.__header = ''

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, flag):
        self.__flag = flag
