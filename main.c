#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void saisitab (int maxi, int TPolynome[]){
int i =0 ;
int c =0;
for (i=0 ; i<= maxi ; i++) {
    printf("donner le coefiicient de la puissance %d ",i);
    scanf("%d",&c);
        TPolynome[i]= c ;
}}
void affichageTab (int maxi , int TPolynome[]){
    int i = 0 ;
    for (i=0;i<=maxi ; i++){
           printf("\n %d\n",TPolynome[i]);
}}
int calcul (int maxi , int TPolynome[]){
int i = 0 ;
int c = 0 ;
int x = 0;
printf("donner la valeur %d ",x);
scanf("%d",&x);
for (i=1 ; i<= maxi ; i++){
    c = TPolynome[i]*pow(x,i);
}
return c ;}
int derivee (int p,int TPolynomeA[], int TPolynomeB[])
  {
  int i= 0;

    if (p==-1)
      return -1;
    for (i=p;i>=1;i--)
      TPolynomeA[i-1]=i*TPolynomeB[i];
    return p-1;
  }
void produit (int maxi,int TPolynome1[], int TPolynome2[]){
int i,j = 0;
int TPolynome3[maxi];
for (i=1 ; i<= maxi ; i++){
        for (j=1;j<=i;j++){
  TPolynome3[i] = (TPolynome1[i]*TPolynome2[j]);
}}}
void somme ( int maxi,int TPolynome1[], int TPolynome2[]){
int i = 0;
int TPolynome3[maxi] ;
for (i=1 ; i<= maxi ;i++){
     TPolynome3[i] = (TPolynome1[i]+TPolynome2[i]) ;
     printf ("\n %d \n ", TPolynome3[i]);}}
int affichageMenu()
{int choixMenu ;
     printf("---Menu---\n\n");
     printf("1.saisitab\n");
     printf("2.somme\n");
     printf("3.produit\n");
     printf("4.derivee\n");
     printf("3.affichageTab\n");
     printf("\nVotre choix?\n\n");
     scanf("%d", &choixMenu);
     return choixMenu ;
}
int choixpol () {
    int choixpol;
printf("1.polynome1 \n");
printf("2.polynome2 \n ");
scanf("%d", &choixpol);
     return choixpol ;
}
int main(){
 int maximum = 3 ;
 int TPolynome [maximum];
int TPolynomeA[maximum];
int TPolynomeB[maximum];
int maxi = 0 ;
printf ("donner le plus haut degré du polynome %d",maxi);
scanf("%d",&maxi);
saisitab( maxi,TPolynome[maxi]);
    switch (affichageMenu()) /* pourquoi choixMenu ca n'esxiste que dans la fonction affichageMenu */
    {
    case 1:
        printf("Vous avez choisis le saisitab!\n");
        switch (choixpol()){
            case 1 :
        saisitab(maxi , TPolynomeA); break ;
            case 2 : printf("\n"); saisitab(maxi , TPolynomeB); break ; }
        break;
    case 2:
        printf("Vous avez choisis la somme!");somme(maxi , TPolynomeA, TPolynomeB);
        break;
    case 3:
        printf("Vous avez choisis le produit!");
        break;
    case 4:
        printf("Vous avez choisi le derivé!");derivee(maxi ,TPolynomeA,TPolynomeB);
derivee(maxi ,TPolynomeA,TPolynomeB);
    case 5:
        printf ("vous avez choisi d'afficher le tab");switch (choixpol()){
            case 1 :
                affichageTab(maxi ,TPolynomeA);break ;
            case 2 :  affichageTab(maxi , TPolynomeB); break ; }
        break;
    default:
        printf("Vous ne ferez rien du tout!");
        break;
    }

    system("PAUSE");

return 0;
}
