"""
Belman Ford
"""

def bellmanFord(n, edges, src):
    
    costs = [float('inf')] * n
    costs[src] = 0
    
    for _ in range(n-1):
        for u, v, w in edges:
            costs[v] = min(costs[v], costs[u] + w)
        
    return costs

"""
Time: O(V * E)
Space: O(V)
"""

n = 6
edges = [[1,2,1],[2,3,1],[3,4,1],[4,5,1],[1,5,2]]
src = 1

ans = bellmanFord(n, edges, src)
print(ans)