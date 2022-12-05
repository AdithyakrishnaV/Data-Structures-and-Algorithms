//Prime Or NotPrime
#include <stdio.h>

int main(){
    int n, flag=0;
    scanf("%d",&n);
    //155 1 - n  144/
    for(int i=2; i < n; i++){ 
        //if we divide a prime number with any other number and get 0 then not prime 
        if(n%i == 0){
            flag=1;
            break;
        } 
    }
    
    printf("%d\n", flag);
    if(flag==1){
        printf("NotPrime");
    }else{
        printf("Prime");
    }
    
}