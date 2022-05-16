from PIL import Image

image_original = Image.open('desert.jpg')

image_original.show()

(width, height) = image_original.size

print(width)
print(height)

pixels_original = image_original.load()

r, g, b = pixels_original[0, 0]
print(f'{r} {g} {b}')

r, g, b = pixels_original[0, 1]
print(f'{r} {g} {b}')

r, g, b = pixels_original[0, 2]
print(f'{r} {g} {b}')

r, g, b = pixels_original[0, 3]
print(f'{r} {g} {b}')

r, g, b = pixels_original[0, 4]
print(f'{r} {g} {b}')

r=255
g=0
b=0

pixels_original[0,0] = (r, g, b)
pixels_original[0,2] = (r, g, b)
pixels_original[0,4] = (r, g, b)
pixels_original[0,6] = (r, g, b)
pixels_original[0,8] = (r, g, b)

image_original.show()


r,g, b =pixels_original[0, 0]
print(r, g, b)