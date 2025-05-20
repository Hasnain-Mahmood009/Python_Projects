class Node:
    def __init__(self,item = None,prev = None, next = None):
        self.item = item
        self.prev = prev
        self.next = next
class DBL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count_item = 0
    def is_emtpy(self):
        return self.count_item == 0
    def insert_front(self,data):
        n = Node(data,None, self.front)
        if self.is_emtpy():
            self.rear = n
        else:
            self.front.prev = n
        self.front = n
        self.count_item += 1
    def insert_rear(self,data):
        n = Node(data,self.rear,None)
        if self.is_emtpy():
            self.rear = n
        else:
            self.rear.next = n
        self.rear = n
        self.count_item += 1
    def delete_front(self):
        if self.is_emtpy():
            print("Doque is empty...")
            return
        else:
            if self.front.next == None:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
        self.count_item -= 1
    def delete_rear(self):
        if self.is_emtpy():
            print("Deque is empyt....")
            return
        else:
            if self.rear.prev == None:
                self.rear = None
            else:
                self.rear = self.rear.prev
                self.rear.next = None
        self.count_item -= 1
    def get_front(self):
        temp = self.front
        if self.is_emtpy():
            return "Doque is emtpy....."
        else:
            return temp.item
    def get_rear(self):
        temp = self.rear
        if self.is_emtpy():
            return "Doque is emtpy....."
        else:
            return temp.item
        
dq = DBL()
dq.insert_front(1)
dq.insert_front(2)
dq.insert_front(3)
dq.insert_rear(4)
print("length : ",dq.count_item)
print("Front : ",dq.get_front())
print("Rear : ",dq.get_rear())
print("After deletion.....")
dq.delete_front()
dq.delete_rear()
print("Front : ",dq.get_front())
print("Rear : ",dq.get_rear())
print("length : ",dq.count_item)
