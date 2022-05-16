# yes this is rushed and not good:|


import csv

with open('students.csv') as csv_file:
    dictionary = {}
    reader = csv.reader(csv_file)
    next(reader)
    for row_list in reader:
        key = row_list[0]
        dictionary[key] = row_list
number = input('WHat is number? ')
if number in dictionary:
    person = dictionary[number]
    name = person[1]
    print (name)
else:print('Person does not exist.')
