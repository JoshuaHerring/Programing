with open ('request.csv') as requests_file:
    list = []
    for line in requests_file:
        clean_line = line.strip()
        split_line = clean_line.split(',')
        list.append(split_line)
list.pop(0)

print(list)