highest_life = '0'
highest_country=''
highest_year = ''
lowest_life = '100000000000'
lowest_country=''
lowest_year = ''
target_year = input('What is your target year? ')
target_high = '0'
target_low = '1000000000000000'
average_target = []
country_target_low = ''
country_target_high =''

with open('life-expectancy.csv') as life_file:
    for line in life_file:
        stripped_line = line.strip()
        split_line=stripped_line.split(',')

        if split_line[3] > highest_life:
            highest_life = split_line[3]
            highest_country = split_line[0]
            highest_year = split_line[2]

        if split_line[3] < lowest_life:
            lowest_life = split_line[3]
            lowest_country = split_line[0]
            lowest_year = split_line[2]
        
        if split_line[2] == target_year:
            average_target.append(float(split_line[3]))
            if target_high < split_line[3]:
                country_target_high = split_line[0]
                target_high = split_line[3]
            if target_low > split_line[3]:
                country_target_low = split_line[0]
                target_low = split_line[3]

sum = sum(average_target)
length = len(average_target)

print(f'The highest life is {highest_life} from {highest_country} in {highest_year}.')
print(f'The lowest life is {lowest_life} from {lowest_country} in {lowest_year}')

print(f'For the year {target_year} the average life was {sum / length}')
print(f'The lowest life was {target_low} from {country_target_low}')
print(f'With the highest being {target_high} from {country_target_high}')