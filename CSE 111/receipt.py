import csv
from datetime import datetime
def main():
    products_dict = read_dict('products.csv',0)
    # for line in products_dict:
    #     print(f'{line} {products_dict[line]}')
    try:
        with open ('request.csv') as requests_file:
            list = []
            for line in requests_file:
                clean_line = line.strip()
                split_line = clean_line.split(',')
                list.append(split_line)
    except FileNotFoundError as ex:
        print(f'Error: {requests_file} does not exist.')
    except PermissionError as ex:
        print(f'Error: You do not have permission to view file: {requests_file}')
    list.pop(0)
    #print(list)
# Print the store name at the top of the receipt.
    print("Bob's Mart")
# Print the list of ordered items.
    subtotal = 0
    for sub_list in  list:
        iteam = products_dict[sub_list[0]]
        name = iteam[1]
        # Sum and print the number of ordered items.
        print(f'Product: {name} *{sub_list[1]}, Price: ${(float(iteam[2]) * float(sub_list[1])):.2f}')
        # Sum and print the subtotal due.
        subtotal += (float(iteam[2]) * float(sub_list[1]))
    print(f'subtotal: ${subtotal:.2f}')
# Compute and print the sales tax amount. Use 6% as the sales tax rate.
    sales_tax = (subtotal * .06)
    print(f'Sales tax: ${sales_tax:.2f}')
# Compute and print the total amount due.
    total = subtotal + sales_tax
    print(f'Total: ${total:.2f}')
# Print a thank you message.
    print("Thank you for shopping ar Bob's Mart")
# Get the current date and time from your computer's operating system and print the current date and time.
    date = datetime.now()
    print(date)
# Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.

        # for sub_list in  list:
        #     iteam = products_dict[sub_list[0]]
        #     name = iteam[1]
        #     print(f'Product: {name}, Quantity: {sub_list[1]}, Price: {iteam[2]}')


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    with open(filename) as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
        return dictionary

if __name__ == '__main__':
    main()