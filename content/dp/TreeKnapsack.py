"""
 * Author:
 * Description:
 * Usage: tin[u] = début de visite
 *  order.append(u)
 *  tout[v] = fin de visite du subtree root en v
"""
dp = [[0] * (w+1) for _ in range(n+1)]
for v in order[::-1]:
    i, o = tin[v], tout[v]+1
    wi, vi = weights[v], values[v]
    for j in range(w+1):
        # use child
        if j-wi >= 0:
            dp[i][j] = max(dp[i][j], dp[i+1][j-wi] + vi)
        # or skip subtree of child
        dp[i][j] = max(dp[i][j], dp[o][j])
print(dp[0][w])