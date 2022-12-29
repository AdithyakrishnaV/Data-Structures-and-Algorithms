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
    
    for(int j=0; j<n; j++){
        
      int min_index=j;

        for(int i=j+1; i<n; i++){
            if(arr[min_index]>arr[i]){
                min_index=i;
            }
                
            }
            int s = arr[j];
            arr[j] = arr[min_index];
            arr[min_index] = s;
    //         for(int i=0; i<4; i++){
    //     printf("%d \t ", arr[i]);
    //    }
    //    printf("\n");
        }
        
        for(int i=0; i<n; i++){
        printf("%d ", arr[i]);
       }
}
    
    