class Shape:
    def __init__(self,w,l):
        self.width=w
        self.length=l
    def what_am_i(self):
        print("I am Shape.")

class Rectangle(Shape):
    def calculate_perimeter(self):
        print("below is the perimeter of Rectangle whose width is {} and length is {}.".format(self.width,self.length))
        print(self.width*2+self.length*2)
    def change_size(self):
        self.width+=int(input("type a number to add or subract width"))

class Square(Rectangle):
    def calculate_perimeter(self):
        print("below is perimeter of Square whose width is {} and length is {}.".format(self.width,self.length))
        print(self.width*2+self.length*2)

rect=Rectangle(5,4)
sqr=Square(10,10)

rect.calculate_perimeter()
sqr.calculate_perimeter()
#rect.change_size()
#sqr.change_size()
#rect.calculate_perimeter()
#sqr.calculate_perimeter()
rect.what_am_i()
sqr.what_am_i()

class Horse:
    def __init__(self,name,rider):
        self.name=name
        self.rider=rider

class Rider:
    def __init__(self,name,sex):
        self.name=name
        self.sex=sex

Yutaka_Take=Rider("Take Yutaka","male")
deep_impact=Horse("Deep Impact",Yutaka_Take.name)
print(deep_impact.rider)
