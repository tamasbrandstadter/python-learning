import random


class Pirate(object):

    def __init__(self):
        self.__toxication = 0
        self.__alive = True
        self.__passed_out = False

    def drink_rum(self):
        self.__toxication += 1

    def hows_it_going_mate(self):
        if not self.__alive:
            print("He's dead")
        elif self.__toxication < 5:
            print('Pour me anudder!')
        else:
            print("Arghh, I'ma Pirate. How d'ya d'ink its goin?")
            self.__passed_out = True

    def die(self):
        self.__alive = False

    def brawl(self, other_pirate):
        num = random.randint(0, 3)
        if num == 0:
            self.__alive = False
        elif num == 1:
            other_pirate.__alive = False
        else:
            self.__passed_out = True
            other_pirate.__passed_out = True

    def get_toxication(self):
        return self.__toxication

    def is_alive(self):
        return self.__alive

    def set_alive(self, alive):
        self.__alive = alive
