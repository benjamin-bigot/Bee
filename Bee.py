import math


def calcul_distance(fleur1, fleur2):
    return int(math.sqrt((fleur2[0] - fleur1[0]) ** 2 + (fleur2[1] - fleur1[1]) ** 2))


class Bee:
    def __init__(self):
        self.__chemin = []
        self.__distance = 0

    def get_chemin(self):
        return self.__chemin

    def get_step(self, i):
        return self.__chemin[i]

    def set_chemin(self, chemin):
        self.__chemin = chemin

    def get_distance(self):
        return self.__distance

    def add_step(self, fleur):
        self.__chemin.append(fleur)

    def calcul_longueur(self):
        total = 0
        start = (500, 500)
        if len(self.__chemin) != 0:
            total += calcul_distance(start, self.__chemin[0].getCoordinates())
        for i in range(len(self.__chemin)):
            if i != len(self.__chemin) - 1:
                total += calcul_distance(self.__chemin[i].getCoordinates(), self.__chemin[i + 1].getCoordinates())
        self.__distance = total
