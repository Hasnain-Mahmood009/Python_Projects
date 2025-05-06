class stack(list):
    def is_empty(self):
        return len(self) == 0
    def push(self,data):
        self.append(data)
    def pop(self):
        return super().pop()
    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            print("List is empty")
    def size(self):
        return len(self)
    def insert(self,index,value):
        raise Exception("Insert method is not allowed in stack.")

st = stack()
st.push(20)
st.push(30)
st.push(40)
print(st.pop())
print(st.peek())
print(st.size())