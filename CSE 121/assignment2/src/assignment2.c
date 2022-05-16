/*
 ============================================================================
 Name        : assignment2.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {

/*Create my variables as integers */
	int a = 0;
	int b = 0;

/*Receive input from user for variables a and b*/
	printf("Please enter two integers\n");
	scanf("%d %d" , &a, &b);

/*A series of logical if statements which prints the result */
	if (a > b)
	{
		printf("%d is greater than %d\n",a,b);
	}
	else if (a < b)
	{
		printf("%d is greater than %d\n",b,a);
	}
	else if (a == b)
	{
		printf("%d is equal to %d\n",a, b);
	}
	printf("\n");
/*display the shopping options.*/
	int item = 0;
	printf("What item do you want to select?\n1. Milk\n2. eggs\n3. Juice\n4. Meat\n5. Diapers\n");
	scanf("%d",&item);
/*A switch statement to select a shopping option and view the prices*/
	switch(item)
	{
	case 1:
		printf("Milk costs $4.99\n");
		break;
	case 2:
		printf("Eggs costs $3.99\n");
		break;
	case 3:
		printf("Juice costs $2.99\n");
		break;
	case 4:
		printf("Meat costs $6.99\n");
		break;
	case 5:
		printf("Diapers cost $5.99\n");
		break;
	default:
		printf("Invalid number entered please try again\n");
		break;
	}
	int day = 0;
	printf("Select a day. \n1. Sunday\n2. Monday\n3. Tuesday\n4. Wednesday\n5. Thursday\n6. Friday\n7. Saturday\n");
	scanf("%d",&day);

	int age = 0;
	printf("What is the age of your child?\n");
	scanf("%d",&age);
	if (day <= 5)
	{
		if (age <= 5)
		{
			printf("Bedtime is at 7");
		}
		else if (age >= 6 || age <= 10)
		{
			printf("Bedtime is at 8");
		}
		else if (age >= 11 || age <= 17)
			printf("Bedtime is at 9");
	}
	else if (day == 6)
	{
		if (age <= 5)
			{
				printf("Bedtime is at 7");
			}
			else if (age >= 6 || age <= 10)
			{
				printf("Bedtime is at 9");
			}
			else if (age >= 11 || age <= 17)
				printf("Bedtime is at 12");
	}
	else if (day == 7)
	{
		if (age <= 5)
		{
			printf("Bedtime is at 7");
			}
		else if (age >= 6 || age <= 10)
		{
			printf("Bedtime is at 9");
			}
		else if (age >= 11 || age <= 17)
			printf("Bedtime is at 11");
	}

	return EXIT_SUCCESS;
}
