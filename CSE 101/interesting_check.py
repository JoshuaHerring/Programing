with open('interesting.text') as f:
    for line in f:
        stripped_line = line.strip()
        split_line = stripped_line.split()
        print(stripped_line)