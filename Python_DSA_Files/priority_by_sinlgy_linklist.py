class Node:
    def __init__(self,item=None,next=None):
        self.item = item
        self.next = next
class priorityQueue:
    def __init__(self,start=None):
        self.start = start
        self.item_count = 0
    def push(self,data):
        n = Node(data) 
        if self.start != None:
            n.next = self.start
        self.start = n
        self.item_count += 1
    def pop(self):
        temp = self.start
        heightest = 0
        if temp == None:
            print("Priority queue is empty.....")
            return
        else:
            while temp != None:
                y = temp.item
                if heightest < y:
                    heightest = y
                else:
                    temp = temp.next
        return heightest
    def is_emtpy(self):
        return self.start == None          
pq = priorityQueue()
pq.push(1)
pq.push(2)
pq.push(7)
pq.push(4)
pq.push(9)
print(pq.pop())
print("Size : ", pq.item_count)