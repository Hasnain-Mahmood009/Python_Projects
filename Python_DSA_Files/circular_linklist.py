class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self):
        self.last = None  

    def insert_at_start(self, item):
        new_node = Node(item)
        if not self.last:
            self.last = new_node
            self.last.next = self.last
        else:
            temp = self.last
            while temp.next != self.last:
                temp = temp.next
            new_node.next = self.last
            self.last = new_node
            temp.next = self.last

    def insert_at_last(self, item):
        new_node = Node(item)
        if not self.last:
            self.last = new_node
            self.last.next = self.last
        else:
            temp = self.last
            while temp.next != self.last:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.last

    def insert_after(self, value, item):
        if not self.last:
            print("List is empty!")
            return
        temp = self.last
        while True:
            if temp.item == value:
                new_node = Node(item, temp.next)
                temp.next = new_node
                return
            temp = temp.next
            if temp == self.last:
                print(value)
                break

    def delete_start(self):
        if not self.last:
            return
        if self.last.next == self.last:
            self.last = None
        else:
            temp = self.last
            while temp.next != self.last:
                temp = temp.next
            self.last = self.last.next
            temp.next = self.last

    def delete_last(self):
        if not self.last:
            return
        if self.last.next == self.last:
            self.last = None
        else:
            temp = self.last
            while temp.next.next != self.last:
                temp = temp.next
            temp.next = self.last

    def delete_after(self, value):
        if not self.last:
            return
        temp = self.last
        while True:
            if temp.item == value:
                if temp.next == self.last:
                    print("No node exists after", value)
                    return
                temp.next = temp.next.next
                return
            temp = temp.next
            if temp == self.last:
                print("Value not found:", value)
                break

    def print_code(self):
        if not self.last:
            print("List is empty")
            return
        temp = self.last
        while True:
            print(temp.item, end=" ") 
            temp = temp.next
            if temp == self.last:
                break


# Example Usage
cll = CLL()
cll.insert_at_start(20)
cll.insert_at_start(10)
cll.insert_at_last(40)
cll.insert_after(20, 30)
cll.print_code()
print()
cll.delete_start()
cll.print_code()
print()
cll.delete_last()
cll.print_code()
print()
cll.delete_after(20)
cll.print_code()
