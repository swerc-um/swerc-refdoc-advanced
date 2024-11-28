"""
 * Author: X
 * Description: Small-To-Large Merging. Query the number of distinct colors in each subtree.
 * Usage: When done with u :
 * ans[u] = _sum[u]; merge(prev[u], u) 
 * Time: $O(N \log N)$
"""

def merge(u, v):
    if len(colors[u]) < len(colors[v]):
        colors[v], colors[u] = colors[u], colors[v]
        _sum[v], _sum[u] = _sum[u], _sum[v]
        mx[v], mx[u] = mx[u], mx[v]
    for c, value in colors[v].items():
        if c not in colors[u]:
            colors[u][c] = 0
        colors[u][c] += value
        if colors[u][c] > mx[u]:
            mx[u] = colors[u][c]
            _sum[u] = c
        elif colors[u][c] == mx[u]:
            _sum[u] += c

_sum = list(map(int,input().split()))
mx = [1] * n
colors = [{c:1} for c in _sum]