
#include <stdio.h>
#include <stdlib.h>
void parinsertion (int t[1000], int n){
int i,j,x;
for(i=1;i<9;i++){
     x=t[i]; while((j>0)&&(t[j-1]>x)){
          t[j]=t[j-1]; j--; }
t[j]= x; }
}
