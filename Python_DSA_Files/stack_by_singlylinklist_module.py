from Singly_linklist import * 
class stack:
    def __init__(self):
        self.mylist = SLL()
        self.item_count = 0
    def is_empty(self):
        return self.mylist.is_empty()
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count += 1
    def pop(self):
        self.mylist.delete_first()
    def peek(self):
        if self.is_empty():
            print("Stack is empty...")
            return
        else:
            return self.mylist.start.item
st = stack()
st.push(20)
st.push(30)
st.push(40)
st.pop()
print("Size of stack : ",st.item_count)
print("Last element of stack : ",st.peek())