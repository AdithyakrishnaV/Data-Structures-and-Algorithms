#include <stdio.h>

int main(){
    int n;
    scanf("%d ", &n);
    //declare array
    int arr[n];
    //take input of array
    for(int i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }
    // int n =5;

    // int arr[]={5,4,3,2,1};

    for(int i=1; i<n; i++){

        while(arr[i]<arr[i-1]){
            int t = arr[i];
            arr[i]=arr[i-1];
            arr[i-1]=t;
            i=i-1;
        }
    }

    //print the array
    for(int j=0; j<n; j++){
        printf("%d ",arr[j]);
    }
}

