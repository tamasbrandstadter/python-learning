from weeks.week2.day2.pirate import Pirate
import random


class Ship(object):

    def __init__(self, name):
        self.__crew = []
        self.__name = name

    def fill_ship(self):
        captain = Pirate()
        self.__crew.append(captain)
        num = random.randint(1, 10)
        for i in range(num):
            self.__crew.append(Pirate())

    def print_ship(self):
        crew = self.__crew
        captain = crew[0]
        print('Captain toxication: {}, alive: {}'.format(captain.get_toxication(), captain.is_alive()))
        print('Alive pirates: {}'.format(self.__get_alive_count()))

    def __get_alive_count(self):
        count = 0
        crew = self.__crew
        for pirate in crew:
            if pirate.is_alive():
                count += 1
        return count

    def battle(self, other_ship):
        this_alive_count = self.__get_alive_count()
        other_alive_count = other_ship.__get_alive_count()
        this_score = this_alive_count - self.get_captain_toxication()
        other_score = other_alive_count - other_ship.get_captain_toxication()
        if this_score > other_score:
            loss = random.randint(1, len(other_ship.get_crew()))
            crew = other_ship.get_crew()
            del crew[::-loss]
            return True
        else:
            loss = random.randint(1, len(self.get_crew()))
            crew = self.get_crew()
            del crew[::-loss]
            return False

    def get_crew(self):
        return self.__crew

    def drink_for_captain(self):
        crew = self.get_crew()
        captain = crew[0]
        captain.drink_rum()
        captain.hows_it_going_mate()

    def get_captain_toxication(self):
        crew = self.__crew
        captain = crew[0]
        return captain.get_toxication()
