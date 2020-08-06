class Shape:
    def __init__(self,number,name):
        self.number=int(number)
        self.name=name
    def __repr__(self):
        return self.name

triangle=Shape(4,"Pyramid")
print(Shape)
print(triangle)
print(triangle.number)

#Q1
class Square:
    square_list=[]
    def __init__(self,length):
        self.length=length
        self.square_list.append(self)
    def __repr__(self):
        return "{} by {} by {} by {}.".format(self.length,self.length,self.length,self.length)
def compare(object1,object2):
    return object1 is object2


sqt1=Square(4)
sqt2=Square(4)
sqt3=Square(10)

print(sqt1)
print(Square.square_list)
for i in Square.square_list:
    print(i)
    print(compare(i,i))
print(compare(sqt1.length,sqt2.length))
