from numpy import zeros, array 
import matplotlib.pyplot as plt 
from typing import Iterable 
class Personne: 
    x=0 
    y=0 
    flash = None 
    couleur = (0,0,0) 
    Couleur = (float, float, float) 
    
TabPersonnes = Iterable[Personne] 
def creer_personne(x:float, y:float)->Personne: 
    p:Personne = Personne() 
    p.x = x 
    p.y = y 
    return p 
def ajouter_personne(x:float, y:float, tab:TabPersonnes, n:int)->int: 
    p = creer_personne(x,y) #person created 
    tab[n] = p 
    return n+1 
def flasher_personnes(tab:TabPersonnes, n:int): 
    for i in range(0,n): 
        tab[i].flash = tab[i+1] #flash sur la derniere personne 
        tab[n-1].flash = tab[0] #la derniere flash sur le premier 
def dessiner_regards(tab:TabPersonnes, n:int): 
    for i in range(0,n): 
        plt.plot([tab[i].x, tab[i].flash.x],[tab[i].y, tab[i].flash.y]) 
def test_algos(): 
#creation d'un tableau pour 10 personnes : 
    tab:TabPersonnes = zeros(10,Personne) 
#ajout de 4 personnes : 
    n = 0
    n = ajouter_personne(0,0,tab,n) 
    n = ajouter_personne(10,0,tab,n) 
    n = ajouter_personne(10,10,tab,n) 
    n = ajouter_personne(0,10,tab,n) 
#mise en relation des personnes 
    flasher_personnes(tab,n) 
#test du dessin 
    dessiner_regards(tab, n) 
#lancer l'affichage du graphique 
    plt.show() 
def avancer_personne(tab:TabPersonnes, n:int): 
    pas = 0.025 #modifier plus facilement le pas 
    for i in range(0,n-1): 
        tab[i].x = tab[i].x + pas*(tab[i+1].x - tab[i].x) 
        tab[i].y = tab[i].y + pas*(tab[i+1].y - tab[i].y) 
        tab[n-1].x = tab[n-1].x + pas*(tab[0].x - tab[n-1].x) 
        tab[n-1].y = tab[n-1].y + pas*(tab[0].y - tab[n-1].y) 
def rosace(): 
#creation d'un tableau pour 10 personnes : 
    tab:TabPersonnes = zeros(10,Personne) 
#ajout de 4 personnes : 
    n=0 
    n = ajouter_personne(0, 0, tab, n) 
    n = ajouter_personne(10, 0, tab, n) 
    n = ajouter_personne(10, 10, tab, n) 
    n = ajouter_personne(0, 10, tab, n) 
#mise en relation des personnes 
    flasher_personnes(tab,n) 
#test du dessin 
    for i in range(0,100): 
        dessiner_regards(tab, n) 
        avancer_personne(tab, n) 
#lancer l'affichage du graphique 
    plt.show() 
def dessiner_regards_colores(tab:TabPersonnes, n:int): 
    for i in range(0,n): 
        plt.plot([tab[i].x, tab[i].flash.x],[tab[i].y, tab[i].flash.y], color=tab[i].couleur, linewidth=0.5) 
def rosace_coloree(): 
#creation d'un tableau pour 10 personnes : 
    tab:TabPersonnes = zeros(10,Personne) 
#ajout de 4 personnes : 
    n=0 
    n = ajouter_personne(0, 0, tab, n) 
    n = ajouter_personne(5, 0, tab, n) 
    n = ajouter_personne(10, 0, tab, n) 
    n = ajouter_personne(10, 5, tab, n) 
    n = ajouter_personne(10, 10, tab, n) 
    n = ajouter_personne(5, 10, tab, n) 
    n = ajouter_personne(0, 10, tab, n) 
    n = ajouter_personne(0, 5, tab, n) 
#ajout de la couleur bleu a la premiere personne du tableau 
    c:Couleur = (1,0,1) 
    pas = 0.1 
    tab[0].couleur = c 
    tab[1].couleur = (tab[0].couleur[0] - pas, 0, tab[0].couleur[2] - pas) 
    tab[2].couleur = (tab[1].couleur[0] - pas, 0, tab[1].couleur[2] - pas) 
    tab[3].couleur = (tab[2].couleur[0] - pas, 0, tab[2].couleur[2] - pas) 
    tab[4].couleur = (tab[3].couleur[0] - pas, 0, tab[3].couleur[2] - pas) 
    tab[5].couleur = (tab[4].couleur[0] - pas, 0, tab[4].couleur[2] - pas) 
    tab[6].couleur = (tab[5].couleur[0] - pas, 0, tab[5].couleur[2] - pas) 
    tab[7].couleur = (tab[6].couleur[0] - pas, 0, tab[6].couleur[2] - pas) 
#mise en relation des personnes 
    flasher_personnes(tab,n) 
#test du dessin 
    for i in range(0,500): 
        dessiner_regards_colores(tab, n) 
        avancer_personne(tab, n) 
#lancer l'affichage du graphique 
    plt.show() 
rosace_coloree()