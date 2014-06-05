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

int min(int a,int b)
{
	return a < b ? a:b;
}


int get_height(struct node *root)
{
	if(root == NULL)
	{
		return 0;
	}
	
	return 1 + max(get_height(root->left), get_height(root->right));

}


int get_minheight(struct node *root)
{
	if(root == NULL)
	{
		return 0;
	}
	
	return 1 + min(get_height(root->left), get_height(root->right));

}

bool check_if_balanced(struct node *root)
{
	return get_height(root) == get_minheight(root) ? 1 : 0;
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