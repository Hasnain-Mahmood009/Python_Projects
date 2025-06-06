import queur as q

class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_list = {v:[] for v in range(vno)}
    def add_edge(self,u,v,weight=1):
        if 0 <= u< self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
    def remove_edge(self,u,v):
        if 0 <= u< self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u] = [pair for pair in self.adj_list[u] if pair[0] != v]
    def has_edge(self,u,v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            for node, weight in self.adj_list[u]:
                if node == v and weight != 0:
                    return "Edge exists..."
            return "No edge..."

    def print_edge(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")
   
    def bfs(self,s):
        queue = q.Queue()
        # li = []
        v = [False] * self.vertex_count     
        queue.inequeue(s)
        v[s] = True
        while not queue.is_empty():
            node = queue.get_front()
            queue.dequeue()
            for neighbor, _ in self.adj_list[node]:
                if not v[neighbor]:
                    queue.inequeue(neighbor)
                    v[neighbor] = True
        print(v)




al = Graph(5)
al.add_edge(0,0)
al.add_edge(1,0)
al.add_edge(0,1)
al.add_edge(1,1)
al.add_edge(0,0)
al.add_edge(2,3)
al.add_edge(1,1)
al.add_edge(1,4)
al.bfs(0)
