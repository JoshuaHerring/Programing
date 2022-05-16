#include <stdio.h>
#include <stdlib.h>

struct bank
{
	int num;
	char name[20];
	float balance;
	struct bank *next;
};

void enter_information (struct bank * point)
{
	printf("Account number: \n");
	scanf("%d",&point->num);
	printf("Account name: \n");
	scanf("%s",point->name);
	printf("Balance: \n");
	scanf("%f",&point->balance);
}

int main(void) {

	struct bank* head = NULL;
	struct bank* tail = NULL;

	int request = 0;
		printf("1. Add a new account\n2. View all accounts\n3. Find an account\n4. Update account\n0. Quit\n Enter '1' '2' '3' '4' or '0'");
		scanf("%d",&request);
		while (request != 0)
				{
			if (request == 1)//add
					{
				struct bank* new_account = malloc(sizeof(struct bank));
				new_account->next = NULL;
				enter_information(new_account);
				if (head == NULL){
						head = new_account;
				}
				else if (head != NULL)
				{
					tail = head;
					while (tail->next != NULL)
					{
						tail = tail->next;
					}
					if (tail->next == NULL)
							{
						tail->next = new_account;
							}
				}
					}
			else if (request == 2)//view all
					{
				tail = head;
				printf("Account number: %d Account name: %s Account balance: %f \n",tail->num, tail->name, tail->balance);
				while (tail->next != NULL)
				{
					tail = tail->next;
					printf("Account number: %d Account name: %s Account balance: %f \n",tail->num, tail->name, tail->balance);
				}

					}
			else if (request == 3)//find account
			{
				tail = head;
				int chosen = 0;
				printf("Enter an account number: ");
				scanf("%d", &chosen);

				if (tail->num == chosen)
					{
					printf("Account number: %d Account name: %s Account balance: %f\n",tail->num, tail->name, tail->balance);
					}

				while (tail->num != chosen)
				{
					(tail = tail->next);

					if (tail->num == chosen)
					{
						printf("Account number: %d Account name: %s Account balance: %f\n",tail->num, tail->name, tail->balance);
					}
					else if (tail->next == NULL)
					{
						printf("Account number: '%d' could not be found\n",chosen);
						break;
					}
				}
			}
			else if (request == 4)// Update account
			{
				tail = head;
				int chosen = 0;
				printf("Enter an account number to edit: ");
				scanf("%d", &chosen);

				if (tail->num == chosen)
						{
						enter_information(tail);
						printf("Account number: %d Account name: %s Account balance: %f\n",tail->num, tail->name, tail->balance);
					}

					while (tail->num != chosen)
						{
						(tail = tail->next);

						if (tail->num == chosen)
						{
						enter_information(tail);
						break;
						}
						else if (tail->next == NULL)
						{
						printf("Account number: '%d' could not be found\n",chosen);
						break;
								}
							}
						}

			printf("1. Add a new account\n2. View all accounts\n3. Find an account\n4. Update account\n0. Quit\n Enter '1' '2' '3' '4' or '0'");
			scanf("%d",&request);
				}
	return EXIT_SUCCESS;
}
