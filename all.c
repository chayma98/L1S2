#include <stdio.h>
#include <stdlib.h>

int fact(int x){
int f = 1 ;
int n =1;
while (x> 1){
    f= f * x ;
    n-- ;
}
return f ;}
float cosinus ( float x,float e){
int i= 1;
float y = 0 ;
float s = 0;
y = (pow(x,2*i+1))*(pow(1,i))/(fact(2i+1));
while (abs(y) < e ){
    s = s+y ;
    i++ ;}
    return (s) ;
}
int somme (int n){
    int i = 1 ;
    int s = 0;
    for (i=1 ; i<=n ; i++){
        if (n % i == 0){
            s= s+1 ;}}
       return s ;  }
int sommep (x) {
int i=1 ;
int s = 0 ;
for (i=2 ; i<=x ; i++ ){
    if (x % i == 0 ){ s = s+ i;}
}
return s ;
}
 int amis (int x , int y) {
 if (somme(x)== somme (y)){ return 0;}
}
 int sommepremiers (int n , int k) {int i = 1 ;
    int d = 0 ;
    for (i=1 ; i<=n ; i++){
        if (somme(n) == k){d = d + i ;}
    printf("la somme des % premiers nombres premiers est %d",k,d);
    }
    return 0 ;
 }
 int premiernbpremier (int n,int k){
     int i = 1;
    for (i=1 ; i<= n; i++) {
        if ((n % i == 0)&& (i > k) ){
            printf("le premier nombre premier supérieur à %d est %",k,i);
        }
    }
    return 0;
 }
void main () {
    int x = 0 ;
    int y= 0 ; int z =0 ; int n =0 ; int e =0 ;
     int k =0 ;
printf("donner deux nombres %d et %d",x,y);
scanf("%d et %d",&x,&y);
if((amis(x,y))== 0) {printf("%d et %d sont amis",x,y);}
printf("donner le nombre %d et epsilonne %d",n,e);
scanf("%d et %d",&n,&e);
cosinus(n,e);
printf("donner le nombre %d et l'indice",z,k);
scanf("%d et %d",&z,&k);
printf(premiernbpremier(z,k));
printf(sommepremiers(z,k));
}







