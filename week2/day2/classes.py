class Animal(object):
    def __init__(self):
        self.hunger = 50
        self.thirst = 50

    def eat(self):
        self.hunger -= 1

    def drink(self):
        self.thirst -= 1

    def play(self):
        self.hunger += 1
        self.thirst += 1


class Farm(object):
    def __init__(self):
        self.animals = []
        self.free_slots = 120

    def breed(self):
        if self.free_slots != 0:
            self.animals.append(Animal())

    def slaughter(self):
        hunger = float('inf')
        least_hungry = Animal()
        for animal in self.animals:
            if animal.hunger < hunger:
                least_hungry = animal
        self.animals.remove(least_hungry)


class Counter(object):
    def __init__(self, count=0):
        self.count = count
        self.initial = count

    def add(self, number):
        self.count += number

    def add_one(self):
        self.count += 1

    def get(self):
        return self.count

    def reset(self):
        self.count = self.initial


class Domino(object):
    def __init__(self, value_a, value_b):
        self.values = [value_a, value_b]

    def __repr__(self):
        return '[{}, {}]'.format(self.values[0], self.values[1])


class Station(object):
    def __init__(self):
        self.gas_amount = 100

    def refill(self, car):
        delta = car.capacity - car.left_in_tank
        if delta < self.gas_amount:
            car.left_in_tank += delta
            self.gas_amount -= delta
        else:
            print('There is not enough gas in station, amount: {}'.format(self.gas_amount))
            car.left_in_tank += self.gas_amount
            self.gas_amount = 0


class Car(object):
    def __init__(self):
        self.capacity = 100
        self.left_in_tank = 100


class BankAccount(object):
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class PostIt(object):
    def __init__(self, text, background_color, text_color):
        self.background_color = background_color
        self.text = text
        self.text_color = text_color


post_it_one = PostIt('Superb', 'yellow', 'green')
tomiAccount = BankAccount('Tomi', 1000000.0)
