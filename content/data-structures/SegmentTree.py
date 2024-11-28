"""
 * Author: X
 * Description: SegmentTree
 * Time: $O(N\log N)$
"""

def update(p, val):
    p += N
    seg[p] = val
    while p > 1:
        seg[p>>1] = seg[p] + seg[p^1]
        p >>= 1
def query(l, r): # [l, r)
    res = 0
    l += N; r += N
    while l < r:
        if l&1: res += seg[l]; l += 1
        if r&1: r -= 1; res += seg[r]
        l >>= 1; r >>= 1
    return res
N = 1 << n.bit_length()
seg = [0] * (2 * N)
for i in range(n):
    seg[N + i] = a[i]
for k in range(N - 1, 0, -1):
    seg[k] = seg[k<<1] + seg[k<<1|1]

# supprimer ligne -> for k in range(N - 1, 0, -1):
def update(l, r, val): # [l, r)
    l += N; r += N
    while l < r:
        if l&1: seg[l] += val; l += 1
        if r&1: r -= 1; seg[r] += val
        l >>= 1; r >>= 1
def query(p):
    res = 0
    p += N
    while p > 0:
        res += seg[p]
        p >>= 1
    return res

# reduce the complexity from O(N log N) to O(N) to get all values.
# works only in case the order of modifications on a single element doesn't affect the result.
def push():
    for i in range(1, N):
        seg[i<<1] += seg[i]
        seg[i<<1|1] += seg[i]
        seg[i] = 0
