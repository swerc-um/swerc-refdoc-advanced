"""
 * Author: X
 * Description: Longest Common Subsequence of two strings. Reconstruct it from the dp table
 * Time: $O(N^2)$
"""

dp = [[0] * (len(a)+1) for _ in range(len(b)+1)]
for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]: dp[i][j] = dp[i-1][j-1]+1
        else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(b)][len(a)])
# n types, k occurences for each
occ = [[] for _ in range(n+1)]
for i, x in enumerate(b):
    occ[x].append(i)
T = [0] * (n*k+1)
for i, x in enumerate(a, 1):
    for j in occ[x][::-1]:
        update(j, query(j) + 1)
print(query(n*k+1))
