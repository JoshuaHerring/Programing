import math
from datetime import datetime

# 205/60R15 The first number is the width of the tire in millimeters. The second number is the aspect ratio.
# The third number is the diameter in inches of the wheel that the tire fits.

width = float(input('What is the width of your tire in mm? '))
aspect_ratio = float(input('What is the aspect ratio of your tire? '))
diameter_in_inches= float(input('What is the diameter of your tire in inches? '))

change = '1'
while change != '':
    change = input ('would you like to chnage any of your records? (width, aspect, diameter) If not press enter.')
    if change.lower() == 'width':
        width = float(input('Enter your new width. '))
    elif change.lower() == 'aspect':
        aspect_ratio = float(input('Enter your new aspect ratio. '))
    elif change.lower() == 'diameter':
        diameter_in_inches = float(input('Enter your new diameter in inches. '))
    else:
        print('It seems you spelt somehting wrong. Please try again using the keywords\n\
            "diameter", "width", or "aspect" if you do not want to chaneg anything please press "enter"')


tire_volume = (math.pi * (width**2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter_in_inches) / 10000000000)

print(f'Your tire volume is {tire_volume:.2f} liters')


date_time = datetime.now()

date = (f'{date_time:%Y-%m-%d}')


with open('volumes.txt', 'at') as text_file:
    text_file.write(f'{date}, {width}/{aspect_ratio}{diameter_in_inches}, {tire_volume}\
        ')