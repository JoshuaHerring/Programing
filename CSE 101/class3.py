first_name= input('What is your first name?')
last_name=input('What is your last name?')
email=input('What is your email address?')
number=input('What is your phone number?')
job=input('What is your job title?')
id=input('what is your ID number?')
hair=input('What color is your hair?')
eyes=input('What color are your eyes?')
month=input('What month did you start working here?')
train=input('Have you been trained?')

print('-----------------------------')
print(last_name.upper()+', '+first_name)
print(job.capitalize())
print('ID:'+(id))

print('\n' + email.lower())
print(number)

output=f'\nHair:{hair.capitalize():20}Eyes:{eyes.capitalize()})'
print(output)
output2=f'Month:{month:20}                Trainnig:{train}'
print(output2)
print('--------------------------------')