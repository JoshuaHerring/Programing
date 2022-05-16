import random

def main():
    numbers = []
    for _ in range(3):
        number = round(random.uniform(0,100), 1)
        numbers.append(number)
    print(numbers)
    numbers = append_random_numbers(numbers)
    print(numbers)
    numbers = append_random_numbers(numbers, 3)
    print(numbers)

def append_random_numbers(numbers_list, quantity = 1):
    for _ in range(quantity):
        number = round(random.uniform(0,100), 1)
        numbers_list.append(number)
    return numbers_list




if __name__ == '__main__':
    main()