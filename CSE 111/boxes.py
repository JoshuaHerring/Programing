#Calculate how many boxes will be needed
#math.ceil()
import math

iteams = float(input('How many Iteams do you have? '))
iteams_per_box = float(input('How many Iteams can fit per box? '))

boxes = math.ceil(iteams / iteams_per_box)


print (f'For {iteams} iteams with {iteams_per_box} iteams per box you will need \n{boxes} Boxes')