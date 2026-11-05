stack = []

# push
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
print(stack)

# Peek
topElement = stack[-1]
print("Peek: ", topElement)

# Pop
poppedElement = stack.pop()
print("Popped Element: ", poppedElement)

# Stack after pop
print("Stack after pop: ", stack)

# isEmpty
isEmpty = not bool(stack)
print("Is stack empty? ", isEmpty)

# Size
size = len(stack)
print("Size of stack: ", size)

# creating stack using class:

class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        return not bool(self.stack)

    def size(self):
        return len(self.stack)
    
# creating an instance of Stack class
my_stack = Stack()
my_stack.push(10)
my_stack.push(20)   
my_stack.push(30)
print("Stack: ", my_stack.stack)

print("Peek: ", my_stack.peek())
print("Popped Element: ", my_stack.pop())
print("Stack after pop: ", my_stack.stack)
print("Is stack empty? ", my_stack.is_empty())
print("Size of stack: ", my_stack.size())

# Creating stack using linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        popped_node = self.top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.size == 0

    def length(self):
        return self.size

# creating an instance of Stack class using linked list
linked_stack = Stack()
linked_stack.push(100)
linked_stack.push(200)
linked_stack.push(300)
print("Stack: ", linked_stack.peek())
print("Popped Element: ", linked_stack.pop())
print("Stack after pop: ", linked_stack.peek())
print("Is stack empty? ", linked_stack.is_empty())
print("Size of stack: ", linked_stack.length())