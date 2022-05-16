

with open('hr_system.txt') as f:
    for line in f:
        stripped_line = line.strip()
        split_line = stripped_line.split()

        split_line[3] = int(split_line[3]) / 24

        if split_line[2] == ('Engineer'):
            split_line[3] = split_line[3] +1000

        print (f'Name: {split_line[0]} (ID: {split_line[1]}), Title: {split_line[2]} - ${split_line[3]:.2f}')