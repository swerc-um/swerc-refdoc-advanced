"""
 * Author: X
 * Description: Returns BCC
"""

def find_BCC(G):
    n = len(G)
    dep = [0] * n
    Q = [0]
    d = 0
    while Q:
        node = Q.pop()
        if node < 0:
            node = ~node
            d -= 1
        elif not dep[node]:
            d = dep[node] = d + 1
            Q.append(~node)
            Q += G[node]
    G2 = [[v for v in G[u] if dep[u] + 1 >= dep[v] != dep[u] - 1] for u in range(n)]
    return find_SCC(G2)