#include<stdio.h>
#include<stdlib.h>
struct node
{
	struct node *left;
	struct node *right;
	int data;
}*root;

int max(int a, int b)
{
	return a>b ? a: b;
}


int get_height(struct node *root)
{
	if(root == NULL)
	{
		return 0;
	}
	
	return 1 + max(get_height(root->left), get_height(root->right));

}

int main()
{
	struct node *temp = (struct  node*) malloc(sizeof(struct node));
	temp->data = 123;
	temp->left = NULL;
	temp->right = NULL;
	root = temp;
	struct node *temp2 = (struct  node*) malloc(sizeof(struct node));
	temp->data = 123;
	temp->left = NULL;
	temp->right = NULL;
	root->left = temp2;
	printf(" height  %d",get_height(root));
}