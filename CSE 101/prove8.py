from PIL import Image

image_backround = Image.open('desert.jpg')
pixels_backround = image_backround.load()

image_foreground = Image.open('penguin.jpg')
pixels_foreground = image_foreground.load()
# pixels_foreground[0,0]=(255,0,0)
# image_foreground.show()

(width, hieght) = image_backround.size
print(width)
print(hieght)

(width, hieght) = image_foreground.size
print(width)
print(hieght)

# (r,g,b) = pixels_foreground[400,0]
# pixels_foreground[400,400] = (255,0,0)
# print(r,g,b)
# image_combined = Image.new()('RGB', image_foreground.size)


for x in range (0,800):
    for y in range (0,600):
        (r,g,b) = pixels_foreground[x,y]
        if (r,g,b) == (44,207,64):
            pixels_foreground[x,y] = pixels_backround[x,y]

            
image_foreground.show()