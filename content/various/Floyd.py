"""
 * Author: X
 * Description: Cycle detection
 * Time: $O(N + M)$
"""

def floyd(x0, f):
    t, h = f(x0), f(f(x0))
    while t != h:
        t, h = f(t), f(f(h))
    start, t = 0, x0
    while t != h:
        t, h = f(t), f(h)
        start += 1
    period, h = 1, f(t)
    while t != h:
        h = f(h)
        period += 1
    return start, period
