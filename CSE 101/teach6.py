age1 = float(input('How old are you?'))
height1 = float(input('How many inches tall are you?'))
friend = input('Do you have a friend yes/no?')
if friend == ('yes'):
    age2 = float(input('How old is your friend?'))
    height2 = float(input('How many inches tall is your friend?''\n'))

#strech2
if age1 > 11 and age1 < 18:
    golden = input('Do you have a golden passport?yes/no')
    if golden==('yes'):
        age1=float(('18'))
if age2 > 11 and age2 < 18:
    golden = input('Do you have a golden passport?yes/no')
    if golden==('yes'):
        age2=float(('18'))

rider1=True
rider2=True
together=False

if height1 < 36:
    rider1 = False
if friend == ('yes'):
   if height2 < 36:
    rider2 = False

if friend == ('no'):
    if age1 >= 18 and height1 >= 62:
        rider1=True
    else:
       rider1 = False

if friend == ('yes'):
   if age1 >= 18 or age2 >= 18:
    together = True

#strech challenge begins here
#all code above here funcitions properly
#check strech2 above

#strech1
if age1 > 18 and age2 > 18:
    if age1 >= 12 and age2 >= 12 and height1 >= 52 and height2 >= 52:
        rider1 = True
        rider2 = True

#strech2 is above the saftey line

#Strech3
if age1 < 18 and age2 < 18:
    if age1 >= 16 and age2 >= 14:
        rider1=True
        rider2=True
    elif age2>=16 and age1 >=14:
        rider1=True
        rider2 = True

#Result
if rider1:
    print('Rider 1 may ride the ride')
elif not rider1:
    print('Rider 1 may not ride')
if friend == ('yes'):
   if rider2:
     print('Rider2 may ride the ride.')
   elif not rider2:
    print('Rider2 may not ride the ride.')
if together and rider1 == True and rider2 == True:
    print('You may ride together')
