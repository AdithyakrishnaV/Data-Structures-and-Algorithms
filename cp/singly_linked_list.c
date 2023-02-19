//array is contiguous memory
//linked list  is unidirectional
//C Classes
// A class consists of an instance type and a class object: An instance type is a struct

 #include <stdio.h>
#include <stdlib.h>

struct node{
    int data;
    struct node *next;
    //node* next; is a pointer to a struct named "Node." This means that next variable
    // is a pointer which will hold the address of another node.
};
//declare the head is NULl
struct node *head=NULL;

int main(){

    struct node *newNode;
    struct node *p;
    int choose, val;

    do{
        scanf("%d", &choose);
        switch(choose){
            //insert node @ begining
            case 1:{
                scanf("%d", &val);
                newNode=(struct node*)malloc(sizeof(struct node));
                newNode->data=val;
                newNode->next=NULL;
                
                if(head == NULL){
                    head = newNode;
                }else{
                    newNode->next=head;
                    head=newNode;
                }
                break;

            }

            //insert @ end
            case 2:{
                scanf("%d", &val);
                newNode=(struct node*)malloc(sizeof(struct node));
                newNode->data=val;
                newNode->next=NULL;
                if(head == NULL){
                    head=newNode;
                }else{
                    p=head;
                    while(p->next!=NULL){
                        p=p->next;
                    }
                    p->next=newNode;
                    break;
                    
                }
            }
            
            //delete from front

            case 3:{
                if(head == NULL){
                    printf("Empty");
                }else{
                    head = head->next;

                }
                break;

            }

            //delete from end

            case 4:{
                if(head == NULL){
                    printf("Empty");
                }else{

                    p=head;
                    if(p->next!=NULL){
                        if(p->next->next==NULL){
                            p->next=NULL;
                        }else{
                            p=p->next;
                        }
                    }else{
                        p = p->next;
                    }
                }
                
                break;
            }

            //display linked list
            case 5:{
                p=head;
                while(p->next!=NULL){
                    printf("%d", p->data);
                }
            }
            case6:{
                break;
            }

        }
    }while (choose!=6);
   
  return 0;
}

//add this 
//1.Display the list \n 2.Add node at the beginning \n 3.Add node at the end \n 4.Delete node from the beginning \n 5.Delete node from the end 












#include <stdio.h>
#include <malloc.h>

struct node
{
    int data;
    struct node *next;
};
struct node *head = NULL;

int main()
{
    int choice, val;
    struct node *temp, *p;
    do
    {
        printf("\n 1.Display the list \n 2.Add node at the beginning \n 3.Add node at the end \n 4.Delete node from the beginning \n 5.Delete node from the end \n 6.Exit \n Enter an option: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
        {
            p = head;
            if (p != NULL)
            {

                while (p != NULL)
                {
                    printf("%d ", p->data);
                    p = p->next;
                }
            }
            else
                printf("Nothing to display\n");
            break;
        }
        case 2:
        {
            printf("Enter the value to be added: ");
            scanf("%d", &val);
            temp = (struct node *)malloc(sizeof(struct node));
            temp->data = val;
            temp->next = NULL;
            if (head == NULL)
            {
                head = temp;
            }
            else
            {
                temp->next = head;
                head = temp;
            }
            break;
        }
        case 3:
        {
            printf("Enter the value to be added: ");
            scanf("%d", &val);
            temp = (struct node *)malloc(sizeof(struct node));
            temp->data = val;
            temp->next = NULL;
            if (head = NULL)
                head = temp;
            else
            {
                p = head;
                while (p->next != NULL)
                {
                    p = p->next;
                }
                p->next = temp;
            }
            break;
        }
        case 4:
        {
            if (head = NULL)
                printf("NOTHING TO DELETE");
            else
                head = head->next;
            break;
        }
        case 5:
        {
            p = head;
            if (p != NULL)
                printf("NOTHING TO DELETE");
            else
            {
                p = head;
                while (p != NULL)
                    p = p->next;
            }
            break;
        }
        }
    } while (choice != 6);
    return 0;
}