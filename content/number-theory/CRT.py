"""
 * Author: X
 * Description: a, n = values, modulos
 * For non-coprime moduli : crtNonCoprime
"""

def crt(a, n):
    x = 0
    p = 1
    for ni in n: p *= ni
    for ai, ni in zip(a, n):
        xi = p // ni
        try: inv = pow(xi, -1, ni)
        except ValueError: return None
        x += ai * xi * inv
    return x % p

def crtNonCoprime(a, n):
    prime = {}
    for ai, ni in zip(a, n):
        for k, v in getPrimeFactors(ni).items():
            m = pow(k, v)
            aj, nj = prime.get(k, (ai % m, m))
            if aj != (ai % m) % nj:
                return None
            if nj > m:
                continue
            prime[k] = (ai % m, m)
    newa, newn = [], []
    for k, (ai, ni) in prime.items():
        newa.append(ai)
        newn.append(ni)
    return crt(newa, newn)