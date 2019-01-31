from numpy import zeros, array 
from typing import Iterable, TypeVar 


TabReels = TypeVar(Iterable[float])
MatReels = TypeVar(Iterable[TabReels]) 
MAXPRODUITS = 100
def saisir_produit (no : int , tabPrixNote : MatReels):
    x = int(input("donner le prix:"))
    print("vous aver fourni le prix",x)
    tabPrixNote[0][no]= x
    y = int(input("donner la note:"))
    print("vous avez fourni la note",y)
    tabPrixNote[1][no]= y
def saisir_product (nb : int , tabPrixNote : MatReels):
    x = int(input("donner le nombre du produit recherché:"))
    print ("vous avez fourni le nombre produit cherché",x)
    saisir_produit (x,tabPrixNote)
def afficheDetailProduit (nb : int , tabPrixNote : MatReels):
     saisir_produit (nb,tabPrixNote)
def affiche_produits (nb : int , tabPrixNote : MatReels):
    afficheDetailProduit (nb)
def maxTab (nb : int , tab : TabReels) :
    i =1
    x=0 
    for i in range (nb):
        if tab[i]< tab[i+1]:
            x = tab[i+1]

    return x 
def minTab (nb : int , tab : TabReels):
    i= 1
    x= 0
    for i in range( nb) :
        if tab[i]< tab[i+1] :
            x = tab[i]
    return x 
def afficheMoinsCher (nb : int , tabPrixNote : MatReels):
    i=1 
    x=0
    for i in range  (nb) :
        if tabPrixNote[0][i]> tabPrixNote[0][i+1]:
            x = tabPrixNote [0][i+1]
            afficheDetailProduit (x, tabPrixNote)
def afficheMieuxNote (nb : int , tabPrixNote : MatReels):
    i=1
    x=0
    for i in range (nb) :
        if tabPrixNote[1][i]> tabPrixNote[1][i+1]:
            x = tabPrixNote[1][i]
    afficheDetailProduit(x)

def remplirTabNorme (nb : int , tab : TabReels , tabNorme : TabReels):# tab norme c'est la sortie
    i= 1
    x = maxTab (nb,tab)
    for i in range (nb) :
           tabNorme[i] = tab[i]/x 
def trouverCompromis (nb: int , tabPrixNote : MatReels,tabNormNote : TabReels,tabNormPrix : TabReels ):
    remplirTabNorme(nb,tabPrixNote[0] , tabNormNote )
    remplirTabNorme(nb, tabPrixNote[1] , tabNormPrix  )
    
def tabMixte (nb : int, tabNormNote: TabReels ,tabNormPrix : TabReels , tabMixte : TabReels):
    for i in range (nb) :
        tabMixte[i]= (tabNormNote[i]*(1-tabNormPrix[i]*0,9))
        
def affichegeInteret (nb : int , tabMixte : TabReels):
    print (maxTab(nb , tabMixte))
    
def moyenne ( nb: int, tab : TabReels):
    i = 1
    s = 0
    m = 0
    for i in range (nb) :
         s = s+ tab[i]
         m = s/nb
    return m      
def testTP1():
    prix:TabReels = array([81,72,85,71,66,104,91,87])
    notes:TabReels = array([2,4,5,3,2,0,2,5])
    prixNotes:MatReels = array([prix, notes])
    nb:int = len(prix)
    afficheMoinsCher(nb, prixNotes)
    afficheMieuxNote(nb, prixNotes)
    trouverCompromis(nb, prixNotes)
    print("Moyenne des prix : " + str(moyenne(nb, prix)))
    print("Moyenne des notes : " + str(moyenne(nb, notes)))

testTP1()
