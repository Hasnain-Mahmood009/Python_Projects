class Deque:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def insert_front(self,data):
        self.item.insert(0,data)
    def insert_rear(self,data):
        self.item.append(data)
    def delete_front(self):
        if self.is_empty():
            print("deque is empty....")
            return
        else:
            self.item.pop(0)
    def delete_rear(self):
        if self.is_empty():
            print("Deque is epmty....")
            return
        else:
            self.item.pop()
    def get_front(self):
        if self.is_empty():
            return "Deque is empty...."
        else:
            return self.item[0]
    def get_rear(self):
        if self.is_empty():
            return "Deque is empty....."
        else:
            return self.item[-1]
    def size(self):
        return len(self.item)
dq = Deque()
dq.insert_front(1)
dq.insert_front(2)
dq.insert_front(3)
dq.insert_front(4)
dq.insert_rear(5)
print("Front : ",dq.get_front())
print("Rear : ", dq.get_rear())
print("After deletion....")

dq.delete_front()
dq.delete_rear()
print("Front : ",dq.get_front())
print("Rear : ", dq.get_rear())