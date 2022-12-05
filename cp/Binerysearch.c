#include <stdio.h>
//binery search

//recursive method

int binarySearch(int low,int high,int arr[],int f){
	if(low>high){
    return 0;
  }else{
    int mid; 
	  mid = (low+high)/2;
    if(arr[mid]==f){
        return 1;
        
    }else if(arr[mid]<f){
		return binarySearch(mid+1, high, arr, f);
    }else{// 8<9
		return binarySearch(low, mid-1, arr, f);
    }
  }

	return 0;
}

int main(void) 
{
    int low, high, n, f, mid,  i;
    //take the input of number of elements of 
    printf("Enter the size of array:");
    scanf("%d", &n);
    //take the input of array
    int arr[n];
    printf("Input elements of array:");
    for(i=0; i<n; i++){
        scanf("%d", &arr[i]);
    }

    scanf("%d", &f);
    
    int flag = binarySearch(0, n-1, arr, f);
    (flag == 1)
      ?printf("Yes\n")
      :printf("No\n");  
    return 0;
}
