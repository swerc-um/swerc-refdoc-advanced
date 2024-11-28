"""
 * Author: X
 * Description: Z[i] is length of the longest substr starting from str[i] which is also a prefix of str[0..n-1]
 * (i + Z[i] == n) => prefix suffix
 * Si recherche de motif, concaténer motif devant la string
 * if i + Z[i] == n and n \% (i+1) == 0 : period = max(period, i+1)
 * Time: $O(N)$
"""

Z, l, r = [0] * n, 0, 0
for i in range(1, n):
    if i <= r: Z[i] = min(Z[i-l],r-i+1)
    while i+Z[i]<n and s[Z[i]]==s[i + Z[i]]: Z[i] += 1
    if i + Z[i] - 1 > r: l, r = i, i + Z[i] - 1