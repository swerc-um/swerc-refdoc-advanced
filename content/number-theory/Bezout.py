"""
 * Author: X
 * Description: bezout(a, b) calcule une solution à l’équation ax + by = pgcd(a, b)
 * solve(a, b, n) calcule (x, y) tq ax + by = n
"""

def bezout(a, b):
    px, py = 1, 0
    x, y = 0, 1
    while b != 0:
        a, (q, b) = b, divmod(a, b)
        px, x = x, px - q * x
        py, y = y, py - q * y
# pgcd, x, y
    return a, px, py 

def solve(c1, a, c2, b, n):
    g, x, y = bezout(a, b)
    if n%g: return -1
    # to get to ax + by = n
    x *= n // g
    y *= n // g
    # lo <= k <= hi to get x and y positive
    lo = -((x * g) // b)
    hi = (y * g) // a
    if lo > hi:
        return -1
    return x + (b * lo) // g, y - (a * lo) // g
