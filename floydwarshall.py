"""
Floyd Warshall Algorithm
"""

import collections

def floydWarshall(edges, n):
    
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
        
    for a, b, w in edges:
        dist[a][b] = w
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

"""
Time: O(V^3)
Space: O(V^2)
"""

edges = [[0,1,1],[1,2,5],[2,1,1],[2,3,1],[3,4,1],[2,4,1],[2,5,3],[3,5,1],[4,5,2],[5,2,1],[2,0,1]]
n = 6
ans = floydWarshall(edges, n)
for a in ans:
    print(a)


