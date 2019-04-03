from numpy import array,zeros
from typing import Iterable
from random import randint
##Les Types
TabInt = Iterable[int]
TexteOpe = (str,15)
TabOpe = Iterable[str]
class Calcul:
 etapes:TabOpe=None
 valeur:int=0
##Les constantes
SIGNES:TabOpe=array(["+", "*", "-", "//"])
def copier_tab (src: TabInt , dest : TabInt, nb: int):
    for i in range (0,nb):
        dest[i]= src[i] 
def extraire(tab : TabInt , i : int , pos_fin : int)-> int:
    x : int
    x = tab[i] 
    tab[i] = tab[pos_fin]
    tab[pos_fin]= 0
    return x;
def verifier(op:str, a:int, b:int)->bool:
    r : bool
    r= True
    if op== "/":
       if b==1 :
           
           r= False
       elif a%b != 0:
           r= False
    if op== "*":
        if b==1 :
            r= False
    if op== "-":
        if a*b < 0 :
            r = False
    else : r = True 
def calculer (op : str , a : int , b : int)-> int :
    x : int
    if op=="/" and verfier(op,a,b)== True :
        x= a/b
        print("la division a donné",x)
    if op=="*" and verifier(op,a,b)== True :
        x= a*b
        print("la multiplication a donné:",x)
    if op=="-" and verifier(op,a,b):
        x = a-b
        print ("la soustraction a donné",x)
    else : x= a+b
    return x
def choisir_operateur(a:int, b:int)->str :
    op : str
    i: int
    i=randint(0,3)
    while verifier (SIGNES[i],a,b) != True:
        i= randint(0,3)
    return SIGNES[i]
def essayer_calcul(tab_num : TabInt,but: int)-> Calcul:
    calcul : Calcul
    copie_num : TabInt
    j: int =0
    a: int=0
    b: int=0
    signe : str 
    copier_tab(tab_num, copie_num, 6)
    for nb in range(0,4) :
        i= randint(0,nb)
        a= extraire(copie_num, i, nb)
        i= randint(0, nb-1)
        b=extraire(copie_num, i, nb-1)
        signe=choisir_operateur(a, b)
        valeur= calculer(signe, a, b)
        copie_num[nb-1] = valeur
        calcul.valeur = valeur
        calcul.etapes[j] =( "" + a + signe + b + "=" + valeur)
        j=j+1
        if valeur==but :
            return calcul
        return calcul
def lancer_essais():
    but : int=0
    maxi : int =0
    n: int=0
    nb: int=0
    tab_num : TabInt
    print("donner le nbre des case du tableau",nb)
    nb= input()
    for i in range(0,nb):
        print("donner les nbre ")
        tab_num[i]=input()
    print("donner le but")
    but= input()
    print("donner le nbre d essai max")
    maxi= input()
    while essayer_calcul != but and n<=maxi:
        essayer_calcul(tab_num,but)
        n=n+1
def main():
    tab_num : TabInt
    but : int=0
    nb: int=0
    print("donner le nbre des case du tableau",nb)
    nb= input()
    for i in range(0,nb):
        print("donner les nbres ")
        tab_num[i]=input()
    essayer_calcul(tab_num,but)
    lancer_essais() 
main()
        

    
        
        

            