from collections import dequeue, defaultdict

class Graph:
    
    def __init__(self, vertices):
        self.adj_list = defaultdcit(list);
        self.vertics = vertices;    
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) 
        
    def bfs(self, start):
        visted = [false] * (self.vertices + 1)
        queue = deque()
        visited[start] = true
        queue.append(start)  
        
        
        
        
        


g = Graph(9);

g.add_edge(1,2)
g.add_edge(1,6)
g.add_edge(2,3)
g.add_edge(2,4)
g.add_edge(6,7)
g.add_edge(6,9)
g.add_edge(4,5)
g.add_edge(7,8)
g.add_edge(5,8)


#Graph Traversal
bfs_result = g.bfs(1);
print("BFS Traversal:", bfs_result)