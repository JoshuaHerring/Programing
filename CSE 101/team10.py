name_acount = ('')
amount_acount = ('')
names = []
balances = []

while name_acount != ('quit'):
    name_acount = input('What is the name of the acount(type "quit" when finished)? ')
    if name_acount != ('quit'):
        amount_acount = input(f'What is the balance of the account {name_acount}? ')
        names.append(name_acount)
        balances.append(amount_acount)

for i in range (len(names)):
    print(f'{names[i]} - ${balances[i]}')