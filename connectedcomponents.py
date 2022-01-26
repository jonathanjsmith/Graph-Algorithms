"""
Connected Components
"""

import collections

def connectedComponents(n, edges):
    
    # create adj list
    graph = collections.defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    # use dfs to find connected components
    seen = [0] * n
    def dfs(i):
        if seen[i]:
            return 0
        seen[i] = 1
        for adj in graph[i]:
            dfs(adj)
        return 1
    
    return sum(dfs(i) for i in range(n))

"""
Time: O(V + E)
Space: O(V + E)
"""

n = 4
connections = [[0,1],[0,2],[1,2]]
ans = connectedComponents(n, connections)
print(ans)