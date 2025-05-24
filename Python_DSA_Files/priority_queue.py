class priority_queue():
    def __init__(self):
        self.item = []
    def push(self,data):
        self.item.insert(0, data)
    def pop(self):
        if len(self.item) == 0:
            print("Priority Queue is emtpy...")
            return
        else:
            return max(self.item)
    def is_empty(self):
        return len(self.item) == 0
    def size(self):
        return len(self.item)
    
pq = priority_queue()
pq.push(1)
pq.push(2)
pq.push(6)
pq.push(3)
pq.push(4)
print(pq.pop())
print(pq.size())