class Fraction:
    num:int = 1
    denom:int = 1
    
def creer_fraction(num:int, denom:int)->Fraction:
    f = Fraction()
    f.num = num
    f.denom = denom
    return f
def saisir_Fraction (f:Fraction)-> Fraction :
    print("donner le numerateur"); f.num=input()
    print("donner le denominateur"); f.denom=input()
    return f
    
def f2str(f:Fraction)->str:
    if f.num:
        if f.denom == 1:
            return str(f.denom)
        else:
            return(str(f.num) + "/" + str(f.denom))
    else:
        return str(0)

def pgcd(a:int, b:int)->int: #facon recursive
    if a % b == 0:
        return b
    else:
        return pgcd(b, a % b)
        
def simplifieFraction(f:Fraction):
    d = pgcd(f.num,f.denom)
    f.num /= d
    f.denom /= d
    
def addition(a:Fraction, b:Fraction)->Fraction:
    f = Fraction()
    if a.denom == b.denom:
        f.num = a.num + b.num
        f.denom = a.denom
    else:
        f.num = (a.num * b.denom) + (a.denom * b.num)
        f.denom = a.denom * b.denom
        
    simplifieFraction(f)
    return f
    
def soustraction(a:Fraction, b:Fraction)->Fraction:
    f = Fraction()
    if a.denom == b.denom:
        f.num = a.num - b.num
        f.denom = a.denom
    else:
        f.num = (a.num * b.denom) - (a.denom * b.num)
        f.denom = a.denom * b.denom
        
    simplifieFraction(f)
    return f
    
def multiplication(a:Fraction, b:Fraction)->Fraction:
    f = Fraction()
    f.num = a.num * b.num
    f.denom = a.denom * b.denom
    simplifieFraction(f)
    return f

def division(a:Fraction, b:Fraction)->Fraction:
    f = Fraction()
    f.num = a.num * b.denom
    f.denom = a.denom * b.num
    simplifieFraction(f)
    return f

def menu(f1:Fraction, f2:Fraction, f3:Fraction):
    continuer = 1
    while(continuer):
        print("------- GESTION DE FRACTIONS -------")
        print("F1 = " + f2str(f1))
        print("F2 = " + f2str(f2))
        print("F3 = " + f2str(f3),end="\n\n")
        
        print("1 -> saisir F1")
        print("2 -> saisir F2")
        print("3 -> F3 = F1 + F2")
        print("4 -> F3 = F1 - F2")
        print("5 -> F3 = F1 * F2")
        print("6 -> F3 = F1 / F2")
        print("0 -> Quitter")
        
        choix = int(input("\nVoitre choix : "))
        if choix == 1:
            f1num = int(input("\n    F1 numerateur : "))
            f1denom = int(input("    F1 denominateur : "))
            print()
            f1 = creer_fraction(f1num, f1denom)
            simplifieFraction(f1)
        elif choix == 2:
            f2num = int(input("\n    F2 numerateur : "))
            f2denom = int(input("    F2 denominateur : "))
            print()
            f2 = creer_fraction(f2num, f2denom)
            simplifieFraction(f2)
        elif choix == 3:
            f3 = addition(f1,f2)
            print("\n    [+] F3 = (" + f2str(f1) + ") + ("+ f2str(f2) + ") = " + f2str(f3),end="\n\n")
        elif choix == 4:
            f3 = soustraction(f1,f2)
            print("\n    [+] F3 = (" + f2str(f1) + ") - ("+ f2str(f2) + ") = " + f2str(f3),end="\n\n")
        elif choix == 5:
            f3 = multiplication(f1,f2)
            print("\n    [+] F3 = (" + f2str(f1) + ") * ("+ f2str(f2) + ") = " + f2str(f3),end="\n\n")
        elif choix == 6:
            f3 = division(f1,f2)
            print("\n    [+] F3 = (" + f2str(f1) + ") / ("+ f2str(f2) + ") = " + f2str(f3),end="\n\n")
        elif choix == 0:
            continuer = 0
        
    
def interagir():
    f1 = Fraction()
    f2 = Fraction()
    f3 = Fraction()
    
    menu(f1, f2, f3)
    
interagir()
    