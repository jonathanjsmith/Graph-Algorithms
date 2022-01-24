"""
Dijkstra's Algorithm
"""

import collections
import heapq

def dijkstra(edges, n, k):
    
    # create adj list
    graph = collections.defaultdict(dict)
    for u, v, w in edges:
        graph[u][v] = w
        
    # use min priority queue to implement dijkstra's
    pq = [(0, k)]
    dist = {}
    while pq:
        d, node = heapq.heappop(pq)
        if node not in dist:
            dist[node] = d
            for adj in graph[node]:
                heapq.heappush(pq, (d + graph[node][adj], adj))
    
    return dist

"""
Time: O(E * lgV)
Space: O(V + E)
"""

edges = [[2,1,1],[2,3,1],[3,4,1],[2,4,1],[2,5,3],[3,5,1]]
n = 5
k = 2
ans = dijkstra(edges, n, k)
print(ans)
