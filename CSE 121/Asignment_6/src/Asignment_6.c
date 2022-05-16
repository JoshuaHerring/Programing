#include <stdio.h>
#include <stdlib.h>
#include<time.h>


struct workout
{
	char name[40];
	struct workout *next;
};


void choose_workout(struct workout* initial)
{
	/* Function that receives a linked list of work-outs and outputs
	 *6 random work-outs from the list
	 */
	int i;
	int y;
	int w;
	int a;
	int numbers_used[6] = {0};

	for (i = 0; i <= 5; i++)
			{
		struct workout* finder = initial;
		int random_number = rand() %10;
		a = 0;

		for (w = 0; w <= i; w++)
		{
			if (random_number == numbers_used[w])
			{
				a += 1;
				break;
			}
		}
		if (a == 0)
		{
			numbers_used[i] = random_number;


		for (y = 1; y <= random_number; y++)
		{
			finder = finder->next;
		}
			printf("%s \n",finder->name);
				}
		else
		{
			(i--);
		}
		}
	printf("\n \n");

}



int main(void) {
	srand(time(0));
	// linked lists of different muscle groups
	struct workout chest1 = {"Push-Ups", NULL};
	struct workout chest2 = {"Bench Press", NULL};
	chest1.next = (&chest2);
	struct workout chest3 = {"Incline Bench Press", NULL};
	chest2.next = (&chest3);
	struct workout chest4 = {"Dumbbell Press", NULL};
	chest3.next = (&chest4);
	struct workout chest5 = {"Incline Dumbbell Press", NULL};
	chest4.next = (&chest5);
	struct workout chest6 = {"Plate Press", NULL};
	chest5.next = (&chest6);
	struct workout chest7 = {"Decline Push-Ups", NULL};
	chest6.next = (&chest7);
	struct workout chest8 = {"Incline Push-Ups", NULL};
	chest7.next = (&chest8);
	struct workout chest9 = {"Bent Over Row", NULL};
	chest8.next = (&chest9);
	struct workout chest10 = {"Machine Fly", NULL};
	chest9.next = (&chest10);


	struct workout triceps1 = {"Overhead Tricep Extension", NULL};
	struct workout triceps2 = {"Skull Crusher", NULL};
	triceps1.next = (&triceps2);
	struct workout triceps3 = {"Tricep Pushdown", NULL};
	triceps2.next = (&triceps3);
	struct workout triceps4 = {"Diamond Push-Up", NULL};
	triceps3.next = (&triceps4);
	struct workout triceps5 = {"Tricep Dip", NULL};
	triceps4.next = (&triceps5);
	struct workout triceps6 = {"Close Grip Bench", NULL};
	triceps5.next = (&triceps6);
	struct workout triceps7 = {"Single Arm Cable", NULL};
	triceps6.next = (&triceps7);
	struct workout triceps8 = {"Bench Dip", NULL};
	triceps7.next = (&triceps8);
	struct workout triceps9 = {"Cable Overhead Extension", NULL};
	triceps8.next = (&triceps9);
	struct workout triceps10 = {"Cable Pushdown", NULL};
	triceps9.next = (&triceps10);

	struct workout biceps1 = {"Preacher Curls", NULL};
	struct workout biceps2 = {"Reverse Preacher Curls", NULL};
	biceps1.next = &biceps2;
	struct workout biceps3 = {"Hammer Curls", NULL};
	biceps2.next = &biceps3;
	struct workout biceps4 = {"Concentration Curls", NULL};
	biceps3.next = &biceps4;
	struct workout biceps5 = {"Bicep Cable Curl", NULL};
	biceps4.next = &biceps5;
	struct workout biceps6 = {"Chin-Up", NULL};
	biceps5.next = &biceps6;
	struct workout biceps7 = {"Incline Dumbbell Curl", NULL};
	biceps6.next = &biceps7;
	struct workout biceps8 = {"Barbell Curl", NULL};
	biceps7.next = &biceps8;
	struct workout biceps9 = {"Seated Dumbbell Curls", NULL};
	biceps8.next = &biceps9;
	struct workout biceps10 = {"Bent Over Row", NULL};
	biceps9.next = &biceps10;

	struct workout legs1 = {"Squats", NULL};
	struct workout legs2 = {"Calf Raises", NULL};
	legs1.next = &legs2;
	struct workout legs3 = {"Lunges", NULL};
	legs2.next = &legs3;
	struct workout legs4 = {"Bulgarian Split Squat", NULL};
	legs3.next = &legs4;
	struct workout legs5 = {"Leg Curl", NULL};
	legs4.next = &legs5;
	struct workout legs6 = {"Leg Extension", NULL};
	legs5.next = &legs6;
	struct workout legs7 = {"Front Squats", NULL};
	legs6.next = &legs7;
	struct workout legs8 = {"Seated Toe Raise", NULL};
	legs7.next = &legs8;
	struct workout legs9 = {"Romanian Dead Lift", NULL};
	legs8.next = &legs9;
	struct workout legs10 = {"Kettle Bell Swing", NULL};
	legs9.next = &legs10;


	struct workout* type = NULL;
	int p;

	/* Loops through the program allowing you to select a work-out and
	 * if you are not happy you can request a new set.
	 */
	while (p != 0)
	{
	printf("Select a muscle group: \n1. Chest\n2. Triceps\n3. Biceps\n4. Legs\n0. Quit \n");
	scanf("%d",&p);
	if (p == 1)
		{
		type = &chest1;
		}
	else if (p == 2)
	{
		type = &triceps1;
	}
	else if (p == 3)
	{
		type = &biceps1;
	}
	else if (p == 4)
	{
		type = &legs1;
	}

	printf("Your set is as follows:\n");
	choose_workout(type);
	}

	return EXIT_SUCCESS;
}
