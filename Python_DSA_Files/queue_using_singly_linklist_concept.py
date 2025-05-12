class Node:
    def __init__(self,item = None, next = None):
        self.item  = item
        self.next = next
class Queue:
    def __init__(self,front = None, rear = None):
        self.front = front 
        self.rear = rear
        self.item_count = 0
    def is_empty(self):
        return self.front  == None
    def enqueue(self,data):
        n = Node(data)
        if self.is_empty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count += 1
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty...") 
            return
        else:
            self.front = self.front.next
        self.item_count -= 1
    def get_front(self):
        if self.is_empty():
            print("Queue is empty...")
            return
        else:
            return self.front.item
    def get_rear(self):
        if self.is_empty():
            print("Queue is empty...")
            return
        else:
            return self.rear.item

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Front : ",q.get_front())
print("Rear : ",q.get_rear())
print("Size : ",q.item_count)
print("After Dequeue.......")
q.dequeue()
print("Front : ",q.get_front())
print("Size : ",q.item_count)