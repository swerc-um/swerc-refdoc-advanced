"""
 * Author: X
 * Description: Bellman-Ford
 * Usage: edges 1-indexed
 * Time: O(VE)
"""

def bellmanford(n, edges):
    dist = [float('inf')] * (n + 1)
    prec = [-1] * (n + 1)
    for _ in range(n):
        x = -1
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                prec[v] = u; dist[v] = dist[u] + w; x = v
    if x == -1: return []
    for _ in range(n): x = prec[x]
    end, path = x, [x]
    while prec[x] != end:
        x = prec[x]
        path.append(x)
    return (path+[end])[::-1]