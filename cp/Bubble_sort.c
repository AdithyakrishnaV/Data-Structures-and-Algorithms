/*
The bubble sort gets its name because elements tend to move 
up into the correct order like bubbles rising to the surface. 

Bigger elements bubble up lower elements under it
*/

#include <stdio.h>

int main(void) 
{
    int n;
    scanf("%d", &n);
    //declare array
    int a[n];
    //take input of array
    for(int i=0; i<n; i++){
        scanf("%d", &a[i]);
    }

    //run loop for all elements in array
    for(int j=0; j<n; j++){
        //run loop throughout the array
        for(int i=0; i<n; i++){
            if(a[i]>a[i+1]){
                int f = a[i+1];//f=0
                a[i+1] = a[i];//i+1=45
                a[i] = f;//a[i]=0
            }
        }
    }
    // Write the rest of your code here
    //Use int a[n] as aay of size n
    
    for(int i=0;i<n;i++){
    printf("%d ",a[i]);
    }
    printf("\n");
}