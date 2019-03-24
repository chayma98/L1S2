#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Question 1
typedef TGeneration[51][51];

// Question 2

void Reset (TGeneration G){

    int i;
    int j;
    for ( i = 0 ; i < 51 ; i++){
        for ( j = 0 ; j < 51 ; j++){
            G[i][j] = 0;
        }
    }

}


int Saisie_Generation()
{
    int GeneIni;
    printf("Saisir le nombre de la premiere generation : ");
    scanf("%d",&GeneIni);
    return GeneIni;
}

void GenAlea (TGeneration G , int GeneIni)
{
    int i; int j; int k;
    for (k=0 ; k<GeneIni ; k++)
    {
        i = rand()%50; /* randomisation de 0 à 49 */
        j = rand()%50; /* randomisation de 0 à 49 */
        if (G[i+1][j+1]==1)
        {
            k--;
        }
        else
            G[i+1][j+1] = 1;
    }
}


// Question 3

int Affichage_Generation (TGeneration G)
{
    int i ; int j;
    for (i=0 ; i< 50 ; i++)
    {
        for (j=0 ; j<50 ; j++)
        {
            if ( G[i+1][j+1] == 0)
                printf("  ");
            else
                printf("0 ");
        }
        printf("|\n|");
    }
}

int Verification (TGeneration G , int i , int j)
{
    int k = 0; int p; int q;

    for (p=i-1 ; p < i+1 ; p++)
    {
        for (q=j-1 ; q < j+1 ; q++)
        {
            if (p!=i && q!=j && (G[p][q] == 1))
                {
                    k+=1;
                }
        }
    }
    return k;
}

int Regles (int valeur, int k)
{
    int s;
    s=0;
    if (valeur==0 && k==3)
        s=1;
    if (valeur==1)

    if ( (k==2) || (k==3)){  // CA MARCHE POOOO #FaireChierLaProf <3
        printf("debug");
        s=1;}
    else
        s=0;
    return s;
}

void GeneAnneeSup (TGeneration G, TGeneration Gp )
{
    int i ; int j;
    for (i=1 ; i<51 ; i++)
    {
        for (j=1 ; 1<51 ; j++)
            Gp[i][j] = Regles (G[i][j],Verification(G, i, j));

    }
}

void Rearange (TGeneration G, TGeneration Gp)
{
    int i; int j;
    for (i=1 ; i<51 ; i++)
    {
        for (j=1 ; j<51 ; j++)
            G[i][j]=Gp[i][j];
    }
}

// Question 4
/*
int Calcule_Gene (Tgeneration G)
{
    int i; int j;
    for (i=0 ; i<50 ; i++)
    {
        for (j=0 ; j<50 ; j++)
        {
            // regle A
            if
        }
    }
}







*/
int main()
{
   TGeneration G; TGeneration Gp; int GeneIni; int i;
   GeneIni = Saisie_Generation(G);
   Reset(G);
   GenAlea(G, GeneIni);
   Affichage_Generation(G);
   for (i=0 ; i<1500 ; i++)
   {
       GeneAnneeSup( G, Gp);
       Rearange(G, Gp);
       Affichage_Generation(G);
   }
}
