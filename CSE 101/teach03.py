
import math
square=float(input('How long is the side of your square in cm? '))
squarearea=square*square
print(f'the square has an area of {squarearea}cm\u00B2 or {squarearea/100}m\u00B2')
cubearea=square**3
print(f'Your cube has an volume of {cubearea}cm\u00B3 or {squarearea/100}m\u00B3')
recside=float(input('What is the length of your rectangle? '))
rech=float(input('What is the width of your rectangle? '))
recarea=recside*rech
print(f'Your rectangle is {recarea}cm\u00B2 or {recarea/100}m\u00B2')
circle=float(input('What is the radius of your circle? '))
circlearea= math.pi*circle**2
print(f'Your circle has an area of {circlearea}cm\u00B2 or {circlearea/100}m\u00B2')
spherearea=4/3*math.pi*circle**3
print(f'Your sphere has a volume of {spherearea}cm\u00B3 or {spherearea/100}m\u00B3')