"""
 * Author: X
 * Description: Sieve of eratosthenes
"""

maxn = 1000000
divisors = [[] for _ in range(maxn + 1)]
for i in range(1, maxn + 1):
    for j in range(i, maxn + 1, i):
        divisors[j].append(i)

spf = [-1] * (maxn + 2)
for i in range(2, maxn+1):
    if spf[i] == -1:
        for j in range(i+i, maxn+1, i):
            spf[j] = i

mobius = [0] * (maxn + 2)
mobius[1] = 1
for i in range(2, maxn + 1):
    if spf[i // spf[i]] == spf[i]:
        mobius[i] = 0
    else:
        mobius[i] = -1*mobius[i//spf[i]]

def getnpf(x):
    pfac = defaultdict(int)
    while spf[x] != -1:
        pfac[spf[x]] += 1
        x //= spf[x]
    if x != 1:
        pfac[x] += 1
    tot, pf = 1, 0
    for k, v in pfac.items():
        tot *= (v + 1)
        pf += 1
    return tot - pf