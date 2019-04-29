#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import  array,zeros
from typing import Iterable
from random import randint
from multiprocessing import Pool
from math import sqrt
#nb d'objets possibles
NBOBJETS = 8
#nb se sacs dans la population
NBSACS = 40
  
##Les Types et Constantes
Tabint = Iterable[int]
TabReels = Iterable[float]

#un sac contient un tableau d'entiers entre 0 et 1 indiquant la présence ou non d'un produit
 #et contient également un poids */
class Sac:
    genome:Tabint = None
    poids:float=0.0
    interet:float=0.0
    note:float = 0.0
  
#tableau de sacs
TabPopulation = Iterable[Sac]


#les poids des 8  différents produits
POIDS:TabReels = array([10.4, 1.4, 5.4, 8.4, 1.4, 6.8, 6.3, 1.1])
#les interets des 8  différents produits
INTERETS:TabReels = array([8,4,4,6,5,3,7, 2])

##Les fonctions

#crée le contenu d'un sac et permet de saisir les valeurs 
def creerSac(sac:Sac):
    sac.genome = zeros(NBOBJETS, int)
    for i in range(0,NBOBJETS):
        sac.genome[i] = randint(0,1)

#calcul le poids, l'interet et la note d'un sac
def calculProprietes(sac:Sac):
    sommePoids:float = 0.0
    sommeinteret:float = 0.0
    #à faire, somme des poids et des interets des objets presents dans le sac
    sac.poids = sommePoids
    sac.interet = sommeinteret
    sac.note = sommeinteret - sommePoids

#créer NBSACS sacs et les place dans le tableau population
def creerPopulation(population:TabPopulation):
    for i in range(0, NBSACS):
        s:Sac  = Sac()
        creerSac(s)
        calculProprietes(s)
        population[i] = s

#affiche les no des produits contenu dans un sac, ainsi que son poids, son interet et sa note*/
def afficheSac(sac:Sac):
    for i in range(0, NBOBJETS):
        if(sac.genome[i]==1): print(i, end=", ")
    print("    poids = ",sac.poids, ",     interet = " ,sac.interet, ",     note = " , sac.note )

#affiche tous les sacs du tableau population 
def affichePopulation(population:TabPopulation):
    for sac in population:
        afficheSac(sac)

        
#échange de poisitions les sacs situés aux positions i et j de tab
def permuter(tab: TabPopulation, i: int, j: int):
    # a completer
    x: int = 0
    x= tab[i]
    tab[i]= tab[j]
    tab[j] = x

#tri les sacs du tableau population, en utilisant le tri par insertion, et en triant les sacs par odre de note décroissante
def triPopulationInsertion(population:TabPopulation):
    n = len(population)
    # a completer
    for i in range(1,len(population)):
        temp = t[i]
        j=i
        while j>0 and temp< t[j-1]:
            t[j] = t[j-1]
            j=1
        t[j]=temp
    return t
#croisement de sacs les parents 1 et 2 donnent les enfants 1 et 2. la 1ere moitie des parents 1 et 2 est recopiée dans les enfants 1 et 2,  puis la seconde moitiee des parents 2 et 1 est recopiée dans les enfants 1 et 2
def croisementSacs(parent1:Sac, parent2:Sac, enfant1:Sac, enfant2:Sac):
    enfant1.genome = zeros(NBOBJETS, int)
    enfant2.genome = zeros(NBOBJETS, int)
    milieu = NBOBJETS/2
    # a completer
    
    calculProprietes(enfant1)
    calculProprietes(enfant2)
    
#demande le croisement des 2 premiers sacs du tableau population pour obtenir 2 enfants qui seront placés en fin de tableau 
def croisementPopulation(population:TabPopulation):
    parent1 = population[0]
    parent2 = population[1]
    enfant1 = Sac()
    enfant2 = Sac()
    croisementSacs(parent1, parent2, enfant1, enfant2)
    population[NBSACS-1] = enfant1
    population[NBSACS-2] = enfant2

#effectue une mutation : un sac (s'il ne fait pas parti des 2 premiers) est choisi au hasard et une valeur de son contenu est transformee (0 <-> 1)*/
def mutationPopulation(population:TabPopulation):
    noMutant = 0 # a modifier
    sacMutant = population[noMutant]    
    noGeneMutant = 0# a modifier
    # a completer
    calculProprietes(sacMutant)

#effectue nb croisements et mutations des sacs du tableau population*/
def reproductionDeSacs(nb:int, population:TabPopulation):
    # a completer
    
#petite fonction pour tester le tout..*/
def vie():
    population:TabPopulation= zeros(NBSACS, Sac)
    creerPopulation(population)
    reproductionDeSacs(5, population)
    triPopulationInsertion(population)
    affichePopulation(population)
