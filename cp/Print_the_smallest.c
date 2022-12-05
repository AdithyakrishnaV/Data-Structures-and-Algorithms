//Accept three integers. Print the smallest.

#include <stdio.h>

int main(void) {
    int a, b, c;

    scanf("%d %d %d", &a, &b, &c);

    if(a<=b && a<=c){ //Logical AND ||
        printf("%d", a);
    }else if(b<=c){
        printf("%d", b);
    }else{
        printf("%d", c);
    }
    return 0; 
    
}