from PIL import Image
string_var = '''Michelangelo'''
int_var = 2
float_var = 2.5
boolean_var = True
image_var = Image.open('desert.jpg')
size_var = image_var.size  # retrieve the size of the image, as a (width,height) tuple
pixels_var = image_var.load()  # retrieve the entire collection of pixels from the image
single_pixel_var = pixels_var[400,321]  # retrieve (r,g,b) tuple of a particular pixel
list_var1 = [ 'B', 'D' ]
list_var2 = [ 'I', 'Y' ]
list_var3 = [ 'G', 'W' ]
team20_initials = [ list_var1, list_var2, list_var3 ]  # a list of three lists of two strings

# the following line demonstrates that you can put everything in a list. But don't do this!
mega_list = [string_var, int_var, float_var, boolean_var, image_var, size_var, pixels_var, single_pixel_var, team20_initials]

print(string_var)
print(int_var)
print(float_var)
print(boolean_var)
print(image_var)
print(size_var)
print(size_var[0])  # index of 0 into the size_var tuple
print(pixels_var)
print(single_pixel_var)
print(single_pixel_var[2])  # index of 2 into the single_pixel_var tuple
print(team20_initials)
print(team20_initials[2][1])  # use two indexes to access one item out of a list of lists
print(mega_list)
