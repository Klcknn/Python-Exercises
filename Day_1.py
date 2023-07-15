""" 
# My preliminary notes about Class ( OOP class ):

# Define a class 
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age


person_1 = Person("John",25)
name_of_person_1 = person_1.name
print(name_of_person_1)

# Define a class as a Person2
class Person2:
    # Define a constructor function
    def __init__(self,n,a):
        self.name = n 
        self.age = a


person_2 = Person2("Tomm",30)
name_of_person_2 = person_2.name
age_of_person_2 = person_2.age
print(name_of_person_2,age_of_person_2)


class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area
    def paint_needed(self):
        return self.wall_area*2.5
           
class Paint:
    def __init__(self,buckets,colors):
        self.buckets = buckets
        self.colors = colors
    def total_prices(self):
        if self.colors == 'white':
            return self.buckets*2
        else:
            return self.buckets*3
    
class Shape:
    # define a constructor function
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    # define a calculate function
    def calculate(self):
        self.text = input("Please enter the calculated the text of the shape ").lower()
        if self.text == "triangle":
            return self.x*self.y*self.z
        elif self.text == "square":
            return self.x**2
        elif self.text == "rectangle":
            return self.x+self.y+self.z
        else:
            print("Unknown text")
    # define a write function 
    def write(self,a):
        self.a = a
        print(f"The shape of the objects {self.text} is calculated value {self.a}")
         
shape = Shape(3,4,5)
return_value_to_us = shape.calculate()
shape.write(return_value_to_us)

"""



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y :
            return True
        else:
            return False
    def distance_from_points(self, x, y):
        return ( (self.x - x )**2 + (self.y - y )**2 )**0.5 

"""    
point = Point(1,1)
value= point.distance_from_points(3,3)
print(value)
"""
class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

point_x = Point(8,9)
rectangle_x = Rectangle(Point(5,6), Point(7,9))
point_x.falls_in_rectangle(rectangle_x)


""" 
class Point_2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1] :
            return True
        else:
            return False
    def distance_from_points(self, point):
        return ((self.x - point.x )**2 + (self.y - point.y)**2)**0.5 
    
point_2 = Point_2(1,1)
point_3 = Point_2(3,3)
value_2= point_2.distance_from_points(point_3)
print(value_2) 
"""