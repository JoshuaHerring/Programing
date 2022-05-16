from audioop import reverse


def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    fruit_list.reverse()
    print(f'list reversed: {fruit_list}')
    fruit_list.append('Oarange')
    print(fruit_list)
    apple_index = fruit_list.index('apple')
    fruit_list.insert(apple_index, 'cherry')
    print(fruit_list)
    fruit_list.remove('banana')
    print(fruit_list)
    pop = fruit_list.pop()
    print(f'{pop} and {fruit_list}')
    fruit_list.sort()
    print(fruit_list)
    fruit_list.clear()
    print(f'cleared? {fruit_list}')



if __name__ == '__main__':
    main()