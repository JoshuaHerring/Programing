names = []
numbers = []
name = ('0')
number = ('not a number')

while name != (''):
    name = input('Give me a name:  ')
    if name != (''):
        number = input(f'What is {name}\'s number?   ')
        names.append(name)
        numbers.append(number)

remove = int(input('What do you want to remove from the list?  '))
for i in range(len(names)):
    if i == remove:
        names.pop(i)
        numbers.pop(i)
        print('worked')
print(f'{names} {numbers}')



# chosen = int(input('Which number in the list do you want?  ')) - 1
# for i in range(len(names)):
#     if i == chosen:
#        name = names[i]
#        number = numbers[i]

# print (f'{name} and {number}')