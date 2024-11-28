"""
 * Author: X
 * Description: Minimum Clique Cover <=> Coloring of Complement Graph
 * Constraints : N <= 20, No multiples or self edge
 * Time: O(2^N)
"""

def chromatic_number(n:int, edges:list[tuple[int,int]])->int:
    edge = [0] * n
    for uv in edges:
        u, v = uv
        edge[u] |= 1 << v
        edge[v] |= 1 << u
    dp = [0] * (1 << n)
    dp[0] = 1
    cur = [0] * (1 << n)
    for bit in range(1, 1 << n):
        v = (~bit & (bit-1)).bit_count()
        dp[bit] = dp[bit^(1<<v)]+dp[(bit^(1<<v))&(~edge[v])]
    for bit in range(1 << n):
        if (n - bit.bit_count()) & 1:
            cur[bit] = -1
        else:
            cur[bit] = 1
    for k in range(1, n):
        tmp = 0
        for bit in range(1 << n):
            cur[bit] *= dp[bit]
            tmp += cur[bit]
        if tmp != 0:
            res = k
            break
    else: res = n
    return res