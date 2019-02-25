#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void saisitab (int maxi, int TPolynome[]){
int i =0 ; int c=0;
for (i=1 ; i<= maxi ; i++) {
    printf("donner le coefiicient de la puissance i",c);
    scanf("%d",&c);
        TPolynome[i]= c ;
}}
void affichageTab (int maxi , int *TPolynome){
    int i = 0 ;
    for (i=1;i<=maxi ; i++){
           printf("\n %d \n",TPolynome[i]);
}}
void calcul (int maxi , int TPolynome[]){
int i = 0 ;
int x = 0;
printf("donner a valeur ",x);
scanf("%d",&x);
for (i=1 ; i<= maxi ; i++){
    TPolynome[i]*pow(x,i);
}}
void derivee(int maxi , int *TPolynome){
int i = 0 ;
int j = 0;
for (i=2; i<= maxi ; i++){
    for (j=1 ; j<= maxi ; j++){
       TPolynome[j]= TPolynome[i] ;
    }
}}
void produit (int maxi){
saisitab(int maxi , int TPolynome1[]);
saisitab(int maxi , int TPoynome2[]);
int i = 0;
int TPolynome3 [maxi];
for (i=1 ; i<= maxi ; i++){
  TPolynome3[i] = (TPolynome1[i]*TPolynome2[i]);
}}
void somme ( int maxi){
int i = 0;
saisitab(int maxi , int TPolynome1[]);
saisitab(int maxi , int TPoynome2[]);
for (i=1 ; i<= maxi ;i++){
     printf ("\n %d \n "(TPolynome1[i])+TPolynome2[j]);}}
int main(){
const int maxi = 2 ;
int TPolynome [maxi];
return 0;
}
