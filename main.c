#include <stdio.h>
#include <stdlib.h>
void permuter (int x,int y){
 int z =0;
 z= x;
 x= y ;
 y= z;
}
void triselec(int t[1000],int n) {
int i =0 ;
int j=0 ;
for (i=1 ; i<=n ; i++){;
    for ( (j=(i+1)) ; i<= n ; j++){
        if (t[j]< t[i]){ permuter(&t[i],&t[j]);}
    }
}
}
