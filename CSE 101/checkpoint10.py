shopping_list = []
iteam = ('0')

while iteam != (''):
    iteam = input('Add an iteam to your list?  ')
    if iteam != (''):
       shopping_list.append(iteam)

print(f'Your list with indexes is:')

number = 0

for i in range(len(shopping_list)):
    iteam = shopping_list[i]
    print(f'{number}. {iteam}')
    number += 1

change = int(input('Which index would you like to change?  '))

for i in range(len(shopping_list)):
    if i == change:
        new = input('What do you wnat the new iteam to be?  ')
        shopping_list[i] = new

print (shopping_list)