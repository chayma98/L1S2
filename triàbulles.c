#include <stdio.h>
#include <stdlib.h>
void tri_bulles (int T[], int n)
{int i,j,x;
     for(i=n-1; i>0 ; i--)
         for(j=1;j<=i;j++){
        if(T[j-1]>T[j]){
            x=T[j-1];
            T[j-1]=T[j];
            T[j]=x;}}
}
