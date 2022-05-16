#This is crappy and disorgainized and should be split into seperate functions;)

# Open the provinces.txt file for reading.
with open ('provinces.txt') as text_file:
    # Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
    list_of_file = []
    for line in text_file:
        clean_line = line.strip()
        list_of_file.append(clean_line)
# Print the entire list.
print (list_of_file)

# Remove the first element from the list.
list_of_file.pop(0)
# Remove the last element from the list.
list_of_file.pop(-1)
# Replace all occurrences of "AB" in the list with "Alberta".
########You do not need to use those functions you could simply write if x == ab then x = Alberta
for x in list_of_file:
    if x == 'AB':
        list_of_file.remove('AB')
        list_of_file.append('Alberta')
print(list_of_file)
# Count the number of elements that are "Alberta" and print that number.
number_of_alberta = list_of_file.count('Alberta')
print(number_of_alberta)
