class Node():
    def __init__(self,item=None,prev=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
class DCLL():
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_at_start(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n
        self.start = n
      
    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def search(self,data):
        temp = self.start
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.start:
                break
        print("Not found!")
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(data)
            n.next = temp.next
            n.prev = temp
            temp.next.prev = n
            temp.next = n
    def delete_first(self):
        temp = self.start
        if self.is_empty():
            return
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.start = temp.next
    def delete_last(self):
        temp = self.start
        if self.is_empty():
            return
        else:
            temp.prev.prev.next = temp
            temp.prev = temp.prev.prev
    def delete_after(self,temp):
        if temp is not None:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
    def print_code(self):
        temp = self.start
        if self.is_empty():
            print("List is empty")
            return
        while True:
            print(temp.item, end=" ") 
            temp = temp.next
            if temp == self.start:
                break
mylist = DCLL()
mylist.insert_at_start(30)
mylist.insert_at_last(50)
mylist.insert_at_start(40)
mylist.insert_after(mylist.search(50), 60)
mylist.print_code()
print()
mylist.delete_first()
mylist.print_code()
print()
mylist.delete_last()
mylist.print_code()
print()
mylist.delete_after(mylist.search(50))
mylist.print_code()
