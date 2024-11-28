"""
 * Author: X
 * Description: Binary Lifting
 * Time: $O(N \log N)$
"""

LOG = n.bit_length()
up = [[0] * LOG for _ in range(n)]
depth = [0] * n
for node in range(1, n):
    up[node][0] = prev[node]
    depth[node] = depth[prev[node]] + 1
for k in range(1, LOG):
    for node in range(1, n):
        up[node][k] = up[up[node][k-1]][k-1]
def get_lca(a, b):
    if depth[a] < depth[b]: a, b = b, a
    k = depth[a] - depth[b]
    for j in range(LOG):
        if k & (1<<j): a = up[a][j]
    if a == b: return a
    for j in range(LOG - 1, -1, -1):
        if up[a][j] != up[b][j]: a,b = up[a][j],up[b][j]
    return up[a][0]
def get_kth_ancestor(a, k):
    if depth[a] < k: return -1
    for j in range(LOG):
        if k >> j & 1: node = up[node][j]
    return node