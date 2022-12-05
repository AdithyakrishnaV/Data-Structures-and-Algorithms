//Accept an integer. Print the sum of its digits


#include <stdio.h>

int main(void) 
{
    int a, b, c;
    scanf("%d",&a);//43

    while(a!=0){
        b=a%10;//4
        a=a/10;//4
        c=c+b;//3+4
    }
    printf("%d", c);//  %  	Modulus  	Returns the division remainder
    
    return 0;
}