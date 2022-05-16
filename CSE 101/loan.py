print('Give a rating of 1 to 10 for all the following questions.\n')

loan = float(input('How large is the loan?'))
credit = float(input('How good is your credit?'))
income = float(input('How high is your income?'))
down = float(input('How big is your down payment?'))
print('')
decision = False

if loan >= 5:
    if credit >= 7 and income >= 7:
        decision = True
    elif credit >= 7 or income >= 7:
        if down >= 5:
            decision = True
    elif credit < 7 or income < 7:
        decision = False

else:
    if credit < 4:
        decision = False
    else:
        if income >= 7 or down >= 7:
            decision = True
        elif income>= 4 and down >= 4:
            decision = True
        else: decision = False

if decision:
    print('Yes')
if not decision:
    print('No')