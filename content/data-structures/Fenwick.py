"""
 * Author:
 * Description:
"""

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
