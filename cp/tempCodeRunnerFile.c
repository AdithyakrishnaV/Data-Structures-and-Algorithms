//array is contiguous memory
// //linked list  is unidirectional
// //C Classes
// // A class consists of an instance type and a class object: An instance type is a struct

//  #include <stdio.h>
// #include <stdlib.h>

// struct node{
//     int data;
//     struct node *next;
//     //node* next; is a pointer to a struct named "Node." This means that next variable
//     // is a pointer which will hold the address of another node.
// };
// //declare the head is NULl
// struct node *head=NULL;

// int main(){

//     struct node *newNode;
//     struct node *p;
//     int choose, val;

//     do{
//         switch(choose){
//             //insert node @ begining
//             case 1:{
//                 scanf("%d", &val);
//                 newNode=(struct node*)malloc(sizeof(struct node));
//                 newNode->data=val;
//                 newNode->next=NULL;
                
//                 if(head == NULL){
//                     head = newNode;
//                 }else{
//                     newNode->next=head;
//                     head=newNode;
//                 }
//                 break;

//             }

//             //insert @ end
//             case 2:{
//                 scanf("%d", &val);
//                 newNode=(struct node*)malloc(sizeof(struct node));
//                 newNode->data=val;
//                 newNode->next=NULL;
//                 if(head == NULL){
//                     head=newNode;
//                 }else{
//                     p=head;
//                     while(p->next!=NULL){
//                         p=p->next;
//                     }
//                     p->next=newNode;
//                     break;
                    
//                 }
//             }
            
//             //delete from front

//             case 3:{
//                 if(head == NULL){
//                     printf("Empty");
//                 }else{
//                     head = head->next;

//                 }
//                 break;

//             }

//             //delete from end

//             case 4:{
//                 if(head == NULL){
//                     printf("Empty");
//                 }else{

//                     p=head;
//                     if(p->next!=NULL){
//                         if(p->next->next==NULL){
//                             p->next=NULL;
//                         }else{
//                             p=p->next;
//                         }
//                     }else{
//                         p = p->next;
//                     }
//                 }
//             }

//             //display linked list
//             case 5:{
//                 p=head;
//                 while(p->next!=NULL){
//                     printf("%d", &p);
//                 }
//             }

//         }
//     }while (choose!=6);
   
//   return 0;
// }