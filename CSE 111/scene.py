# Import the functions from the Draw 2-D library
# so that they can be used in this program.
# https://byui-cse.github.io/cse111-course/lesson03/draw2d.html
# ^^^^^^ this website is the instruction for the drawing including color options
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.

    draw_grid(canvas,scene_height,scene_width, 30)
    draw_ground(canvas,scene_height,scene_width)
    draw_sky(canvas, scene_height, scene_width)
    draw_sun(canvas,scene_height, scene_width)
    draw_picket_fence(canvas, scene_height, scene_width, 40)
    draw_cloud(canvas,40,300)
    draw_cloud(canvas, 200, 250)
    draw_cloud(canvas, 550, 400)
    draw_cloud(canvas, 400, 380)
    draw_tree(canvas, scene_height, scene_width)

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_grid(canvas, height, width, interval):
    '''draw vertical lines for the grid, having interval be the 1st number makes it so that
    the first line will not be written at 0 off of the screen but at the first line'''
    label_distance_from_edge = 10
    for x in range(interval, width, interval):
       draw_line(canvas,x,0,x,height )
       draw_text(canvas, x, label_distance_from_edge-18, f'{x}')
       #draw horizontal lines, I did not use interval as the starting point here because 0 appears on the grid
       #you will notice that the numbers for the grid actually appear below the grid so you have to expand
       # the scene window in order to see the labels
    for y in range(0, height, interval):
       draw_line(canvas, 0, y, width, y)
       draw_text(canvas, label_distance_from_edge, y+5, f'{y}' )
def draw_ground(canvas,height,width):
   draw_rectangle(canvas,0,0,width,height/2.5,fill='green', outline = '')

def draw_sky(canvas, height, width):
    draw_rectangle(canvas, 0, height/2.5, width, height,fill='deepskyblue', outline = '')

def draw_sun(canvas,height,width):
    draw_oval(canvas, width-100, height-100, width, height, fill='yellow', outline = '')

def draw_picket_fence(canvas,height, width, interval):
    for z in range(0, width, interval):
        draw_rectangle(canvas, z, 0, z+20, height/4, fill='white', outline = '')
        draw_polygon(canvas, z, height/4, z+20, height/4, z+10, ((height/4)+20), fill ='white', outline = '')
    draw_rectangle(canvas, 0, height/5, width, (height/5)+10, fill = 'white', outline = '')
    draw_rectangle(canvas, 0, height/8, width, (height/8)+10, fill = 'white', outline = '')
    draw_rectangle(canvas, 0, height/20, width, (height/20)+10, fill = 'white', outline = '')

def draw_cloud(canvas,x,y):
    draw_oval(canvas, x ,y ,x+100 ,y+50 , fill = 'white', outline = '')
    draw_oval(canvas,x+15,y-10, x+50, y+55, fill = 'white', outline = '')
    draw_oval(canvas,x+50, y-10, x+85, y+55, fill = 'white', outline = '')

def draw_tree(canvas,height, width):
    draw_rectangle(canvas, width*.8, height/3, (width*.8)+20, (height/3)+30, fill = 'tan4')
    draw_polygon(canvas, (width*.8)-80, (height/3)+30, (width*.8) + 100, (height/3)+30, (width*.8)+10, (height/3)+300, fill = 'darkGreen', outline = '')


# Call the main function so that
# this program will start executing.
main()