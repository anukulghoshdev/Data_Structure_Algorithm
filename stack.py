
# stack using list
stack = []
stack.append(1)
stack.append(2)     
stack.append(3)     
print("Initial stack:", stack)  
top = stack.pop()  
print("Popped element:", top)
print("after pop :", stack)  
print("top element:", stack[-1]) 


# stack using deque 
from collections import deque 
stack = deque()
stack.append("a")
stack.append("b")
stack.append("c")
print(stack)
stack.append("d")    
print(stack)


# full implamentation
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0 
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"
        
    def peek(self):
            if self.is_empty():
                return "Stack is empty!"
            else:
                return self.items[-1]
    def size(self):
        return len(self.items)
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.items)  # [10, 20, 30]

s1.pop()
print(s1.items)  # [10, 20]

s1.peek()
print(s1.peek())  # 20