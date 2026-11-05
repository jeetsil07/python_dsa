# Queue implementation using python list

queue = []

# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)
print("Queue: ", queue)

# Peek
frontElement = queue[0]
print("Front Element: ", frontElement)

# Dequeue
dequeuedElement = queue.pop(0)
print("Dequeued Element: ", dequeuedElement)

print("Queue after dequeue: ", queue)   

# isEmpty
isEmpty = not bool(queue)
print("Is queue empty? ", isEmpty)

# Size
size = len(queue)
print("Size of queue: ", size)

#Implementing a queue using class:

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self,item):
        self.queue.append(item)
    def dequeue(self):
        return self.queue.pop(0)
    def peek(self):
        return self.queue[0]
    def is_empty(self):
        return not bool(self.queue)
    def size(self):
        return len(self.queue)

# creating an instance of Queue class
my_queue = Queue()
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
print("Queue: ", my_queue.queue)

print("Peek: ", my_queue.peek())
print("Dequeued Element: ", my_queue.dequeue())
print("Queue after dequeue: ", my_queue.queue)
print("Is queue empty? ", my_queue.is_empty())
print("Size of queue: ", my_queue.size())


# Implementing a queue using linked list:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    def dequeue(self):
        if self.front is None:
            return None
        else:
            dequeued_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.size -= 1
            return dequeued_data

    def is_empty(self):
        return self.front is None
    
    def peek(self):
        if self.is_empty():
            return "Queue is empty"
        return self.front.data

    def get_size(self):
        return self.size
    
    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print()
    
# creating an instance of Queue class
my_queue = Queue()  
my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.printQueue()

print("Peek: ", my_queue.peek())
print("Dequeued Element: ", my_queue.dequeue())
print("Queue after dequeue: ", end="")
my_queue.printQueue()

print("Is queue empty? ", my_queue.is_empty())
print("Size of queue: ", my_queue.get_size())