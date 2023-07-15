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
           
class Paint:
    def __init__(self,buckets,colors):
        self.buckets = buckets
        self.colors = colors
    
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



