#include <stdio.h>
#include <stdlib.h>
void affichage (int t[1000]){
    int i = 0 ;
    for (i=1; i<= 1000;i++){
    printf("%d",t[i]); printf("\n");
}}

void main (int t[1000]){
int i;
for (i=1 ; i<=1000; i++){
    t[i]= rand();
    }
}
