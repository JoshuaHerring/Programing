# y = input('Give me a number:')
# if y ==str(22):
    # print('lucky')
# else:
    # print('unlucky')
    # print('die')

#anything 4 spaces in will not run unless the if critirea is met
#you can nest if statements in if statements that wont run if the original if statement is not satisfied.
#instead of nesting if statements you can use the and function.
#ex. if health >=(20) and hunger>=(20):
#with and statements both conditions must be met in order to register as true.
#        print(healthy)
#Boolean flags. You can mark a variable as true or false for later in your code.
#ex. if... then alive = true     using that your code will remember that alive is a true comment and you can write
# if alive
#        print(you win)
status= input('Are you alive? ')
if status== ('yes'):
    province=input('how much hp do you have: ')
    if float(province)==(0) or float(province)==(100):
#instead of using or you can use in
#ex. if float(province) in('10,20,30,40'):
        print('You died')
    elif float(province)<=(10):
        print('hurt')
    elif float(province)==(20):
        print('weak')
    elif float(province)>=(30):
        print('well')
    else:
        print('sick')
else:
    print('You died')
#the advantage of using elif insted of if is that it stops multiple if statements from running at the same time.
#if you want multiple if statments to run at the same time do not use elif just use several if statements.
#      always test every line of code the first and last might work but there oculd be a problem in the middle