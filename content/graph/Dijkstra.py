"""
 * Author: X
 * Description: Dijkstra for dense graphs.
 * Time: $O(V^2)$
"""

def dijkstra(s, t, adjlist, adjmat):
    n = len(adjlist); d = [float('inf')] * n; d[s] = 0
    vis = [False] * n
    for _ in range(n):
        v = -1
        for j in range(n):
            if not vis[j] and (v == -1 or d[j] < d[v]): v=j
        if d[v] == float('inf'): break
        vis[v] = True
        for u in adjlist[v]:
            if (v==s and u==t) or (v==t and u==s):continue
            if d[v] + adjmat[v][u] < d[u]:
               d[u] = d[v] + adjmat[v][u]
    return d[t] if d[t] != float('inf') else -1