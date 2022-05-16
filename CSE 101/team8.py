number=int(input('How many Columns and Rows do you want? '))
range_size=number+1

for row in range(1,range_size):
    for column in range(1,range_size):
        number=row*column
        print(f'{number:3}',end='')
    print('')