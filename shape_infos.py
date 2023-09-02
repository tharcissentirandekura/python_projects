from math import pi # import math module to use pi value
#create classes and their required method and parameters
class Rectangle: 
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def perimeter(self):
        return (self.length + self.width) * 2
    def area(self):
        return self.length * self.width
class Circle:
    def __init__(self,r):
        self.radius = r
    def area(self):
        return pi * self.radius**2
    def circomference(self):
        return 2*pi*self.radius

class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h
    def area(self):
        return (self.base * self.height)/2
class Squarre:
    def __init__(self,s):
        self.side = s
    def area(self):
        return self.side * self.side
    def perimeter(self):
        return 4*self.side

shape_file= open("shapes.txt",'r') # read the file containing the shapes information to have enough inforamtion
read_file = shape_file.read().split()# read it 
#initialize the circle varialbes 
circles,max_circle_radius = 0,0
# initialize the triangle variables
triangles,max_triangle_base,max_triangle_height = 0,0,0
#initialize the rectangles variable
rectangles,max_rectangle_width,max_rectangle_length = 0,0,0
#initialize the square variables
squares,max_square_side = 0,0

for shape in read_file: # iterate through the list of shapes read already
    if shape.split(",")[0] == "circle": # set a condition to take all circles are there
        circles += 1 # for each circle found, add to 1 to the memory
        if int(shape.split(",")[1]) > max_circle_radius: # for all circles found, check the one with the max radius
            max_circle_radius = int(shape.split(",")[1]) # if so, swap
    # the same to all the shapes(circle,triangles,squares,and also the rectangle) as done for the circle above
    if shape.split(",")[0] == "triangle":
        triangles += 1
        if int(shape.split(",")[1]) > max_triangle_base:
            max_triangle_base = int(shape.split(",")[1])
            max_triangle_height = int(shape.split(",")[2])

    if shape.split(",")[0] == "rectangle":
        rectangles += 1
        if int(shape.split(",")[1]) > max_rectangle_width:
            max_rectangle_width = int(shape.split(",")[1])
            max_rectangle_length = int(shape.split(",")[2])
    if shape.split(",")[0] == "square":
        squares += 1
        if int(shape.split(",")[1]) > max_square_side:
            max_square_side = int(shape.split(",")[1])

# create the four object instances that represent the four shapes we have in the file and the classes
# pass them with the parameters matched we extracted from the file shapes.txt
rectangle = Rectangle(max_rectangle_width,max_rectangle_length) # this is the class method instance
circle = Circle(max_circle_radius)
triangle = Triangle(max_triangle_base,max_triangle_height)
squarre = Squarre(max_square_side)

print("In this file shapes.txt, we have:\n\n")
print(".............................................................")
print(rectangles,"rectangles","\n",
    circles,"circles","\n",triangles,"triangles","\n",squares,"squares"
        )
print(".....................................................\n")
print("And we have the circle with the biggest radius is: ",max_circle_radius,"which will give the area of:",circle.area(),"and the circomference of:",circle.circomference(),"\n")

print("And we have the square with the biggest side is: ",max_square_side," which will give the area of:",squarre.area()," and the perimeter of:",squarre.perimeter(),"\n")

print("And we have the triangle with the biggest base is: ",max_triangle_base,"and the height of:",max_triangle_height," which will yield the area of:",triangle.area(),"\n")

print("And we have the rectangle with the biggest width of: ",max_rectangle_width,"and biggest length of:",max_rectangle_length," which will provide us the area of: ",rectangle.area()," and the perimeter of:",rectangle.perimeter())


    




        






