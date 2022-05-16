with open('books.txt') as books_file:
    for line in books_file:
        line1=line.strip()
        fancy_line=line1.split()
        print(line1)