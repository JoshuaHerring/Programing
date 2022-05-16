# Near the beginning of your program replace the code that asks the user for the subtotal with a loop
#  that repeatedly asks the user for a price and a quantity and computes the subtotal. This loop should repeat
#   until the user enters "0" for the price.

from datetime import datetime

day_of_the_week = datetime.now().weekday()
subtotal = 0
price_of_iteam = 10
while price_of_iteam:
   price_of_iteam = float(input('What is the price of the iteam? '))
   if price_of_iteam:
      number_of_iteam = float(input('How many of those iteams do you have? '))
      amount = (price_of_iteam * number_of_iteam)
      subtotal += amount


if day_of_the_week == 1 or day_of_the_week == 2:
    if subtotal < 50:
        purchases_needed = 50 - subtotal
        print(f'You need to purchase {purchases_needed} more money in order to qualify for the discount')
    if subtotal >= 50:
        subtotal = subtotal * .9
tax_amount = subtotal * .06
total = subtotal + tax_amount
print(f'Sales tax: {tax_amount:.2f}')
print(f'Total {total:.2f}')

