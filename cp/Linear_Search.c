// Do a Linear Search on an array of size n
// input n, arr, m 
#include <stdio.h>

int main(void) {
    
    int n, m;
    scanf("%d", &n);

    //array input
    int arr[n];
    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }//n=5 <5 

    scanf("%d", &m);

    for(int j=0; j<n; j++){
        if(arr[j]==m){
            printf("Yes\n");
        }else{
            printf("No\n");
        }
    }
    return 0;
}