import random
import pandas as pd
import numpy as np
import Ruche
import Fleur
import Bee


def parse():
    return pd.read_excel('./fleurs.xlsx')


def initFlower(file):
    list = []
    id = 0
    for i in range(len(file)):
        fleur = Fleur.Fleur(file.loc[i, "x"], file.loc[i, "y"], id)
        list.append(fleur)
        id += 1
    return list


def getFleur(id, liste_fleur):
    for fleur in liste_fleur:
        if fleur.get_id() == id:
            return fleur


def generer_chemin(population, liste_fleur):
    for pop in range(100):
        bee = Bee.Bee()
        id = random.sample(range(len(liste_fleur)), len(liste_fleur))
        for i in id:
            bee.add_step(getFleur(liste_fleur, i))
        bee.calcul_longueur()
        population.append(bee)
    return population


def distance_parcourue(abeilles):
    distance = {}
    bee_id = 0
    for bee in abeilles:
        bee.calcul_longueur()
        distance[bee_id] = bee.get_longueur()
        bee_id += 1
    return distance


def trier(population):
    return sorted(population, key=lambda bee: bee.get_distance())


def crossover(parent1, parent2, population, listeFleur):
    enfant = Bee.Bee()
    chemin_enfant = []
    for i in range(len(parent1.get_chemin())):
        if i % 2 == 0:
            chemin_enfant.append(parent1.get_step(i))
        else:
            chemin_enfant.append(parent2.get_step(i))
    chemin_enfant = supp_doublons(chemin_enfant)
    chemin_enfant = fleursManquantes(chemin_enfant, listeFleur)
    enfant.set_chemin(chemin_enfant)
    population.append(enfant)
    return population


def distanceMoyenne(population):
    score_moyen = 0
    for bee in population:
        score_moyen += bee.get_distance()
    return score_moyen / len(population)


def supp_doublons(chemin):
    for i in chemin:
        iteration = 0
        for j in chemin:
            if i == j:
                iteration += 1
            if iteration > 1:
                chemin.pop(j)
    return chemin


def fleursManquantes(chemin, listeFleur):
    for i in listeFleur:
        est_present = False
        for j in chemin:
            if i == j:
                est_present = True
        if est_present is False:
            chemin.append(i)
    return chemin


def mutation(population):
    x = random.randint(0, len(population))
    chemin = population[x].get_chemin()
    rand = random.randint(1, len(chemin - 2))
    if rand == 1:
        tmp = chemin[rand]
        chemin[rand] = chemin[rand + 1]
        chemin[rand + 1] = tmp
    else:
        tmp = chemin[rand]
        chemin[rand] = chemin[rand - 1]
        chemin[rand - 1] = tmp
    population[x].set_chemin(chemin)
    return population


def bannir_abeille(population):
    population = trier(population)
    for i in range(len(population) - 20, len(population)):
        del population[i]
    return population


def new_generation(moyenne_precedente, liste_fleur, population):
    bestList = []
    if abs(moyenne_precedente - distanceMoyenne(population)):
        population = mutation(population)
    population = trier(population)
    for i in range(20):
        bestList.append(population[i])
    for i in bestList:
        for j in bestList:
            if i != j:
                population = crossover(i, j, population, liste_fleur)
                bestList.pop(i)
                bestList.pop(j)
    population = bannir_abeille(trier(population))
    return population

