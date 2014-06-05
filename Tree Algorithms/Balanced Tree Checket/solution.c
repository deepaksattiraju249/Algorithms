#include<stdio.h>
struct node
{
	node *left;
	node *right;
	int data;
}*root;

int get_height(node *root)
{
	if(ptr->left == NULL && ptr->right == NULL)
	{
		return 0;
	}
	
	return max(get_height(root->left)+1, get_height(root->right)+1)

}

main()
{
	node root = new node;
	root->data = 123;
	printf(" height  %d",get_height(root));
}