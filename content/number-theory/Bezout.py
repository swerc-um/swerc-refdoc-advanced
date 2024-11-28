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
    x *= n//g; y *= n//g
    a //= g; b //= g
    lo = -(x // b)
    hi = y // a
    if lo > hi: return -1
# minimize c1 * x
    res1 = c1 * (x + b * lo) + c2 * (y - a * lo) 
# minimize c2 * y
    res2 = c1 * (x + b * hi) + c2 * (y - a * hi) 
    if res1 < res2: return x + b * lo, y - a * lo
    return x + b * hi, y - a * hi