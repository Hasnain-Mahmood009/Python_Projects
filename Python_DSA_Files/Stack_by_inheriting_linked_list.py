from Singly_linklist import *
class stack(SLL):
    def is_empty(self):
        return super().is_empty()
    def push(self,data):
         self.insert_at_start(data)
    def pop(self):
        self.delete_first()
    def peek(self):
        if self.is_empty():
            print("Stack is empty...")
            return
        else:
            return self.start.item
    def size(self):
        temp = self.start
        count = 0
        while temp.next is not None:
            count += 1
            temp = temp.next
        return count
st = stack()
st.push(10)
st.push(20)
st.push(30)
st.pop()
print("Top element of stack : ",st.peek())
print("Length of stack : ",st.size())
