class Apple:
    def __init__(self, w, c, s, p):
        self.weight=w
        self.color=c
        self.sugar=s
        self.price=p

apple1=Apple(100,"red",10,300)
print(apple1.weight)
print(apple1.color)

class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        import math
        return self.radius**2*math.pi

circle1=Circle(10)
print(circle1.area())

class Triangle:
    def __init__(self,a,b,c):
        self.side1=int(a)
        self.side2=int(b)
        self.side3=int(c)
    def area(self):
        s=(self.side1+self.side2+self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5

a=input("type the length of a side of triangle: ")
b=input("type the length of second side of triangle: ")
c=input("type the length of third side of triangle: ")
tri1=Triangle(a,b,c)
print(tri1.area())
