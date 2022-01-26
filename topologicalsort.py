"""
Topological Sort
"""

import collections

def topologicalSort(n, edges):
    
    # create adjacency list and count indegrees for each vertex
    graph = collections.defaultdict(list)
    indegree = [0] * n
    for a, b in edges:
        graph[a].append(b)
        indegree[b] += 1
        
    # create queue of all nodes with no indegree
    l = []
    q = [i for i in range(n) if indegree[i] == 0]
    
    # loop through each node with no indegree
    while q:
        node = q.pop(0)
        l.append(node)
        for adj in graph[node]:
            indegree[adj] -= 1
            if not indegree[adj]:
                q.append(adj)
                
    return l
                
"""
Time: O(V + E)
Space: O(V + E)
"""

n = 4
edges = [[0,2],[0,1],[2,1],[2,3],[1,3]]
ans = topologicalSort(n, edges)
print(ans)