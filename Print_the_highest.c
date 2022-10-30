//Accept two integers. Print the highest

#include <stdio.h>

int main(void) { //it clearly specifies that main can only be called without any 
                //parameter
  int num;
  int dig;

  scanf("%d", &num);
  scanf("%d", &dig);

 if(num>dig){
    printf("%d", num);
     
 }else if(num == dig){
     printf("same number");
    
 }else{
     printf("%d", dig);
 }
    
  return 0;
}