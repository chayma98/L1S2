# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from numpy import zeros, array from typing import Iterable, TypeVar 


TabReels = TypeVar(Iterable[float])
 MatReels = TypeVar(Iterable[TabReels]) 
 MAXPRODUITS = 100
def saisir_produit (no : int , tabPrixNote : MatReels):
    x=0 y=0
    print("donner le prix",x)
    tabPrixNote[0][no]= x 
    print("donner la note",y)
    tabPrixNote[1][no]= y
def saisir_product (nb : int , tabPrixNote : MatReels):
    x = 0
    print ("donner le nombre produit cherché",x)
    saisir_produit (x,tabPrixNote)
 def afficheDetailProduit (nb : int , tabPrixNote : MatReels):
     saisir_produit (nb)
def affiche_produits (nb : int , tabPrixNote : MatReels):
    afficheDetailProduit (nb)
def maxTab (nb : int , tab : TabReels)-> float :
    i =1 x=0 
    for i in nb:
        if tab[i]< tab[i+1]:
            x = tab[i+1]
return x 
def minTab (nb : int , tab : TabReels)-> float:
    i= 1 x= 0
    for i in nb :
        if tab[i]< tab[i+1] :
            x = tab[i]
return x 
def afficheMoinsCher (nb : int , tabPrixNote : MatReels):
    i=1 x=0
    for i in nb :
        if tabPrixNote[0][i]> tabPrixNote[0][i+1]:
            x = tabPrixNote [0][i+1]
            afficheDetailProduit (x)
def afficheMieuxNote (nb : int , tabPrixNote : MatReels):
    i=1 x=0
    for i in nb :
        if tabPrixNote[1][i]> tabPrixNote[1][i+1]:
            x = tabPrixNote[1][i]
afficheDetailProduit(x)
def remplirTabNorme (nb : int , tab : TabReels , tabNorme : TabReels)
i= 1
x = maxTab (nb,tab)
       for i in nb:
           tabNorme[i] = tab[i]/x 
def trouverCompromis
       
     