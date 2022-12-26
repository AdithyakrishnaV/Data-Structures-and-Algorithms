#include <stdio.h>

int main(void) 
{
    int n;
    scanf("%d ", &n);
    //declare array
    int a[n];
    //take input of array
    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
    }

    //run loop for all elements in array
    for(int j=0; j<n-1; j++){//2   n

        //run loop throughout the array

        for(int i=0; i<n-1-j; i++){
        
            if(a[i]>a[i+1]){
                int f = a[i+1];
                a[i+1] = a[i];
                a[i] = f;
            }
        }
    }
    
    for(int i=0;i<n;i++){
    printf("%d ",a[i]);
    }
    printf("\n");
}