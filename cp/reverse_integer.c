/*Name:
  Description:
*/

//Accept a positive integer and print its reverse

//543 345

#include <stdio.h>

int main(void) {
    int a, b;
    scanf("%d", &a);

    if(a>0){
        while(a!=0){ 
           b=a%10;
           a=a/10;
            printf("%d", b);
        }
    }
    
    
    return 0;
} 