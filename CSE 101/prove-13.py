#Wind chill calculations for 5mph increment winds. 
# Equation = Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
#Where,T= Air Temperature (ºF) V= Wind Speed (mph)
#To convert temperatures in degrees Celsius to Fahrenheit, multiply by 1.8 (or 9/5) and add 32.
type = input('Farenheight or Celsius? f/c:')
t = int(input('What is the temperture? '))
v = [5,10,15,20,25,30,35,40,45,50,55,60]
c = (t - 32) * (5/9)
if type == 'c':
    t = t * (9/5) + 32

for i in range(12):
    wind_chill = 35.74 + (0.6215*t) - 35.75*(v[i]**0.16) + (0.4275*t)*(v[i]**0.16)

    if type == 'f':
        print(round(wind_chill,2))

    if type == 'c':
        c = (wind_chill - 32) * (5/9)
        print(round(c,2))