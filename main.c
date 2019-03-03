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
void derivee(int maxi , int TPolynome[]){
int i = 0 ;
int j = 0;
for (i=1; i<= maxi ; i++){
    for (j=0 ; j<= maxi ; j++){
       (TPolynome[j]= TPolynome[i]) ;
    }
}}
void produit (int maxi,int TPolynome1[], int TPolynome2[]){
int i = 0;
int TPolynome3[maxi];
for (i=0 ; i<= maxi ; i++){
  TPolynome3[i] = (TPolynome1[i]*TPolynome2[i]);
}}
void somme ( int maxi,int TPolynome1[], int TPolynome2[]){
int i = 0;
int TPolynome3[maxi] ;
for (i=0 ; i<= maxi ;i++){
     TPolynome3[i] = (TPolynome1[i]+TPolynome2[i]) ;
     printf ("\n %d", TPolynome3[i]);}}
int main(){
 int maxi = 3;
int TPolynome [maxi];
int TPolynomeA[maxi];
int TPolynomeB[maxi];
saisitab(maxi , TPolynomeA);
saisitab(maxi , TPolynomeB);
somme(maxi , TPolynomeA, TPolynomeB);
affichageTab(maxi ,TPolynomeA);
affichageTab(maxi , TPolynomeB);
derivee(maxi ,TPolynomeA);
derivee(maxi ,TPolynomeB);
somme(maxi, TPolynomeA , TPolynomeB);
produit(maxi, TPolynomeA , TPolynomeB);
return 0;
}
