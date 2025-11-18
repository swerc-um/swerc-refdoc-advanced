"""
 * Author:
 * Description:
"""

up = [up]
wei = [wei]
for _ in range(1, LOG):
    wei.append([max(wei[-1][v], wei[-1][up[-1][v]]) for v in range(n)])
    up.append([up[-1][up[-1][v]] for v in range(n)])

def lca(u, v):
    if dep[u] > dep[v]: u, v = v, u
    k = dep[v] - dep[u]
    maxw = 0
    for i in range(LOG):
        if k>>i&1:
            maxw = max(maxw, wei[i][v])
            v = up[i][v]
    if v == u: return maxw
    for i in range(LOG-1, -1, -1):
        if up[i][u] != up[i][v]:
            maxw = max(maxw, wei[i][u], wei[i][v])
            u, v = up[i][u], up[i][v]
    maxw = max(maxw, wei[0][u], wei[0][v])
    # return up[0][u]
    return maxw
