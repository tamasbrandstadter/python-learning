from weeks.week2.day2.classes import Domino


def initialize_dominos():
    return [Domino(5, 2), Domino(4, 6), Domino(1, 5), Domino(6, 7), Domino(2, 4), Domino(7, 1)]


dominos = initialize_dominos()
# You have the list of Dominoes
# Order them into one snake where the adjacent dominoes have the same numbers on their adjacent sides
# eg: [2, 4], [4, 3], [3, 5] ...
for i in range(len(dominos)):
    domino = dominos[i]
    for j in range(i + 1, len(dominos)):
        other_domino = dominos[j]
        if domino.values[1] == other_domino.values[0]:
            temp = dominos[i + 1]
            dominos[i + 1] = other_domino
            dominos[j] = temp

print(dominos)
