class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)


rev_stack=Stack()
for c in "yesterday":
    rev_stack.push(c)

reverse=""
while rev_stack.size():
    reverse+=rev_stack.pop()
    print(reverse)

number=[0,1,2,3,4,5]
reverse1=[]
stack=Stack()
for i in number:
    stack.push(i)

while stack.size():
    reverse1.append(stack.pop())
print(reverse1)
