class UnionFind:
    
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
        
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX == rootY:
            return
          
        if self.rank[rootX] > self.rank[rootY]:
            self.parent[rootY] = rootX
        elif self.rank[rootX] < self.rank[rootY]:
            self.parent[rootX] = rootY
        else:
            self.parent[rootY] = rootX
            self.rank[rootX] += 1
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
    def get_set_count(self):
        count = 0
        for i in range(len(self.parent)):
            if self.parent[i] == i:
                count += 1
        return count

if __name__ == "__main__":
    uf = UnionFind(10)
    
    uf.union(1,2)
    uf.union(3,4)
    uf.union(5,6)
    uf.union(2,6)
    uf.union(7,8)
    uf.union(8,9)
    uf.union(4,9)
    
    print("1 and 5 is connected?", uf.connected(1,5))
    print("3 and 7 is connected?", uf.connected(3,7))
    print("1 and 9 is connected?", uf.connected(1,9))
    print("0 and 1 is connected?", uf.connected(0,1))
    
    print("Number of disjoint sets:", uf.get_set_count())
