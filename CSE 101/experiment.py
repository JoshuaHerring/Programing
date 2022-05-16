colors = []
color =('0')

while color != (''):
   color = input('Name a color: ')
   if color != (''):
      colors.append(color)

length = len(colors)
print(length)

print(colors)
print (colors[2])

for i in range(len(colors)):
    color = colors[i]
    print(f'{i+1} {color}')