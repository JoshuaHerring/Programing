# make a function that computes the area of a square one for circle and one for a rectanble.

# shape = input('What is your shape')
# length = int(input('What is the length/radius? '))
# width = ''
# if shape == 'rectangle':
#     width = int(input('WHat is the width? '))
def compute_area(shape,length,width):
    if shape == 'square':
        area = length * length
    
    if shape == 'circle':
        area = 3.14 * (length * length)
    
    if shape == 'rectangle':
        area = length * width
    print(area)
shape = ''
while shape != 'quit':
    shape = input('What is your shape')
    if shape != 'quit':
        length = int(input('What is the length/radius? '))
        width = ''
        if shape == 'rectangle':
            width = int(input('WHat is the width? '))

        compute_area(shape,length,width)