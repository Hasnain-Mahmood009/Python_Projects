class Queue():
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def inequeue(self,data):
        self.item.append(data)
    def dequeue(self):
        self.item.pop(0)
    def get_front(self):
        if self.is_empty():
            print("Queue is empty...")
            return
        else:
            return self.item[0]
    def get_rear(self):
        if self.is_empty():
            print("Queue is empty...")
            return
        else:
            return self.item[-1]
    def size(self):
        return len(self.item)

que = Queue()
que.inequeue(1)
que.inequeue(2)
que.inequeue(3)
print("Front element of queue : ",que.get_front())        
print("Rear element of queue : ",que.get_rear())
print("Size of queue : ",que.size())
que.dequeue()
print()
print("After dequeue...")
print()
print("Front element of queue : ",que.get_front()) 
print("Size of queue : ",que.size())