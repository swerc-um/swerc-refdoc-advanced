"""
 * Author: X
 * Description: For subtree queries with Fenwick
 * Usage: update(index[u], x - val[index[u]]); query(index[u], index[u] + sz[u])
 * Time: $O(N)$
"""

prev = [None] * n
sz, ts = [1] * n, [-1] * n
ts[0] = 0
Q, order = [0], []
while Q:
    v = Q[-1]
    if ts[v] == len(adj[v]):
        for u in adj[v]:
            if u == prev[v]: continue
            sz[v] += sz[u]
        order.append(Q.pop())
    else:
        u = adj[v][ts[v]]
        if u == prev[v]:
            ts[v] += 1
            if ts[v] == len(adj[v]):continue
            u = adj[v][ts[v]]
        ts[v] += 1; ts[u] = 0; prev[u] = v
        Q.append(u)
order.reverse()
index = [None] * n
for i, e in enumerate(order):
    index[e] = i
val = [val[i] for i in order]
