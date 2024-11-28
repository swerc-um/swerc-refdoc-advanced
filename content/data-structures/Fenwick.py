"""
 * Author: X
 * Description: Fenwick
 * Time: $O(N\log N)$
"""

# POINT UPDATE, RANGE QUERY
def update(pos, v):
    while pos < len(T):
        T[pos] += v
        pos |= pos + 1
def _query(pos):
    r = 0
    while pos:
        r += T[pos-1]
        pos &= pos-1
    return r
def query(a, b): # [l, r)
    return _query(b) - _query(a)
T = list(X)
for i in range(n):
    j = i | (i+1)
    if j < n: T[j] += T[i]

# RANGE UPDATE, POINT QUERY
def update_(i, val):
    i = i + 1
    while i < len(T):
        T[i] += val
        i += i & (-i)
def update(l, r, val): # [l, r)
    update_(l, val)
    update_(r, -val)  # T length n+1
def query(i):
    res = 0
    i = i + 1
    while i > 0:
        res += T[i]
        i -= i & (-i)
    return res

# 1-indexed RANGE UPDATE, RANGE QUERY
def add(b, idx, v):
    while idx <= n:
        b[idx] += v
        idx += idx & -idx
def range_add(l, r, v):
    j = l
    while j <= n:
        B1[j] += v
        B2[j] += v * (l - 1)
        j += j & -j
    j = r + 1
    while j <= n:
        B1[j] -= v
        B2[j] -= v * r
        j += j & -j
def _query(b, idx):
    total = 0
    while idx > 0:
        total += b[idx]
        idx -= idx & -idx
    return total
def prefix_sum(idx):
    return _query(B1, idx) * idx - _query(B2, idx)
def range_sum(l, r):
    return prefix_sum(r) - prefix_sum(l - 1)

B1, B2 = [0] * (n + 1), [0] * (n + 1)
for i, v in enumerate(X, 1):
    range_add(i, i, v)