class Node():
    def __init__(self,prev=None,item=None,next=None):
        self.prev = prev
        self.item = item
        self.next = next
class DLL:
    def __init__(self,start=None):
        self.start = start
    def is_empty(self):
        return self.start == None
    def insert_it_start(self,data):
        node = Node()
        if self.start is None:
            node.item = data
            self.start = node
        else:
            node.item = data
            node.next = self.start
            self.start.prev = node
            self.start = node
    def insert_at_last(self,data):
        node = Node()
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            node.prev = temp
            node.item = data
        else:
            self.start = node
            node.item = data
    
    def print_list(self):
        temp = self.start
        if temp is None:
            pass
        else:
            while temp is not None:
                print(temp.item,end=" ")
                temp = temp.next
    def search(self,data):
        temp = self.start
        while temp.next is not None:
            if temp.item == data:
                return temp 
            temp = temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n = Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n
    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start is None:
            self.start  = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
    def delete_item(self,data):
        if self.start is None:
            pass
        else:
            temp = self.start
            while temp is not None:
                if temp.item == data:
                    if temp.next is not None:
                        temp.next.prev = temp.prev
                    if temp.prev is not None:
                        temp.prev.next = temp.next
                    else:
                        self.start = temp.next
                    break
                temp = temp.next
mylist = DLL()
mylist.insert_it_start(20)
mylist.insert_it_start(10)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.print_list()
mylist.insert_after(mylist.search(20),50)
print()
mylist.print_list()
mylist.delete_first()
print()
mylist.print_list()
mylist.delete_last()
print()
mylist.print_list()
mylist.delete_item(50)
print()
mylist.print_list()

