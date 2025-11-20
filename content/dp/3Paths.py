"""
 * Author:
 * Description: one left, one middle and the other right.
 * they must not intersect (except in the leftmost upper corner and rightmost bottom corner)
 * So for each row y (except first and last), the x coordinates of the lines (x1[y] , x2[y] and respectively x3[y] ) will be : x1[y] < x2[y] < x3[y]
 * Usage: 1 < N, M <= 50; each cell contains between 0 and 1000 apples inclusive.
"""

if m <= 3:
    print(sum(sum(row) for row in g))
    return
dp = [[[0] * m for _ in range(m)] for _ in range(m)]
for x in range(m):
    for y in range(x+1, m):
        for z in range(y+1, m):
            dp[x][y][z] = sum(g[0][:z+1])
pairs = [(x, y) for x in range(m) for y in range(x+1, m)]
for i in range(1, n):
    dq = [[[0] * m for _ in range(m)] for _ in range(m)]
    for x, y in pairs:
        for z in range(y+1, m):
            dq[x][y][z] = dp[x][y][z] + g[i][x]+g[i][y]+g[i][z]
    for y, z in pairs:
        for x in range(1, y):
            dq[x][y][z] = max(dq[x][y][z], dq[x-1][y][z] + g[i][x])
    for x, z in pairs:
        for y in range(x+2, z):
            dq[x][y][z] = max(dq[x][y][z], dq[x][y-1][z] + g[i][y])
    for x, y in pairs:
        for z in range(y+2, m):
            dq[x][y][z] = max(dq[x][y][z], dq[x][y][z-1] + g[i][z])
    dp = dq
print(dp[-3][-2][-1])