import sys

class Rectangle:
    def __init__(self,l,w):
        self.length = l
        self.width = w
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return (self.length + self.width)*2
class Circle:
    def __init__(self,r):
        self.radius = r
    def area(self):
        return  3.14 * self.radius**2
    def circomference(self):
        return 2 * 3.14 * self.radius
class Triangle:
    def __init__(self,b,h):
        self.base = b
        self.height = h
    def area(self):
        return 1/2*self.base * self.height

flag = True
while flag == True:
    
    print("please choose an operation: ")
    ask = input("Enter the operation on:rectangle,circle,or triangle or e ro quit:>:")
    if ask == "e":
        sys.exit()
    elif ask.lower() == "rectangle":
        l = int(input("Enter width:"))
        w = int(input("Enter height:"))
        r = Rectangle(l,w)
        ask2 = input("Enter: perimeter or area:")
        if ask2 == "area":
            print("area:",r.area())
        elif ask2 == "perimeter":
            print(r.perimeter())
            
    elif ask.lower() == "circle":
        r = int(input("Enter radius of circle:"))
        c = Circle(r)
        ask2 = input("Enter: circomference or area:")
        if ask2 == "area":
            print("area:",c.area())
        elif ask2 == "circomference":
            print(c.circomference())
    
    elif ask.lower() == "triangle":
        b = int(input("Enter its base:"))
        h =  int(input("Enter its height:"))
        t = Triangle(b,h)
        ask2 = input("Enter: area or other:")
        if ask2 == "area":
            print("area:",t.area())
        elif ask2 == "other":
            print("No such operation exists!")



    