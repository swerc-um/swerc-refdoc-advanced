"""
 * Author:
 * Description:
"""

def calc(pos, k, und, st, t1, t2=-1):
    if pos == len(num):
        if not st: return 0
        if t2 == -1: return int(k >= 20)
        return int(k == 20)
    state = (pos, k, und, st)
    if state in dp: return dp[state]
    res = 0
    for d in range(10):
        ddiff = int(num[pos])
        if not und and d > ddiff: break
        is_und = und or (d < ddiff)
        is_st = st or (d > 0)
        if is_st and -1 != t2 != d and t1 != d: continue
        new_k = k
        if is_st:
            new_k += (d == t1)
            new_k -= (d != t1)
        res += calc(pos+1, new_k, is_und, is_st, t1, t2)
    dp[state] = res
    return res