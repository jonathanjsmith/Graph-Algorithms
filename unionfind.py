"""
Union Find
"""

class UnionFind:
    
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
        
    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot != yroot:
            if self.rank[xroot] > self.rank[yroot]:
                self.root[yroot] = xroot
            elif self.rank[xroot] < self.rank[yroot]:
                self.root[xroot] = yroot
            else:
                self.root[yroot] = xroot
                self.rank[xroot] += 1
                
        print("root: " + str(self.root), end='\t')
        print("rank: " + str(self.rank))
                
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
"""
Time:
    init: O(V)
    find: O([alpha](V))
    union: O([alpha](V))
    connected: O([alpha](V)
    
Space:
    O(N)
"""

edges = [[0,1],[3,4],[2,3],[1,5]]
n = 6
uf = UnionFind(n)
for a, b in edges:
    uf.union(a, b)