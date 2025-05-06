class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class stack:
    def __init__(self):
        self.start = None
        self.item_count = 0
    def is_empty(self):
        return self.start == None
    def push(self,data):
        node = Node()
        if not self.is_empty():
            node.item = data
            node.next = self.start
            self.start = node
        else:
            self.start = node
            node.item = data
    def pop(self):
        if self.is_empty():
            pass
        else:
            self.start = self.start.next
    def peek(self):
        if self.is_empty():
            print("Stack is empty...")
            return
        else:
            return self.start.item
    def size(self):
        temp = self.start
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        return count
    
st = stack()
st.push(20)
st.push(30)
st.push(40)
st.pop()
print("Top element of stack : ",st.peek())
print("Size of stack : ", st.size())