amount = []

number = ('')

#Recieve the list from the user
while number != 0:
    number = float(input('Add a number to the list: '))
    if number != 0:
        amount.append(number)

# Calculate the sum
sum = 0

for numbers in amount:
    sum += numbers

print (f'Your sum is: {sum}')

#Calculate the average

average = sum / len(amount)
print(f'Your average is : {average}')

#Calculate the largest number
large = 0
for numbers in amount:
    if numbers > large:
        large = numbers
print (f'The largest number in your lsit is {large}')

#Smallest positive number
small_pos = 1000000000000000000000
for numbers in amount:
    if numbers > 0:
        if numbers < small_pos:
            small_pos = numbers
print(f'Your smallest positive number is:{small_pos}')

# Sorted list

amount.sort()
print(f'Your sorted list:\n{amount}')