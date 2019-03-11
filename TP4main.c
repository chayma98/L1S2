#include <stdio.h>
#include <stdlib.h>
void saisie(int matrice[][]){
    int nbLigne = 0 ;
    int nbColonnes = 0 ;
    int i = 0 ;
    int j = 0 ;
    int c = 0 ;
printf("donner le nbre des ligne %d et le nbre de colonnes %d", nbLigne ,nbColonnes);
scanf("%d %d",&nbLigne,&nbColonnes);
// la premiere dimension correspond au lignes et la deuxieme au colonne
for (i=1 ; i<= nbLigne ; i++){
        for (j= 1 ; j<= nbColonnes; j++){
    printf("Elément[%d][%d] : ",i,j);
    scanf("%d",&matrice[i][j]);}
}}
void affichage (int nbLigne , int nbColonnes, int matrice[nbLigne][nbColonnes]){
    int i,j= 0;
    if (nbColonnes < 20 ){
        for (i=1 ; i<= nbLigne ; i++){
        for (j=1 ; j<= nbColonnes ; j++){
            printf ("%7d",matrice [i][j]);
            printf("\n");
        }}
    else { printf("idk");}}
}
void zéroo (int nbLigne , int matrice){
int i,j = 0 ;
for (i=1; i<= nbLigne; i++){
        for (j=1 ;j<= i ; j++){
    matrice[i][j]= 0 ;}}}
void transposé(int matrice , int nbLigne, int nbColonnes){
int i,j = 0 ;
int B[50][50];
 /* Affectation de la matrice transposée à B */
 for (i=0; i<nbLigne; i++)
     for (j=0; j<nbColonnes ; j++)
          B[j][i]=matrice[i][j];
 /* Affectation de la matrice transposée à B */
 for (i=0; i<nbLigne; i++)
     for (j=0; j<nbColonnes; j++)
          B[j][i]=matrice[i][j];
  /* Edition du résultat */
 /* Attention: maintenant le rôle de nbLigne et nbcolonnes est inversé. */
  printf("Matrice résultat :\n");
 for (i=0; i<nbColonnes; i++){
     for (j=0; j<nbLigne; j++)
     printf("%7d", B[i][j]);
     printf("\n");}
int main(){
//int maxi = 50 ;
int matrice[50][50];
return 0;
}
