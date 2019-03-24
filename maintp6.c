#include <stdio.h>
#include <stdlib.h>
typedef struct TMorceau { char titre[10];
char auteur[20];
char genre[10];
double duree ; }TMorceau ;
typedef struct TDisque {float numero;
char support[5];
char titreDalbum[20];
TMorceau morceaux;}TDisque ;
typedef struct tDiscotheque{int nb ;
TDisque disques[50];}TDiscotheque ;
TMorceau saisieMorceau (TMorceau newMorceau){
    printf("donner l'auteur %s",newMorceau.auteur);
    scanf("%s", &newMorceau.auteur);
    printf("donner le genre %s",newMorceau.genre);
    scanf("%s", &newMorceau.genre);
    printf("donner le titre %s",newMorceau.titre);
    scanf("%s", &newMorceau.titre);
    printf("donner la duree %d",newMorceau.duree);
    scanf("%d", &newMorceau.duree);
    return newMorceau ;
}
void afficheMorceau(int r , TMorceau m){
printf("le",r,"ieme morceau :");
printf("auteur :" ,m.auteur);
printf("titre :",m.titre);
printf("genre :" ,m.genre);
printf("duree :" ,m.duree);
}
TDisque saisieDisque(TDisque d){
printf("donner le numero %d");
scanf("%d",&d.numero);
printf("donner support %s");
scanf("%s",&d.support);
printf("donner le titre d'album %s");
scanf("%s",&d.titreDalbum);
printf("donner les morceaux %d");
scanf("%d",&d.morceaux);
return d ;
}
void afficheDisque (int num , TDisque d){
printf ("le disque numero",num);
printf("numero:",d.numero);
printf("support:",d.support);
printf("titre d'album:",d.titreDalbum);
printf("morceaux:",d.morceaux);
}
int tempDisque( TDisque d){
int s=0 ; int i=0;
s= s+d.morceaux.duree ;
return s;}
int tempDisco (TDiscotheque d){
int s=0;
for (i=1;i<=d.nb ;i++){
    s=s+ d[i].disques.morceau.duree;
}
return s;
}
void afficheListe (TDiscotheque d, char nom){
int i= 0;
for (i=1;i<=d.nb ; i++){
    if (d[i].morceaux.auteur== nom) {
        printf (d[i].morceaux.auteur);
    }
}}




