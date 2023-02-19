#include<stdio.h>
#include<malloc.h>
struct dnode{
	struct dnode *prev;
	int data;
	struct dnode *next;
};
struct dnode *head=NULL;
struct dnode *temp,*p;
void insertAtFrontDLL();
void insertAtEndDLL();
void deleteFromFrontDLL();
void deleteFromEndDLL();
void displayDLL();
int main()
{
	int choice;
	do{
		printf("1.Insert@Front 2:Insert@End 3:DeleteFromFront 4:DeleteFromEnd 5.DisplayLinkedList 6:Exit\t");
		scanf("%d",&choice);
		switch(choice){
			case 1:{
        		insertAtFrontDLL();
        		break;
      		}
      		case 2:{
        		insertAtEndDLL();
        		break;
      		}
      		case 3:{
        		deleteFromFrontDLL();
        		break;
      		}
      		case 4:{
        		deleteFromEndDLL();
        		break;
      		}
      		case 5:{
        		displayDLL();
        		break;
      		}
      		case 6:{
        		printf("\nBye\n");
        		break;
      		}
      		default:
        		printf("Wrong Choice\n");
    		}
	}while(choice!=6);
}
void insertAtFrontDLL()
{
	int val;
	scanf("%d",&val);
  	temp=(struct dnode*) malloc(sizeof(struct dnode));
  	temp->data=val;
  	temp->prev=NULL;
  	if(head==NULL){
    	temp->next=NULL;
    	head=temp;
    }
    else
    {
    	temp->next=head;
    	head->prev=temp;
    	head=temp;
    }
   }
void insertAtEndDLL()
{
	int val;
	scanf("%d",&val);
    temp=(struct dnode*) malloc(sizeof(struct dnode));
    temp->data=val;
    temp->next=NULL;
    if(head==NULL){
    	head=temp;
    	temp->prev=NULL;
    }
    p=head;
    while(p->next!=NULL){
    	p=p->next;
    }
    p->next=temp;
    temp->prev=p;
}
void deleteFromFrontDLL()
{
	if(head!=NULL){
		head=head->next;
		head->prev=NULL;
	}
}
void deleteFromEndDLL()
{
	p=head;
    while(p->next->next!=NULL){
        p=p->next;
    }
    p->next=NULL;
    
}
void displayDLL()
{       
	if(head==NULL){
		printf("List is empty");
	}
	else
	{
		p=head;
   		while(p!=NULL){
       		printf("%d ",p->data);
       		p=p->next;
    	}
    	printf("\n");
	}
}