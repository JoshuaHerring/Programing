#include <stdio.h>
#include <stdlib.h>

/*
Extend the bank program from last week's project to enable
a menu system interface to your account system. This menu
should give the user three choices: Add a new account, display
all the information in all of the accounts, and
quit the program. You should create new specialized functions as
needed to provide this functionality. Use a linked list to store
the information about each account. The menu system should be run
in a loop until the user quits the program.
*/
struct bank
{
	int num;
	char name[20];
	float balance;
	struct person *next;
};

void create(struct bank * point)
{
	printf("Account number: \n");
	scanf("%d",&point->num);
	printf("Account name: \n");
	scanf("%s",point->name);
	printf("Balance: \n");
	scanf("%f",&point->balance);
	point->next = NULL;
}

void output(struct bank * point)
{
	printf("Account info:   Num: %d   Name: %s    Balance:%f \n", point->num, point->name, point->balance);
}
//

int find_min(int* a,int* b) {
		printf("Give me two numbers.\n");
		scanf("%d",a);
		printf("\n");
		scanf("%d",b);

		if (*a < *b)
		{
			return (*a);
		}
		else
		{
			return (*b);
		}
	}

int main(void) {
	/* Part 1 set two variables then use a function to determine the lowest one. print the lowest then after the function print them both.
	int a = 0;
	int b = 0;
	int minimum = find_min(&a,&b);
	printf("The minimum is %d \n",minimum);
	printf("a is now %d and b is now %d\n",a,b);
	*/

	//part 2 create a bank structure and have a function for input
	//and one for output, use pointers


	struct bank* pointer = malloc(sizeof(struct bank));
	int request = 0;
	printf("1. Add a new account\n2. View all accounts\n0. Quit\n Enter '1' '2' or '0'");
	scanf("%d",&request);
	while (request != 0)
			{
		if (request == 1)
				{
			create(pointer);
				}
		else if (request == 2)
				{
			output(pointer);
				}
		printf("1. Add a new account\n2. View all accounts\n0. Quit\n Enter '1' '2' or '0'");
		scanf("%d",&request);
			}
	free(pointer);

	return EXIT_SUCCESS;
}
