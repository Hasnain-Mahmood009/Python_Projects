class stack:
    def __init__(self):
        self.item = []
    def is_empty(self):
        return len(self.item) == 0
    def push(self,data):
        self.item.append(data)
    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("stack is empty")
    def peek(self):
        if self.is_empty():
            raise IndexError("stack is empty")
        else:
            return self.item[-1]
    def size(self):
        return len(self.item)
# s1 = stack()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# print("Top element is :", s1.peek())
# print("Removed element is :", s1.pop())
# print("Top element is :", s1.peek())
# print("Removed element is :", s1.pop())
# print("Top element is :", s1.peek())
# print("Removed element is :", s1.pop())
# print("Top element is :", s1.peek())




