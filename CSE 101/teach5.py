grade = int(input('What is your percent grade?'))

if grade >= 90:
    letter=('A')
elif grade >= 80:
    letter=('B')
elif grade >=70:
    letter=('C')
elif grade >=60:
    letter=('D')
else: letter=('F')

if grade%10 >=7:
    sign = ('+')
elif grade%10<3:
    sign = ('-')
else:sign= ('')

if letter == ('A') or letter == ('F'):
   print(f'Your letter grade is: {letter}')
else:print(f'Your letter grade is: {letter+sign}')

#Both the above and below commands are options that work :)

#  if grade >=90:
    #  print(f'Your letter grade is: {letter}')
# elif grade<60:
    # print(f'Your letter grade is: {letter}')
# else:print(f'Your letter grade is: {letter+sign}')

if grade>=70:
    print('Congragulations You Passed!!!!!!!')
else: print('You Failed:( Better luck next time chap:)')