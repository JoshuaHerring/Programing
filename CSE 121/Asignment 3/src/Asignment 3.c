/*
 ============================================================================
 Name        : Asignment.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void display_binary(unsigned int num){
// tests the number against a tester int that bit shifts and prints a 1 or a 0 if it is equal
	int x = 0;
	unsigned int tester = 4294967295;
	while (x < 32)
	{
		if (num & tester)
		{
			printf("1");
		}
		else
		{
			printf("0");
		}
		tester = tester >> 1;
		x++;
	}
	printf("\n");

}


int main(void) {
	//PART 1
	char name [20];
	// Receive a string from the user
	printf("What is your name?\n");
	scanf("%s",name);
	int length = strlen(name);
	int index = 0;
	printf("%s in hexadecimal is ", name);
	// use a for loop to get the hexadecimal for each letter in the string
	for (index = 0; index < length; index++)
	{
		printf("%x",name[index]);
	}
	printf("\n");

	// Part 2 convert to binary
	//Receives a number from a user and passes it to the function
	unsigned int number = 0;
	printf("Give me a number: ");
	scanf("%u",&number);
	display_binary(number);

	//Part 3
	int var_1 = 30;
	int var_2 = 20;
	int and = var_1 & var_2;
	int or = var_1 | var_2;
	display_binary(var_1);
	display_binary(var_2);
	display_binary(and);
	display_binary(or);

	return EXIT_SUCCESS;
}
