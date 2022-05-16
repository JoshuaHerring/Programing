# 01 class activity 1//6/2022
# CSE 111
# Author: Joshua Day Herring
import math
PI_MULTIPLIER = 2
GRAVITATIONAL_ACELERATION = 9.81

length_in_meters = float(input('What is the length of the pendulum in meters? '))

time_to_swing = PI_MULTIPLIER * math.pi * (math.sqrt(length_in_meters / GRAVITATIONAL_ACELERATION))

print(f'Time to swing once in seconds: {time_to_swing:.2f}')